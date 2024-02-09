from commands.addWorkshop     import AddWorkshop     as aw
from commands.displayWorkshop import DisplayWorkshop as dw
from commands.setWorkshop     import SetWorkshop     as sw
from commands.unsetWorkshop   import UnsetWorkshop   as usw
def execute(IN):
	command = ''
	if IN != '':
		command = IN.split()[0]
		
	match command:

		# Workshop
		case "setworkshop" | "setw" | "sw":
			
			sw.execute(IN)
			
		case "unsetworkshop" | "unsetw" | "usw":

			usw.execute(IN)

		case "addworkshop" | "addw" | "aw":

			aw.execute(IN)
    

		case "displayworkshop" | "displayw" | "dw":
			
			dw.execute(IN)
    
		case "updateworkshop" | "updatew" | "uw":
			print('EXECUTING update workshop..')
    
		case "deleteworkshop" | "deletew" | "delw":
			print('EXECUTING delete workshop..')

		# Domain
		case "adddomain" | "addd" | "ad":
			print('EXECUTING add domain..')
    
		case "displaydomain" | "displayd" | "dd":
			print('EXECUTING display domain..')
    
		case "updatedomain" | "updated" | "ud":
			print('EXECUTING update domain..')
    
		case "deletedomain" | "deleted" | "deld":
			print('EXECUTING delete domain..')

		# URL
		case "addurl" | "addu" | "au":
			print('EXECUTING add URL..')
    
		case "displayurl" | "displayu" | "du":
			print('EXECUTING display URL..')
    
		case "updateurl" | "updateu" | "uu":
			print('EXECUTING update URL..')
    
		case "deleteurl" | "deleteu" | "delu":
			print('EXECUTING delete URL..')

		# Parameter
		case "addparameter" | "addp" | "ap":
			print('EXECUTING add parameter..')
    
		case "displayparameter" | "displayp" | "dp":
			print('EXECUTING display parameter..')
    
		case "updateparameter" | "updatep" | "up":
			print('EXECUTING update parameter..')
    
		case "deleteparameter" | "deletep" | "delp":
			print('EXECUTING delete parameter..')

		# Cookie
		case "addcookie" | "addc" | "ac":
			print('EXECUTING add cookie..')
    
		case "displaycookie" | "displayc" | "dc":
			print('EXECUTING display cookie..')
    
		case "updatecookie" | "updatec" | "uc":
			print('EXECUTING update cookie..')
    
		case "deletecookie" | "deletec" | "delc":
			print('EXECUTING delete cookie..')

		# Capture
		case "addcapture" | "addcap" | "acap":
			print('EXECUTING add capture..')
    
		case "displaycapture" | "displaycap" | "dcap":
			print('EXECUTING display capture..')
    
		case "updatecapture" | "updatecap" | "ucap":
			print('EXECUTING update capture..')
    
		case "deletecapture" | "deletecap" | "dcap":
			print('EXECUTING delete capture..')

		# Transaction
		case "addtransaction" | "addt" | "at":
			print('EXECUTING add transaction..')
    
		case "displaytransaction" | "displayt" | "dt":
			print('EXECUTING display transaction..')
    
		case "updatetransaction" | "updatet" | "ut":
			print('EXECUTING update transaction..')

		case "deletetransaction" | "deletet" | "delt":
			print('EXECUTING delete transaction..')
		#quitting
		case "quit" | "q":
			return False
		#Invalid Command
		case _:
			print('Invalid Command')
	return True
			
			
