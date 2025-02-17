def arrange(row, target_diff, heights):
    heights.sort()
    first_row = heights[:row]
    second_row = heights[row:]

    first, second = 0,0

    while first < len(first_row) and second < len(second_row):
        diff = second_row[second] - first_row[first]
        if diff < target_diff:
            return 'NO'
        else:
            return 'YES'
t = int(input())
for i in range(t):
    n,x = map(int, input().split())
    heights = list(map(int, input().split()))
    print(arrange(n,x,heights))
