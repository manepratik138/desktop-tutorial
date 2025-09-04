#Create a list of 5 fruits and print the second fruit.
fruits=["apple","banana","custerred apple","cherry","pineapple"]
print(fruits[1])

#Find the length of this list: [10, 20, 30, 40, 50].
num=[10,20,30,40,50]
print(len(num))

#Add "Mango" at the end of the list ["Apple", "Banana", "Orange"].
fruits=["apple","banana","orange"]
fruits.append("mango")
print(fruits)

#Insert "Watermelon" at position 2 in the list ["Apple", "Banana", "Orange"].
friuts=["Apple", "Banana", "Orange"]
fruits.insert(2,"waterlemon")
print(fruits)

#Remove "Banana" from the list ["Apple", "Banana", "Orange"].
fruits=["Apple", "Banana", "Orange"]
fruits.remove("Banana")
print(fruits)

#Reverse the list [1, 2, 3, 4, 5] without using reverse() or slicing.
num=[1,2,3,4,5]
num.reverse()
print(num)

#Find the largest number in the list [10, 25, 5, 90, 45].
nums=[10,25,5,90,45]
print(max(nums))

#Count how many times 2 appears in the list [1, 2, 3, 2, 4, 2, 5].
nums=[1, 2, 3, 2, 4, 2, 5]
count=0
x=2
for el in nums:
    if el==x:
        count+=1
print("count",count)

#Make a list of squares of numbers from 1 to 10 using a loop.
list=[]
for i in range(1,11):
    list.append(i*i)
print(list)

#Combine two lists: [1, 2, 3] and [4, 5, 6] into one list.
list1=[1,2,3]
list2=[4,5,6]
combined=list1+list2
print(combined)

#Remove duplicates from the list [1, 2, 2, 3, 4, 4, 5].
nums=[1,2,2,3,4,4,5]
new=set(nums)
print(new)
#other way
nums=[1,2,2,3,4,4,5]
new=[]
for el in nums:
    if el not in new:
        new.append(el)
print(new)

#split list into even and odd
list=[1,2,3,4,5,6,7,8,9,11,22,31,34,56,65]
even=[]
odd=[]
for el in list:
    if el%2==0:
        even.append(el)
    else:
        odd.append(el)
print(even)
print(odd)
    
#find common element in list
list1=[1,2,3,4,5,6,8]
list2=[1,3,5,6,9,10]
common=[]
for el in list1:
    if el in list2:
        common.append(el)
print(common)

#find the diferent element in list
list1=[1,2,3,4,5,6,7]
list2=[1,2,3,5,6,7]
diffrent=[]
for el in list1:
    if el not in list2:
        diffrent.append(el)
print(diffrent)