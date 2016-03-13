
def isProductive(term,gramatica,NTs):
	
	if term not in NTs:
		return False
	#print term,not ''.join(gramatica[term]).islower(),
	return not ''.join(gramatica[term]).islower()

def replaceProductions(NTs,gramatica,productions):
	"""
	ex. productions -> ['Bxy','x'] 
	"""
	
	gama = []
	
	if [d in NTs for d in ''.join(productions)].count(False)==len(''.join(productions)):
		return productions
	
	print 'Replacing------Ai=%sAj=%s' %(str(productions).ljust(20),str(gramatica[NTs[0]]).ljust(10))
	for production in productions:
		newterms = ['']

		for term in production:
			
			if isProductive(term,gramatica,NTs):
				
				while len(newterms) < len(gramatica[term]):
					newterms.append(newterms[0])
				for index in xrange(len(gramatica[term])):
					newterms[index] += gramatica[term][index]
			else:
				for index in xrange(len(newterms)):
			 		newterms[index]+= term

		gama.extend(newterms)
	return gama

def isImediateRecursion(NT,productions):
	for term in productions:
		if term[0] in NT:
			return True
	return False

def resolveLeft(NT,productions):
	print '\nSolve left Recursion of {%s:%s}=>' % (NT,str(productions)),
	newNT = NT+'"'
	newproductions = {NT:[],newNT:[]}
	alfas = []
	betas = []
	for production in productions:
		if production[0]==NT:
			alfas.append(production[1:])
		else:
			betas.append(production)

	for b in betas:
		newproductions[NT].append(b+newNT)

	for a in alfas:
		newproductions[newNT].append(a+newNT)
	print newproductions
	return newproductions

def solve(gramatica):
	NTs = gramatica.keys()
	NTs.sort()

	for i in xrange(len(NTs)):
		Ai = NTs[i]
		for j in xrange(i):
			Aj = NTs[j]
			gramatica[Ai]=replaceProductions([Aj],gramatica,gramatica[Ai])

		if isImediateRecursion(Ai,gramatica[Ai]):
			ypson = resolveLeft(Ai,gramatica[Ai])

			for key,value in ypson.iteritems():
				gramatica[key]=ypson[key]

	print '\n',gramatica,'\n\n'

if "__main__":
	solve(gramatica = {'A':['Bxy','x'],'B':['CD'],'C':['A','c'],'D':['d']})
	solve(gramatica = {'S':['Aa','b'],'A':['Ac','Sd','vazio']})