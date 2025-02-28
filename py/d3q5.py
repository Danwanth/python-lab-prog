L=[]
sum=0
dan=input("Enter numbers seperated by spaces: ")
for i in dan:
	if i!=' ':
		l=int(i)
		L.append(l)
print("the given list is: ")
for i in L:
	print(i)
	sum=sum+i

print("the sum is: ",sum)
