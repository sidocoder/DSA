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
#-------------------------------------------------AVERAGE OF ELEMENTS------------------------------------
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

card = list()
card.append("H")
card.append("e")
card.append("l")
card.append("l")
card.append("o")
reverse = card[::-1]
print(reverse)

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
print'''
#-----------------------SORT DICTIONARY-----------------------------------------
d = {"a":3, "c":2, "b":5}
t = sorted(d.items())
print(t)
for a,b in t:
    print(a,b)


c = {'a':10, 'b': 1,'c':3}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
tmp.sort( reverse=True)
print(tmp)

