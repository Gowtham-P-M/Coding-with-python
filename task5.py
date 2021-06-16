#1)Write a program to create a list of n integer values
def add(k):
    l=int(input("What position do you want to add the item "))
    m=int(input("What is the item value "))
    k.insert(l,m)
    print("The new list is ",k)
def dele(k):
    f=int(input("What is the item you want to delete "))
    for i in k:
        if i==f:
           k.remove(i)
    print ("The new string is ", k)        

n=int(input("Enter the value of n "))
u=[]
for i in range(1,n+1):
    u.append(i)
j=int(input("Enter a number\n1.add to the list\n2.delete from the list\n"))
if j==1:
    add(u)
elif j==2:
    dele(u)
m=max(u)
n=min(u)
print("max-",m,"\nmin-",n)
      
#2)Create a tuple and print the reverse of the created tuple
tu=('f',1,'b',2,3,4,5)
for i in range(len(tu)-1,-1,-1):
    print(tu[i],end=' ')

#3)Create a tuple and convert tuple into list
u=('a','b','c',1,2,3,4)
print("\nThe data type of u is ",type(u))
u=list(u)
print("The data type of u is ",type(u))
