from fractions import Fraction, gcd
from itertools import imap, islice, izip
from operator import mul

def solution(m):
    m = map(list, m)
    to_fractions(m)
    t = canonicalize(m)
    if not t:
        return [1, 1]
    n0 = get_n0(islice((ps[:t] for ps in m), t))
    res = [sum(imap(mul, n0, ps))
           for ps in izip(*islice((ps[t:] for ps in m), t))]
    lcd = reduce(lambda x, y: (x * y) / gcd(x, y),
                 (p.denominator for p in res), 1)
    return [int(p * lcd) for p in res] + [lcd]

def to_fractions(m):
    for r, ps in enumerate(m):
        s = sum(ps)
        if s:
            m[r] = [Fraction(p, s) for p in ps]

def canonicalize(m):
    rt = 0
    while any(m[rt]):
        rt += 1
    for r in xrange(rt + 1, len(m)):
        if any(m[r]):
            m[rt], m[r] = m[r], m[rt]
            for ps in m:
                ps[rt], ps[rt + 1:r + 1] = ps[r], ps[rt:r]
            rt += 1
    return rt

def get_n0(q):
    aug = map(list, izip(*([(1 if r == c else 0) - p for c, p in enumerate(ps)]
                           for r, ps in enumerate(q))))
    aug[0].append(1)
    for ps in aug[1:]:
        ps.append(0)
    rref(aug)
    return [ps[-1] for ps in aug]

def rref(m):
    l = 0
    nr = len(m)
    nc = len(m[0])
    for r in xrange(nr):
        if l >= nc:
            return
        i = r
        while not m[i][l]:
            i += 1
            if i == nr:
                i = r
                l += 1
                if l == nc:
                    return
        m[i], m[r] = m[r], m[i]
        if m[r][l]:
            m[r] = [x / m[r][l] for x in m[r]]
        for j in xrange(nr):
            if j != r:
                m[j] = map(lambda jx, rx: jx - m[j][l] * rx, m[j], m[r])
        l += 1
