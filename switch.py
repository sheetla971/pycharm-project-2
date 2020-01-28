def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mult(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
calculator={"+":add,"-":sub,"*":mult,"/":div}
op=input("enter operator")
num=input("enter num")
x=[int (i) for i in num.split(",")]
print(calculator[op](x[0],x[1]))