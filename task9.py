#Write a program to loop through a list of numbers and add +2 to every value to elements in list
def a(i):
    return i+2
f=[1,2,3,4,5,6,7]
f=list(map(a,f))
print(f)

#Write a program to get the below pattern
"""54321
4321
321
21
1"""

def f(o):
   i=0
   for g in range(o,0,-1):
       i=i*10+g
   return i
o=int(input("Enter the number"))
for p in range(o,0,-1):
    print(f(p))

#Python Program to Print the Fibonacci sequence
f=int(input("Enter the number"))
i=0
j=1
print(i,j,end=' ')
f=f-2
while  f>0:
    print(i+j,end=' ')
    f-=1
    d=i
    i=j
    j=i+d

#Explain Armstrong number and write a code with a function
def s(a):
    s=0
    t=a
    while t>0:
        s+=(t%10)**(len(str(a)))
        t//=10
    if a==s:
        return True
    else :
        return False
y=int(input("Enter a number"))
print(s(y))

#Write a program to print the multiplication table of 9
u=int(input("Enter the range you need"))
for i in range(1,u+1):
    print(9*i)

#Check if a program is negative or positive
u=int(input("Enter the range you need "))
if u>0:
    print("It is positive")
elif u==0:
    print("It is zero")
else :
    print("It is negative")

#Write a program to convert the number of days to ages
u=int(input("Enter the number of days "))
print(u//365)

#Solve Trigonometry problem using math function write a program to solve using math function
import math
y=int(input("Enter the function you need\n1.sin\n2.cosine\n3.tan"))
f=int(input("Enter the angle(in degrees)"))
if y==1:
    print(math.sin(math.radians(f)))
elif y==2:
    print(math.cos(math.radians(f)))
else:
    print(math.tan(math.radians(f)))

#Create a calculator only on a code level by using if condition (Basic arithmetic calculation)
o=int(input("Enter the first number"))
p=int(input("Enter the second number"))
l=input("Enter the operation")
if l=='+':
    print(o+p)
if l=='-':
    print(o-p)
if l=='*':
    print(o*p)
if l=='/':
    print(o/p)

