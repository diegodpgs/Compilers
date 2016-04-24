from grammar import *

def test_encode():
	totalUNIT = 2

	print '='*20,'test_encode()','='*20
	g1 = Grammar({'A':['table','car','tree'],'MY':['name','stuffs','house']})
	g1.encode()

	if g1 == Grammar({'AAE': ['aaf', 'aag', 'aah'], 'AAA': ['aab', 'aac', 'aad']}):
		print 'test_encode -  test 01: OK'
		totalUNIT -= 1
	else:
		print 'Test 01 - Expected:\n    {AAE: [aaf, aag, aah], AAA: [aab, aac, aad]}'
		print 'Test 01 - Returned:\n    %s' % g1

	g2 = Grammar({'illnesses': ['government', 'contemplates', 'second', 'terrace', 'literal', 'plural', 'minute', 'beneath', 'batters', 'leaguer', 'speech', 'adventure', 'runners', 'particles', 'appealing', 'account', 'redskins', 'continue', 'imagined', 'passed'], 'declared': ['rather', 'fulfilling', 'americans', 'famous', 'runners', 'musicians', 'minaret', 'recreating', 'teacher', 'transformation', 'himself', 'neurochemical', 'husband', 'political', 'device', 'reported', 'fascinating', 'throughout', 'crossing', 'counts'], 'figure': ['photograph', 'minutes', 'parents', 'america', 'adventure', 'father', 'confectioner', 'spanish', 'dodgers', 'dramatic', 'entered', 'themselves', 'sixteen', 'handsomeness', 'opening', 'heroics', 'version', 'complex', 'magnificent', 'concert'], 'certain': ['support', 'officials', 'popular', 'version', 'orphaned', 'committee', 'konfidenz', 'before', 'ethnic', 'described', 'district', 'luxembourg', 'intoxicated', 'understanding', 'critical', 'extended', 'laughing', 'dismiss', 'theirs', 'performed'], 'agreed': ['sunlight', 'trembled', 'dedicated', 'demonstration', 'decrease', 'amateurism', 'version', 'according', 'questioning', 'voices', 'laughed', 'upheavals', 'admired', 'rematch', 'looked', 'suffered', 'series', 'strange', 'romania', 'berlin'], 'marked': ['central', 'excellent', 'sexual', 'pinned', 'renders', 'greeks', 'redskins', 'remark', 'fabric', 'completed', 'domesticated', 'carrolls', 'depends', 'children', 'championship', 'serious', 'suggested', 'lobster', 'created', 'disciples'], 'expectations': ['debates', 'resident', 'cheevers', 'clamor', 'leader', 'cornucopia', 'separate', 'decided', 'surged', 'sitting', 'pocket', 'measure', 'traced', 'obliqueness', 'unremarkable', 'cinder', 'remains', 'pumping', 'obliqueness', 'looking'], 'escaped': ['supporters', 'support', 'athletes', 'diffuses', 'promotional', 'service', 'length', 'admired', 'ibuprofen', 'redskins', 'picture', 'rerouted', 'encourages', 'inaugural', 'digging', 'credited', 'resurrect', 'christ', 'sulfur', 'soccer'], 'performed': ['reception', 'account', 'researcher', 'admired', 'economics', 'people', 'progress', 'previous', 'inject', 'international', 'besides', 'burstein', 'throughout', 'anxious', 'account', 'athens', 'caldeira', 'simulated', 'reflect', 'manuscript'], 'entering': ['because', 'students', 'reported', 'previous', 'fitzpatrick', 'boundaries', 'edition', 'adventure', 'literal', 'underground', 'thousand', 'graduated', 'completing', 'generate', 'francisco', 'evangelist', 'chicago', 'almost', 'criteria', 'enthusiastic'], 'george': ['remembers', 'dishonor', 'admired', 'romania', 'intended', 'heroics', 'unexpected', 'anxious', 'spartans', 'larger', 'admitted', 'process', 'surrealist', 'efforts', 'ibuprofen', 'frenzied', 'plural', 'survived', 'agreed', 'combination'], 'decade': ['alices', 'disrupt', 'nations', 'article', 'uttered', 'almost', 'pietri', 'troublemaker', 'people', 'passed', 'serious', 'thousands', 'member', 'understand', 'litanies', 'happens', 'perverse', 'related', 'although', 'happens'], 'shorter': ['fulfilling', 'outlet', 'created', 'cameron', 'expanding', 'pitchers', 'offering', 'justified', 'marathons', 'fitzpatrick', 'gospel', 'illustrations', 'leaves', 'careens', 'itself', 'poetic', 'incoming', 'offering', 'fiction', 'morphine'], 'poetic': ['throughout', 'remains', 'giants', 'besides', 'capital', 'credited', 'images', 'students', 'singles', 'managing', 'inaugural', 'brasher', 'musicians', 'although', 'industrialized', 'difficult', 'suffer', 'achieving', 'singles', 'hendricks'], 'sunlight': ['suspect', 'catholic', 'disappeared', 'esophagus', 'inject', 'evening', 'unusual', 'conditioning', 'students', 'mexico', 'sexual', 'cheered', 'expected', 'predicament', 'separate', 'lending', 'sitting', 'cheevers', 'dishonor', 'question'], 'starters': ['sought', 'amateurism', 'reminder', 'adventure', 'graduated', 'choosing', 'dominant', 'measuring', 'traces', 'another', 'rooters', 'supporters', 'recreating', 'indoors', 'encourages', 'difference', 'breathe', 'neurochemical', 'readers', 'depends'], 'participants': ['thrilling', 'cartooning', 'successive', 'describe', 'stoked', 'reception', 'donald', 'advertised', 'auditorium', 'justified', 'assumptions', 'understatement', 'central', 'spectacular', 'opening', 'expanding', 'suggested', 'things', 'poetic', 'handsomeness'], 'believing': ['through', 'critical', 'support', 'chaotic', 'pelota', 'ancient', 'blossomed', 'reminder', 'generate', 'running', 'another', 'stadium', 'narrator', 'flouted', 'garnered', 'trends', 'desperation', 'rerouted', 'models', 'individual'], 'advancing': ['readers', 'relegated', 'expectations', 'distinguished', 'missouri', 'dishonor', 'rebellion', 'predicament', 'called', 'america', 'sponsored', 'larger', 'surrealist', 'auditorium', 'interpret', 'raucous', 'became', 'facing', 'maiden', 'constructed'], 'narrator': ['nations', 'location', 'fortune', 'emerging', 'hitting', 'ephraim', 'million', 'depends', 'happen', 'reached', 'surrealist', 'trends', 'athlete', 'neighbors', 'afflictions', 'previous', 'edition', 'finished', 'stadium', 'illustration'], 'reacts': ['needed', 'ominous', 'satirist', 'breathe', 'principle', 'brandenburg', 'artists', 'impossible', 'orphanage', 'technological', 'chapter', 'applied', 'happened', 'vision', 'incubator', 'discovered', 'accused', 'rooters', 'backstreet', 'marked'], 'literal': ['italian', 'illnesses', 'results', 'inject', 'amphitheater', 'neighbors', 'finishers', 'konfidenz', 'gathering', 'cultural', 'during', 'manuscript', 'applied', 'little', 'program', 'expanded', 'resonance', 'double', 'destruction', 'propelled'], 'deliver': ['volume', 'countries', 'upheavals', 'admitted', 'holocaust', 'impossible', 'reported', 'enthusiastic', 'american', 'troublemaker', 'ironic', 'emotional', 'jumped', 'minded', 'minaret', 'reputable', 'curtis', 'finishes', 'gathering', 'sought'], 'chorale': ['neighbors', 'resonance', 'london', 'berlin', 'bodies', 'respond', 'individual', 'tenniels', 'understanding', 'described', 'cocktail', 'demonstrated', 'minute', 'circles', 'singles', 'scream', 'nothing', 'measure', 'exiled', 'perverse'], 'during': ['amateurism', 'remembers', 'satirist', 'reports', 'because', 'conclusion', 'sensitive', 'embark', 'relegated', 'service', 'artists', 'francis', 'research', 'narrates', 'better', 'firefighter', 'medallist', 'remark', 'message', 'allendes'], 'friends': ['romania', 'offers', 'failed', 'poetic', 'salvador', 'looking', 'nights', 'boroughs', 'promised', 'granderson', 'coaxed', 'stretch', 'demonstrated', 'permits', 'talent', 'exiled', 'scenic', 'schools', 'dependent', 'handsomeness'], 'matched': ['message', 'husband', 'fastballs', 'schools', 'narrates', 'gotham', 'reactions', 'sexual', 'greater', 'gardners', 'contest', 'jumped', 'africa', 'through', 'transformation', 'participants', 'sending', 'aspirin', 'program', 'people'], 'chapter': ['simple', 'quarterback', 'enhanced', 'gathering', 'fascinating', 'digging', 'recall', 'konfidenz', 'perplexing', 'brasher', 'rooftop', 'brings', 'unsettling', 'consume', 'illustration', 'transgression', 'qualities', 'colleagues', 'planting', 'global'], 'involve': ['pocket', 'litanies', 'circle', 'himself', 'people', 'belongs', 'though', 'xenophobic', 'gardners', 'sulfate', 'inhaled', 'elected', 'fascinating', 'circle', 'entering', 'stracher', 'stanford', 'serious', 'reactions', 'largest'], 'athlete': ['angeles', 'strange', 'predicament', 'distinct', 'steadman', 'siblings', 'ancient', 'inaugural', 'claims', 'banned', 'outlet', 'seemed', 'levels', 'basque', 'satirist', 'things', 'dependent', 'placebo', 'garnered', 'heroism'], 'british': ['reduce', 'information', 'american', 'brings', 'support', 'underground', 'response', 'designed', 'drought', 'domesticated', 'dopamine', 'mexican', 'photograph', 'thousand', 'remembers', 'manhattan', 'matched', 'ambivalence', 'amenable', 'leader'], 'placed': ['connection', 'adjustments', 'frenzied', 'started', 'musicians', 'either', 'ideals', 'shortcuts', 'injections', 'escaped', 'giants', 'flouted', 'individuals', 'complex', 'credited', 'medallist', 'dorando', 'certain', 'middle', 'reported'], 'competed': ['recreating', 'survives', 'location', 'evangelist', 'advancing', 'finishes', 'accused', 'difference', 'starts', 'admitted', 'bizarre', 'evangelist', 'perverse', 'intention', 'pointing', 'positions', 'marked', 'bicentennial', 'message', 'fantastic'], 'castle': ['mexican', 'digging', 'informed', 'another', 'recalls', 'thirties', 'carrolls', 'berlin', 'sensitive', 'impresario', 'volume', 'heaters', 'cheered', 'encourages', 'nuclear', 'encourages', 'streets', 'better', 'during', 'leaders'], 'rodgers': ['besides', 'tunnels', 'protagonists', 'francis', 'narrates', 'toronto', 'unmitigated', 'dangerous', 'chaotic', 'devitalize', 'numbers', 'admired', 'begins', 'promoted', 'constructed', 'caused', 'maclachlan', 'balance', 'mourning', 'benevolent']})
	g2.encode()
	Eg2 = Grammar({'AGN': ['ago', 'agp', 'agq', 'agr', 'ags', 'agt', 'agu', 'agv', 'agw', 'agx', 'agy', 'agz', 'aha', 'ahb', 'ahc', 'ahd', 'ahe', 'ahf', 'ahg', 'ahh'], 'AVW': ['avx', 'avy', 'avz', 'awa', 'awb', 'awc', 'awd', 'awe', 'awf', 'awg', 'awh', 'awi', 'awj', 'awk', 'awl', 'awm', 'awn', 'awo', 'awp', 'awq'], 'AAA': ['aab', 'aac', 'aad', 'aae', 'aaf', 'aag', 'aah', 'aai', 'aaj', 'aak', 'aal', 'aam', 'aan', 'aao', 'aap', 'aaq', 'aar', 'aas', 'aat', 'aau'], 'BAS': ['bat', 'bau', 'bav', 'baw', 'bax', 'bay', 'baz', 'bba', 'bbb', 'bbc', 'bbd', 'bbe', 'bbf', 'bbg', 'bbh', 'bbi', 'bbj', 'bbk', 'bbl', 'bbm'], 'AEX': ['aey', 'aez', 'afa', 'afb', 'afc', 'afd', 'afe', 'aff', 'afg', 'afh', 'afi', 'afj', 'afk', 'afl', 'afm', 'afn', 'afo', 'afp', 'afq', 'afr'], 'ATL': ['atm', 'atn', 'ato', 'atp', 'atq', 'atr', 'ats', 'att', 'atu', 'atv', 'atw', 'atx', 'aty', 'atz', 'aua', 'aub', 'auc', 'aud', 'aue', 'auf'], 'AZC': ['azd', 'aze', 'azf', 'azg', 'azh', 'azi', 'azj', 'azk', 'azl', 'azm', 'azn', 'azo', 'azp', 'azq', 'azr', 'azs', 'azt', 'azu', 'azv', 'azw'], 'ACM': ['acn', 'aco', 'acp', 'acq', 'acr', 'acs', 'act', 'acu', 'acv', 'acw', 'acx', 'acy', 'acz', 'ada', 'adb', 'adc', 'add', 'ade', 'adf', 'adg'], 'AZX': ['azy', 'azz', 'baa', 'bab', 'bac', 'bad', 'bae', 'baf', 'bag', 'bah', 'bai', 'baj', 'bak', 'bal', 'bam', 'ban', 'bao', 'bap', 'baq', 'bar'], 'AEC': ['aed', 'aee', 'aef', 'aeg', 'aeh', 'aei', 'aej', 'aek', 'ael', 'aem', 'aen', 'aeo', 'aep', 'aeq', 'aer', 'aes', 'aet', 'aeu', 'aev', 'aew'], 'AAV': ['aaw', 'aax', 'aaz', 'aba', 'abb', 'abc', 'abd', 'abe', 'abf', 'abg', 'abh', 'abi', 'abj', 'abk', 'abl', 'abm', 'abn', 'abo', 'abp', 'abq'], 'AKO': ['akp', 'akq', 'akr', 'aks', 'akt', 'aku', 'akv', 'akw', 'akx', 'aky', 'akz', 'ala', 'alb', 'alc', 'ald', 'ale', 'alf', 'alg', 'alh', 'ali'], 'AID': ['aie', 'aif', 'aig', 'aih', 'aii', 'aij', 'aik', 'ail', 'aim', 'ain', 'aio', 'aip', 'aiq', 'air', 'ais', 'ait', 'aiu', 'aiv', 'aiw', 'aix'], 'AIY': ['aiz', 'aja', 'ajb', 'ajc', 'ajd', 'aje', 'ajf', 'ajg', 'ajh', 'aji', 'ajj', 'ajk', 'ajl', 'ajm', 'ajn', 'ajo', 'ajp', 'ajq', 'ajr', 'ajs'], 'AXM': ['axn', 'axo', 'axp', 'axq', 'axr', 'axs', 'axt', 'axu', 'axv', 'axw', 'axx', 'axy', 'axz', 'aya', 'ayb', 'ayc', 'ayd', 'aye', 'ayf', 'ayg'], 'ASQ': ['asr', 'ass', 'ast', 'asu', 'asv', 'asw', 'asx', 'asy', 'asz', 'ata', 'atb', 'atc', 'atd', 'ate', 'atf', 'atg', 'ath', 'ati', 'atj', 'atk'], 'ANU': ['anv', 'anw', 'anx', 'any', 'anz', 'aoa', 'aob', 'aoc', 'aod', 'aoe', 'aof', 'aog', 'aoh', 'aoi', 'aoj', 'aok', 'aol', 'aom', 'aon', 'aoo'], 'AME': ['amf', 'amg', 'amh', 'ami', 'amj', 'amk', 'aml', 'amm', 'amn', 'amo', 'amp', 'amq', 'amr', 'ams', 'amt', 'amu', 'amv', 'amw', 'amx', 'amy'], 'AWR': ['aws', 'awt', 'awu', 'awv', 'aww', 'awx', 'awy', 'awz', 'axa', 'axb', 'axc', 'axd', 'axe', 'axf', 'axg', 'axh', 'axi', 'axj', 'axk', 'axl'], 'AMZ': ['ana', 'anb', 'anc', 'and', 'ane', 'anf', 'ang', 'anh', 'ani', 'anj', 'ank', 'anl', 'anm', 'ann', 'ano', 'anp', 'anq', 'anr', 'ans', 'ant'], 'AOP': ['aoq', 'aor', 'aos', 'aot', 'aou', 'aov', 'aow', 'aox', 'aoy', 'aoz', 'apa', 'apb', 'apc', 'apd', 'ape', 'apf', 'apg', 'aph', 'api', 'apj'], 'BBN': ['bbo', 'bbp', 'bbq', 'bbr', 'bbs', 'bbt', 'bbu', 'bbv', 'bbw', 'bbx', 'bby', 'bbz', 'bca', 'bcb', 'bcc', 'bcd', 'bce', 'bcf', 'bcg', 'bch'], 'AYH': ['ayi', 'ayj', 'ayk', 'ayl', 'aym', 'ayn', 'ayo', 'ayp', 'ayq', 'ayr', 'ays', 'ayt', 'ayu', 'ayv', 'ayw', 'ayx', 'ayy', 'ayz', 'aza', 'azb'], 'AUG': ['auh', 'aui', 'auj', 'auk', 'aul', 'aum', 'aun', 'auo', 'aup', 'auq', 'aur', 'aus', 'aut', 'auu', 'auv', 'auw', 'aux', 'auy', 'auz', 'ava'], 'AJT': ['aju', 'ajv', 'ajw', 'ajx', 'ajy', 'ajz', 'aka', 'akb', 'akc', 'akd', 'ake', 'akf', 'akg', 'akh', 'aki', 'akj', 'akk', 'akl', 'akm', 'akn'], 'ABR': ['abs', 'abt', 'abu', 'abv', 'abw', 'abx', 'aby', 'abz', 'aca', 'acb', 'acc', 'acd', 'ace', 'acf', 'acg', 'ach', 'aci', 'acj', 'ack', 'acl'], 'ADH': ['adi', 'adj', 'adk', 'adl', 'adm', 'adn', 'ado', 'adp', 'adq', 'adr', 'ads', 'adt', 'adu', 'adv', 'adw', 'adx', 'ady', 'adz', 'aea', 'aeb'], 'AFS': ['aft', 'afu', 'afv', 'afw', 'afx', 'afy', 'afz', 'aga', 'agb', 'agc', 'agd', 'age', 'agf', 'agg', 'agh', 'agi', 'agj', 'agk', 'agl', 'agm'], 'ALJ': ['alk', 'all', 'alm', 'aln', 'alo', 'alp', 'alq', 'alr', 'als', 'alt', 'alu', 'alv', 'alw', 'alx', 'aly', 'alz', 'ama', 'amb', 'amc', 'amd'], 'ARV': ['arw', 'arx', 'ary', 'arz', 'asa', 'asb', 'asc', 'asd', 'ase', 'asf', 'asg', 'ash', 'asi', 'asj', 'ask', 'asl', 'asm', 'asn', 'aso', 'asp'], 'AHI': ['ahj', 'ahk', 'ahl', 'ahm', 'ahn', 'aho', 'ahp', 'ahq', 'ahr', 'ahs', 'aht', 'ahu', 'ahv', 'ahw', 'ahx', 'ahy', 'ahz', 'aia', 'aib', 'aic'], 'APK': ['apl', 'apm', 'apn', 'apo', 'app', 'apq', 'apr', 'aps', 'apt', 'apu', 'apv', 'apw', 'apx', 'apy', 'apz', 'aqa', 'aqb', 'aqc', 'aqd', 'aqe'], 'AQF': ['aqg', 'aqh', 'aqi', 'aqj', 'aqk', 'aql', 'aqm', 'aqn', 'aqo', 'aqp', 'aqq', 'aqr', 'aqs', 'aqt', 'aqu', 'aqv', 'aqw', 'aqx', 'aqy', 'aqz'], 'AVB': ['avc', 'avd', 'ave', 'avf', 'avg', 'avh', 'avi', 'avj', 'avk', 'avl', 'avm', 'avn', 'avo', 'avp', 'avq', 'avr', 'avs', 'avt', 'avu', 'avv'], 'ARA': ['arb', 'arc', 'ard', 'are', 'arf', 'arg', 'arh', 'ari', 'arj', 'ark', 'arl', 'arm', 'arn', 'aro', 'arp', 'arq', 'arr', 'ars', 'art', 'aru']})
	
	if g2 == Eg2:
		print 'test_encode -  test 02: OK'
		totalUNIT -= 1
	else:
		print 'Test 02 - Expected:\n    %s' % Eg2
		print 'Test 02 - Returned:\n    %s' % g2
	
	print '%d incorrect tests' % totalUNIT
	
def test_solve_recursion():
	totalUNIT = 6

	print '='*20,'test_solve_recursion()','='*20

	#------------------------- Test 01 ------------------------
	g1 = Grammar({'A':['B'],'B':['C'],'C':['D'],'D':['E'],'E':['Ea']})
	Eg1 = Grammar({'A': ['B'], 'C': ['D'], 'B': ['C'], 'E': [], 'D': ['E'], 'E"': ['aE"','EMPTY']})
	g1.solve()

	if(g1 == Eg1):
		print 'test_solve_recursion - Test 01: OK'
		totalUNIT -= 1
	else:
		print 'Test 01 - Excected:\n   {A: [B], C: [D], B: [C], E: [], D: [E], E": [aE",EMPTY]}'
		print 'Test 01 - Returned:\n   %s' % Eg1
	

	#------------------------- Test 02 ------------------------
	g2 = Grammar({'A':['Ac','Sd','F'],'S':['Aa','b'],'F':['EMPTY']})
	Eg2 = Grammar({'A': ['SdA"', 'FA"'], 'S"': ['dA"aS"', 'EMPTY'], 'S': ['FA"aS"', 'bS"'], 'A"': ['cA"', 'EMPTY'], 'F': ['EMPTY']})
	g2.solve()
	if(g2 == Eg2):
		print 'test_solve_recursion - Test 02: OK'
		totalUNIT -= 1
	else:
		print 'Test 02 - Excected:\n   {A: [SdA", FA"], S": [dA"aS", EMPTY], S: [FA"aS", bS"], A": [cA", EMPTY], F: [EMPTY]}'
		print 'Test 02 - Returned:\n   %s' % Eg2

	
	#------------------------- Test 03 ------------------------
	g3 = Grammar({'A':['Ac','Sd','EMPTY'],'S':['Aa','b']})
	Eg3 = Grammar({'A': ['SdA"', 'EMPTYA"'], 'S"': ['dA"aS"', 'EMPTY'], 'S': ['EMPTYA"aS"', 'bS"'], 'A"': ['cA"', 'EMPTY']})
	g3.solve()

	if(g3 == Eg3):
		print 'test_solve_recursion - Test 03: OK'
		totalUNIT -= 1
	else:
		print g3
		print Eg3
		#print 'Test 03 - Excected:\n   {A: [SdA", T"], S": [dA"aS", T], S: [T"aS", bS"], A": [cA", T],T:[EMPTY]}'
		#print 'Test 03 - Returned:\n   %s' % Eg3
 

	#------------------------- Test 04 ------------------------
	g4 = Grammar({'A':['Bb'],'B':['a'],'C':['Ac']})
	Eg4 = Grammar({'A':['Bb'],'B':['a'],'C':['abc']})
	g4.solve()
	if(g4 == Eg4):
		print 'test_solve_recursion - Test 04: OK'
		totalUNIT -= 1
	else:
		print 'Test 04 - Excected:\n   {A:[Bb],B:[a],C:[abc]}'
		print 'Test 04 - Returned:\n   %s' % Eg4
	
	#------------------------- Test 05 ------------------------
	g5 = Grammar({'A':['Ba','cb','a','EMPTY'],'B':['a','Ga'],'C':['Ac'],'F':['Fb','g'],'G':['AaF','EMPTY']})
	Eg5 = Grammar({'A': ['Ba', 'cb', 'a', 'H'], 'C': ['aac', 'Gaac', 'cbc', 'ac', 'Hc'], 'B': ['a', 'Ga'], 'G': ['aaagF"G"', 'cbagF"G"', 'aagF"G"', 'HagF"G"', 'HG"'], 'F': ['gF"'], 'H': ['EMPTY'], 'F"': ['bF"', 'EMPTY'], 'G"': ['aaagF"G"', 'EMPTY']})
	g5.refactor_empty()
	g5.solve()
	if(g5 == Eg5):
		print 'test_solve_recursion - Test 05: OK'
		totalUNIT -= 1
	else:
		print 'Test 05 - Excected:\n   {A: [Ba, cb, a, H], C: [aac, Gaac, cbc, ac, Hc], B: [a, Ga], G: [aaagF"G", cbagF"G", aagF"G", HagF"G", HG"], F: [gF"], H: EMPTY, F": [bF", EMPTY], G": [aaagF"G", EMPTY]}'
		print 'Test 05 - Returned:\n   %s' % Eg5
	
	#------------------------- Test 06 ------------------------
	g6 = Grammar({'A':['Ba','Db','a','EMPTY'],'B':['D','Ga'],'C':['Ac'],'D':['A','B'],'F':['FD','g'],'G':['AaF','EMPTY']})
	Eg6 = Grammar({'A': ['Ba', 'Db', 'a', 'EMPTY'], 'C': ['Dac', 'Gaac', 'Dbc', 'ac', 'Ac'], 'B': ['D', 'Ga'], 'D': ['GaaD"', 'aD"', 'AD"', 'GaD"'], 'G': ['aDaagF"G"', 'ADaagF"G"', 'aDbagF"G"', 'ADbagF"G"', 'aagF"G"', 'AagF"G"', 'EG"', 'MG"', 'PG"', 'TG"', 'YG"'], 'F': ['gF"'], 'D"': ['aD"', 'bD"', 'D"', 'EMPTY'], 'F"': ['DF"', 'EMPTY'], 'G"': ['aaDaagF"G"', 'aDaagF"G"', 'aaagF"G"', 'aaDbagF"G"', 'aDbagF"G"', 'EMPTY']})
	g6.solve()
	if(g6 == Eg6):
		print 'test_solve_recursion - Test 06: OK'
		totalUNIT -= 1
	else:
		print 'Test 06 - Excected:\n   {A: [Ba, Db, a, EMPTY], C: [Dac, Gaac, Dbc, ac, Ac], B: [D, Ga], D: [GaaD", aD", AD", GaD"], G: [aDaagF"G", ADaagF"G", aDbagF"G", ADbagF"G", aagF"G", AagF"G", EG", MG", PG", TG", YG"], F: [gF"], D": [aD", bD", D", EMPTY], F": [DF", EMPTY], G": [aaDaagF"G", aDaagF"G", aaagF"G", aaDbagF"G", aDbagF"G", EMPTY]}'
		print 'Test 06 - Returned:\n   %s' % Eg6

	print '%d incorrect tests' % totalUNIT

if "__main__":
	test_encode()
	test_solve_recursion()