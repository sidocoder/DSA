t = int(input())
def median(arr):
    if arr:
        arr.sort()
        left = 0
        right = len(arr) -1
        mid = left + (right - left) // 2
        return arr[mid]
    return 
def find_combinations(nums, target, n):
    result = []
    nums.sort()  # Optional: sort to help with optimization
    
    def backtrack(start, target, current_combination):
        # Base case: if the combination has 'n' elements
        if len(current_combination) == n:
            if target == 0:  # If the sum of selected numbers equals the target
                result.append(list(current_combination))  # Add the valid combination
            return
        
        # Explore further combinations
        for i in range(start, len(nums)):
            # Skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue
            # Add the current number and recurse
            current_combination.append(nums[i])
            backtrack(i + 1, target - nums[i], current_combination)
            current_combination.pop()
    backtrack(0, target, [])
    return result  # Backtrack by removing the number
    
    



for _ in range(t):
    n, s = map(int, input().split())
    
    if n == 1:
        print(s)
        continue

    if n > s:
        print(0)
        continue

    query = list(range(1, s + 1))
    query.sort()

    ans = []
    ans.append(find_combinations(0,s,[]))
        
    print(median(ans))

#     if not ans:
#         print(0)
#     else:
#         print(median(ans))

# # t = int(input())

# # for _ in range(t):
# #     n, s = map(int, input().split())
    
# #     # The median position in a sorted array (1-indexed)
# #     median_pos = (n + 1) // 2
    
# #     # The maximum possible value for the median
# #     max_median = s // median_pos
    
# #     # Output the result
# #     print(max_median)
