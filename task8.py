#Write a Python script to merge two Python dictionaries
r={'a': '1','b': '2'}
d={'A':'3','B':'4'}
r.update(d)
print(r)

#Write a program to sort the value from descending to ascending in list and convert it in to a set.
f=[97,34,100,89]
f.sort(reverse=True)
print (f)
f=set()
print(type(f))

#Write a Python program to list number of items in a dictionary key and sort the list with the help of a function & without the function.
def s():
   g.sort()
   return g
u={'b': '1','a': '2'}
g=list(u)
g.sort()
print(u)
print(g)
print("With a function",s())

#Write a Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input.
g=input("Enter a string")
d=input("Enter the word to be changed")
r=input("Enter the replacing word")
g=g.replace(d,r,1)
print(g)

#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to capital letter.
g=input("Enter a string")
d=input("Enter the word to be used for capitalization")
d=d.upper()
o=d[0]
d=d.lower()
g=g.replace(d[0],o)
print(g)


#Write a Python program to find the repeated items of a list
d=['a','b','c','b','c','z','e','a']
print('Repeated items are',d)
for i in d:
    if d.count(i)>1:
        print(i,end=' ')

#Write a Python program to check the sum of three elements and divided by a value which is given as an input by the user
f=0
for i in range(3):
    f+=int(input("Enter the number"))
d=int(input("Enter a number"))
print(f/d)

#Write a Python program to find the Mean,median,mode among three given numbers
import statistics
d=[]
for i in range(3):
    d.append(int(input("Enter a number")))
print(statistics.mean(d))
print(statistics.median(d))
print(statistics.mode(d))

#Write a Python program to swap cases of a given string
f='22B,bakEr\'S StrEET'
f=f.swapcase()
print(f)

#Write a program to convert an integer to binary & octa decimal
g=[]
h=[]
def i(d):
    if d==1 or d==0:
        g.append(d)
    else:
        g.append(d%2)
        return i(d//2)
def o(d):
    if d==1 or d==0:
        h.append(d)
    else:
        h.append(d%8)
        return o(d//8)

d=int(input("Enter the number"))
i(d)
o(d)
h.reverse()
g.reverse()
print(g,'\n',h)




