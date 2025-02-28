import random
L=[]

for i in range(10):
	L.append(random.randint(1,100))

print("The original list is: ")
for i in L:
	print(i," ")
		
smol=0
big=0
sum=0
for i in L:
	if i<smol:
		smol=i
	if i>big:
		big=i
	sum=sum+i 
avg=sum/10

print("The largest number is:",big)
print("The smallest number is:",smol)
print("The average is:",avg)

L2=L[::-1]
print("Reverse the list")
for i in L2:
	print(i," ")

L3=[]	
for i in L:
	if i%2==0:
		L3.append(i*i)

print("Sum of squares of even numbers")
for i in L3:
	print(i," ")
