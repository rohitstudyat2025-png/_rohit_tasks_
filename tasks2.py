"""
#1) Find bitwise AND of two numbers
o=int(input("Enter the number:"))
t=int(input("Enter the number:"))
print("The bitwise AND of two numbers:")
print(o&t)
"""
"""
#2) Find bitwise OR of two numbers
o=int(input("Enter the number:"))
t=int(input("Enter the number:"))
print("The bitwise OR of two numbers:")
print(o|t)
"""
"""
#3) Find bitwise XOR of two numbers
o=int(input("Enter the number:"))
t=int(input("Enter the number:"))
print("The bitwise XOR of two numbers:")
print(o^t)
"""
"""
#4) Find bitwise NOT of two numbers
o=int(input("Enter the number:"))
t=int(input("Enter the number:"))
print("The bitwise NOT of two numbers:")
print(~o)
print(~t)
"""
"""
#5) Input bill amount, add gst give total amount
b=int(input("Enter a bill amount:"))
gst=b*18/100
total=b+gst
"""
"""
# 6) Input five person weight find average
p1=int(input("Enter a weight of the person:"))
p2=int(input("Enter a weight of the person:"))
p3=int(input("Enter a weight of the person:"))
p4=int(input("Enter a weight of the person:"))
p5=int(input("Enter a weight of the person:"))
avg=(p1+p2+p3+p4+p5)/5
print("The average weight of five person is")
print(avg)
"""
"""
# 7) Check whether a number is even using bitwise operator
e=int(input("Entert the number:"))
if (2&e)==0:
    print(e," is a even number")
else:
    print(e,' is a odd number')
"""
"""
# 8) Input a number find it square
n=int(input("Enter the number want to square:"))
sq=n**2
print("The square of ",n,"is :",sq)
"""
"""
# 9) Input a number find it cube
n=int(input("Enter the number want to square:"))
cb=n**3
print("The square of ",n,"is :",cb)
"""
#10) Swap two numbers using XOR operator
n1=int(input("Enter the n1:"))
n2=int(input("Enter the n2: "))
n1=n1^n2
n2=n1^n2
n1=n1^n2
print("Afther swaping the two number:")
print("n1:",n1)
print("n2:",n2)
"""
#11) Compare two numbers and print whether they are equal
n1=int(input("Enter the number:"))
n2=int(input("Enter the number:"))
if n1==n2:
    print("The given to number are equal")
else:
    print("The given to number are not equal")
"""
"""
# 12) Chech whether first number is greater than secondf number
n1=int(input("Enter the number:"))
n2=int(input("Enter the number: "))
if n1>n2:
    print(n1," is greater than ",n2)
else:
    print(n1," is lessthan ",n2)
"""
"""
#13) Check whether a number is less than 50
n=int(input("Enter the number:"))
if n<50:
    print(n, " is lessthan 50" )
elif n==50:
    print(n," is equal to 50 ")
else:
    print(n," is greaterthan 50")
"""
"""
#14) Compare two numbers using >= operator
n1=int(input("Enter the number:"))
n2=int(input("Enter the number: "))
print(n1>=n2)
"""
"""
#15) Check whether two values are not equal
n1=int(input("Enter the number:"))
n2=int(input("Enter the number: "))
if n1!=n2:
    print(n1," not equal to ",n2)
else:
    print(n1," is equal to ",n2)
"""
"""
#16) Check whether a number exists in a list
l=[1,2,3,4]
print(1 not in l)
print(1 in l)
"""
"""
#17) Calculate compound interset
p=int(input("Enter the principal amount"))                           # Formula:
a_r=int(input("Enter the annual interst rate"))                   # a=p(1+r/n)**n*t
y=int(input("Enter the number of years:"))
c_p=int(input("Enter the compounding times per year:"))
rate_decemal=a_r/100
Total_A=p*(1+(rate_de))
print("Compond interset is:",Total_A)
"""
"""
#18) Verify whether an element exists in a=[2,3,4,5,6,7] use membership operators
a=[2,3,4,5,6,7]
print(2 in a)
print(2 not in a)
"""
"""
#19) Create two varible with same value and check using is
a=3
b=3
print(a is b)
print(b is a)
"""
"""
#20) Assign one variable to another and check using "is not"
a=3
b=a
print(a is not b)
print(b is not a)
"""

