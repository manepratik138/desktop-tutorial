#Q1. Print numbers from 1 to 20 using a for loop.
for i in range(1,21):
    print(i)
#Q2. Print the squares of numbers from 1 to 10.
for i in range(1,11):
    square=i*i
    print("square:",square)
#Q3. Print the multiplication table of 7.
num=7
for i in range(1,11):
    table=num*i
    print(table)
#Q4. Print all even numbers between 1 and 50.
for i in range(2,51,2):
    print(i)
"""#Q5. Print the sum of numbers from 1 to 100.
sum=0
for i in range(1,101):
    sum+=i
print("total sum:",sum)"""
#Q6. Print each character of a string "Python".
str="python"
for ch in str:
    print(ch)
#Q7. Count how many vowels are in a string.
text="india is my country"
vowels="aeiouAEIOU"
count=0
for ch in text:
    if ch in vowels:
        count+=1
print("vowels:",count)
#Q8. Print each element of a list [10, 20, 30, 40, 50].
list= [10, 20, 30, 40, 50]
for el in list:
    print(el)
#adding the total number in list.
total=0
numbers=[12,3,34,5,2312,132,3,42,4]
for el in numbers:
    total+=el
print("total addition:",total)
print("total addition by other method:",sum(numbers))

##using for loop print thre star...................
for i in range(5):
    for j in range(5):
        
       print("*",end="")
    print("*")
    
    
#3Print the cube of numbers from 1 to 10.
for i in range(1,11):
    cube=i*i*i
    print("cube:",cube)
    
#Print the sum of all even numbers between 1 and 100.
add=0
for i in range(2,100,2):
    add+=i
print("addition:",add)

#Print the factorial of a number using a for loop.
n=int(input("enter any number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial:",fact)