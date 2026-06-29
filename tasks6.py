"""
#list tasks
#1) Create a list of 5 student name
l=['ram', 'rani', "raja",'rohit','sham']

#2) Add a new name to the list
l=[55,44]
l.append(121)
print(l)

#3) Remove a student name from the list.
s=['ram', 'rani', "raja",'rohit','sham']
s.pop(3)
print(s)

#4) Print all elements using loop.
l=[66,78,76,54,33,44,22]
for i in l:
    print(i)
   
#5) Find largest and smallest number in list.
l=[90,98,97,76,5,43,1,23,60,0]
m=max(l)
s=min(l)
print(" Largest number:",m,"\n","Smallest number:",s)
#6) Count even and odd numbers in list.

#7) Reverse a list.
list1=[90,80,70,60,50,40,30,20,10]
print(list1[::-1])

#8) Sort a list in ascending order.
asc=[90,80,70,60,50,40,30,20,10]
print(sorted(asc))

#9) Find sum and average of list elements.
list2=[2,4,6,8,10]
s=sum(list2)
l=len(list2)
print(s/l)
print(s)
#10) search and element in list.
"""


"""
#Tuple tasks
#1) Create a tuple with 5 number
t=(5,4,6,3,5)

#2) Access tuple elements using indexing.
a=(98,9,7,80,70,98,6)
print(a[2])

#3) Find lenght of tuple.
l=(44,33,55,3,66,88,54,66,75,90)
print(len(l))

#4)Count occurrence of an element.
e=(5,6,4,55,55,7,6,5,4,88,77,90,88,76,5,43,55,90)
print(e.count(55))

#5) Find index position of element.
i=(1,2,3,4,5,6,7,8,9,10)
print(i.index(5))

#6) Slice a tuple.
s=(5,6,7,8,9)
print(s[1:2])

#7)Convert tuple into list.
t1=(2,46,8,10)
l1=list(t1)

#8) Convert list into tuple.
l2=[2,4,6,8,10]
t2=tuple(l2)

#9) Find maximum and minmum value.
v=(33,54,66,77,90,9,8,1,33,2,000.1,0)
print(max(v))
print(min(v))

#10) Iterate tuple using loop.
loop=(44,66,55,44,33,4,5,3)
for i in loop:
    print(i)
"""

#Set tasks
#1) Create a set of numbers.
s={45,47,49,43,41,90,90,41}
print(s)

#2) Add elements into set.
ss={3,34,54,65,4,4}
ss.add(90)
print(ss)

#3) Remove elements from set.
se={3,34,54,65,4,4}
se.remove(3)

#4) Find union of two sets.
st={3,34,54}
stt={65,44,47}
u=st.union(stt)
print(u)

#5) Find intersection of two sets.
si={33,44,54}
sit={65,44,47}
i=si.intersection(sit)
print(i)

#6) Find difference between sets.
sd1={33,44,54}
sd2={65,44,47}
d=sd1.difference(sd2)
print(d)

#7) Remove duplicates from list using set.
l=[4,3,5,4,6,4,6,6,5,3,23]
sl=set(l)
print(sl)

#8) Check subset and superset.

#Subset
a={1,2,3,4,5,6,7,8,9,10}
su={6,5,7}
print(a.issubset(su))

#Superset
b={1,2,3,5,6,7,8,9,10}
sp={6,5,7}
print(b.issuperset(sp))

#9) Find unique vowels in string.
sf="pytho programming"
sc=set(sf)
for i in sc:
    if i in "AEIOUaeiou":
        print(i)
    
#10) Convert list into set.
li=[6,5,7,56,6,5,7]
stt=set(li)
print(stt)

#Dictionary Tasks
#1) Create a student dictionary with name and marks.
#2) Add new key-value pair.
#3) Update dictionary value.
#4) Delete an item from dictionary.
#5) Print all keys and values.
