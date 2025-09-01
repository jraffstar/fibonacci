sequence = int(input("How many iterations of the fibonacci sequence would you like to do? \n "))
fib = [None] * (sequence + 1)

# Starting fibonacci sequence numbers
x = 0
y = 1

# Used for later to check if we are adding the starting numbers to the array or not
firstloop = True

for i in range(0, sequence):
	# Assign starting sequence numbers to array
	while firstloop == True:
		fib[i] = x # 0
		fib[i + 1] = y # 1
		firstloop = False

	# Assign the rest of the numbers of the fibonacci sequence of earlier specified length into the array
	if not(i+2 > len(fib) - 1):
		fib[i + 2] = fib[i] + fib[i + 1] # 2

print(fib)