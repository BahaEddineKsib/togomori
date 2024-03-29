import re
from urllib.parse import urlparse

# DRYFFC : DON'T REPEAT YOURSELF FUNCTIONS FOR COMMANDS



def option(op,value,MultiValues,IN):
	if(op in IN.split()):
		if(value):
			if(IN.split().index(op)+1 <= len(IN.split())-1 and IN.split()[IN.split().index(op)+1][0] != '-'):
				if(not MultiValues):
					return IN.split()[IN.split().index(op)+1]
				else:
					val="  "
					valList=[]
					count=1
					while(IN.split().index(op)+count < len(IN.split()) and IN.split()[IN.split().index(op)+count][0]!= '-'):
						val=IN.split()[IN.split().index(op)+count]
						valList.append(val)
						count += 1
					return valList

			else:
				return "UserNeedsHelp"
		else:
			if(IN.split().index(op)+1 == len(IN.split()) or IN.split()[IN.split().index(op)+1][0] == '-'):
				return True
			else:
				return "UserNeedsHelp"
	else:
		return False
	
def short_command(IN,cmnd):
	INs = IN.split()
	INs[0] = cmnd
	return ' '.join(INs)
def saveIt(save, save_function):
	if(save):
		return save_function()
	else:
		stay = True
		while stay :
			s = input("\nsave it (y/n) ?")
			stay = False if s in ['y','n'] else True
		if(s=='n'):
			print("❌: THIS OBJECT WON'T BE SAVED")
			return False
		else:
			return save_function()

def questionToExecute(for_sure, func, arguments, question):
	if(for_sure):
		return func(**arguments)
	else:
		ask=True
		while ask:
			y_n = input(question)
			ask = False if y_n in ['yes','no','y','n'] else True
		if(y_n == 'y'):
			return func(**arguments)
def canBeMap(LP,updating=False):
	
	testingList = LP.copy()
	if updating:
		if testingList[0] == '+' or testingList[0] == '_':
			testingList .pop(0)

	for l in testingList:
		if not re.match(r'^\w+:\d+$', l):
			return False
	return True


def listToMap(LP, updating=False):

	if(updating):
		if(LP[0] == '+' or LP[0] == '_'):
			LP[0] += ':0'

	Map={}
	for l in LP:
		Map[l.split(':')[0]] = int(l.split(':')[1])
	return Map

def segmentUrl(url):
	if url:
		result = {}
		if( len(url.split("://")) == 1 ):
			url = "https://"+url
		url_no_scheme = url.split("://")[1]
		if( len(url_no_scheme.split('/')) == 1):
			if(len(url_no_scheme.split('.')) == 1):
				return {"domain":"NoDomain","path":"InvalidPath"}
			else:
				url = urlparse(url)
				return {"domain":url.netloc,"path":"NoPath"}
			
		else:
			if(url_no_scheme[0] == '/'):
				url = urlparse(url)
				return {"domain":"NoDomain","path":url.path}
			else:
				domain = url_no_scheme.split("/")[0]
				if(len(domain.split('.')) == 1):
					return {"domain":"NoDomain","path":"InvalidPath"}
				else:
					url = urlparse(url)
					return {"domain":url.netloc,"path":url.path}
	else:
		return {"domain":"NoDomain","path":"Nopath"}
		
