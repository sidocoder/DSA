# t = int(input())
# for _ in range(t):
#     n = int(input())
#     nums = list(map(int, input().split()))

#     if n % 2 != 0:
#         pre = [0]
#         curr = 0
#         for i in range(n):
#             curr ^= nums[i]
#             pre.append(curr)
#         print(pre[-1])
#     else:

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total_xor = 0
    for num in a:
        total_xor ^= num
    if n % 2 == 0:
        if total_xor == 0:
            print(0)
        else:
            print(-1)
    else:
        print(total_xor)

