""" 
#1) to check the string how many times the character is printed in the string
ch=input("Enter the name:")
cch=input("Enter the character want to count:")
c=ch.count(cch)
print("There are",c,"character")
"""
"""
#2) to count number of vowels in the given string and display it
n=input("Enter the name:")
c=0
for i in n:
    if i in 'aeiouAEIOU':
        c+=1
if n not in 'aeiouAEIOU' :
    pass
else:
     print("NO vowels in the given string")
print("There are",c,"vowels in the given string")
"""
"""
#3) write a program to get input in a sring , convert into upppercase and print separate lines
n=input("Enter the sentance:")
s=n.split()
for i in s:
    print(i.upper())
"""
"""
#4)Define a  function to accept string input and print it reverse and to find number of vowels in the string
n=input("Enter the name:")
r=n[::-1]
print(r)

c=0
for i in n:
    if i in "aeiouAEIOU":
       c+=1
    
if c==0:
    print("There is no vowels ")
else:
     print("Number of vowels =",c)
"""
"""
#6) String palindrome
n=input("Enter the string:")
r=n[::-1]
if n==r:
    print("The give string is palindrome")
else:
    print("The give string is not palindrome")
""" 
