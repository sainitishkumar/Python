#!/usr/bin/env python3

import matplotlib.pyplot as plt 
file = open('1.txt','r')   #files having co-ordinates
file2 = open('2.txt','r')
file3= open('3.txt','r')
x=[]
y=[]
x2=[]
y2=[]
x3=[]
y3=[]
for i in file.read().split('\n'):
	
	try:
		x.append(int(i.split()[0]))
		y.append(float(i.split()[1]))
		
	except IndexError:
		pass
for i in file2.read().split('\n'):
	
	try:
		x2.append(int(i.split()[0]))
		y2.append(float(i.split()[1]))
		
	except IndexError:
		pass
for i in file3.read().split('\n'):
	
	try:
		x3.append(int(i.split()[0]))
		y3.append(float(i.split()[1]))
		
	except IndexError:
		pass			
	plt.plot(x,y,marker='o')
    x2=[5,4,3,2,1]
	y2=[6,5,4,3,2]
	plt.plot(y2,x2,marker='o',label='l2')
plt.plot(x,y,label='recursion')
plt.plot(x2,y2,label='iter')
plt.plot(x3,y3,label='n/2')
plt.xlabel('n')
plt.ylabel('time')

plt.legend()
plt.show()