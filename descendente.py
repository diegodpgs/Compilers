#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils import *


class Descendente:

	def __init__(self,gramatica,initial,empty):
		self.gramatica = gramatica
		self.__EMPTY__ = empty
		self.__INITIAL__ = initial
		self.__SYMBOL_MARK = '$'
		self.follows = {}
		self.firsts = {}
		self.NTs = gramatica.keys()
		self.terms = self.getTerms()
		self.terminals = set(self.terms) - set(self.NTs)
		self.table = dict([(keyNT,dict([(key,'') for key in list(self.terminals)])) for keyNT in self.NTs])
		self.trackfollow = []


	def setGramatica(self,gramatica,initial):
		self.gramatica = gramatica
		self.terms = self.getTerms()
		self.cache_follows = {}
		self.cache_firsts = {}
		self.__INITIAL__ = initial
		self.terminals = set(self.terms) - set(self.NTs)
		self.table = dict([(keyNT,dict([(key,'') for key in list(self.terminals)])) for keyNT in self.NTs])

	def getTerms(self):
		productions = []
		terms = []
		[productions.extend(v) for v in self.gramatica.values()]

		[terms.extend(splitProduction(v,self.NTs)) for v in productions]
		terms.extend(self.NTs)
		return list(set(terms)-set([self.__EMPTY__]))

	def computeFirst(self):
		
		for term in self.terms:

			if term not in self.NTs:

				self.firsts[term] = [term]

			else:
				
				self.firsts[term] = self.first(term)

	def printFirst(self,):

		for key,value in self.firsts.iteritems():
			
			if len(value) > 1:
				print 'First(%s) -> {%s}' % (key,",".join(value))
			else:
				print 'First(%s) -> {%s}' % (key,value[0])

	def printFollow(self):

		for key,value in self.follows.iteritems():
			
			if len(value) > 1:
				print 'Follow(%s) -> {%s}' % (key,",".join(value))
			else:
				print 'Follow(%s) -> {%s}' % (key,value[0])

	def first(self,NT):
	
		if NT in self.firsts:
			return self.firsts[NT]

		f = []
		
		if NT not in self.NTs:
			return [NT]
		
		if self.__EMPTY__ in self.gramatica[NT]:
			f.append(self.__EMPTY__)

		for production in self.gramatica[NT]:
			index = 0
			
			production = splitProduction(production,self.NTs)
			first_term = self.first(production[0])

			
			while index < len(production) and self.__EMPTY__ in first_term:
			
				first_term = production[index]
				index += 1

				if first_term != self.__EMPTY__:
					if first_term in self.NTs:
						first_term = self.first(first_term)
						f.extend(first_term)
						if self.__EMPTY__ in f:
							f.remove(self.__EMPTY__)

					else:
						f.extend(first_term)
						if self.__EMPTY__ in f:
							f.remove(self.__EMPTY__)
			
			if self.__EMPTY__ not in first_term:
				
				f.extend(first_term)

		return list(set(f))

	def getFollowProductions(self,B):
		productions_B = []

		for NTP, productions in self.gramatica.iteritems():
			
			for production in productions:
				
				production = splitProduction(production,self.NTs)
				
				if B in production and B not in productions_B:
						
					if B == production[-1]:
						productions_B.append({'A':NTP})
					else:
						productions_B.append({'A':NTP,'Beta':production[production.index(B)+1:]})

		return productions_B

	def follow(self,NT):
		
		if NT in self.follows:
			return self.follows[NT]
		
		if len(self.trackfollow) > 5 and len(set(self.trackfollow)) < len(self.trackfollow):
			return []
	
		

		F = []

		if NT == self.__INITIAL__:
			F = [self.__SYMBOL_MARK]

		productions =  self.getFollowProductions(NT)
		
		self.trackfollow.append(NT)

		for production in productions:

			if 'Beta' in production:
				
				indexbeta = 0

				#while Empty in First(Betai)
				while indexbeta < len(production['Beta']):
					first_beta = self.firsts[production['Beta'][indexbeta]][:]
					
					#Follow(B) <- Fist(Beta)- Empty
					for f in first_beta:
						if self.__EMPTY__ != f:
							F.append(f)

					if self.__EMPTY__ not in first_beta:
						break

					indexbeta += 1

			
			if 	('Beta' not in production) or \
				('Beta' in production and self.__EMPTY__ in self.firsts[production['Beta'][0]]):
				
				if production['A'] != NT:
					F.extend(self.follow(production['A']))
				
		self.trackfollow = []
		return list(set(F))

	def computFollow(self):
		self.computeFirst()

		for n in self.gramatica.keys():
			self.follows[n] = self.follow(n)

	def buildTable(self):
		
		#rule 1 Para cada terminal a em FIRST(⍺), inclua A -> ⍺ em M[A, a]

		for A,productions in self.gramatica.iteritems():
			
			for production in productions:
				production = splitProduction(production,self.NTs)
				alfa = production
				alfa_0 = alfa[0]
				
				first_alfa = alfa #just in case of empty

				if alfa_0 in self.firsts:
					first_alfa = self.firsts[alfa_0]

				value = '%s->%s' % (A,''.join(alfa))

				for a in first_alfa:
					if a != self.__EMPTY__:
						self.table[A][a] = value
				
				#Rule 2 Se EMPTY pertence a FIRST(⍺), inclua A -> ⍺ em M[A, b] para cada terminal b em FOLLOW(A).
				
				if self.__EMPTY__ in first_alfa:
					for b in self.follows[A]:
						if self.__SYMBOL_MARK in self.follows[A]:
							self.table[A][self.__SYMBOL_MARK] = value
						
						self.table[A][b] = value

	def printTable(self):

		for NT, Ts in self.table.iteritems():
			print '>>>>',NT,'#'*30
			for t,values in Ts.iteritems():
				if len(values) != 0:
					print t,'   %s' % (values.rjust(12))
	
	def recognize(self,input_source):
		stack = [self.__INITIAL__,self.__SYMBOL_MARK]
		input_source.append(self.__SYMBOL_MARK)
		action = []

		NT_analised = stack[0]
		terminal_input_analised = input_source[0]
		print '%s %s %s' % ('Stack'.ljust(25),'Input'.ljust(10),'Action'.ljust(15))
		
		while NT_analised != self.__SYMBOL_MARK:
			print '%s %s' % ("".join(stack).ljust(25),"".join(input_source).ljust(10)),

			if NT_analised == terminal_input_analised:
				print ' %s' % ('terminal'.ljust(15))
				del input_source[0]
				del stack[0]

			elif NT_analised not in self.NTs:
				raise Exception('ERROR: symbol not recognized')

			elif self.table[NT_analised][terminal_input_analised] == 'ERROR':
				raise Exception('ERROR: symbol not recognized')

			elif NT_analised in self.NTs:
				#print '\nT:%s   NT:%s' % (terminal_input_analised,NT_analised)
				#print 'table[%s]: %s' % (NT_analised,str(self.table[NT_analised])) 
				production = self.table[NT_analised][terminal_input_analised].split('->')[1]
				print ' %s' % ("".join(production).ljust(15))
				del stack[0]

				for p in splitProduction(production,self.NTs)[::-1]:
					if p != self.__EMPTY__:
						stack.insert(0,p)


			NT_analised = stack[0]
			terminal_input_analised = input_source[0]

		print '%s %s %s' % (self.__SYMBOL_MARK.ljust(25),self.__SYMBOL_MARK.ljust(10),'ACCEPTED'.ljust(15))






		







if "__main__":
	gramatica	 = {'E':['TE"'],'E"':['+TE"','empty'],
						'T':['FT"'],'T"':['*FT"','empty'],
						'F':['(E)','id']}

	g1 = {'S':['iEtSS"','a'],'S"':['eS','empty'],'E':['b']}

	g2 = {'S':['ABCDE'],'A':['a','empty'],
	'B':['b','empty'],
	'C':['c'],
	'D':['d','empty'],'E':['e','empty']}

	g3 = {'S':['xTU','1X','X'],'T':['c','1'],'X':['xX','U'],'U':['iY','vI','I'],
			'Y':['x','v'],'I':['iI','empty']}

	g4 = {'E':['TE"'],
			'E"':['+E','empty'],
			'T':['FT"'],
			'T"':['T','empty'],
			'F':['PF"'],
			'F"':['*F"','empty'],
			'P':['(E)','a','b','ep']}

#	First(E)  = First(T) = First(F) = First(P) = (,a,b,ep
#	First(E") = +,empty
#	First(T") = (,a,b,ep,empty
#	First(F") = *,empty

#	Follow(E) = Follow(E") = ),$
#	Follow(T) = Follow(T") = +,),$
#	Follow(F) = Follow(F") = (,a,b,ep,+,),$
#	Follow(P) = (,a,b,ep,+,),*,$


	D = Descendente(g4,'E','empty')
	D.computFollow()
	D.printFirst()
	D.printFollow()
	D.buildTable()
	#D.printTable()
	D.recognize(['a','b','*'])


