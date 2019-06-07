def solution(m):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    lss = { None: {} }
    def go(l, r, c, ls, removable):
        if not (0 <= r < len(m) and 0 <= c < len(m[r])): return
        if m[r][c]:
            if removable:
                removable = False
                if not (r, c) in lss:
                    lss[r, c] = ls.copy()
                ls = lss[r, c]
            else: return
        if (r, c) in ls and ls[r, c] <= l: return
        ls[r, c] = l
        for dr, dc in dirs:
            go(l + 1, r + dr, c + dc, ls, removable)
    go(1, 0, 0, lss[None], True)
    escape = len(m) - 1, len(m[-1]) - 1
    return min(ls[escape] for ls in lss.viewvalues() if escape in ls)
