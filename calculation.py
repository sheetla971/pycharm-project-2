op=input("enter operator")
num=input("enter number")
x=[int(i) for i in num.split(",")]
if op is"+":
    print(x[0]+x[1])
if op is "-":
    print(x[0]-x[1])
if op is "*":
    print(x[0]*x[1])
if op is "/":
    print(x[0]/x[1])