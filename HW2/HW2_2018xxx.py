# CSE 101 - IP HW2
# K-Map Minimization 
# Name:Asmit Kumar Singh
# Roll Number:2018025
# Section:A
# Group:1
# Date:

#this program is written taking inspiration from the quine mc-clusky algo and petrik's method in order to create a minimized expression


# #this function converts decimal to equivalent binary with required number of bits.

	
def decToBinary(n,numVar):
	a=bin(n)
	a=a[2:]
	zero_to_add = numVar - len(a)
	a = '0' * zero_to_add + a
	return a

#this function creates implicants which can be pairs quads octs or even a sixteen one, thehse are the all possible implicants
def primeimpnd(min,numvar):
	l=[]
	newmin=list(min)
	for i in min:
			for j in min:
					ctr=0
					for k in range(numvar):
						if i[k]!=j[k]:
							ctr+=1
				
					if ctr==1:
						for k in range(numvar):
							if i[k]!=j[k]:
								new=i[0:k]+'-'+i[k+1:numvar]
						if new not in newmin and new not in l:
							newmin.append(new)
							l.append(new)
	return l


'''this function returns a list of minterms excluding the dont care terms'''		
def mintnd(stringIn,numVar):
	min=[]
	i=0
	j=stringIn.find('d')
	stringIn=stringIn[:j]
	while stringIn[i]!=')':
		if i==0:
			if stringIn.find(',')!=-1:

				min.append(decToBinary(int(stringIn[1:stringIn.find(',')]),numVar))
			else:
				min.append(decToBinary(int(stringIn[1:stringIn.find(')')]),numVar))


		if stringIn[i] == "," :
			
			if stringIn.find(',',i+1) != -1:
				min.append(decToBinary(int(stringIn[i+1:stringIn.find(',',i+1)]),numVar))
			else:
				min.append(decToBinary(int(stringIn[i+1:stringIn.find(')')]),numVar))
		i+=1				
	return min
'''this function returns a list of minterms including the dont care terms'''		

def mintwd(stringIn,min,numVar):
	i=stringIn.find('d')
	stringIn=stringIn[i+1:]
	i=0
	mind=list(min)	

	while stringIn[i]!=')':
		if i==0:
			if stringIn.find(',')!=-1:
				mind.append(decToBinary(int(stringIn[1:stringIn.find(',')]),numVar))
			else:
				mind.append(decToBinary(int(stringIn[1:stringIn.find(')')]),numVar))


		if stringIn[i] == "," :
			
			if stringIn.find(',',i+1) != -1:
				mind.append(decToBinary(int(stringIn[i+1:stringIn.find(',',i+1)]),numVar))
			else:
				mind.append(decToBinary(int(stringIn[i+1:stringIn.find(')')]),numVar))
		i+=1	
	return mind	

'''this function's aim is to calucate the prime implicants from all possible implicants. var (0,1,2,3,4) are the all possible singlets pairs quads and octs from which the prime implicants are calculated
this function checks if there is any singlet which is not covered in pairs , if there is any pair which is not covered in quads any quads not covered in octets and hex if any nd appends them
to the prime implicant's list this is done using newvar and sudo var variabe lists   '''
def piscal(var0,var1,var2,var3,var4):
	sudovar3=[]
	for i in var3:
		sudovar3.append(i.replace('-','1'))
		sudovar3.append(i.replace('-','0'))
	newvar4=[]

	for i in var4:
		if i not in sudovar3:
			newvar4.append(i)

	sudovar2=[]
	for i in var2:
		i1=i.find('-')
		i2=i.find('-',i1+1)
		sudovar2.append(i[:i1]+'1'+i[i1+1:])
		sudovar2.append(i[:i1]+'0'+i[i1+1:])
		sudovar2.append(i[:i2]+'1'+i[i2+1:])
		sudovar2.append(i[:i2]+'0'+i[i2+1:])

	newvar3=[]
	for i in var3:
		if i not in sudovar2:
			newvar3.append(i)

	sudovar1=[]
	for i in var1:
		i1=i.find('-')
		i2=i.find('-',i1+1)
		i3=i.find('-',i2+1)
		sudovar1.append(i[:i1]+'1'+i[i1+1:])
		sudovar1.append(i[:i1]+'0'+i[i1+1:])
		sudovar1.append(i[:i2]+'1'+i[i2+1:])
		sudovar1.append(i[:i2]+'0'+i[i2+1:])
		sudovar1.append(i[:i3]+'0'+i[i3+1:])
		sudovar1.append(i[:i3]+'1'+i[i3+1:])

	sudovar0=[]
	for i in var0:
		i1=i.find('-')
		i2=i.find('-',i1+1)
		i3=i.find('-',i2+1)
		i4=i.find('-',i3+1)
		sudovar0.append(i[:i1]+'1'+i[i1+1:])
		sudovar0.append(i[:i1]+'0'+i[i1+1:])
		sudovar0.append(i[:i2]+'1'+i[i2+1:])
		sudovar0.append(i[:i2]+'0'+i[i2+1:])
		sudovar0.append(i[:i3]+'0'+i[i3+1:])
		sudovar0.append(i[:i3]+'1'+i[i3+1:])
		sudovar0.append(i[:i4]+'0'+i[i4+1:])
		sudovar0.append(i[:i4]+'1'+i[i4+1:])


	newvar2=[]
		

	for i in var2:
		if i not in sudovar1:
			newvar2.append(i)

	newvar1=[]
	for i in var1:
		if i not in sudovar0:
			newvar1.append(i)

	pis=[]

	for i in var0:
		pis.append(i)


	for i in newvar1:
		pis.append(i)

	for i in newvar2:
		pis.append(i)

	for i in newvar3:
		pis.append(i)


	for i in newvar4:
		pis.append(i)

	

	return pis

'''this is our main function which is callled'''
def minFunc(numVar, stringIn):
	i=stringIn.find('d')

	if stringIn[i+1]=='-':
		dontcare=0
	else:
		dontcare=1
	   


	if dontcare==0:
		var4=mintnd(stringIn,numVar)
		var3=primeimpnd(var4,numVar)
		var2=primeimpnd(var3,numVar)
		var1=primeimpnd(var2,numVar)
		var0=primeimpnd(var1,numVar)

	if dontcare==1:
		
		var4=mintnd(stringIn,numVar)
		mind=mintwd(stringIn,var4,numVar)
		var3=primeimpnd(mind,numVar)
		var2=primeimpnd(var3,numVar)
		var1=primeimpnd(var2,numVar)
		var0=primeimpnd(var1,numVar)


	if dontcare==0:
		pis=piscal(var0,var1,var2,var3,var4)
		# print("hi",pis)

	if dontcare==1:
		pis=piscal(var0,var1,var2,var3,mind)
#this functioin creates a virtual table which is a nested list this method is inspires from quine mccluskya prime implicant table is made .#the epis cal function traverses the table and searches for rows a single one which are basically the epis and are appended into the list theses are basically in the final solution
	def tablewithoutd(var4,pis):
		table=[]
		inj=0
		ini=0
		for i in var4:
			table.append([])
			for j in pis:
				t=1
				if j.count('-')==2:
					i1=j.find('-')
					i2=j.find('-',i1+1)
					if i==(j[:i1]+'1'+j[i1+1:i2]+'1'+j[i2+1:]) or i==(j[:i1]+'0'+j[i1+1:i2]+'1'+j[i2+1:]) or i==(j[:i1]+'1'+j[i1+1:i2]+'0'+j[i2+1:]) or i == (j[:i1]+'0'+j[i1+1:i2]+'0'+j[i2+1:]) :
						table[ini].append('1')
						t=0
				if j.count('-')==1:
					if i==j.replace('-','1') or i==j.replace('-','0'):
						table[ini].append('1')
						t=0
				
				if j.count('-')==0:
					if i==j:
						table[ini].append('1')
						t=0

				if j.count('-')==3:
					i1=j.find('-')
					i2=j.find('-',i1+1)
					i3=j.find('-',i2+1)
					if i==(j[:i1]+'0'+j[i1+1:i2]+'0'+j[i2+1:i3]+'0'+j[i3+1:]) or i==(j[:i1]+'0'+j[i1+1:i2]+'0'+j[i2+1:i3]+'1'+j[i3+1:]) or i==(j[:i1]+'0'+j[i1+1:i2]+'1'+j[i2+1:i3]+'0'+j[i3+1:]) or i==(j[:i1]+'0'+j[i1+1:i2]+'1'+j[i2+1:i3]+'1'+j[i3+1:])or i==(j[:i1]+'1'+j[i1+1:i2]+'0'+j[i2+1:i3]+'0'+j[i3+1:])or i==(j[:i1]+'1'+j[i1+1:i2]+'0'+j[i2+1:i3]+'1'+j[i3+1:])or i==(j[:i1]+'1'+j[i1+1:i2]+'1'+j[i2+1:i3]+'0'+j[i3+1:])or i==(j[:i1]+'1'+j[i1+1:i2]+'1'+j[i2+1:i3]+'1'+j[i3+1:]) :
						table[ini].append('1')
						t=0	
				if j.count('-')==4:
						table[ini].append('1')
						t=0				




				if t==1: 
					table[ini].append('0')	
				inj+=1

				
			ini+=1


		# print (table)
		return table
	table=tablewithoutd(var4,pis)
		
#the epis cal function traverses the table and searches for rows a single one which are basically the epis and are appended into the list theses are basically in the final solution
	def episcal(table,pis)	:
		epis=[]
		for i in table:
			if i.count('1')==1:
				for j in range(len(i)):
					if i[j]=='1':
						if pis[j] not in epis:
							epis.append(pis[j])

		# print(epis)
		return epis

	epis=episcal(table,pis)
#this funciton creates a list of pi's which are not in the epis and are columns of the new final table
	def pis_e(pis,epis):
		pis_e=[]
		for i in pis:
			if i not in epis:
				pis_e.append(i)


		# print(pis_e)
		return pis_e

	pis_e=pis_e(pis,epis)

#this function calculates the needed minterms which are not yet covered by the epis and are the rows of the final table

	def neededcal(table,var4,epis):
		notneeded=[]
		ini=0
		for i in table:
			for j in range(len(i)):
				if pis[j] in epis:
					if i[j]=='1':
						notneeded.append(var4[ini])
			ini+=1			
		 


		needed=[]
		for i in var4:
			if i not in notneeded:
				needed.append(i)

		# print(needed)
		return needed

	needed=neededcal(table,var4,epis)
	#table1 is the final table on which petrik's method will be applied.
	print(needed)
	if needed!=[]:

		table1=[]
		inj=0
		ini=0
		for i in needed:
			table1.append([])
			for j in pis_e:
				t=1
				if j.count('-')==2:
					i1=j.find('-')
					i2=j.find('-',i1+1)
					if i==(j[:i1]+'1'+j[i1+1:i2]+'1'+j[i2+1:]) or i==(j[:i1]+'0'+j[i1+1:i2]+'1'+j[i2+1:]) or i==(j[:i1]+'1'+j[i1+1:i2]+'0'+j[i2+1:]) or i == (j[:i1]+'0'+j[i1+1:i2]+'0'+j[i2+1:]) :
						table1[ini].append('1')
						t=0
				if j.count('-')==1:
					if i==j.replace('-','1') or i==j.replace('-','0'):
						table1[ini].append('1')
						t=0
				
				if j.count('-')==0:
					if i==j:
						table1[ini].append('1')
						t=0

				if j.count('-')==3:
					i1=j.find('-')
					i2=j.find('-',i1+1)
					i3=j.find('-',i2+1)
					if i==(j[:i1]+'0'+j[i1+1:i2]+'0'+j[i2+1:i3]+'0'+j[i3+1:]) or i==(j[:i1]+'0'+j[i1+1:i2]+'0'+j[i2+1:i3]+'1'+j[i3+1:]) or i==(j[:i1]+'0'+j[i1+1:i2]+'1'+j[i2+1:i3]+'0'+j[i3+1:]) or i==(j[:i1]+'0'+j[i1+1:i2]+'1'+j[i2+1:i3]+'1'+j[i3+1:])or i==(j[:i1]+'1'+j[i1+1:i2]+'0'+j[i2+1:i3]+'0'+j[i3+1:])or i==(j[:i1]+'1'+j[i1+1:i2]+'0'+j[i2+1:i3]+'1'+j[i3+1:])or i==(j[:i1]+'1'+j[i1+1:i2]+'1'+j[i2+1:i3]+'0'+j[i3+1:])or i==(j[:i1]+'1'+j[i1+1:i2]+'1'+j[i2+1:i3]+'1'+j[i3+1:]) :
						table1[ini].append('1')
						t=0	

				if t==1: 
					table1[ini].append('0')	
				inj+=1

				
			ini+=1
		print(table1)	
		#sopvar is the list containing names 'P0','P1','P2'etc. which are id's assigned to various pi's from pi_e list for function of petrick's method
		sopvar=[]
		for i in range(len(pis_e)):
			sopvar.append('p'+str(i))

		# print(sopvar)
		#anstr is a list of lists containing terms from sopvar in order to create a virtual pos form of type (p1+p2)(p1+...)(sd) i which is implemented in form of listsof lists
		anstr=[]
		for i in range(len(needed)):
			anstr.append([])
			for j in range(len(sopvar)):
				if table1[i][j]=='1':
					anstr[i].append(sopvar[j])
			
		print(anstr)

		#this part is used to implement petrik's method in orderto get the final terms from the table which need to be in the solution.		
		#this is a recursive function 
		def petrick(a,b,c):
			if len(c)==1:
				
				return c


			if b < len(c):
				print (len(c))
				s = []
				for  i in c[b]:
					for j in c[a]:

						s.append(i+" "+j)
				# print (s)
				del c[0]
				del c[0]

				n = [s]+ c
				return petrick(0,1,n)
			 
			
		upd = petrick(0,1,anstr)
		

		new_dist = []
		for i in upd[0]:

			a = list(set(i.split(" ")))
			a.sort()
			
			new_dist.append(" ".join(a))
		
		emp = []
		for i in list(set(new_dist)):

			for j in list(set(new_dist)):
				if set(i.split(" ")) < set(j.split(" ")):
					if j not  in emp:
						emp.append(j)


		z = list(set(new_dist).difference(set(emp)))
		print(z)

		#now we have a sop form in form of list of lists ad we ant the term with minimum numbers of terms which is don here
		minl=100
		for i in z:
			if len(i)<minl:
				minl=len(i)
		print(minl)

		finalz=[]
		for i in z:
			if len(i)==minl:
				finalz.append(i)

		print(finalz)
		pakkafinalz=[]
		for i in finalz:
			pakkafinalz.append(i.split(' '))

			# a dictionary is made to easily access the corresponding terms to p0,p1,p2

		dic_num_to_p = {}


		for i,j in enumerate(pis_e):
			dic_num_to_p['p'+str(i)] = j

		
		soln=[]
		print(pakkafinalz)
		for i in pakkafinalz:
			temp=[]		
			for j in i:
				temp.append( dic_num_to_p[j] )
			
			soln.append(epis+temp)
		print(soln)
		sort_1=sorted(soln, key=lambda x: sum([y.count("-") for y in x]),reverse=True )
		print(sort_1)
		answer=sort_1[0]
		print(answer)


			#dictionaries corresponding to my code to present the answer in terms of w,x,y,z
		indexp={'0':'w','1':'x','2':'y','3':'z'}
		indexn={'0':'w\'','1':'x\'','2':'y\'','3':'z\''}
		
		f_s = ""
		for i in answer:
			s = ""
			for j in range(len(i)):
				if i[j] == '0':
					s += indexn[str(j)]
				elif i[j] == '1':
					s += indexp[str(j)]


			
			f_s = f_s +  s + "+"
		k=f_s[:-1]
		A=list(map(str,k.split('+')))
		A.sort()	
		return('+'.join(A))
		
	

	else:
		
		indexp={'0':'w','1':'x','2':'y','3':'z'}
		indexn={'0':'w\'','1':'x\'','2':'y\'','3':'z\''}
		answer=[]
		f_s = ""
		for i in epis:
			s = ""
			for j in range(len(i)):
				if i[j] == '0':
					s += indexn[str(j)]
				elif i[j] == '1':
					s += indexp[str(j)]


			
			f_s = f_s +  s + "+"
		if epis[0].count('-')==numVar:
			return "1"
		k=f_s[:-1]
		A=list(map(str,k.split('+')))
		A.sort()
		
		return('+'.join(A))


print((minFunc(3,'(0,1,2,3,7) d-')))