2
import math
import random
from tkinter import *


class Circle:
    def __init__(self):
        self.radius=5


    def setRadius(self,radius):
        self.radius=radius


    def getRadius(self):
        return self.radius


    def find_area(self):
        return (self.radius*(math.pi*math.pi))


    def display(self):
        return "Circle"


class Square:
    def __init__(self):
        self.sides=5.3


    def setSides(self,sides):
        self.sides=sides


    def getSides(self):
        return self.sides


    def find_area(self):
        return (self.sides*self.sides)


    def display(self):
        return "Square"


class Cube:
    def __init__(self):
        self.length=8.5
        self.width=8.5
        self.height=8.5


    def setLength(self,length):
        self.length=length


    def setWidth(self,width):
        self.width=width


    def setHeight(self,height):
        self.height=height


    def getLength(self):
        return self.length


    def getWidth(self):
        return self.width


    def getHeight(self):
        return self.height


    def find_area(self):
        return(6*self.length*self.length)


    def display(self):
        return "Cube"


def main():
    mylist=[]


    for i in range(10):
        number=random.randint(0, 2)


        if number==1:
            obj=Circle()
            mylist.append(obj)
        elif number==2:
            obj=Square()
            mylist.append(obj)
        else:
            obj=Cube()
            mylist.append(obj)


    print("1. Save the results into a file")
    print("2. Print the results on screen")
    print("3. Print the reuslts in GUI Windows")


    choice= int(input("Enter Your Choice: "))


    if choice==1:
        filename=input("Enter File Name: ")
        f = open(filename, "w")


        for shape in mylist:
            out= shape.display()+' Area: '+str(shape.find_area())+"\n"
            f.write(out)


        f.close()


    elif choice==2:
        for shape in mylist:
            print(shape.display(),' Area: ',shape.find_area())


    else:
        root = Tk()
        t = Text(root)


        for shape in mylist:
            t.insert(END, shape.display(),' Area: ',str(shape.find_area()) +'\n')
        t.pack()


        root.mainloop()
            
if __name__=="__main__":
    main()
0
