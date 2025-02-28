dict={1:'dan',2:'david',3:'densel'}
print("Printing th values")
for i in dict.values():
	print(i)

print("Printing the keys")
for i in dict.keys():
	print(i)
	
print(dict)

key=int(input("Enter the key you want to update: "))
value=input("Enter the value you want to update: ")

dict[key]=value

key=int(input("Enter the key you want to add: "))
value=input("Enter the value you want to add: ")

dict[key]=value

print(dict)
