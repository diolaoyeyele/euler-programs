a = list(range(1,101))
b = []
c = []
for item in a:
	b.append(item^2)

	
c = (sum(a))^2
b = []
for item in a:
	b.append(item**2)

	
print(sum(b))
#338350
print(sum(b) - c)
#333302
c = (sum(a))**2

print(c)
#25502500
print(c - sum(b))
#25164150
