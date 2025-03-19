def min_kicks_to_decide(s):
    first_team = second_team = 0
    def team(first):
        team1_remaining = team2_remaining = 5  

        for i in range(10):
            if all(char == '?' for char in s):
                return 6
            if i % 2 == 0:  
                if s[i] == '1' or s[i] == '?' and first_team:
                    first_team += 1
                team1_remaining -= 1
            else:  
                if s[i] == '1' or s[i] == '?' and second_team:
                    second_team += 1
                team2_remaining -= 1

        
            if first_team > second_team + team2_remaining:
                return i + 1
            elif second_team > first_team + team1_remaining:
                return i + 1

    return 10  

t = int(input())
for _ in range(t):
    s = input().strip()
    print(min_kicks_to_decide(s))
