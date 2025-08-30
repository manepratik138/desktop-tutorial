#Write a function that takes two numbers as input and returns their sum.
def calc(a,b):
    sum=(a+b)
    return sum
x=calc(2,3)
print("result=",x)
#Write a function that checks whether a number is even or odd.
def number(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
    return n
number(7)
number(6)
#Write a function that takes a string and returns it in reverse order.
def reverse(s):
    result=s[::-1]
    return result
print(reverse("pratik"))
#Write a function that returns the factorial of a number.
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(factorial(5))
#Write a function that prints multiplication table of a given number and put in list.
def number(n):
    table=[]
    for i in range(1,11):
        table.append(n*i)
    return table
print(number(3))

def number(n):
    for i in range(1,11):
        print(n*i)
        
number(6)


#FINDING THE GRETEST VALUE
def find(a,b,c):
    maximum=max(a,b,c)
    return maximum    ##without return value not dispaly it display none
    
finding=find(12,34,2)
print("finding greter numbers",finding)

#finding thw smallest value 
def find(a,b,c):
    minimum=min(a,b,c)
    return minimum
finding=find(21,45,11)
print("the smallet number is:",finding)

#THIS IS OTHER METHOD FINDING THE GRETEST NUMBER,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number"))
if a>b and a>c:
    print("a is greter:",a)
elif(b>a and b>c):
    print("b is greter:",b)
else:
    print("c is greter:",c)
    
#FINDING THE VOWELS
def pratik_vowels(s):
    vowels="aeiouAEIOU"
    count=0
    for i in s:
        if i in vowels:
            count+=1
    return count
            
print(pratik_vowels("maharashtra"))
            
#finding the minimum and maximum number
def max_min(numbers):
    return max(numbers),min(numbers)
print(max_min([12,34,56,33,21,55,22,44,1,44,55,6]))


#POWER OF NUMBER 
def power(a,b):
    return pow(a,b)
print(power(2,3))


#ROUND NUMBER
def number(a):
    return round(a)
print(number(8.7))


#CHECK THE NUMBER IT IS PRIME OR NOT
def number(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
num=number(4)
print(num)


