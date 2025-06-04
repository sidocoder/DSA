t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

#     for i in range(n):
#         for j in range(i + 1, n):
#             _or = a[i] | a[j]
#             _min = min(a[i], a[j])
#             _max = max(a[i], a[j])
#             b_or = str(bin(_or))
#             b_max = str(bin(_max))
#             b_min = str(bin(_min))
           
#             b_x = str(bin(0)) * 32
#             for a in range(32):
#                 if b_or[a] == '1' and b_min[a] == '1':
#                     b_x[a] = '0'

#                 if b_or[a] == '1' and b_min[a] == '0':
#                     b_x[a] = '1'

#                 if b_or[a] == '0' and b_min[a] == '0':
#                     b_x[a] = '0'


#             inx = a.index(_max)
#             a[inx] = int(b_x)
#     print(sum(a))

    result = 0
    for num in a:
        result |= num
    print(result)

            

