from collections import Counter

ls = []
with open("inputs/day07.txt") as f:
    for l in f:
        ls.append(l.strip().split())
        ls[-1][1] = int(ls[-1][1])

def rank(h):
    ct = Counter()

    for c in h:
        ct[c] += 1

    k, n = ct.most_common(1)[0]
    if k == 'J':
        if n != 5:
            k2, n2 = ct.most_common(2)[1]
            ct[k2] += ct['J']
            del ct['J']
    else:
        ct[k] += ct["J"]
        del ct["J"]

    vs = sorted(ct.values())

    return [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 2],
        [1, 2, 2],
        [1, 1, 3],
        [2, 3],
        [1, 4],
        [5]
    ].index(vs) + 1

order = "AKQT98765432J"[::-1]
order = str.maketrans(order, ''.join(chr(ord('A') + _) for _ in range(len(order))))

ar = []
for h, b in ls:
    ar.append([h, b, rank(h)])

rs = 0
for n, (_, p, _) in enumerate(sorted(ar, key=lambda _: (_[2], _[0].translate(order)))):
    rs += (n+1) * p

print(rs)