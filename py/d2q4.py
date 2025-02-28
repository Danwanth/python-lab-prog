a=int(input("Enter the number to find sum of digits: "))
s=0
while a>0:
	rem=a%10
	s=s+rem
	a=a/10

sum=int(s)
print("the sum of digits is:",sum)
