#how to print a value ?
print("30 days 30 hour challenge")
print ('30 days 30 hours challenge')

#Assigning string to variable
Hours="thirty"
print(Hours)

#indexing using string
days="thirty"
print(days[0])
print(days[2*2])

#how to print the particular character from certain text?
challenge="I will win"
print(challenge[7:10])

#how to print the length of character
challenge="I will win"
print(len(challenge))

#convert string into lower character
challenge="I Will Win"
print(challenge.lower())

#string concatenation-joining two strings
a="30 days"
b="30 hours "
c=a+b
print(c)

#adding space during concatenation
a="30 days"
b="30 hours "
c=a+ " "+b
print(c)

#casefold()-usage
text="Thirty days and Thirty hours"
x=text.casefold()
print(x)
d="DON'T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
print(d.capitalize())
print(d.find('T'))
print(d.isalpha())
print(d.isalnum())
