# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))

#     summ = 0
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 summ += (a[i] & a[j]) * (a[j] | a[k])
#     print(summ)


import sys
input = sys.stdin.read

MOD = 10 ** 9 + 7
data = input().split()
idx = 0

t = int(data[idx])
idx += 1

for _ in range(t):
    n = int(data[idx])
    idx += 1
    a = list(map(int, data[idx:idx + n]))
    idx += n

    cnt = [0] * 60  
    for x in a:
        for b in range(60):
            if (x >> b) & 1:
                cnt[b] += 1

    result = 0
    for j in range(n):
        and_sum = 0
        or_sum = 0
        for b in range(60):
            p = (1 << b) % MOD
            if (a[j] >> b) & 1:
                and_sum = (and_sum + cnt[b] * p) % MOD
                or_sum = (or_sum + n * p) % MOD
            else:
                or_sum = (or_sum + cnt[b] * p) % MOD
        result = (result + and_sum * or_sum) % MOD

    print(result)
