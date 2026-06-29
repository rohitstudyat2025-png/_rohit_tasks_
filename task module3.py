# Random
import random as r

i=[10,20,30,40,50]
print("Random():",r.random())
print("Randint():",r.randint(1,100))
print("Randrange();",r.randrange(10,50,5))
print("choice():",r.choice(i))
print("Sample():",r.uniform(1,10))
r.shuffle(i)
print("Shuffle():",(i))
"""
#######Module no found error#######
# Numpy
import nmpy as n

a=n.array([3,4,5,2,4])
print(n.sum(a))
print(n.mean(a))
print(n.max(a))
print(n.min(a))
print(n.sort(a))

# Scipy
from scipy import linalg
a=[[1,2],[5,6]]
det=linalg.det(a)
print("Determinant=",det)
"""
"""
# Pandas
# Series
import pandas as p
s=p.series([10,20,30,40,50,60,70])
print(s)

# Data frame
import pandas as pp
date={'Name':['john','sham','ram'],
            'Age':[23,34,12]}
print(data)

# Panel
for collections  import deque
q=deque()
q.append(10)
q.append(20)
q.append(30)
print("Queue:",list(q))
print("Removed:",a.popleft())
print("Queue after deletion:",list(q))

"""
# Web Browser Module

import webbrwoser
sebbrowser.open("https://www.youtube.com/")

# Pillo Module
from pil import image
i=Image.open(r"")
i=i.rotate(60)
i.show()

# Maplotlib
import matplotlib.pyplot as p
x=[1,2,3,4]
y=[10,20,30,40]
p.plot()x,y
p.title("graph")
p.xlable("x axis")
p.ylable("y aixs")

# Bar chat
Bar chart import matplotlib as m
courses=["ECE","EEE","CSE"]
feess=[80,70,100]
p.zlable('course')
p.ylable('fees(k)')
p.show()

# Histogram
import matplotlib pyplot as plt
import numpy as np
data=np.random.rand(100)
plt.hist(data,bius=30,color='skyblue',edgecolor="black")
plt.title("Histogram")
plt.xlables("Value")
plt.ylables("Frequency")

# Scatter plot
import matpotlib.pyplot as p
x=[1,2,3,4,9]
y=[3,4,5,6,0]
p.scatter(x,y)
p.tittle("Scatter plot")
p.xlable("xvalue")
p.ylable("yvalue")
p.show()

#Pie chart
import matlplotlib.pyplot as pl
course=["ECE","EEE","CSE"]
fees=[80,70,100]
pl.pie(fees.lables=course,autopit=fees)
pl.tittle("College fees distribution")
pl.show()











