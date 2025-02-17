# from collections import Counter

# def arraytransformation(nums):
#     hashh = Counter(nums)
#     count = 0
#     for key, value in hashh.items():
#         if key == 1 and value >= 2:
#             count += 1
#             break

#         elif key == value:
#             count += 1
#     return count if count > 0 else 1

# n = int(input())  
# for _ in range(n):
#     length = int(input())  
#     nums = list(map(int, input().split()))  # Read the list at once
#     result = arraytransformation(nums)
#     print(result)







from collections import Counter

def min_removals_to_beautiful(n, arr):
    hashh = Counter(arr)  
    freq_count = Counter(hashh.values())      
    total_elements = n
    min_rem = n  
    removed = 0
    
    
    for count, num_elements in sorted(freq_count.items()):
        
        removals = removed + (total_elements - count * num_elements)
        min_rem = min(min_rem, removals)
        
    
        removed += num_elements * count
        total_elements -= num_elements * count
    
    return min_rem

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(min_removals_to_beautiful(n, arr))
