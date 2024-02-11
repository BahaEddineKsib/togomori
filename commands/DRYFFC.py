


# DRYFFC : DON'T REPEAT YOURSELF FUNCTIONS FOR COMMANDS



def option(op,value,IN):
	if(op in IN.split()):
		if(value):
			if(IN.split().index(op)+1 <= len(IN.split())-1 and IN.split()[IN.split().index(op)+1][0] != '-'):
				return IN.split()[IN.split().index(op)+1]
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


