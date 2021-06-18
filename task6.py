#Write a Python script to merge two Python dictionaries
f={"a":"A","b":"B","c":"C"}
d={"z":"26","f":"6"}
d.update(f)
print(d)

#Write a Python program to remove a key from a dictionary
f={"a":"A","b":"B","c":"C"}
print("\nThe dictionary before",f)
f.pop('a')
print("The dictionary after",f)

#Write a Python program to map two lists into a dictionary
o=['a','b','c','d']
g=['A','B','C','D']
k=dict(zip(o,g))
print('\n',k)

#Write a Python program to find the length of a set
f={'a',1,'b','2'}
print('\n',len(f),'\n')

#Write a Python program to remove the intersection of a 2nd set from the 1st set
r={'a',1,'b','2'}
d={'a','b','c','d'}
r-=d
print(r)
