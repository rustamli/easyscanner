import sys
import string
from random import choice

def Dict(**args):
    """
        Return a dictionary with argument names as the keys,
        and argument values as the key values
    """
    return args

# The grammar
# A line like:
#    NP = [['Det', 'N'], ['N'], ['N', 'PP']],
# means
#    NP -> Det N
#    NP -> N
#    NP -> N PP
def cnf_grammar(option):
	global grammar
	if option == '1':
		grammar = Dict(
				S = [['P','N'],['NP','N'], ['PP','N'],['P','NP'],['NP','NP'],['NP','S'],['PP','S'],['S','S']],
				NP = [['N', 'P'],['N','N']],
				PP = [['P', 'NP']],
				P = ['from', 'to', 'in'],
				N = ['abidjan','abu','dhabi','accra','addis','ababa','adelaide','ahmadabad','alexandria','algiers','almaty','amman'
,'amsterdam','ankara','antwerp','arhus','asuncion','athens','atlanta','auckland','baghdad','baku','baltimore','bandar','seri','begawan','bandung'
,'bangalore','bangkok','barcelona','basel','batam','beijing','beirut','belfast','belgrade','belo','horizonte','bergen','berlin','bern','bilbao'
,'birmingham','bogoto','bologna','bonn','bordeaux','boston','bratislava','brasilia','brazzaville','brisbane','bristol','brussels','bucharest'
,'budapest','buenos','aires','buffalo','bulawayo','cairo','calcutta','calgary','canberra','cape','town','caracas','cardiff','casablanca','charlotte'
,'chennai','chicago','christchurch','cincinnati','cleveland','cologne','colombo','columbus','conakry','copenhagen','cuidad','juarez','curitaba'
,'dakar','dalian','dallas','damascus','dar','es','salaam','denver','detroit','dhaka','djibouti','doha','dortmund','doula','dresden','dubai','dublin'
,'durban','dusseldorf','edinburgh','edmonton','essen','frankfurt','freetown','gaborone','geneva','genoa','georgetown','glasgow','gothenburg','grenoble'
,'guadalajara','guangzhou','guatemala','guayaquil','hamburg','hamilton','hannover','harare','hartford','havana','helsinki','ho','chi','minh','hobart',
'hong','kong','honolulu','houston','hyderabad','indianapolis','islamabad','istanbul','jaipur','jakarta','jeddah','jerusalem','johannesburg'
,'kabul','kampala','kansas','city','karachi','kawasaki','khartoum','kiev','kingston','kinshasa','kobe','krakow','kuala','lumpur','kuwait','kyoto'
,'la','paz','labuan','lagos','lahore','las','vegas','lausanne','leeds','leipzig','liege','lille','lima','limassol','linz','lisbon','liverpool'
,'ljubljana','lome','london','los','angeles','luanda','lucknow','lusaka','luxembourg','lyon','macau','madrid','mainz','malacca','malmo','managua'
,'manama','manaus','manchester','manila','mannheim','maputu','marseille','medan','medellin','melbourne','mexico','miami','milan','minneapolis'
,'minsk','mombasa','monrovia','monterrey','montevideo','montreal','moscow','mumbai','munich','nagoya','nairobi','nanjing','naples','nassau','new','delhi'
,'new','orleans','new','york','newcastle','nicosia','norwich','nottingham','nuremberg','omaha','osaka','oslo','ottawa','palermo','palo','alto','panama','paris'
,'penang','perth','philadelphia','phoenix','pittsburgh','plymouth','port','louis','port','moresby','port','of','spain','port-au-prince','portland'
,'porto','alegre','prague','pretoria','pusan','pyongyang','quebec','quito','rabat','rawalpindi','refice','reykjavik','richmond','riga','rio','de','janeiro'
,'riyadh','rochester','rome','rotterdam','ruwi','racramento','salvador','san','diego','san','francisco','san','jose','(ca)','san','jose','(cr)','san','salvador'
,'sanaa','santiago','santo','domingo','sao','paulo','sarajevo','seattle','seoul','seville','shanghai','sheffield','shenzhen','singapore','sofia','southampton'
,'st','louis','st','petersburg','stockholm','strasbourg','stuttgart','suva','sydney','taipei','tallinn','tampa','tashkent','tbilisi','tegucigalpa','tehran'
,'tel','aviv','the','hague','tianjin','tijuana','tirana','tokyo','toronto','trieste','tripoli','tunis','turin','ulan','bator','utrecht','valencia','vancouver'
,'venice','vienna','vilnius','warsaw','washington','wellington','wilmington','windhoek','winnipeg','xiamen','yangon','yaonde','yerevan','yokohama'
,'zagreb','zurich','january','february','march','april','may','june','july','august','september','october','november','december']				
			)
	else:
		grammar = Dict(
				S = [['P','N'],['NP','N'], ['PP','N'],['P','NP'],['NP','NP'],['NP','S'],['S','S']],
				NP = [['N', 'P'],['N','N']],
				PP = [['P', 'NP']],
				P = ['From', 'To', 'In'],
				N = ['London', 'Edinburgh', 'Hong', 'Kong', 'New', 'York', 'City']			
			)
	return grammar
		

def generate(phrase):
	"""
		Generate a random sentence or phrase
	"""
	global grammar
	if isinstance(phrase, list):
		return mappend(generate, phrase)
	elif phrase in grammar:
		return generate(choice(grammar[phrase]))
	else:
		return [phrase]


def generate_tree(phrase):
	""" 
		Generate a random sentence or phrase,
		with a complete parse tree.
	"""
	global grammar
	if isinstance(phrase, list):
		return map(generate_tree, phrase)
	elif phrase in grammar:
		return [phrase] + generate_tree(choice['P', 'N'](grammar[phrase]))
	else:
		return [phrase]


def mappend(fn, list):
	"""
		Append the results of calling fn on each element of list.
	"""
	return reduce(lambda x,y: x+y, map(fn, list))

def producers(constituent):
	"""
		Argument is a list containing the rhs of some rule; return all possible lhs's
	"""
	global grammar
	results = []
	for (lhs,rhss) in grammar.items():
		for rhs in rhss:
			if rhs == constituent:
				results.append(lhs)
	return results


def printtable(table, wordlist):
    """
        Print the dynamic programming table.  The leftmost column is always empty.
    """
    print "    ", wordlist
    for row in table:
        print row

def printlanguage ():
    """
        Randomly generate many sentences, saving and printing the unique ones
    """
    language = {}
    size = 0
    for i in range(100):
        sentencestr = ' '.join(generate('S'))
        language[sentencestr] = 1
        if len(language) > size:
            size = len(language)
            print '+',
        else:
            print '.',
            sys.stdout.flush()
        print
    for s in language.keys():
        print s
    print size


def printsentence ():
    print ' '.join(generate('S'))

'''
	Reads a file and returns its content
'''
def readFile(filename):
	f = open(filename, 'r')
	try:
	    content = f.read()
	finally:
	    f.close()
	return content
