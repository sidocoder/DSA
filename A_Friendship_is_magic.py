n = int(input())
mishka = 0
chris = 0
for _ in range(n):
    m,c = map(int,input().split())
    if m > c:
        mishka += 1
    elif c > m:
        chris += 1
    
if chris > mishka:
    print("Chris")
elif mishka > chris:
    print("Mishka")
else:
    print("Friendship is magic!^^")