def splitProduction(production,noterminals):
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