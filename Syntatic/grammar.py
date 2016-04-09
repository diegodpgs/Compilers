from utils import *

class Grammar:

	def __init__(self,grammar,ACTIVATED_LOG=False,EMPTY='EMPTY'):
		self.grammar = grammar
		self.EMPTY = EMPTY
		self.__ACTIVATED_LOG__ = ACTIVATED_LOG
		self.NTs = self.grammar.keys()


	#A derive B that derive C
	#Example B -> C -> D
	def isProductive(self,term):
	
		if term not in self.NTs:
			return False
		
		for production in self.grammar[term]:

			if not production.islower() and production != self.EMPTY:
				return True

		return False
	
	def containsNT(self,productions,NT):
		"""
			A -> DBa
			C -> Bc|Xy|aA|xA
			C has the NT A.

			return True
		"""
		for production in productions:

			if production != self.EMPTY and NT in splitProduction(production,self.NTs):
				return True
		return False

	def replaceProductions(self,NT_Aj,productions_Ai):
		"""
		ex. productions -> ['Bxy','E'] 
		"""
		
		gama = []
		
		
		#Aj derivate Ai
		if not self.containsNT(productions_Ai,NT_Aj):
			
			if self.__ACTIVATED_LOG__:
				print 'LOG..........%s is not within %s' % (NT_Aj,productions_Ai)
			
			return productions_Ai

		if self.__ACTIVATED_LOG__:
			print 'LOG..........Replacing..... Aj->%s in Ai->%s' %(str(self.grammar[NT_Aj]),str(productions_Ai))
		

		for production in productions_Ai:

			production_modified = ['']
			
			if production != self.EMPTY:
				
				for term in splitProduction(production,self.NTs):

					if term == NT_Aj:

						
						while len(production_modified) < len(self.grammar[term]):
							production_modified.append('')
						
						
					 	
						for index in xrange(len(self.grammar[term])):

							if self.grammar[term][index] == self.EMPTY:
								production_modified[index] = term
							else:
								production_modified[index] += self.grammar[term][index]
							
					else:
						
						for index in xrange(len(production_modified)):
					 		production_modified[index]+= term
			else:
				production_modified = production


			gama.extend(production_modified)
		
		if self.__ACTIVATED_LOG__:
			print 'LOG..........Ai After Replacing %s' % (str(gama))
		
		return gama

	def isImediateRecursion(self,NT,productions):
		
		for term in productions:
			if term[0] in NT:
				return True
		
		return False

	#OK
	def resolveLeft(self,NT,productions):
		
		if self.__ACTIVATED_LOG__:
			print 'LOG..........Solve left Recursion in {%s:%s}' % (NT,str(productions))
		
		newNT = NT+'"'
		
		self.NTs.append(newNT)

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
		newproductions[newNT].append(self.EMPTY)
		
		if self.__ACTIVATED_LOG__:
			print 'LOG.........Grammar after Solve left Recursion'
			print '            ',newproductions,'\n'
		return newproductions

	def refactor_empty(self):
		"""
		 This is used to remove all empty termianals from the grammar and replace it by a NT
		"""
		
		NTs_r = ",".join(self.NTs).replace('"','').split(',')
		NTs_r.sort()

		empty_NT = chr(ord(NTs_r[-1])+1)
		
		for NT, productions in self.grammar.iteritems():

			productions = ','.join(productions)

			if self.EMPTY in productions:
				productions = productions.replace(self.EMPTY,empty_NT)
			self.grammar[NT] = productions.split(',')
				

		self.grammar[empty_NT] = self.EMPTY

	def solve(self):
		
		self.NTs.sort()

		for i in xrange(len(self.NTs)):
			
			Ai = self.NTs[i]
			for j in xrange(i):
				Aj = self.NTs[j]
				
				if self.__ACTIVATED_LOG__:
					print 'LOG..........I=%d,J=%d.....analiying Ai=%s->%s and Aj=%s->%s ' % (i+1,j+1,Ai,self.grammar[Ai],Aj,self.grammar[Aj])
				
				
				self.grammar[Ai]=self.replaceProductions(Aj,self.grammar[Ai])
				


			if self.isImediateRecursion(Ai,self.grammar[Ai]):
				
				ypson = self.resolveLeft(Ai,self.grammar[Ai])
				
				

				for key,value in ypson.iteritems():
					self.grammar[key]=ypson[key]
			

			

	def setGrammar(self,grammar):
		self.grammar = grammar
		self.NTs = grammar.keys()
	
	def __eq__(self,obj):
		g1 = zip(self.grammar.keys(),self.grammar.values())
		g1.sort()
		g2 = zip(obj.grammar.keys(),obj.grammar.values())
		g2.sort() 

		
		return str(g1)==str(g2)


def test():

	g1 = Grammar({'A':['B'],'B':['C'],'C':['D'],'D':['E'],'E':['Ea']})
	Eg1 = Grammar({'A': ['B'], 'C': ['D'], 'B': ['C'], 'E': [], 'D': ['E'], 'E"': ['aE"','EMPTY']})
	g1.solve()
	assert(g1 == Eg1)
	print 'Test1 [OK]:    Grammar %s' % str({'A':['B'],'B':['C'],'C':['D'],'D':['E'],'E':['Ea']})

	g2 = Grammar({'A':['Ac','Sd','F'],'S':['Aa','b'],'F':['EMPTY']})
	Eg2 = Grammar({'A': ['SdA"', 'FA"'], 'S"': ['dA"aS"', 'EMPTY'], 'S': ['FA"aS"', 'bS"'], 'A"': ['cA"', 'EMPTY'], 'F': ['EMPTY']})
	g2.solve()
	assert(g2 == Eg2)
	print 'Test2 [OK]:    Grammar %s' % str({'A':['Ac','Sd','F'],'S':['Aa','b'],'F':['EMPTY']})

	g3 = Grammar({'A':['Ac','Sd','EMPTY'],'S':['Aa','b']})
	Eg3 = Grammar({'A': ['SdA"', 'EMPTYA"'], 'S"': ['dA"aS"', 'EMPTY'], 'S': ['EMPTYA"aS"', 'bS"'], 'A"': ['cA"', 'EMPTY']})
	g3.solve()
	g3.refactor_empty()
	Eg3.refactor_empty()
	assert(g3 == Eg3)
	print 'Test3 [OK]:    Grammar %s' % str({'A':['Ac','Sd','EMPTY'],'S':['Aa','b']})
 

	g4 = Grammar({'A':['Bb'],'B':['a'],'C':['Ac']})
	Eg4 = Grammar({'A':['Bb'],'B':['a'],'C':['abc']})
	g4.solve()
	assert(g4==Eg4)
	print 'Test4 [OK]:    Grammar %s' % str({'A':['Bb'],'B':['a'],'C':['Ac']})
	
	g5 = Grammar({'A':['Ba','cb','a','EMPTY'],'B':['a','Ga'],'C':['Ac'],'F':['Fb','g'],'G':['AaF','EMPTY']})
	Eg5 = Grammar({'A': ['Ba', 'cb', 'a', 'H'], 'C': ['aac', 'Gaac', 'cbc', 'ac', 'Hc'], 'B': ['a', 'Ga'], 'G': ['aaagF"G"', 'cbagF"G"', 'aagF"G"', 'HagF"G"', 'HG"'], 'F': ['gF"'], 'H': 'EMPTY', 'F"': ['bF"', 'EMPTY'], 'G"': ['aaagF"G"', 'EMPTY']})
	g5.refactor_empty()
	g5.solve()
	assert(g5==Eg5)
	print 'Test5 [OK]:    Grammar %s' % str({'A':['Ba','cb','a','EMPTY'],'B':['a','Ga'],'C':['Ac'],'F':['Fb','g'],'G':['AaF','EMPTY']})
	
	
	g5 = Grammar({'A':['Ba','Db','a','EMPTY'],'B':['D','Ga'],'C':['Ac'],'D':['A','B'],'F':['FD','g'],'G':['AaF','EMPTY']})
	Eg5 = Grammar({'A': ['Ba', 'Db', 'a', 'EMPTY'], 'C': ['Dac', 'Gaac', 'Dbc', 'ac', 'Ac'], 'B': ['D', 'Ga'], 'D': ['GaaD"', 'aD"', 'AD"', 'GaD"'], 'G': ['aDaagF"G"', 'ADaagF"G"', 'aDbagF"G"', 'ADbagF"G"', 'aagF"G"', 'AagF"G"', 'EG"', 'MG"', 'PG"', 'TG"', 'YG"'], 'F': ['gF"'], 'D"': ['aD"', 'bD"', 'D"', 'EMPTY'], 'F"': ['DF"', 'EMPTY'], 'G"': ['aaDaagF"G"', 'aDaagF"G"', 'aaagF"G"', 'aaDbagF"G"', 'aDbagF"G"', 'EMPTY']})
	g5.solve()
	assert(g5==Eg5)
	print 'Test6 [OK]:    Grammar %s' % str({'A':['Ba','Db','a','EMPTY'],'B':['D','Ga'],'C':['Ac'],'D':['A','B'],'F':['FD','g'],'G':['AaF','EMPTY']})
	
if "__main__":
	test()
	# gramatica = {'A':['Ba'],'B':['b'],'C':['Ac']}
	# print solve(gramatica)








	