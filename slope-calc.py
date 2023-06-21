#This program will help high school students who are strugling to find the the slope of any straight line.
#This program is not built for any kind of inapropriate tasks. Eductional usage only.
import math
print("Welcome to slope-calc!")
print("If you have two points of any straight line type \"p\" and if you have an equation of that straight line then type \"e\".")
a=input("type : ")

if a==str("p"):
    print("2 Points mode")
    x1=float(input("x1: "))
    x2=float(input("x2: "))
    y1=float(input("y1: "))
    y2=float(input("y2: "))
    oper1=y2-y1
    oper2=x2-x1
    slopep=oper1/oper2
    print("slope= "+ str(slopep))

elif a==str("e"):
    print("Equation mode")
    xer=float(input("Coefficient of x: "))
    yer=float(input("Coefficient of y: "))
    slopee= -xer/yer
    print("Slope= "+ str(slopee))
else:
    print("Still working here")
