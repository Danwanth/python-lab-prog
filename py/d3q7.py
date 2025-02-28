dan=input("Enter a string: ")
vowels=0
space=0
c=0
for i in dan:
	if i in 'aeiou':
		vowels=vowels+1
	elif i in ' ':
		space=space+1
	else:
		c=c+1
print("The number of vowels is: ",vowels)
print("The number of spaces is: ",space)
print("The number of consonants is: ",c)
