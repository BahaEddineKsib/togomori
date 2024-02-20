from commands.setWorkshop                    import SetWorkshop     as sw
from commands.unsetWorkshop                  import UnsetWorkshop   as usw
from commands.CRUDs.workshop.addWorkshop     import AddWorkshop     as aw
from commands.CRUDs.workshop.displayWorkshop import DisplayWorkshop as dw
from commands.CRUDs.workshop.deleteWorkshop  import DeleteWorkshop  as delw
from commands.CRUDs.workshop.updateWorkshop  import UpdateWorkshop  as uw
from commands.CRUDs.domain.addDomain         import AddDomain       as ad
from commands.CRUDs.domain.displayDomain     import DisplayDomain   as dd
from commands.CRUDs.domain.deleteDomain      import DeleteDomain    as deld
import os
def execute(IN):
	command = ''
	if IN != '':
		command = IN.split()[0]
		
	match command:

		# Workshop!
		case "setworkshop" | "setw" | "sw":
			
			sw.execute(IN)
			
		case "unsetworkshop" | "unsetw" | "usw":

			usw.execute(IN)

		case "addworkshop" | "addw" | "aw":

			aw.execute(IN)
    

		case "displayworkshop" | "displayw" | "dw":
			
			dw.execute(IN)
    
		case "updateworkshop" | "updatew" | "uw":
			
			uw.execute(IN)
    
		case "deleteworkshop" | "deletew" | "delw":
			
			delw.execute(IN)

		# Domain
		case "adddomain" | "addd" | "ad":
			
			ad.execute(IN)
    
		case "displaydomain" | "displayd" | "dd":
			dd.execute(IN)
    
		case "updatedomain" | "updated" | "ud":
			print('EXECUTING update domain..')
    
		case "deletedomain" | "deleted" | "deld":
			deld.execute(IN)

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
		#clear
		case "clear" | "c":
			os.system('clear')
		#Invalid Command
		case _:
			print('Invalid Command')
	return True
			
			
