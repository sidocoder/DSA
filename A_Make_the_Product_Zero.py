n = int(input())  
numbers = list(map(int, input().split()))  

minimum = min(map(abs, numbers))  

print(minimum) 
