family={
    "main member in family":"pappa",
    "mother name":"shobha",
    "brother name":"shahaji",
    "first sisters name":"sunita",
    "second sisters name":"vanita",
    "and last child is me":"pratik"
}
print("family",family)

#print all the keys
print(family.keys())

#print all the values
print(family.values())

#print items
print(family.items())

#add a new value
family["grandma"]="hirabai"
print(family)

#change the value//update the value
family["main member in family "]="balu"
print(family)

#remove the element in dictionary
family.pop("and last child is me")
family.popitem()
del family["second sisters name"]
print(family)

#UPDATE THE VALUE AND ADD THE VALUE IT IS A SAME..........
family.update({"brother name":"SHAHAJI RAJE........"})
print(family)

#GET A PARTICULAR VALUE USING GET FUNCTION
pappa=family.get("main member in family")
print(pappa)
mummy=family.get("mother name")
print(mummy)
dada=family.get("brother")### if there are no key values it prints none
print(dada)
del family["grandma"]
print(family)

"""##all clear
family.clear()
print(family)###output is {}"""

##add a new value
family.update({"age":"20"})
family["age of pappa"]="56"
print(family)


#setdefault(key, default).....if there are key it shows value if there are not key add the value
family.setdefault("age","25") #there are age is key so it is not change
family.setdefault("second sister name","vanita")#there is not a key so it add value in this key
print(family)

###crete a dictionare in one line 
squares={x:x*x for x in range(1,11)}
print(squares)

cubes={n:n*n*n for n in range(1,11)}
print(cubes)


#check the key is present or not
print("mother name" in family)
print("uncle name" in family)

#check the lenght of dictionary
print(len(family))

#"any" and "all" functions 
marks={
    "physics":72,
    "chemistry":74,
    "maths":92,
    "electronis":52
    
}
print(any(mark>90 for mark in marks.values()))
print(any(mark>100 for mark in marks.values()))
print(all(mark>90 for mark in marks.values()))
print(all(mark>50 for mark in marks.values()))