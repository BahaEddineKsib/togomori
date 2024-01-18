


# DRYFFC : DON'T REPEAT YOURSELF FOR COMMANDS



def option(op,value,IN):
	if(op in IN.split()):
		if(value):
			if(IN.split().index(op)+1 <= len(IN.split())-1 and IN.split()[IN.split().index(op)+1][0] != '-'):
				return IN.split()[IN.split().index(op)+1]
			else:
				return "UserNeedsHelp"
		else:
			return True
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
			s = input("save it (y/n) ?")
			stay = False if s in ['y','n'] else True
		if(s=='n'):
			print("THIS OBJECT WON'T BE SAVED")
			return False
		else:
			return save_function()
	
