uc=0
lc=0
an=0
ln=0
sp=0 
pas=input("Enter your password: ")
ss=len(pas)
for i in pas:
	if i.isupper():
		uc=1
	if i.islower():
		lc=1
	if i.isalnum():
		an=1
	else:
		sp=1
	if ss>5:
		ln=1
		
if uc==1 and lc==1 and an==1 and sp==1 and ln==1:
	print("Strong password")
else:
	print("weak password")
	
	
		

