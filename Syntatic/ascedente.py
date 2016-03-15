#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils import *
import time
"""
	This algorithm does not accept the following grammar 
	A -> aB
	B -> ab

	It has to be converted to the grammar 
	A -> aB 
	B -> aC
	C -> b

	In other words, the algorithm does not work correclty in the case when
	there is terminal subset of other terminals as the example above 'a' is a subset of 'ab'.
	
"""
class Ascedente:

	def __init__(self,gramatica,initial,empty):
		self.gramatica = gramatica
		self.__EMPTY__ = empty
		self.__INITIAL__ = initial
		self.__SYMBOL_MARK = '$'
		#self.follows = {}
		#self.firsts = {}
		self.NTs = gramatica.keys()
		self.terms = self.getTerms()
		self.terminals = set(self.terms) - set(self.NTs)
		self.extendGrammar()
		#self.table = dict([(keyNT,dict([(key,'') for key in list(self.terminals)])) for keyNT in self.NTs])
		#self.trackfollow = []

	def extendGrammar(self):
		self.__INITIAL__ = self.__INITIAL__+'"'
		self.gramatica[self.__INITIAL__] = [self.__INITIAL__[0:-1]]

	def setGramatica(self,gramatica,initial):
		self.gramatica = gramatica
		self.terms = self.getTerms()
		#self.cache_follows = {}
		#self.cache_firsts = {}
		self.__INITIAL__ = initial
		self.terminals = set(self.terms) - set(self.NTs)
		self.extendGrammar()
		#self.table = dict([(keyNT,dict([(key,'') for key in list(self.terminals)])) for keyNT in self.NTs])

	def getTerms(self):
		productions = []
		terms = []
		[productions.extend(v) for v in self.gramatica.values()]

		[terms.extend(splitProduction(v,self.NTs)) for v in productions]
		terms.extend(self.NTs)
		return list(set(terms)-set([self.__EMPTY__]))

	def getItens(self,production):
		production = splitProduction(production,self.NTs)
		items = []

		for index in xrange(len(production)):
			left = "".join(production[0:index])
			right = "".join(production[index:])
			items.append(left+'.'+right)

		items.append("".join(production)+'.')
		return items

	def closure(self,I):
		items = I[:]
		index_items = 0
		item_added = True

		
		while item_added:
			item_added = False

			while index_items < len(items):
				
				item = items[index_items]

				item = splitProduction(item,self.NTs)
				B = item[item.index('.')+1]
				
				
				if B in self.NTs:
					print 'log CLOSURE(%s) analysing the item: %s' % (str(I),str(item))
					for production in self.gramatica[B]:
						new_item = '.'+production

						if new_item not in items:
							print 'log CLOSURE(%s) item added: %s' % (str(I),new_item)
							items.append(new_item)
							item_added = True

				index_items += 1
			print 'log CLOSURE(%s)=%s' % (str(I),str(items))
			return items

	




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

	g5 = {'E':['E+T','T'],'T':['T*F','F'],'F':['(E)','id']}


	D = Ascedente(g5,'E','empty')
	D.closure(['.E'])
	