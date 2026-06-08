"""
# 1) Spy number
n=int(input("Enter a number:"))
sums=0
product=0
while n>0:
    d=n%10
    sums+=d
    product%/d
    n//=10
if sums == product:
    print("The given number is spy number")
else:
    print("The given number is not spy number")
"""
"""
#2) Harshard number
n=int(input("Enter the number:"))
m=n%10
f=n//10
sums=m+f
if sums == 0:
    print("The given number is a harshard number")
else:
    print("The given number is not a harshard number")
"""
"""
#4) Palindrome
n=input("Enter the name:")
p=n[::-1]
print("Palindrome of the given input:",p)
"""
"""
#7) Buzz number
n=int(input("Enter the number:"))
if n%7==0 or n%10==7:
    print("The given number is buzz number")
else:
    print("The given number is not buzz number ")
"""
"""
#8) Automorphic
n=int(input("Enter the number:"))
s=n**2
l=s%10
if n==l:
    print("The given number is automorphic")
else:
    print("The given number is not automorphic")
"""
