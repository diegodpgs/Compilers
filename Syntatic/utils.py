def splitProduction(production,noterminals):
	"""
		All noterminais have to be UPPERCASE 
		all terminals   have to be lowercase

		Example

		NT = ['A','B','CD']
		INPUT : splitProduction('AabCDdeFGh')
		OUTPUT: ['A','ab','CD','deF','G','h']

	"""
	index = 0
	production_splited = []

	while index < len(production):
		
		buffer_production = ''

		while index < len(production) and production[index].isupper():
			buffer_production += production[index]
			index += 1

		if len(buffer_production) > 0:
			production_splited.append(buffer_production)
			buffer_production = ''

		while index < len(production) and production[index].islower():
			buffer_production += production[index]
			index += 1

		if len(buffer_production) > 0:
			production_splited.append(buffer_production)

		if buffer_production == '':
			index += 1

	return production_splited


def _str_Production(NT,production):
	return '%s -> %s' % (NT,str(production))

def termInProductions(productions,term):
	term_production = []

	for production in productions:
		if term in production:
			term_production.append(production)

	return term_production


#print splitProduction('EMPTY',['A', 'B', 'C', 'F', 'G', 'F"'])


