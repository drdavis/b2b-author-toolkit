"""Mechanical quote check for a B2B Author Toolkit book folder.

Interview quotes (a quote followed by [mm:ss]) must be exact transcript words:
segments split on ' … ' / ' ... ' must each appear in the joined transcript text,
and the [mm:ss] must be the start of the line where the first segment begins.
Research quotes (in '## From research') must appear, after light
normalization, somewhere in the research corpus.

Usage: python3 -I check_quotes.py "<book folder>"   -> JSON list of problems on stdout; [] means none
       python3 -I check_quotes.py --selftest     -> proves a wrong quote and a wrong timestamp are caught
"""
import json, re, sys, glob, os

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
LINE = re.compile(r'^\[((?:\d+:)?\d\d:\d\d) - (?:\d+:)?\d\d:\d\d\] ([^:]+): (.*)$')  # mm:ss or h:mm:ss
QUOTE = re.compile(r'["“]([^"“”]{6,}?)["”]')
TS = re.compile(r'\[((?:\d+:)?\d\d:\d\d)\]')


def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('…', '...').replace('\u00a0', ' ')
    return re.sub(r'\s+', ' ', s).strip()


def load_transcripts():
    out = {}
    for p in glob.glob(os.path.join(ROOT, 'Research/Transcripts/*.md')):
        lines = []
        for raw in open(p, encoding='utf-8'):
            m = LINE.match(raw.rstrip('\n'))
            if m:
                lines.append((m.group(1), m.group(2), m.group(3)))
        joined, starts, pos = [], [], 0
        for ts, spk, txt in lines:
            starts.append(pos)
            joined.append(norm(txt))
            pos += len(norm(txt)) + 1
        out[os.path.basename(p)] = (lines, ' '.join(joined), starts)
    return out


def line_at(starts, pos):
    lo, hi = 0, len(starts) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if starts[mid] <= pos:
            lo = mid
        else:
            hi = mid - 1
    return lo


def segments(q):
    parts = re.split(r'\s*(?:…|\.\.\.)\s*', q)
    return [p.strip() for p in parts if len(p.strip()) >= 3]


def check_interview_quote(q, ts, transcripts):
    segs = segments(norm(q))
    if not segs:
        return None
    best, mismatch = None, None
    for name, (lines, text, starts) in transcripts.items():
        found = [text.find(s) for s in segs]
        if all(f >= 0 for f in found):
            i = line_at(starts, found[0])
            # the same words can sit in two transcripts of one call; any exact hit passes
            if lines[i][0] == ts:
                return {'ok': True, 'transcript': name, 'expected_ts': ts, 'given_ts': ts, 'problem': None}
            mismatch = mismatch or {'ok': False, 'transcript': name, 'expected_ts': lines[i][0],
                                    'given_ts': ts, 'problem': 'timestamp'}
            continue
        n = sum(f >= 0 for f in found)
        if best is None or n > best[0]:
            best = (n, name, [s for s, f in zip(segs, found) if f < 0])
    if mismatch:
        return mismatch
    return {'ok': False, 'problem': 'words not in transcript', 'closest': best[1] if best else None,
            'missing_segments': best[2] if best else segs}


def corpus():
    files = []
    for pat in ['Research/**/*.csv', 'Research/**/*.json', 'Research/**/*.md', '01 Planning/*.md']:
        files += [f for f in glob.glob(os.path.join(ROOT, pat), recursive=True) if not f.endswith('Quote Bank.md')]
    text = []
    for p in files:
        try:
            raw = open(p, encoding='utf-8').read()
        except Exception:
            continue
        if p.endswith('.json'):
            raw = raw.encode().decode('unicode_escape', errors='ignore') if '\\u' in raw else raw
            raw = raw.replace('\\n', ' ').replace('\\"', '"')
        text.append(norm(raw))
    return ' \n '.join(text)


def strip_end(s):
    return s.rstrip(' .,;:!?')


def main():
    transcripts = load_transcripts()
    big = corpus()
    report = []
    files = sorted(glob.glob(os.path.join(ROOT, 'Chapters/*.md'))) + [
        os.path.join(ROOT, 'Research/Quote Bank.md')] + sorted(glob.glob(os.path.join(ROOT, '02 Interviews/20*.md')))
    for p in files:
        section = ''
        for n, raw in enumerate(open(p, encoding='utf-8'), 1):
            line = raw.rstrip('\n')
            if line.startswith('## '):
                section = line[3:].strip()
            if section.startswith('Outline'):
                continue
            for m in QUOTE.finditer(line):
                q = m.group(1).strip()
                after = line[m.end():m.end() + 40]
                tsm = TS.search(after)
                is_interview = bool(tsm) and after.lstrip().startswith('[')
                if is_interview:
                    r = check_interview_quote(q, tsm.group(1), transcripts)
                    if r is None:
                        continue
                    if not r['ok']:
                        report.append({'file': os.path.relpath(p, ROOT), 'line': n, 'kind': 'interview', 'quote': q, **r})
                elif section in ('From research',) or 'Quote Bank' in p:
                    nq = strip_end(norm(q))
                    segs = [strip_end(s) for s in re.split(r'\s*\.\.\.\s*', nq) if len(s.strip()) >= 4]
                    missing = [s for s in segs if s not in big]
                    if missing:
                        report.append({'file': os.path.relpath(p, ROOT), 'line': n, 'kind': 'online', 'quote': q,
                                       'ok': False, 'problem': 'not found in research corpus', 'missing_segments': missing})
    print(json.dumps(report, ensure_ascii=False, indent=1))


def selftest():
    lines = [('01:00', 'A', 'First line here.'), ('01:05', 'A', 'Second line says something exact.')]
    text = ' '.join(norm(l[2]) for l in lines)
    tr = {'t.md': (lines, text, [0, len(norm(lines[0][2])) + 1])}
    assert check_interview_quote('Second line says something exact.', '01:05', tr)['ok']
    assert check_interview_quote('First line … something exact', '01:00', tr)['ok']
    assert check_interview_quote('Second line says something exact.', '01:00', tr)['problem'] == 'timestamp'
    assert check_interview_quote('Second line says nothing at all.', '01:05', tr)['problem'] == 'words not in transcript'
    assert LINE.match('[1:02:24 - 1:02:33] A: Late line.') and TS.search('x [1:02:24]').group(1) == '1:02:24'
    print('selftest ok')


if __name__ == '__main__':
    selftest() if ROOT == '--selftest' else main()
