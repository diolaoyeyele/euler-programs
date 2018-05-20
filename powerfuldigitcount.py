a = list(range(2, 2000000))
		 
for item in a:
	if len(str(item*5)) == item:
		print(item)
	elif len(str(item**5)) > item:
		 break
	else:
		continue

		 
for item in a:
	if len(str(item*5)) == 5:
		print(item)
	elif len(str(item**5)) > 5:
		 break
	else:
		continue

		 
for item in a:
	if len(str(item**5)) == 5:
		print(item)
	elif len(str(item**5)) > 5:
		 break
	else:
		continue

def check(n):
	for item in a:
		if len(str(item**n)) == n:
			print(item)
		elif len(str(item**n)) > n:
			 
			 break
		else:
			 
			 continue

		 
check(9)
		 
g = []
		 
g = list(range(1,20))
		 
for item in g:
	check(item)


def check(n):
	for item in a:
		if len(str(item**n)) == n:
			print('{} and {}'.format(item, n))
		elif len(str(item**n)) > n:
			 
			 break
		else:
			 
			 continue

		 
for item in g:
	check(item)


g = list(range(1,40))
		 
for item in g:
	check(item)

