

print("===Calculator===")
print("[1] Add")
print("[2] Subtract")
print("[3] Multiply")
print("[4] Divide")
print("[5] Quit")

while True:
    print("Enter choice:")
    choice = input()

    if choice == '5':
        print("Exiting calculator.")
        break
    
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
        print("Enter first number:")
        num1 = float(input())
        print("Enter second number:")
        num2 = float(input())
        
        if choice == '1':
            result = num1 + num2
            print(f"the sum is = {result}")
        
        elif choice == '2':
            result = num1 - num2
            print(f"The difference is = {result}")
        
        elif choice == '3':
            result = num1 * num2
            print(f"The product is = {result}")
        
        elif choice == '4':
            if num2 == 0:
                print("Division by zero, invalid")
            else:
                result = num1 / num2
                print(f"The quotient is = {result}")
    
    else:
        print("Invalid input. Please select a valid operation.")

