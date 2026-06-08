"""
#1) To find the last digit of the number
f=int(input("Enter more than one digit number to find the last digit of the number:"))
f_d = f%10
print("The last digit of the ",f,"is:",f_d)
"""
"""
#2) To remove last digit of the number
r=int(input("Enter more than one digit number to remove last digit of the number: "))
r_l=r//10
print("After removing the last digit of the number ",r,"is:",r_l)
"""
"""
#3)  To find last two digits of the given number
f=int(input("Enter more than one digit number to find last two digits of the number:"))
f_d=f%100
print("The last two digits of the number",f,"is:",f_d)
"""
"""
#4) Square the middle digit of a five-digit number
f=int(input("Enter the five-digit number to square the middle digit of a five-digit number:"))
f_d=f%1000
l_d=f_d//100
s=l_d**2
print("The square of the middle digit of a given five-digit number is:",s)
"""
"""
#5) BMI calculator
w=int(input("Enter the weight of the body:"))
h=int(input("Enter the height of the body:"))
bmi=w/(h/100)**2
print("BMI is",bmi)
"""
"""
#6) Expant the number
n=int(input("Enter the four digit number:"))
a=n//1000
b=(n//100)%10
c=(n//10)%10
d=n%10
print("The expansion of the given number is:")
print(a*1000,'+',b*100,'+',c*10,'+',d)
"""
"""
#7) Volume of cylinder
r=int(input("Enter the radius of the cylinder:"))
h=int(input("Enter the height of the cylinder:"))
vc=3.14*r*r*h
print("The volume of cylinder is:",vc)
"""
"""
#8) Volume of cuboid
l=int(input("Enter the lenght of the cuboid:"))
b=int(input("Enter the breadth of the cuboid:"))
h=int(input("Enter the height of the cuboid:"))
vc=l*b*h
print("The volume of cuboid is:",vc)
"""
"""
#9) Convert centimeter to meter
c=int(input("Enter the number to convert centimeter to meter:"))
m=c/100
print(m)
"""
"""
#10) To Calculate the speed
d=int(input("Enter the distance to calculate the speed:"))
t=int(input("Enter the time to calculate the speed:"))
s=d/t
print(s)
"""
