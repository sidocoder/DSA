n = int(input())
cards = list(map(int, input().split()))

indexed_cards = [(value, idx + 1) for idx, value in enumerate(cards)]

indexed_cards.sort()

for i in range(n // 2):
    print(indexed_cards[i][1], indexed_cards[n - 1 - i][1])
