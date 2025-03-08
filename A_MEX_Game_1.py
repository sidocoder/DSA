from collections import Counter


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    num_dict = Counter(a)

    alice = 0
    mex = 0
    index = 0
    for key in num_dict:
        if index % 2 != 0:
            num_dict[key] -= 1
            if num_dict[key] == 0:
                print(key)
                return
        index += 1
    if num_dict[0] == 0:
        print(0)
        return
    print(a[-1] + 1)

t = int(input())
for _ in range(t):
    solve()