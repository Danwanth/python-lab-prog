email=input("Enter your email address: ")
if '@' in email:
	if '.' in email:
		print("Valid email address")
	else:
		print("Invalid email address")
else:
		print("Invalid email address")
