def decToBinary(n,numVar):
	if numVar==4:
		a=bin(n)
		a=a[2:]
		if len(a)==3:
			return a
		if len(a)==2:
			a='0'+a
			print(a)
			return a
		if len(a)==1:
			a='00'+a
			print(a)
			return a



print(decToBinary(1,4))