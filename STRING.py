str="india is my country"
name="PRATIK"
lan="   python   "
lan2="   java  "
#PRINT THE LENGHT OF STRING
print(len(str))

#PRINT IN REVERSE
print(str[::-1])

#CAPITALIZE THE STRING
print(str.capitalize())

#LOWERCASE
print(name.lower())

#UPPECASE
print(str.upper())

#ENDSWITH
print(str.endswith("country"))

#STARTWITH
print(str.startswith("india"))

#TITLE
print(str.title())

#REMOVE SPACE FROM RIGHT
print(lan.rstrip())

#REMOVE SPACE FROM LEFT
print(lan.lstrip())

#REMOVE STRIP
print(lan2.strip())

#REPLACE THE WORD
print(str.replace("india","हिंदुस्थान"))

#COUNTS THE NUMBER OF LETTERS
print(str.count("a"))

#check the vowels in string which is present which is not present in string
vowels="aeiou"
count=""
num=0
counts=""
nums=0
for el in str:
    if el in vowels:
        num+=1
        count+=el
    else:
        nums+=1
        counts+=el

print("vowels::",count,num)
print("not vowels::",counts,nums)

#find the words
print(str.find("co"))

#find index number
print(str.index("y"))
print(str.rfind("y"))

#split the words
print(str.split())

name=["india","is my","country"]
print(" ".join(name))

#swapcase
fri="SALoKHenagaR"
print(fri.swapcase())