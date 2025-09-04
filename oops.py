class car():
    colour="blue"
    brand="mercedes"
c1=car()
print(c1.colour,c1.brand)


class student():
    def __init__(self,names,marks,age):
        self.name=names
        self.mark=marks
        self.age=age
s1=student("pratik",98,19)
print("name:",s1.name,"marks:",s1.mark, "age:",s1.age)


#GIVE THE DATA OG STUDENT AND GIVE THREE SUBJECTS MARK AND GIVE AVERAGE OF THIS MARKS

class student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        return(sum(self.marks)/len(self.marks))
    
    def total(self):
        total=0
        for val in self.marks:
            total+=val
        return(total)
            
s1=student("pratik",[90,91,93])
print(s1.avg())
print(s1.total())

    
