#This program will help high school students who are struggling to find the slope of any straight line.
#This program is not built for any kind of inappropriate tasks. Educational usage only.
import math
import sympy
print("Welcome to slope-calc!")
print("""If you have two points of any straight line type \"p\" 
      and if you have an equation of that straight line then type \"e\" 
      if you have an angle of that straight line with the positive X-Axis then type \"a\" 
      if you have an equation of a curve line still you can find the slope type \"ce\" """)
a = str.upper(input("type : "))

if a==str("P"):
    print("2 Points mode")
    x1=float(input("x1: "))
    x2=float(input("x2: "))
    y1=float(input("y1: "))
    y2=float(input("y2: "))
    oper1=y2-y1
    oper2=x2-x1
    slopep=oper1/oper2
    print("slope= "+ str(slopep))

elif a==str("E"):
    print("Equation mode")
    print("check your equation if it's in the standard linear equation ax+by=c")
    xer=float(input("Coefficient of x: "))
    yer=float(input("Coefficient of y: "))
    slopee= -xer/yer
    print("Slope= "+ str(slopee))
    
elif a==str("A"):
    thetadeg=float(input("Angle value in degrees: "))
    theta1=math.pi*thetadeg
    thetaf=theta1/180
    slopea=math.tan(thetaf)
    print("Slope= "+slopea)

elif a == str("CE"):
    variables = sympy.symbols(input("variable = "))
    exp = input("Expression: ")
    derivative_var = sympy.diff(exp, variables)
    print(" m= " + str(derivative_var))
    

else:
    print("Still working here")
