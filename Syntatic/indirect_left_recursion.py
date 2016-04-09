__EMPTY__ = '__EMPTY__'
__ACTIVATED_LOG = False

def isProductive(term,gramatica,NTs):
	
	if term not in NTs:
		return False
	#print term,not ''.join(gramatica[term]).islower(),
	return not ''.join(gramatica[term]).islower()

def replaceProductions(NTs,gramatica,productions_Ai):
	"""
	ex. productions -> ['Bxy','E'] 
	"""
	
	gama = []
	
	if [d in NTs for d in ''.join(productions_Ai)].count(False)==len(''.join(productions_Ai)):
		return productions_Ai
	
	
	if __ACTIVATED_LOG:
		print 'LOG..........Replacing..... Aj=%s->%s in Ai->%s' %(NTs[0],str(gramatica[NTs[0]]),str(productions_Ai))
	

	for production in productions_Ai:
		production_modified = ['']
		
		for term in production:
			
			if isProductive(term,gramatica,NTs):
				print term
				while len(production_modified) < len(gramatica[term]):
					production_modified.append(production_modified[0])


				for index in xrange(len(gramatica[term])):
					if gramatica[term][index] == __EMPTY__:
						production_modified[index] = term
					else:
						production_modified[index] += gramatica[term][index]
			else:
				for index in xrange(len(production_modified)):
			 		production_modified[index]+= term

		gama.extend(production_modified)
	
	if __ACTIVATED_LOG:
		print 'LOG..........Ai After Replacing %s' % (str(gama))
	
	return gama

def isImediateRecursion(NT,productions):
	for term in productions:
		if term[0] in NT:
			return True
	return False

def resolveLeft(NT,productions):
	
	if __ACTIVATED_LOG:
		print 'LOG..........Solve left Recursion in {%s:%s}' % (NT,str(productions))
	
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
	newproductions[newNT].append(__EMPTY__)
	
	if __ACTIVATED_LOG:
		print 'LOG.........Grammar after Solve left Recursion'
		print '            ',newproductions,'\n'
	return newproductions

def solve(gramatica):
	NTs = gramatica.keys()
	NTs.sort()

	for i in xrange(len(NTs)):
		Ai = NTs[i]
		for j in xrange(i):
			Aj = NTs[j]
			
			if __ACTIVATED_LOG:
				print 'LOG..........I=%d,J=%d.....analiying Ai=%s->%s and Aj=%s->%s ' % (i+1,j+1,Aj,gramatica[Aj],Ai,gramatica[Ai])
			
			gramatica[Ai]=replaceProductions([Aj],gramatica,gramatica[Ai])

		if isImediateRecursion(Ai,gramatica[Ai]):
			ypson = resolveLeft(Ai,gramatica[Ai])

			for key,value in ypson.iteritems():
				gramatica[key]=ypson[key]

	
	return gramatica

def assert_gramatica(gramatica1,gramatica2):
	g1 = zip(gramatica1.keys(),gramatica1.values())
	g1.sort()
	g2 = zip(gramatica2.keys(),gramatica2.values())
	g2.sort()
	
	
	return str(g1)==str(g2)


def refactor_empty(gramatica):
	"""
	 This is used to remove all empty termianals from the grammar and replace it by a NT
	"""
	NTs = gramatica.keys()
	NTs = ",".join(NTs).replace('"','').split(',')
	NTs.sort()

	empty_NT = chr(ord(NTs[-1])+1)

	for NT, productions in gramatica.iteritems():
		productions = ','.join(productions)

		if __EMPTY__ in productions:
			productions = productions.replace(__EMPTY__,empty_NT)
		gramatica[NT] = productions.split(',')
			

	gramatica[empty_NT] = __EMPTY__



def test():
	# g1 = {'A':['B'],'B':['C'],'C':['D'],'D':['E'],'E':['Ea']}
	# Eg1 = {'A': ['B'], 'C': ['D'], 'B': ['C'], 'E': [], 'D': ['E'], 'E"': ['aE"',__EMPTY__]}
	# assert(assert_gramatica(solve(g1),Eg1))

	# g2 = {'A':['Ac','Sd','F'],'S':['Aa','b'],'F':[__EMPTY__]}
	# Eg2 = {'A': ['SdA"', 'FA"'], 'S"': ['dA"aS"', __EMPTY__], 'S': ['FA"aS"', 'bS"'], 'A"': ['cA"', __EMPTY__], 'F': [__EMPTY__]}
	# assert(assert_gramatica(solve(g2),Eg2))

	# g3 = {'A':['Ac','Sd',__EMPTY__],'S':['Aa','b']}
	# Eg3 = {'A': ['SdA"', '__EMPTY__A"'], 'S"': ['dA"aS"', '__EMPTY__'], 'S': ['__EMPTY__A"aS"', 'bS"'], 'A"': ['cA"', '__EMPTY__']}

	
	# g3solved = solve(g3)
	# refactor_empty(g3solved)
	# refactor_empty(g3)

	# assert(assert_gramatica(g3solved,g3))


	# g4 = {'A':['Bb'],'B':['a'],'C':['Ac']}
	# Eg4 = {'A':['Ba'],'B':['b'],'C':['bac']}

	# assert(assert_gramatica(solve(g4),Eg4))

	g5 = {'A':['Ba','Db','a','__EMPTY__'],'B':['D','Ga'],'C':['Ac'],'D':['A','B'],'F':['FD','g'],'G':['AaF','__EMPTY__']}
	print solve(g5)

	



if "__main__":
	__ACTIVATED_LOG = True
	test()
	gramatica = {'A':['Ba'],'B':['b'],'C':['Ac']}
	print solve(gramatica)








	