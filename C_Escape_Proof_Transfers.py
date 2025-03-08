n,t,c = map(int, input().split())
nums = list(map(int,input().split()))

# right = 0
# left = 0
# while right < len(nums) and left < right:
#     length = (right - left + 1)
#     # if nums[right] > t:
#     #     right += 1
#     #     left += 1
#     if nums[right] <= t and length == c:
#         count += 1
#         left += 1
#         right += 1
#     right += 1
   

count = 0
left = 0

for right in range(n):
    if nums[right] > t:
        left = right + 1
    elif right - left + 1 == c:
        count += 1
        left += 1

print(count)





