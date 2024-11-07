from itertools import combinations, repeat


def all_variants(text):
    for r in range(1, len(text) + 1):
        for comb in combinations(text, r):
            yield ''.join(comb)
a = all_variants("abc")
for i in a:
    print(i)