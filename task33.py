"""
#1) Check if a number is even or odd
n=int(input("Enter a number:"))
if n%2==0:
    print(n,"is even number")
else:
    print(n,"is odd number")
"""
"""
#2)Write a program to check if a number is positive, negative if not print zero
n=int(input("Enter a number:"))
if n>0:
    print(n," is positive number")
elif n<0:
    print(n,"is negative number")
else:
    print("The given number is ",n)
"""
"""
#3)Check if the number is divisible by both 2 and 5 display the result
n=int(input("Enter a number:"))
if n%2 ==0 and n%5==0:
    print("The given number is divisible by both 2 and 5 ")
else:
    print("The given numbe is not divisible by both 2 and 5")
"""
"""
#4) Input marks of a student with a 5 grades
n=int(input("Enter a total mark out of 600:"))
if n>600:
    print("Enter a mark below 600")
elif n>=510:
    print("GRADE A")
elif n>=410:
    print("GRADE B")
elif n>=350:
    print("GRADE C")
elif n>=310:
    print("GRADE D")
elif n>=300:
    print("GRADE E")
else:
    print("fail")
"""
"""
#5) Input a year and check if it's a leap year
n=int(input("Enter a year want to check if it's a leap year:"))
if n%4==0:
    if n%100==0:
        if n%400==0:
            print(n,"if leap year")
else:
    print(n,"is not a leap year")
"""
"""
#6) Print number from 1 to 10
for i in range(1,11,1):
    print(i)
"""
"""
#7) Print numbers from 1 to10 and square them
for i in range(1,11,1):
    print(i**2)
"""
"""
#8) Print numbers for 10 to 1 in reverse order
for i in range(10,1,-1):
    print(i)
"""
"""
#9) Age Category
age=int(input("Enter your age:"))
if age>0 and age<12:
    print("Child")
elif age>13 and age<19:
    print("Teen")
elif age>20 and age<59:
    print("Adult")
else:
    print("Senior")
"""
"""
#10) Write a program that takes a number as input and checks if its cube is greater than 100 . Display whether it is above or below / equal to 100
n=int(input("Enter a number:"))
if n**3>100:
    print("The cube of ",n**3," is greaterthan 100")
else:
    print("The cube of ",n**3," is lessthan 100")
"""
"""
#11) Login system
n=input("Enter your user name:")
p=input("Enter your password:")
if n=="rohit":
    if p=="rohit@8":
        print("Login successful!!")
    else:
        print("##Try again##")
else:
    print("##Try agian##")
"""
"""
#12) Check if a character is a vowel or consonant
c=input("Enter a character:")
if c in ('a','e','i','o','u') or c in ('A','E','I','O','U'):
    print(c,"is vowel!!")
else:
    print(c,"is consonant")
"""
"""
#13) Print first sum of n nutural numbers
s=0
n=int(input("Enter a number:"))
for n in range(1,n+1):
    s+=n
print("The sum of the number upto",n," is:",s)
"""
"""
#14) Print A to Z
for i in range(65,91):
    print(chr(i))
"""
"""
#15) Print tables
n=int(input("Enter a table number:"))
for i in range(1,11):
    print(i,'*',n,'=',i*n)
"""

