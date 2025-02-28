class bank:
	interest=0
	def __init__(self):
		self.bankna="RBI"
		self.customer={}
		
	def create_account(self):
		cid=int(input("Enter your id: "))
		if cid not in self.customer:
			cna=input("Enter your name: ")
			cbal=int(input("Enter your balance: "))
			self.customer[cid]={"NAME":cna,"BALANCE":cbal}
			print(self.customer)
		else:
			print("Customer already exists,")
			ans=input("Do you want to update(YES/NO): ")
			a=ans.lower()
			if a=="yes":
				cna=input("Enter your name: ")
				cbal=int(input("Enter your balance: "))
				self.customer[cid]={"NAME":cna,"BALANCE":cbal}
				print(self.customer)
				
	def deposit(self):
		cid1=int(input("Enter the Customer ID: "))
		print(self.customer)
		if cid1 in self.customer:
			dep=int(input("Enter the amount to be deposited: "))
			self.customer[cid1]["BALANCE"]=self.customer[cid1]["BALANCE"]+dep
			print("The updated balance is: ",self.customer[cid1]["BALANCE"])
		else:
			print("The customer does not exist")
			
		
	def withdraw(self):
		cid2=int(input("Enter the Customer ID: "))
		if cid2 in self.customer:
			wit=int(input("Enter the amount to be withdrawn: "))
			self.customer[cid2]["BALANCE"]=self.customer[cid2]["BALANCE"]-wit
			print("The updated balance is: ",self.customer[cid2]["BALANCE"])
		else:
			print("The customer does not exist")

	def display(self):
		cn=int(input("Enter the name of the customer you want to find the details about: "))
		if cn in self.customer:
			print("DETAILS\n")
			print(self.customer[cn])
		else:
			print("Customer not found")
			
	def getamt(self,cid):
		return self.customer[cid]["BALANCE"]
		
	def getint(self,cid):
		return self.interest
					
	@classmethod
	def updateinterest(cls):
		cls.interest=int(input("Enter the interest rate: "))
		return cls.interest
		
	@staticmethod
	def calc_int(amt,it,t):
		si=(amt*it*t)/100
		print("The simple interest is: ",si)
		
		
		
		
		
'''b=bank()
b.create_account()
b.deposit()
b.withdraw()
b.display()'''
b=bank()
while(1):
	
	print("\n===STATE BANK OF INDIA==\n")
	print(" [1]Create account \n [2]Deposit money \n [3]Withdraw money \n [4]Display \n [5]Update the interest rate \n [6]Calculate simple interest \n [7]Quit\n")
	ch=int(input("Enter your choice: "))
	if ch==1:
		b.create_account()
	elif ch==2:
		b.deposit()
	elif ch==3:
		b.withdraw()
	elif ch==4:
		b.display()
	elif ch==5:
		bank.updateinterest()
	elif ch==6:
		cc=int(input("Enter the customer id of the person you want to find the interest rate abt: "))
		amt=b.getamt(cc)
		rate=b.getint(cc)
		t=int(input("Enter the time period: "))
		bank.calc_int(amt,rate,t)
	else:
		print("TERMINATING PROGRAM....")
		break;
		
