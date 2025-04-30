t = int(input())
for _ in range(t):
    n = int(input())
    string = input()

    orders = []
    for char in string:        
        orders.append(ord(char.upper()) - ord('A') + 1)

    diff = 26 - max(orders)
    print(26 - diff)