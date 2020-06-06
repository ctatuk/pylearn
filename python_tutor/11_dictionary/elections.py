def usa_elections(state_elections):
    elections_result = {}
    for n, m in state_elections:
        if n in elections_result.keys():
            tmp = elections_result.pop(n) + m
            elections_result[n] = tmp
        else:
            elections_result[n] = m
    print(sorted(elections_result.items()))


def usa_elections2(state_elections):
    candidates = {c for c, v in state_elections}
    elections_result = {candidate: sum([v for c, v in state_elections if c == candidate]) for candidate in candidates}
    print(elections_result)


def usa_elections3(state_elections):
    from collections import defaultdict
    d = defaultdict(int)
    for c, v in state_elections:
        d[c] += v
    print(d.items())


usa_elections([('m', 13), ('o', 76), ('m', 54), ('m', 7)])
usa_elections2([('m', 13), ('o', 76), ('m', 54), ('m', 7)])
usa_elections3([('m', 13), ('o', 76), ('m', 54), ('m', 7)])
