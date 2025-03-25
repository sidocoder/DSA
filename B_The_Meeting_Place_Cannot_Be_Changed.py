n = int(input())
friends = list(map(int, input().split()))
speed = list(map(int, input().split()))

def validate():
    min_right = float('inf')
    max_right = float('inf')
    


left = 0
right = max(friends) - min(friends)

while right - left > percision:
    mid = (left+ right) / 2

    if validate(mid):
        right = mid
    else:
        left = mid
    print(left)
