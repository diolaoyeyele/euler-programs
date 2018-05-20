
def isPrime(n):
	for i in range(2, int(n**0.5)+1):
		if n%i ==0:
			return False
	return True

isPrime(4)
False
isPrime(9)
False
isPrime(7)
True
a = list(range(1,2000000))
b = []
for item in a:
	if isPrime(item) == True:
		b.append(item)
	else:
		continue

	

print(sum(b))
