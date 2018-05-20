a = list(range(2, 20000))
		 
def isPrime(n):
	for i in range(2, int(n**0.5)+1):
		if n%i ==0:
			return False
	return True

		 
b = []
		 
for item in a:
	if isPrime(item) == True:
		 b.append(item)
	else:
		 continue

		 

print(len(b))
		 
a = list(range(2, 200000))
		 
b = []
		 
for item in a:
	if isPrime(item) == True:
		 b.append(item)
	else:
		 continue

		 		 

print(b[10000])
		 
