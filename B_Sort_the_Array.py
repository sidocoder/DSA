n=int(input())
ls=[int(i) for i in input().split()]
ans=[]
cnt=0
sorted_ls=sorted(ls)

left=0
for i in range(1,len(ls)):
    if ls[i-1]>ls[i]:
        left=i-1
        break
right=0
for i in range(len(ls)-1,-1,-1):
    if ls[i-1]>ls[i]:
        right=i
        break
inv=ls[left + 1:right+1]
nw=inv[::-1]
new=ls[:left]+nw+ls[right+1:]
if new==sorted_ls:
    print("yes")
    print(ls[right],ls[left])
else:
    print("no")