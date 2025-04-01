from bisect import bisect_right

def solve(s, b, spaceship_powers, bases):
    bases.sort()
    cumulative_gold = [0] * (b + 1)
    for i in range(b):
        cumulative_gold[i + 1] = cumulative_gold[i] + bases[i][1]
    
    result = []
    for spaceship_power in spaceship_powers:
        idx = bisect_right([base[0] for base in bases], spaceship_power) - 1
        result.append(cumulative_gold[idx + 1])
    
    return result

s, b = map(int, input().split())
spaceship_powers = list(map(int, input().split()))
bases = [tuple(map(int, input().split())) for _ in range(b)]

result = solve(s, b, spaceship_powers, bases)

print(' '.join(map(str, result)))
