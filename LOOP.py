"""#1.Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print("numbers",i)
    
#2.Print numbers from 10 to 1 using a while loop.
i=10
while i>=1:
    print(i)
    i-=1
    
#3.Print the multiplication table of a given number (e.g., 7).
x=7
i=1
while i<=10:
    print("multipication table:",x*i)
    i+=1
#using for loop
n=7
for i in range(1,11):
    print(n*i)
    
#4.Find the sum of numbers from 1 to 100 using a loop.
sum=0
for i in range(1,101):
    sum+=i
print(sum)
#using while loop
sum=0
i=1
while i<=100:
    sum+=i
    i+=1
print("sum",sum)
#5.Print all even numbers between 1 and 50.
for i in range(2,51,2):
    print("even no.",i)
#while loop
i=0
while i<=50:
    i+=2
    print("even ",i)
    
#6.Print all odd numbers between 1 and 50.
for i in range(1,51,2):
    print("odd no.",i)
i=1
while i<=49:
    i+=2
    print("odd",i)

#7.Print the factorial of a given number using a loop.
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return(fact)
print(fact(5))
        
#using while loop

def num(n):
    fact=1
    i=1
    while i<=n:
        fact*=i
        i+=1
    return fact
print(num(5))

#check the word are present in string 
s="india is my country"
x="india"
words=s.split()
for word in words:
    if word==x:
        print("found",x)
        break
    
    else:
        print("not found",x)
print(s.endswith("country"))

##check the character are present in string 
s="i love my india"
ch="m"
if ch in s:
    print("found",ch)
else:
    print("not found")

#check the charactes comes how many times
s="india is my country"
ch="i"
count=0
for c in s:
    if c==ch:
        count+=1
print("total count:",count)"""
    
#Find the largest number in a list
list=[32,43,43,1,3,6,5,76,43,11]
max_num=list[0]
for num in list:
    if num>max_num:
        max_num=num
print("max number:",max_num)
#find the smallest  umber in the list
list=[54,73,82,92,923,923,88,99,65]
min_num=list[0]
for val in list:
    if val<min_num:
        min_num=val
print("minimum value:",min_num)

#count even odd numbers in list
list=[12,23,43,54,54,32,21,11,45,665,6542,1134,95,]
even_count=0
odd_count=0
for c in list:
    if c%2==0:
        even_count+=1
        print(even_count)
    else:
        odd_count+=1
        print(odd_count)
        
    
        