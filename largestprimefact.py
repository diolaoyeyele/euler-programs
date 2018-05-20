a = 13195
b = list(range(1, 13195))
c = []
for item in b:
	if a%item == 0:
		c.append(item)
	else:
		continue

	

def isPrime(n):
	for i in range(2, int(n**0.5)+1):
		if n%i==0:
			return False
	return True


for item in c:
	if isPrime(item) == True:
		print('prime number found')
	else:
		continue

	

c = c[1:]
print(c[-1])

