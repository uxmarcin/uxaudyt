<?php
/**
 * Ekipaż – API (PHP 8 + SQLite)
 * Jeden plik, bez zależności. Wszystkie odpowiedzi w JSON.
 * Tożsamość: token zwracany przy rejestracji (w bazie trzymamy tylko jego hash SHA-256).
 */
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');
header('Referrer-Policy: same-origin');
header('Cache-Control: no-store');

const DATA_DIR = __DIR__ . '/data';

const JOB_TTL  = 2 * 3600;          // zlecenie żyje 2 h po starcie
const VOUCH_WINDOW = 48 * 3600;     // respekt do 48 h po starcie
const ACTIVITIES = ['heist','contact','race','business','freeroam','pvp','rp','cars'];
const TIMES      = ['morning','afternoon','evening','night'];
const STYLES     = ['chill','balanced','tryhard'];
const PLATFORMS  = ['ps5','xbox','pc'];
const FEATURES   = ['map','checklist','guides','photo','events','discordbot'];

$cfgFile = DATA_DIR . '/config.php';
if (!is_file($cfgFile)) {
  if (!is_dir(DATA_DIR)) { @mkdir(DATA_DIR, 0775, true); }
  // losowa nazwa bazy i klucz admina – baza nie da się zgadnąć nawet bez .htaccess
  @file_put_contents($cfgFile, "<?php\nreturn " . var_export(['admin_key' => bin2hex(random_bytes(16)), 'db' => 'db-' . bin2hex(random_bytes(12)) . '.sqlite'], true) . ";\n");
}
$CONFIG = is_file($cfgFile) ? (require $cfgFile) : [];
define('DB_FILE', DATA_DIR . '/' . ($CONFIG['db'] ?? 'ekipaz.sqlite'));
$ADMIN_KEY = $CONFIG['admin_key'] ?? '';

/* ---------- helpers ---------- */
function out($data, int $code = 200): never { http_response_code($code); echo json_encode($data, JSON_UNESCAPED_UNICODE); exit; }
function fail(string $msg, int $code = 400, string $err = 'bad_request'): never { out(['ok' => false, 'error' => $err, 'message' => $msg], $code); }
function now(): int { return time(); }
function uid(int $n = 10): string { return substr(str_replace(['+','/','='], '', base64_encode(random_bytes(16))), 0, $n); }
function clean(?string $s, int $max): string {
  $s = (string)$s;
  $s = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/u', '', $s) ?? '';
  $s = trim(preg_replace('/\s+/u', ' ', $s) ?? '');
  return mb_substr($s, 0, $max);
}
function cleanMulti(?string $s, int $max): string {
  $s = (string)$s;
  $s = preg_replace('/[\x00-\x09\x0B\x0C\x0E-\x1F\x7F]/u', '', $s) ?? '';
  $s = preg_replace("/\n{3,}/", "\n\n", trim($s)) ?? '';
  return mb_substr($s, 0, $max);
}
function pick($v, array $allowed, $default) { return in_array($v, $allowed, true) ? $v : $default; }
function pickMany($v, array $allowed, int $min = 0): array {
  $v = is_array($v) ? array_values(array_unique(array_filter($v, fn($x) => in_array($x, $allowed, true)))) : [];
  return $v;
}
function body(): array {
  static $b = null;
  if ($b !== null) return $b;
  $raw = file_get_contents('php://input', false, null, 0, 20000) ?: '';
  $b = json_decode($raw, true);
  if (!is_array($b)) $b = [];
  return $b;
}
function ip(): string { return $_SERVER['REMOTE_ADDR'] ?? '0.0.0.0'; }

/* ---------- db ---------- */
function db(): PDO {
  static $pdo = null;
  if ($pdo) return $pdo;
  if (!is_dir(DATA_DIR)) { @mkdir(DATA_DIR, 0775, true); }
  if (!is_file(DATA_DIR . '/.htaccess')) { @file_put_contents(DATA_DIR . '/.htaccess', "Require all denied\nDeny from all\n"); }
  if (!is_file(DATA_DIR . '/index.html')) { @file_put_contents(DATA_DIR . '/index.html', ''); }
  $pdo = new PDO('sqlite:' . DB_FILE, null, null, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC]);
  $pdo->exec('PRAGMA journal_mode=WAL; PRAGMA foreign_keys=ON; PRAGMA busy_timeout=4000;');
  $pdo->exec(<<<SQL
  CREATE TABLE IF NOT EXISTS players(
    id TEXT PRIMARY KEY, nick TEXT NOT NULL, nick_lc TEXT NOT NULL UNIQUE, platform TEXT NOT NULL,
    activities TEXT NOT NULL DEFAULT '[]', times TEXT NOT NULL DEFAULT '[]', style TEXT NOT NULL DEFAULT 'balanced',
    mic INTEGER NOT NULL DEFAULT 1, contact TEXT NOT NULL DEFAULT '', bio TEXT NOT NULL DEFAULT '', avatar INTEGER NOT NULL DEFAULT 0,
    token_hash TEXT NOT NULL, recovery_hash TEXT NOT NULL DEFAULT '', rep INTEGER NOT NULL DEFAULT 0, jobs_done INTEGER NOT NULL DEFAULT 0,
    banned INTEGER NOT NULL DEFAULT 0, created INTEGER NOT NULL, last_seen INTEGER NOT NULL);
  CREATE TABLE IF NOT EXISTS jobs(
    id TEXT PRIMARY KEY, owner_id TEXT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
    title TEXT NOT NULL, activity TEXT NOT NULL, platform TEXT NOT NULL, slots INTEGER NOT NULL,
    start_at INTEGER NOT NULL, details TEXT NOT NULL DEFAULT '', mic_required INTEGER NOT NULL DEFAULT 0,
    style TEXT NOT NULL DEFAULT 'balanced', status TEXT NOT NULL DEFAULT 'open', created INTEGER NOT NULL, closed_at INTEGER NOT NULL DEFAULT 0);
  CREATE INDEX IF NOT EXISTS jobs_start ON jobs(start_at);
  CREATE TABLE IF NOT EXISTS requests(
    id TEXT PRIMARY KEY, job_id TEXT NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
    player_id TEXT NOT NULL REFERENCES players(id) ON DELETE CASCADE, msg TEXT NOT NULL DEFAULT '',
    status TEXT NOT NULL DEFAULT 'pending', created INTEGER NOT NULL, decided INTEGER NOT NULL DEFAULT 0, UNIQUE(job_id, player_id));
  CREATE TABLE IF NOT EXISTS vouches(
    from_id TEXT NOT NULL, to_id TEXT NOT NULL, job_id TEXT NOT NULL, created INTEGER NOT NULL,
    PRIMARY KEY(from_id, to_id, job_id));
  CREATE TABLE IF NOT EXISTS crews(
    id TEXT PRIMARY KEY, name TEXT NOT NULL, name_lc TEXT NOT NULL UNIQUE, tag TEXT NOT NULL, details TEXT NOT NULL DEFAULT '',
    platform TEXT NOT NULL, focus TEXT NOT NULL DEFAULT 'heist', owner_id TEXT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
    recruiting INTEGER NOT NULL DEFAULT 1, color INTEGER NOT NULL DEFAULT 0, created INTEGER NOT NULL);
  CREATE TABLE IF NOT EXISTS crew_members(
    crew_id TEXT NOT NULL REFERENCES crews(id) ON DELETE CASCADE, player_id TEXT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
    role TEXT NOT NULL DEFAULT 'member', created INTEGER NOT NULL, PRIMARY KEY(crew_id, player_id));
  CREATE TABLE IF NOT EXISTS reports(
    id INTEGER PRIMARY KEY AUTOINCREMENT, reporter_id TEXT, target_type TEXT NOT NULL, target_id TEXT NOT NULL,
    reason TEXT NOT NULL, created INTEGER NOT NULL, resolved INTEGER NOT NULL DEFAULT 0);
  CREATE TABLE IF NOT EXISTS votes(player_id TEXT NOT NULL, feature TEXT NOT NULL, PRIMARY KEY(player_id, feature));
  CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT NOT NULL, payload TEXT NOT NULL, created INTEGER NOT NULL);
  CREATE TABLE IF NOT EXISTS hits(k TEXT NOT NULL, ts INTEGER NOT NULL);
  CREATE INDEX IF NOT EXISTS hits_k ON hits(k, ts);
  CREATE INDEX IF NOT EXISTS hits_ts ON hits(ts);
  SQL);
  return $pdo;
}
function q(string $sql, array $p = []): PDOStatement { $st = db()->prepare($sql); $st->execute($p); return $st; }
function one(string $sql, array $p = []): ?array { $r = q($sql, $p)->fetch(); return $r ?: null; }
function all(string $sql, array $p = []): array { return q($sql, $p)->fetchAll(); }

function hitKey(string $key): string { global $CONFIG; return $key . ':' . hash_hmac('sha256', ip(), (string)($CONFIG['admin_key'] ?? 'ekipaz')); }
function limitCheck(string $key, int $max, int $window): void {
  q('DELETE FROM hits WHERE ts < ?', [now() - 86400]);
  $n = (int)(one('SELECT COUNT(*) c FROM hits WHERE k=? AND ts>=?', [hitKey($key), now() - $window])['c'] ?? 0);
  if ($n >= $max) fail('Zwolnij trochę – za dużo prób w krótkim czasie. Spróbuj za chwilę.', 429, 'rate_limited');
}
function limitHit(string $key): void { q('INSERT INTO hits(k,ts) VALUES(?,?)', [hitKey($key), now()]); }
function limit(string $key, int $max, int $window): void { limitCheck($key, $max, $window); limitHit($key); }
const RESERVED = ['admin','administrator','moderacja','moderator','mod','ekipaz','ekipaż','rockstar','support','pomoc','system','root'];
function nickKey(string $n): string {
  $n = mb_strtolower($n);
  return strtr($n, ['0'=>'o','1'=>'l','3'=>'e','5'=>'s','_'=>'','-'=>'','.'=>'',' '=>'']);
}
function validContact(string $c): bool { return (bool)preg_match('/^(?:[a-z0-9_.]{2,32}|[^\s#@:]{2,32}#\d{4})$/u', $c); }
function hasLink(string $t): bool { return (bool)preg_match('~(https?://|www\.|\.(com|pl|net|gg|ru|io|xyz)\b)~i', $t); }
function event(string $type, array $payload): void {
  q('INSERT INTO events(type,payload,created) VALUES(?,?,?)', [$type, json_encode($payload, JSON_UNESCAPED_UNICODE), now()]);
  if (random_int(1, 20) === 1) q('DELETE FROM events WHERE id NOT IN (SELECT id FROM events ORDER BY id DESC LIMIT 200)');
}

/* ---------- auth ---------- */
function token(): string {
  $h = $_SERVER['HTTP_X_EKIPAZ_TOKEN'] ?? '';
  return is_string($h) ? preg_replace('/[^A-Za-z0-9_\-]/', '', $h) : '';
}
function me(bool $required = true): ?array {
  static $cache = false;
  if ($cache === false) {
    $t = token();
    $cache = $t ? one('SELECT * FROM players WHERE token_hash=?', [hash('sha256', $t)]) : null;
    if ($cache) {
      if ((int)$cache['banned']) fail('To konto zostało zablokowane przez moderację.', 403, 'banned');
      if (now() - (int)$cache['last_seen'] > 120) q('UPDATE players SET last_seen=? WHERE id=?', [now(), $cache['id']]);
    }
  }
  if ($required && !$cache) fail('Najpierw załóż profil gracza.', 401, 'unauthorized');
  return $cache;
}
function isAdmin(): bool {
  global $ADMIN_KEY;
  $k = $_SERVER['HTTP_X_EKIPAZ_ADMIN'] ?? '';
  return $ADMIN_KEY !== '' && is_string($k) && hash_equals($ADMIN_KEY, $k);
}

/* ---------- presenters ---------- */
function stars(int $rep): int { return $rep >= 40 ? 5 : ($rep >= 20 ? 4 : ($rep >= 10 ? 3 : ($rep >= 4 ? 2 : ($rep >= 1 ? 1 : 0)))); }
function pubPlayer(array $p, bool $withContact = false): array {
  $r = [
    'id' => $p['id'], 'nick' => $p['nick'], 'platform' => $p['platform'],
    'activities' => json_decode($p['activities'], true) ?: [], 'times' => json_decode($p['times'], true) ?: [],
    'style' => $p['style'], 'mic' => (bool)$p['mic'], 'bio' => $p['bio'], 'avatar' => (int)$p['avatar'],
    'rep' => (int)$p['rep'], 'stars' => stars((int)$p['rep']), 'jobsDone' => (int)$p['jobs_done'],
    'created' => (int)$p['created'], 'online' => now() - (int)$p['last_seen'] < 600, 'lastSeen' => (int)$p['last_seen'],
  ];
  if ($withContact) $r['contact'] = $p['contact'];
  return $r;
}
function jobRow(array $j, ?array $me): array {
  $owner = one('SELECT * FROM players WHERE id=?', [$j['owner_id']]);
  $accepted = all('SELECT p.* FROM requests r JOIN players p ON p.id=r.player_id WHERE r.job_id=? AND r.status="accepted" ORDER BY r.created', [$j['id']]);
  $pending = (int)(one('SELECT COUNT(*) c FROM requests WHERE job_id=? AND status="pending"', [$j['id']])['c'] ?? 0);
  $myReq = $me ? one('SELECT status FROM requests WHERE job_id=? AND player_id=?', [$j['id'], $me['id']]) : null;
  $isOwner = $me && $me['id'] === $j['owner_id'];
  $inCrew = $isOwner || ($myReq && $myReq['status'] === 'accepted');
  $taken = 1 + count($accepted);
  $status = $j['status'];
  if ($status === 'open' && $taken >= (int)$j['slots']) $status = 'full';
  if ($status === 'hidden') $status = 'closed';
  if ($status !== 'closed' && now() > (int)$j['start_at'] + JOB_TTL) $status = 'closed';
  return [
    'id' => $j['id'], 'title' => $j['title'], 'activity' => $j['activity'], 'platform' => $j['platform'],
    'slots' => (int)$j['slots'], 'taken' => $taken, 'startAt' => (int)$j['start_at'], 'details' => $j['details'],
    'micRequired' => (bool)$j['mic_required'], 'style' => $j['style'], 'status' => $status, 'created' => (int)$j['created'],
    'owner' => $owner ? pubPlayer($owner, $inCrew) : null,
    'members' => array_map(fn($p) => pubPlayer($p, $inCrew), $accepted),
    'pending' => $isOwner ? $pending : null,
    'myStatus' => $isOwner ? 'owner' : ($myReq['status'] ?? null),
  ];
}
function crewRow(array $c, ?array $me): array {
  $members = all('SELECT p.*, m.role FROM crew_members m JOIN players p ON p.id=m.player_id WHERE m.crew_id=? ORDER BY m.role="boss" DESC, p.rep DESC', [$c['id']]);
  $rep = array_sum(array_map(fn($m) => (int)$m['rep'], $members));
  $mine = $me ? (bool)array_filter($members, fn($m) => $m['id'] === $me['id']) : false;
  return [
    'id' => $c['id'], 'name' => $c['name'], 'tag' => $c['tag'], 'details' => $c['details'], 'platform' => $c['platform'],
    'focus' => $c['focus'], 'recruiting' => (bool)$c['recruiting'], 'color' => (int)$c['color'], 'created' => (int)$c['created'],
    'ownerId' => $c['owner_id'], 'rep' => $rep, 'mine' => $mine, 'count' => count($members),
    'members' => array_map(fn($m) => pubPlayer($m) + ['role' => $m['role']], array_slice($members, 0, 24)),
  ];
}

/* ---------- router ---------- */
foreach ($_GET as $k => $v) { if (!is_string($v)) fail('Nieprawidłowe parametry.', 400, 'bad_request'); }
$a = $_GET['a'] ?? '';
$method = $_SERVER['REQUEST_METHOD'] ?? 'GET';
if ($method === 'POST') {
  $ct = $_SERVER['CONTENT_TYPE'] ?? '';
  if (stripos($ct, 'application/json') === false) fail('Nieprawidłowy format żądania.', 415, 'unsupported');
}

try {
  switch ($a) {

  case 'stats': {
    $t = now();
    out(['ok' => true,
      'players' => (int)one('SELECT COUNT(*) c FROM players WHERE banned=0')['c'],
      'online'  => (int)one('SELECT COUNT(*) c FROM players WHERE last_seen>? AND banned=0', [$t - 600])['c'],
      'jobs'    => (int)one('SELECT COUNT(*) c FROM jobs WHERE status NOT IN ("closed","hidden") AND start_at>?', [$t - JOB_TTL])['c'],
      'crews'   => (int)one('SELECT COUNT(*) c FROM crews')['c'],
      'feed'    => array_map(fn($e) => ['type' => $e['type'], 'created' => (int)$e['created']] + (json_decode($e['payload'], true) ?: []),
                     all('SELECT * FROM events WHERE type!="join" ORDER BY id DESC LIMIT 20')),
    ]);
  }

  /* --- profile --- */
  case 'register': {
    if ($method !== 'POST') fail('Metoda niedozwolona', 405);
    limitCheck('register', 5, 3600);
    $b = body();
    if (!empty($b['website'])) fail('Spam.', 400, 'spam');            // honeypot
    $nick = clean($b['nick'] ?? '', 24);
    if (mb_strlen($nick) < 3) fail('Nick musi mieć co najmniej 3 znaki.');
    if (!preg_match('/^[A-Za-z0-9ĄĆĘŁŃÓŚŹŻąćęłńóśźż_\-\. ]+$/u', $nick)) fail('Nick może zawierać litery (także polskie), cyfry, spację oraz _ - .');
    $nk = nickKey($nick);
    if (in_array($nk, RESERVED, true)) fail('Ten nick jest zarezerwowany. Wybierz inny.', 409, 'taken');
    if (one('SELECT 1 FROM players WHERE nick_lc=?', [$nk])) fail('Ten nick ma już właściciela. Wybierz inny.', 409, 'taken');
    $contact = mb_strtolower(clean($b['contact'] ?? '', 40));
    if (!validContact($contact)) fail('Podaj nazwę użytkownika Discord, np. krolnapadow (bez linków i spacji).');
    $tok = bin2hex(random_bytes(24));
    $rec = strtoupper(implode('-', str_split(bin2hex(random_bytes(6)), 4)));
    $id = uid(10);
    q('INSERT INTO players(id,nick,nick_lc,platform,activities,times,style,mic,contact,bio,avatar,token_hash,recovery_hash,created,last_seen) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', [
      $id, $nick, $nk, pick($b['platform'] ?? '', PLATFORMS, 'ps5'),
      json_encode(pickMany($b['activities'] ?? [], ACTIVITIES)), json_encode(pickMany($b['times'] ?? [], TIMES)),
      pick($b['style'] ?? '', STYLES, 'balanced'), !empty($b['mic']) ? 1 : 0, $contact, cleanMulti($b['bio'] ?? '', 280),
      max(0, min(11, (int)($b['avatar'] ?? 0))), hash('sha256', $tok), hash('sha256', $nk . '|' . $rec), now(), now(),
    ]);
    limitHit('register');
    out(['ok' => true, 'token' => $tok, 'recovery' => $rec, 'me' => pubPlayer(one('SELECT * FROM players WHERE id=?', [$id]), true)]);
  }

  case 'recover': {
    if ($method !== 'POST') fail('Metoda niedozwolona', 405);
    limit('recover', 8, 3600);
    $b = body();
    $nick = nickKey(clean($b['nick'] ?? '', 24));
    $code = strtoupper(preg_replace('/[^A-Fa-f0-9]/', '', (string)($b['code'] ?? '')) ?? '');
    $code = implode('-', str_split($code, 4));
    $p = one('SELECT * FROM players WHERE nick_lc=?', [$nick]);
    if (!$p || !$p['recovery_hash'] || !hash_equals($p['recovery_hash'], hash('sha256', $nick . '|' . $code))) fail('Nick albo kod się nie zgadzają.', 403, 'bad_code');
    if ((int)$p['banned']) fail('To konto zostało zablokowane przez moderację.', 403, 'banned');
    $tok = bin2hex(random_bytes(24));
    q('UPDATE players SET token_hash=?, last_seen=? WHERE id=?', [hash('sha256', $tok), now(), $p['id']]);
    out(['ok' => true, 'token' => $tok, 'me' => pubPlayer(one('SELECT * FROM players WHERE id=?', [$p['id']]), true)]);
  }

  case 'logout': {
    if ($method !== 'POST') fail('Metoda niedozwolona', 405);
    $m = me();
    q('UPDATE players SET token_hash=? WHERE id=?', [hash('sha256', bin2hex(random_bytes(24))), $m['id']]);
    out(['ok' => true]);
  }

  case 'me': {
    $m = me();
    $myJobs = all('SELECT * FROM jobs WHERE owner_id=? AND start_at>? ORDER BY start_at DESC LIMIT 20', [$m['id'], now() - JOB_TTL]);
    $joined = all('SELECT j.*, r.status rstatus FROM requests r JOIN jobs j ON j.id=r.job_id WHERE r.player_id=? AND j.start_at>? ORDER BY j.start_at DESC LIMIT 20', [$m['id'], now() - JOB_TTL]);
    $inbox = all('SELECT r.id rid, r.msg, r.created rcreated, r.job_id, j.title, p.* FROM requests r JOIN jobs j ON j.id=r.job_id JOIN players p ON p.id=r.player_id WHERE j.owner_id=? AND r.status="pending" AND j.status!="closed" ORDER BY r.created DESC LIMIT 50', [$m['id']]);
    $crew = one('SELECT c.* FROM crew_members m JOIN crews c ON c.id=m.crew_id WHERE m.player_id=?', [$m['id']]);
    $votes = array_column(all('SELECT feature FROM votes WHERE player_id=?', [$m['id']]), 'feature');
    // do kogo mogę dać respekt: ludzie z moich wspólnych zleceń (już po starcie)
    $mates = all(<<<SQL
      SELECT DISTINCT p.*, j.id job_id, j.title job_title FROM jobs j
      JOIN (SELECT r.job_id, r.player_id FROM requests r JOIN jobs jj ON jj.id=r.job_id WHERE r.status='accepted' AND r.decided<=jj.start_at UNION SELECT id, owner_id FROM jobs) x ON x.job_id=j.id
      JOIN players p ON p.id=x.player_id
      WHERE j.start_at<=? AND j.start_at>? AND p.id!=? AND (j.closed_at=0 OR j.closed_at>=j.start_at)
        AND j.id IN (SELECT r.job_id FROM requests r JOIN jobs jj ON jj.id=r.job_id WHERE r.status='accepted' AND r.decided<=jj.start_at AND r.player_id=? UNION SELECT id FROM jobs WHERE owner_id=?)
        AND NOT EXISTS (SELECT 1 FROM vouches v WHERE v.from_id=? AND v.to_id=p.id AND v.job_id=j.id)
      ORDER BY j.start_at DESC LIMIT 30
    SQL, [now() - 900, now() - VOUCH_WINDOW, $m['id'], $m['id'], $m['id'], $m['id']]);
    out(['ok' => true, 'me' => pubPlayer($m, true), 'hosted' => (int)one('SELECT COUNT(*) c FROM jobs WHERE owner_id=?', [$m['id']])['c'],
      'jobs' => array_map(fn($j) => jobRow($j, $m), $myJobs),
      'joined' => array_map(fn($j) => jobRow($j, $m), $joined),
      'inbox' => array_map(fn($r) => ['id' => $r['rid'], 'msg' => $r['msg'], 'created' => (int)$r['rcreated'], 'jobId' => $r['job_id'], 'jobTitle' => $r['title'], 'player' => pubPlayer($r)], $inbox),
      'crew' => $crew ? crewRow($crew, $m) : null,
      'votes' => $votes,
      'mates' => array_map(fn($p) => ['player' => pubPlayer($p), 'jobId' => $p['job_id'], 'jobTitle' => $p['job_title']], $mates),
    ]);
  }

  case 'profile.update': {
    if ($method !== 'POST') fail('Metoda niedozwolona', 405);
    $m = me(); $b = body();
    limit('profile', 30, 3600);
    $contact = mb_strtolower(clean($b['contact'] ?? $m['contact'], 40));
    if (!validContact($contact)) fail('Podaj nazwę użytkownika Discord, np. krolnapadow (bez linków i spacji).');
    if (hasLink((string)($b['bio'] ?? ''))) fail('Bez linków w opisie – kontakt idzie przez Discord.');
    q('UPDATE players SET platform=?, activities=?, times=?, style=?, mic=?, contact=?, bio=?, avatar=? WHERE id=?', [
      pick($b['platform'] ?? $m['platform'], PLATFORMS, $m['platform']),
      json_encode(pickMany($b['activities'] ?? json_decode($m['activities'], true), ACTIVITIES)),
      json_encode(pickMany($b['times'] ?? json_decode($m['times'], true), TIMES)),
      pick($b['style'] ?? $m['style'], STYLES, $m['style']), array_key_exists('mic', $b) ? (!empty($b['mic']) ? 1 : 0) : (int)$m['mic'], $contact,
      cleanMulti($b['bio'] ?? $m['bio'], 280), max(0, min(11, (int)($b['avatar'] ?? $m['avatar']))), $m['id'],
    ]);
    out(['ok' => true, 'me' => pubPlayer(one('SELECT * FROM players WHERE id=?', [$m['id']]), true)]);
  }

  case 'player': {
    $id = clean($_GET['id'] ?? '', 16);
    $p = one('SELECT * FROM players WHERE id=? AND banned=0', [$id]);
    if (!$p) fail('Nie ma takiego gracza.', 404, 'not_found');
    $crew = one('SELECT c.* FROM crew_members m JOIN crews c ON c.id=m.crew_id WHERE m.player_id=?', [$id]);
    $vouchers = all('SELECT p.* FROM vouches v JOIN players p ON p.id=v.from_id WHERE v.to_id=? GROUP BY p.id ORDER BY MAX(v.created) DESC LIMIT 12', [$id]);
    $hosted = (int)one('SELECT COUNT(*) c FROM jobs WHERE owner_id=?', [$id])['c'];
    out(['ok' => true, 'player' => pubPlayer($p), 'hosted' => $hosted,
      'crew' => $crew ? ['id' => $crew['id'], 'name' => $crew['name'], 'tag' => $crew['tag'], 'color' => (int)$crew['color']] : null,
      'vouchers' => array_map('pubPlayer', $vouchers)]);
  }

  /* --- jobs --- */
  case 'jobs': {
    $m = me(false);
    $where = ['j.start_at > ?', 'j.status NOT IN ("closed","hidden")', 'p.banned=0']; $p = [now() - 3600];
    if (in_array($_GET['platform'] ?? '', PLATFORMS, true)) { $where[] = 'j.platform=?'; $p[] = $_GET['platform']; }
    if (in_array($_GET['activity'] ?? '', ACTIVITIES, true)) { $where[] = 'j.activity=?'; $p[] = $_GET['activity']; }
    if (in_array($_GET['style'] ?? '', STYLES, true)) { $where[] = 'j.style=?'; $p[] = $_GET['style']; }
    if (($_GET['when'] ?? '') === 'now') { $where[] = 'j.start_at < ?'; $p[] = now() + 3600; }
    if (($_GET['when'] ?? '') === 'today') { $where[] = 'j.start_at < ?'; $p[] = strtotime('tomorrow') ?: now() + 86400; }
    $rows = all('SELECT j.* FROM jobs j JOIN players p ON p.id=j.owner_id WHERE ' . implode(' AND ', $where) . ' ORDER BY j.start_at ASC LIMIT 120', $p);
    $list = array_map(fn($j) => jobRow($j, $m), $rows);
    if (!empty($_GET['open'])) $list = array_values(array_filter($list, fn($j) => $j['status'] === 'open'));
    out(['ok' => true, 'jobs' => $list]);
  }

  case 'job': {
    $m = me(false);
    $j = one('SELECT * FROM jobs WHERE id=?', [clean($_GET['id'] ?? '', 16)]);
    if (!$j) fail('To zlecenie już nie istnieje.', 404, 'not_found');
    $row = jobRow($j, $m);
    if ($m && $m['id'] === $j['owner_id']) {
      $row['requests'] = array_map(fn($r) => ['id' => $r['rid'], 'msg' => $r['msg'], 'status' => $r['status'], 'created' => (int)$r['rcreated'], 'player' => pubPlayer($r, $r['status'] === 'accepted')],
        all('SELECT r.id rid, r.msg, r.status, r.created rcreated, p.* FROM requests r JOIN players p ON p.id=r.player_id WHERE r.job_id=? AND r.status IN ("pending","accepted") ORDER BY r.created', [$j['id']]));
    }
    out(['ok' => true, 'job' => $row]);
  }

  case 'job.create': {
    if ($method !== 'POST') fail('Metoda niedozwolona', 405);
    $m = me(); $b = body();
    limit('job', 8, 3600);
    $active = (int)one('SELECT COUNT(*) c FROM jobs WHERE owner_id=? AND status NOT IN ("closed","hidden") AND start_at>?', [$m['id'], now() - 3600])['c'];
    if ($active >= 3) fail('Masz już 3 aktywne zlecenia. Zamknij któreś, zanim dodasz kolejne.', 409, 'too_many');
    $title = clean($b['title'] ?? '', 60);
    if (mb_strlen($title) < 4) fail('Nazwij zlecenie – minimum 4 znaki, np. „Napad na kasyno, finał”.');
    $start = (int)($b['startAt'] ?? 0);
    if ($start < now() - 60) fail('Ten termin już minął. Wybierz godzinę w przyszłości.');
    if ($start > now() + 7 * 86400) fail('Zlecenie możesz wystawić najwyżej 7 dni do przodu.');
    if (hasLink($title . ' ' . (string)($b['details'] ?? ''))) fail('Bez linków w zleceniu – kontakt idzie przez Discord po przyjęciu do składu.');
    $id = uid(8);
    q('INSERT INTO jobs(id,owner_id,title,activity,platform,slots,start_at,details,mic_required,style,status,created) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', [
      $id, $m['id'], $title, pick($b['activity'] ?? '', ACTIVITIES, 'heist'), pick($b['platform'] ?? $m['platform'], PLATFORMS, $m['platform']),
      max(2, min(8, (int)($b['slots'] ?? 4))), $start, cleanMulti($b['details'] ?? '', 400), !empty($b['micRequired']) ? 1 : 0,
      pick($b['style'] ?? $m['style'], STYLES, 'balanced'), 'open', now(),
    ]);
    event('job', ['nick' => $m['nick'], 'title' => $title, 'jobId' => $id, 'platform' => pick($b['platform'] ?? $m['platform'], PLATFORMS, $m['platform'])]);
    out(['ok' => true, 'job' => jobRow(one('SELECT * FROM jobs WHERE id=?', [$id]), $m)]);
  }

  case 'job.close': {
    if ($method !== 'POST') fail('Metoda niedozwolona', 405);
    $m = me(); $b = body();
    $j = one('SELECT * FROM jobs WHERE id=?', [clean($b['id'] ?? '', 16)]);
    if (!$j) fail('Nie ma takiego zlecenia.', 404, 'not_found');
    if ($j['owner_id'] !== $m['id'] && !isAdmin()) fail('To nie Twoje zlecenie.', 403, 'forbidden');
    limit('close', 30, 3600);
    $chg = q('UPDATE jobs SET status="closed", closed_at=? WHERE id=? AND status NOT IN ("closed","hidden")', [now(), $j['id']])->rowCount();
    // zakończone po co najmniej 15 min od startu – zaliczamy wykonanie (raz)
    if ($chg && (int)$j['start_at'] <= now() - 900) {
      q('UPDATE players SET jobs_done=jobs_done+1 WHERE id=? OR id IN (SELECT player_id FROM requests WHERE job_id=? AND status="accepted")', [$j['owner_id'], $j['id']]);
    }
    out(['ok' => true]);
  }

  case 'job.join': {
    if ($method !== 'POST') fail('Metoda niedozwolona', 405);
    $m = me(); $b = body();
    limit('join', 30, 3600);
    $j = one('SELECT * FROM jobs WHERE id=?', [clean($b['id'] ?? '', 16)]);
    if (!$j) fail('To zlecenie już nie istnieje.', 404, 'not_found');
    if ($j['owner_id'] === $m['id']) fail('To Twoje zlecenie.');
    $row = jobRow($j, $m);
    if ($row['status'] !== 'open') fail('Skład jest już pełny albo zlecenie zostało zamknięte.', 409, 'closed');
    if ($j['platform'] !== $m['platform']) fail('To zlecenie jest na inną platformę niż Twój profil.', 409, 'platform');
    $ex = one('SELECT * FROM requests WHERE job_id=? AND player_id=?', [$j['id'], $m['id']]);
    if ($ex && $ex['status'] === 'declined') fail('Gospodarz tego zlecenia odrzucił już Twoje zgłoszenie.', 409, 'declined');
    if ($ex && $ex['status'] !== 'left') fail('Zgłoszenie jest już wysłane. Poczekaj na decyzję gospodarza.', 409, 'exists');
    $msgTxt = clean($b['msg'] ?? '', 160);
    if (hasLink($msgTxt)) fail('Bez linków w wiadomości.');
    if ($ex) q('UPDATE requests SET status="pending", msg=?, created=?, decided=0 WHERE id=?', [$msgTxt, now(), $ex['id']]);
    else q('INSERT INTO requests(id,job_id,player_id,msg,status,created) VALUES(?,?,?,?,?,?)', [uid(10), $j['id'], $m['id'], $msgTxt, 'pending', now()]);
    out(['ok' => true, 'job' => jobRow($j, $m)]);
  }

  case 'job.leave': {
    if ($method !== 'POST') fail('Metoda niedozwolona', 405);
    $m = me(); $b = body();
    limit('leave', 30, 3600);
    q('UPDATE requests SET status="left" WHERE job_id=? AND player_id=? AND status IN ("pending","accepted")', [clean($b['id'] ?? '', 16), $m['id']]);
    out(['ok' => true]);
  }

  case 'request.decide': {
    if ($method !== 'POST') fail('Metoda niedozwolona', 405);
    $m = me(); $b = body();
    $r = one('SELECT r.*, j.owner_id, j.slots, j.title, j.status jstatus, j.start_at FROM requests r JOIN jobs j ON j.id=r.job_id WHERE r.id=?', [clean($b['id'] ?? '', 16)]);
    if (!$r) fail('Nie ma takiego zgłoszenia.', 404, 'not_found');
    if ($r['owner_id'] !== $m['id']) fail('O składzie decyduje gospodarz zlecenia.', 403, 'forbidden');
    limit('decide', 120, 3600);
    if ($r['status'] !== 'pending') fail('To zgłoszenie jest już rozpatrzone.', 409, 'decided');
    if (in_array($r['jstatus'], ['closed', 'hidden'], true) || now() > (int)$r['start_at'] + JOB_TTL) fail('Zlecenie jest już zamknięte.', 409, 'closed');
    $accept = ($b['decision'] ?? '') === 'accept';
    if ($accept) {
      $taken = 1 + (int)one('SELECT COUNT(*) c FROM requests WHERE job_id=? AND status="accepted"', [$r['job_id']])['c'];
      if ($taken >= (int)$r['slots']) fail('Skład jest już pełny.', 409, 'full');
    }
    q('UPDATE requests SET status=?, decided=? WHERE id=? AND status="pending"', [$accept ? 'accepted' : 'declined', now(), $r['id']]);
    if ($accept) {
      $p = one('SELECT nick FROM players WHERE id=?', [$r['player_id']]);
      event('accept', ['nick' => $p['nick'] ?? '', 'title' => $r['title'], 'jobId' => $r['job_id']]);
    }
    out(['ok' => true]);
  }

  /* --- respekt (reputacja) --- */
  case 'vouch': {
    if ($method !== 'POST') fail('Metoda niedozwolona', 405);
    $m = me(); $b = body();
    $to = clean($b['to'] ?? '', 16); $jobId = clean($b['jobId'] ?? '', 16);
    if ($to === $m['id']) fail('Nie możesz ocenić samego siebie.');
    limit('vouch', 30, 3600);
    $j = one('SELECT * FROM jobs WHERE id=?', [$jobId]);
    if (!$j || (int)$j['start_at'] > now() - 900) fail('Ocenę wystawisz po wspólnej grze – najwcześniej 15 minut po starcie.', 409, 'too_early');
    if ((int)$j['closed_at'] && (int)$j['closed_at'] < (int)$j['start_at']) fail('To zlecenie zostało odwołane przed startem.', 409, 'cancelled');
    if ($j['status'] === 'hidden') fail('To zlecenie zostało ukryte przez moderację.', 409, 'hidden');
    if (one('SELECT 1 FROM vouches WHERE from_id=? AND to_id=? AND created>?', [$m['id'], $to, now() - 7 * 86400])) fail('Ten gracz ma już od Ciebie ocenę w tym tygodniu.', 409, 'weekly');
    if (now() > (int)$j['start_at'] + VOUCH_WINDOW) fail('Minęło 48 godzin od startu – czas na ocenę już się skończył.', 409, 'too_late');
    $inJob = fn($pid) => $j['owner_id'] === $pid || one('SELECT 1 FROM requests WHERE job_id=? AND player_id=? AND status="accepted" AND decided<=?', [$jobId, $pid, (int)$j['start_at']]);
    if (!$inJob($m['id']) || !$inJob($to)) fail('Ocenić możesz tylko graczy z Twojego składu.', 403, 'forbidden');
    $ins = q('INSERT OR IGNORE INTO vouches(from_id,to_id,job_id,created) VALUES(?,?,?,?)', [$m['id'], $to, $jobId, now()]);
    if ($ins->rowCount()) {
      q('UPDATE players SET rep=rep+1 WHERE id=?', [$to]);
      $tp = one('SELECT nick FROM players WHERE id=?', [$to]);
      event('vouch', ['nick' => $tp['nick'] ?? '', 'from' => $m['nick']]);
    }
    out(['ok' => true]);
  }

  case 'leaderboard': {
    $period = $_GET['period'] ?? 'week';
    $since = $period === 'all' ? 0 : now() - ($period === 'month' ? 30 : 7) * 86400;
    $plat = in_array($_GET['platform'] ?? '', PLATFORMS, true) ? $_GET['platform'] : null;
    $sql = 'SELECT p.*, COUNT(v.from_id) score FROM vouches v JOIN players p ON p.id=v.to_id WHERE v.created>=? AND p.banned=0' . ($plat ? ' AND p.platform=?' : '') . ' GROUP BY p.id ORDER BY score DESC, p.rep DESC LIMIT 50';
    $rows = all($sql, $plat ? [$since, $plat] : [$since]);
    $crews = all('SELECT c.*, COALESCE(SUM(p.rep),0) score, COUNT(p.id) cnt FROM crews c JOIN crew_members m ON m.crew_id=c.id JOIN players p ON p.id=m.player_id GROUP BY c.id ORDER BY score DESC LIMIT 20');
    out(['ok' => true,
      'players' => array_map(fn($p) => pubPlayer($p) + ['score' => (int)$p['score']], $rows),
      'crews' => array_map(fn($c) => ['id' => $c['id'], 'name' => $c['name'], 'tag' => $c['tag'], 'color' => (int)$c['color'], 'platform' => $c['platform'], 'score' => (int)$c['score'], 'count' => (int)$c['cnt']], $crews)]);
  }

  /* --- ekipy (crews) --- */
  case 'crews': {
    $m = me(false);
    $where = '1=1'; $p = [];
    if (in_array($_GET['platform'] ?? '', PLATFORMS, true)) { $where .= ' AND platform=?'; $p[] = $_GET['platform']; }
    if (!empty($_GET['recruiting'])) $where .= ' AND recruiting=1';
    $rows = all("SELECT * FROM crews WHERE $where ORDER BY created DESC LIMIT 100", $p);
    $list = array_map(fn($c) => crewRow($c, $m), $rows);
    usort($list, fn($x, $y) => $y['rep'] <=> $x['rep'] ?: $y['count'] <=> $x['count']);
    out(['ok' => true, 'crews' => $list]);
  }

  case 'crew': {
    $m = me(false);
    $c = one('SELECT * FROM crews WHERE id=?', [clean($_GET['id'] ?? '', 16)]);
    if (!$c) fail('Nie ma takiej ekipy.', 404, 'not_found');
    out(['ok' => true, 'crew' => crewRow($c, $m)]);
  }

  case 'crew.create': {
    if ($method !== 'POST') fail('Metoda niedozwolona', 405);
    $m = me(); $b = body();
    limit('crew', 3, 3600);
    if (one('SELECT 1 FROM crew_members WHERE player_id=?', [$m['id']])) fail('Już jesteś w ekipie. Najpierw z niej odejdź.', 409, 'in_crew');
    $name = clean($b['name'] ?? '', 28);
    if (mb_strlen($name) < 3) fail('Nazwa ekipy musi mieć co najmniej 3 znaki.');
    if (one('SELECT 1 FROM crews WHERE name_lc=?', [mb_strtolower($name)])) fail('Ekipa o tej nazwie już istnieje.', 409, 'taken');
    $tag = strtoupper(preg_replace('/[^A-Za-z0-9]/', '', strtr((string)($b['tag'] ?? ''), ['ą'=>'a','ć'=>'c','ę'=>'e','ł'=>'l','ń'=>'n','ó'=>'o','ś'=>'s','ź'=>'z','ż'=>'z','Ą'=>'A','Ć'=>'C','Ę'=>'E','Ł'=>'L','Ń'=>'N','Ó'=>'O','Ś'=>'S','Ź'=>'Z','Ż'=>'Z'])) ?? '');
    if (hasLink($name . ' ' . (string)($b['details'] ?? ''))) fail('Bez linków w opisie ekipy.');
    if (strlen($tag) < 2 || strlen($tag) > 4) fail('Tag ekipy: 2–4 litery lub cyfry, np. KRK.');
    $id = uid(8);
    q('INSERT INTO crews(id,name,name_lc,tag,details,platform,focus,owner_id,recruiting,color,created) VALUES(?,?,?,?,?,?,?,?,?,?,?)', [
      $id, $name, mb_strtolower($name), $tag, cleanMulti($b['details'] ?? '', 300), pick($b['platform'] ?? $m['platform'], PLATFORMS, $m['platform']),
      pick($b['focus'] ?? '', ACTIVITIES, 'heist'), $m['id'], !empty($b['recruiting']) ? 1 : 0, max(0, min(5, (int)($b['color'] ?? 0))), now(),
    ]);
    q('INSERT INTO crew_members(crew_id,player_id,role,created) VALUES(?,?,?,?)', [$id, $m['id'], 'boss', now()]);
    event('crew', ['nick' => $m['nick'], 'crew' => $name, 'crewId' => $id]);
    out(['ok' => true, 'crew' => crewRow(one('SELECT * FROM crews WHERE id=?', [$id]), $m)]);
  }

  case 'crew.join': {
    if ($method !== 'POST') fail('Metoda niedozwolona', 405);
    $m = me(); $b = body();
    limit('crewjoin', 10, 3600);
    $c = one('SELECT * FROM crews WHERE id=?', [clean($b['id'] ?? '', 16)]);
    if (!$c) fail('Nie ma takiej ekipy.', 404, 'not_found');
    if (!(int)$c['recruiting']) fail('Ta ekipa nie prowadzi teraz rekrutacji.', 409, 'closed');
    if (one('SELECT 1 FROM crew_members WHERE player_id=?', [$m['id']])) fail('Już jesteś w ekipie. Najpierw z niej odejdź.', 409, 'in_crew');
    if ((int)one('SELECT COUNT(*) c FROM crew_members WHERE crew_id=?', [$c['id']])['c'] >= 50) fail('Ekipa ma komplet – 50 osób.', 409, 'full');
    q('INSERT INTO crew_members(crew_id,player_id,role,created) VALUES(?,?,?,?)', [$c['id'], $m['id'], 'member', now()]);
    event('crewjoin', ['nick' => $m['nick'], 'crew' => $c['name'], 'crewId' => $c['id']]);
    out(['ok' => true, 'crew' => crewRow($c, $m)]);
  }

  case 'crew.leave': {
    if ($method !== 'POST') fail('Metoda niedozwolona', 405);
    $m = me();
    $mem = one('SELECT * FROM crew_members WHERE player_id=?', [$m['id']]);
    if (!$mem) out(['ok' => true]);
    if ($mem['role'] === 'boss') {
      $next = one('SELECT m.player_id FROM crew_members m JOIN players p ON p.id=m.player_id WHERE m.crew_id=? AND m.player_id!=? ORDER BY p.rep DESC LIMIT 1', [$mem['crew_id'], $m['id']]);
      if ($next) {
        q('UPDATE crew_members SET role="boss" WHERE crew_id=? AND player_id=?', [$mem['crew_id'], $next['player_id']]);
        q('UPDATE crews SET owner_id=? WHERE id=?', [$next['player_id'], $mem['crew_id']]);
      } else {
        q('DELETE FROM crews WHERE id=?', [$mem['crew_id']]);
      }
    }
    q('DELETE FROM crew_members WHERE player_id=?', [$m['id']]);
    out(['ok' => true]);
  }

  case 'crew.update': {
    if ($method !== 'POST') fail('Metoda niedozwolona', 405);
    $m = me(); $b = body();
    $c = one('SELECT * FROM crews WHERE owner_id=?', [$m['id']]);
    if (!$c) fail('Nie jesteś szefem żadnej ekipy.', 403, 'forbidden');
    q('UPDATE crews SET details=?, recruiting=? WHERE id=?', [cleanMulti($b['details'] ?? $c['details'], 300), array_key_exists('recruiting', $b) ? (!empty($b['recruiting']) ? 1 : 0) : (int)$c['recruiting'], $c['id']]);
    out(['ok' => true, 'crew' => crewRow(one('SELECT * FROM crews WHERE id=?', [$c['id']]), $m)]);
  }

  /* --- moderacja --- */
  case 'report': {
    if ($method !== 'POST') fail('Metoda niedozwolona', 405);
    $m = me(); $b = body();
    limit('report', 10, 3600);
    $type = pick($b['type'] ?? '', ['job', 'player', 'crew'], null);
    if (!$type) fail('Nieprawidłowe zgłoszenie.');
    $tid = clean($b['id'] ?? '', 16);
    $table = ['job' => 'jobs', 'player' => 'players', 'crew' => 'crews'][$type];
    if (!one("SELECT 1 FROM $table WHERE id=?", [$tid])) fail('Nie ma czego zgłaszać.', 404, 'not_found');
    $reason = pick($b['reason'] ?? '', ['spam', 'scam', 'toxic', 'cheats', 'other'], 'other');
    if (!one('SELECT 1 FROM reports WHERE reporter_id=? AND target_type=? AND target_id=?', [$m['id'], $type, $tid])) {
      q('INSERT INTO reports(reporter_id,target_type,target_id,reason,created) VALUES(?,?,?,?,?)', [$m['id'], $type, $tid, $reason, now()]);
    }
    // auto-ukrycie zlecenia po 3 zgłoszeniach od różnych kont starszych niż 1 h
    if ($type === 'job') {
      $n = (int)one('SELECT COUNT(DISTINCT r.reporter_id) c FROM reports r JOIN players p ON p.id=r.reporter_id WHERE r.target_type="job" AND r.target_id=? AND r.resolved=0 AND p.created<?', [$tid, now() - 3600])['c'];
      if ($n >= 3) q('UPDATE jobs SET status="hidden" WHERE id=? AND status NOT IN ("closed")', [$tid]);
    }
    out(['ok' => true]);
  }

  case 'admin.reports': {
    if (!isAdmin()) fail('Brak dostępu.', 403, 'forbidden');
    out(['ok' => true, 'reports' => all('SELECT * FROM reports WHERE resolved=0 ORDER BY id DESC LIMIT 200')]);
  }
  case 'admin.unhide': {
    if (!isAdmin()) fail('Brak dostępu.', 403, 'forbidden');
    $b = body();
    q('UPDATE jobs SET status="open" WHERE id=? AND status="hidden"', [clean($b['id'] ?? '', 16)]);
    q('UPDATE reports SET resolved=1 WHERE target_type="job" AND target_id=?', [clean($b['id'] ?? '', 16)]);
    out(['ok' => true]);
  }
  case 'admin.resolve': {
    if (!isAdmin()) fail('Brak dostępu.', 403, 'forbidden');
    $b = body();
    q('UPDATE reports SET resolved=1 WHERE id=?', [(int)($b['rid'] ?? 0)]);
    out(['ok' => true]);
  }
  case 'admin.ban': {
    if (!isAdmin()) fail('Brak dostępu.', 403, 'forbidden');
    $b = body();
    q('UPDATE players SET banned=1 WHERE id=?', [clean($b['id'] ?? '', 16)]);
    q('UPDATE jobs SET status="closed" WHERE owner_id=?', [clean($b['id'] ?? '', 16)]);
    q('UPDATE reports SET resolved=1 WHERE target_type="player" AND target_id=?', [clean($b['id'] ?? '', 16)]);
    q('DELETE FROM crew_members WHERE player_id=?', [clean($b['id'] ?? '', 16)]);
    out(['ok' => true]);
  }

  /* --- roadmapa --- */
  case 'votes': {
    $m = me(false);
    $counts = [];
    foreach (all('SELECT feature, COUNT(*) c FROM votes GROUP BY feature') as $r) $counts[$r['feature']] = (int)$r['c'];
    out(['ok' => true, 'counts' => $counts, 'mine' => $m ? array_column(all('SELECT feature FROM votes WHERE player_id=?', [$m['id']]), 'feature') : []]);
  }
  case 'vote': {
    if ($method !== 'POST') fail('Metoda niedozwolona', 405);
    $m = me(); $b = body();
    limit('vote', 60, 3600);
    $f = pick($b['feature'] ?? '', FEATURES, null);
    if (!$f) fail('Nieznana funkcja.');
    if (!empty($b['on'])) q('INSERT OR IGNORE INTO votes(player_id,feature) VALUES(?,?)', [$m['id'], $f]);
    else q('DELETE FROM votes WHERE player_id=? AND feature=?', [$m['id'], $f]);
    out(['ok' => true]);
  }

  default:
    fail('Nieznana akcja.', 404, 'not_found');
  }
} catch (PDOException $e) {
  error_log('[ekipaz] ' . $e->getMessage());
  fail('Serwer chwilowo nie odpowiada. Spróbuj ponownie za moment.', 500, 'server');
} catch (TypeError | ValueError $e) {
  fail('Nieprawidłowe dane w żądaniu.', 400, 'bad_request');
} catch (Throwable $e) {
  error_log('[ekipaz] ' . $e->getMessage());
  fail('Coś poszło nie tak po stronie serwera.', 500, 'server');
}
