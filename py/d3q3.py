L=[]
t=(1,2,3,4,5,6,7,8,9,10)
sum=0
prod=1
for i in t:
	sum=sum+i
	prod=prod*i
	L.append(i)

print("the sum is:",sum)
print("The prod is:",prod)

no=int(input("Enter a number you want to check in the tuples: "))
if no in t:
	print("The number is there")
else:
	print("The number is not there")

n1=int(input("Enter the 1st number you want to add: "))
n2=int(input("Enter the 2nd number you want to add: "))
L.append(n1)
L.append(n2)

print("printing the list")
for i in L:
	print(i,"\t")

	


