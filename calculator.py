a= float(input("enter the first no:"))
b= float(input("enter the second no:"))
print("1-addition,2-subtract,3-multiply,4-divide")
d=int(input("choose operation:"))

if d==1:
    print("sum:",a+b)
elif d==2:
    print("difference:",a-b)
elif d==3:
    print("product:",a*b)
elif d==4:
    print("quotient:",a/b)
    if b==0:
     print("b cannot be zero")
else:
    print("invalid operation")
    
