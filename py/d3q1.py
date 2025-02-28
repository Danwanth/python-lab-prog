dan=input("enter a string: ")
length=len(dan)
print("Thye length is: ",length)
dan1=dan.upper()
print("The upper case: ",dan1)
dan2=dan.lower()
print("The lower case: ",dan2)
dan3=dan[::-1]
if dan3==dan:
	print("Pallindrome: ",dan3)
else:
	print("not pallindrome",dan3)
count=0
dan4=' '
for i in dan:
	if i in 'aeiou':
		dan4+='_'
		count=count+1
	else:
		dan4+=i
print(dan4)
print("The length is:",count)



