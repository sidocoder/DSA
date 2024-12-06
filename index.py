"""#sum
def sum(num, num2):
    return num + num2

print(sum(3, 8))
#--------------------------------------------- excutes a fabonicci numbers for a given range-------------------------------------------------------------------
start = 0
end = 1
print(start)
print(end)

for i in range(8):
    newnum = start + end
    print(newnum)
    start = end
    end = newnum
#---------------------------------fabonnicci using recursion that excutes the fabonicci number when enter its index----------------------------------
def F(n):
    if n <= 1:
        return n
    else:
        return F(n-1)+ F(n-2)
print(F(5))

count =2
def fabon(start, end):
    global count
    if count <= 19:
        newfab = start + end
        print(newfab)
        start = end
        end = newfab
        count +=1
    else: 
        return
print(fabon(3,4))

arr=[34,302,586,32]
for i in range(len(arr)):
    if arr[i]==301:
        return i
for i in range arr:
    print(i)
# -------------------------------------inserting a number in array----------------------------------------
import array as arr
a = arr.array('i', [1,2,3])
print("the array before insertion contains:", end=" ")
for i in range (len(a)):
    print(a[i], end=" ")#------end is used space between the outputs like text
a.insert(2,5)
print() #---------this is used to add new line
print("the array after insertion contains:", end=" ")
for i in range (len(a)):
    print(a[i], end=" ")
#--------------------------------removing an element from array-------------------------------------------
import array
arr = array.array('i', [1, 2, 3, 1, 5])
print("The new created array is : ", end="")
for i in range(0, 5):
    print(arr[i], end=" ")

print("\r")
print("The popped element is : ", end="")
print(arr.pop(2))
print("The array after popping is : ", end="")
for i in range(0, 4):
    print(arr[i], end=" ")

print("\r")
arr.remove(1)
print("The array after removing is : ", end="")
for i in range(0, 3):
    print(arr[i], end=" ")

#-------------------------------------------SLICING ARRAY--------------------------------------------
import array
arr = array.array('i', [1,2,3,4,5,6])
subset = arr[1:4]
print(subset)
subset = arr[1::2]
print(subset)
subset= arr[::-1]
print(subset)
subset = arr[::-2]
print(subset)
for i in range(1,6):
    print(i * "*")
    print()
print(8)
print(13, end=" ")
print(21)

#-----------------------------------
import array
arr = array.array('i',[1,2,3,4,5])
for i in range(5):
    new_num = arr[i] * arr[i]
    print(arr[i],"-",new_num)
x = int(input(""))
y = int(input(""))
cust = x * y
if 1 <= x <= 100 and 1 <= y <= 100:
    print(cust)
else:
    print("invalid")
  
n = int(input(""))
t = n * 2
print(t)
#------------------------------------------COMPARING NUMBERS-----------------------------------------------
x = 62
y = 62
if x > y:
    print("x is greater")
elif y > x:
    print("y is greater")
else:
    print("both are equal")
n = input("")
y = 0
if n <= y:
    print("the number is negative")
elif n == y:
    print("the number is zero")
else:
    print("the number is positive")
arr = [2,3,2,3,4,5]
#----------------------------------REMOVING ELEMENT OF SAME VALUE WITH GIVEN NUMBER---------------------
class Solution(object):
    def removeElement(self, arr, val):
        for i in range(len(arr)):
            while arr[i]== val:
                arr.pop(i)
            else:
                return val
           
        print(arr)
    print(removeElement)
maths = int(input("enter your math score:"))
phys = int(input("enter your phys score:"))
bio = int(input("enter your bio score:"))
average =(maths + phys +bio)/3

print("average is:",average)
# -------------------------------------------------AVERAGE OF ELEMENTS------------------------------------
a=[]
element_number = int(input("enter the number of subjects u learnt:"))
for i in range(element_number):
    user_input = int(input("enter your score in subjects:"))
    user_input = a.append(user_input)
    average = sum(a)/len(a)
print(average)"""
# ----------------------------------------------------FACTORIAL---------------------------------------------
'''def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

       
num = int(input("enter a number:"))
result = factorial(num)
print(result)        
#---------------------------------------------------
class Solution(object):
    def divide(dividend, divisor):
        if dividend > divisor:
            return dividend/ divisor
    num1 = int(input("enter dividend: "))
    num2 = int(input("enter divisor: "))
    result = divide(num1, num2)
    print(int(result))
word = "banana"
j = 0
for letter in word:
    if letter == 'a':
        j = j + 1
print(j)
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])
import array as arr
a = arr.array('i',[2,3,5,5,1])
reverse = a[::-1]
print(reverse)
#----------------------------REVERSE LIST----------------------------
card = list()
card.append("H")
card.append("e")
card.append("l")
card.append("l")
card.append("o")
reverse = card[::-1]
print(reverse)
#--------------------------------------------------------
word = input("enter a word: ")
card = word.split()
reverse = card[::-1]
print(reverse)
print(card)
for word in card:
    print(word, card[0])
counts ={'chunk': 23, 'fred':45}
key = ('chunk', 'fred', 'nuh')
if key in counts:
    counts[key] = counts[key] + 1
else:
    counts[key] = 1
print
#-----------------------SORT DICTIONARY BY KEY(DEFAULT)-----------------------------------------
d = {"a":3, "c":2, "b":5}
t = sorted(d.items())
print(t)
for a,b in t:
    print(a,b)

#-----------SORT DICTIONARY BY VALUE-------------------------
c = {'a':10, 'b': 1,'c':3}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
tmp.sort() # or tmp.sort( reverse=True)----if wanted in reverse
print(tmp)
#----------------------------------------------------------------------
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        dic2 ={}
        for i in range(len(names)):
            dic[names[i]] = heights[i]
            
        tmp = list()   
        tmp2 = list()
        for k,v in dic.items():
            tmp.append((v,k))
        tmp.sort(reverse = True)
        for i, (value, key) in enumerate(tmp):
            dic2[i] = {key: value}
        for key, value in dic2.items():
            tmp2.append(list(value.keys())[0])
            
       
        print(tmp2)
#-----------------------------------------TWOSUM-----------------------------------------------------    
class solution:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        hash = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hash:
                return [hash[diff],i]
            hash[n] = i
        return
'''
class solution:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        l = 0
        r = len(nums) - 1
        for i in range(len(nums)):
            sum = nums[l] + nums[r]
            while l < r:
                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    return l,r


'''
#----------------------------------------------------------------------------------------
c = {'a':10, 'b': 1,'c':3}
value = c[1]
print(value)
'''
#===------------------------------------THREE SUM using three pointer----------------------------------
'''
nums = []
element_number = int(input("enter the number of array: "))
target = int(input("enter a target: "))
for i in range(element_number):
    uinput = int(input("enter an array: "))
    uinput = nums.append(uinput)
    
def threesum(nums, target):  
    nums.sort()
    pointer1 = 0
    pointer2 = 0 + 1
    pointer3 = len(nums) - 1
    while pointer1 < pointer2 < pointer3:
        sum = nums[pointer1] + nums[pointer2] + nums[pointer3]
        if sum == target:
            return list[nums[pointer1],nums[pointer2], nums[pointer3]]
        elif sum < target:
            pointer2 += 1
        elif sum < target:
            pointer1 += 1
        else:
            pointer3 -= 1
    return False
result = threesum(nums, target)
print(result)
'''
#================================THREE SUM =================================
'''from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
#----------------------------------------------------------------------
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        l = i + 1
        r = len(nums) - 1
        for i in range(len(nums)):
            sum = nums[i] + nums[l] + nums[r]
            if sum < 0 or i == l:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                return [nums[i],nums[l], nums[r]]
            return 
    
'''
nums = [1,2,3,4,5]
res = []
res.append([nums[1], nums[3]])
print(res)