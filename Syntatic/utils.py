def splitProduction(production,noterminals):
	"""
		this algorithm recognize terminals only as lowercase.
		If a term is uppercase and it is not a no terminal, them it will be considered as terminal.
		However, if has more than two uppercase noterminal, the algo will use only as one

		Example

		NT = ['A','B','CD']
		INPUT : splitProduction('AabCDdeFGh')
		OUTPUT: ['A','ab','CD','deF','G','h']

	"""
	p = ['']
	index = 0

	while index < len(production):
		index2 = len(production)
		
		while index2 >= 0 and production[index:index2+1] not in noterminals:
			index2 -= 1

		if index2 >= 0:
			p.append(production[index:index2+1])
			
		elif production[index] not in p[-1]:
			if p[-1].islower():
				p[-1]+= production[index]
			else:
				p.append(production[index])

		index += 1


	return p[1:]

def _str_Production(NT,production):
	return '%s -> %s' % (NT,str(production))

def termInProductions(productions,term):
	term_production = []

	for production in productions:
		if term in production:
			term_production.append(production)

	return term_production

