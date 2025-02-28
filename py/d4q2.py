def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

a = int(input("Enter the range of Fibonacci numbers to generate: "))

fib_sequence = []
for i in range(a):
	fib_sequence.append(fib(i))
print(f"Fibonacci series up to {a} terms: {fib_sequence}")
