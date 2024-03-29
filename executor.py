from commands.CRUDs.workshop.setWorkshop     import SetWorkshop     as sw
from commands.CRUDs.workshop.unsetWorkshop   import UnsetWorkshop   as usw
from commands.CRUDs.workshop.addWorkshop     import AddWorkshop     as aw
from commands.CRUDs.workshop.displayWorkshop import DisplayWorkshop as dw
from commands.CRUDs.workshop.deleteWorkshop  import DeleteWorkshop  as delw
from commands.CRUDs.workshop.updateWorkshop  import UpdateWorkshop  as uw
from commands.CRUDs.domain.addDomain         import AddDomain       as ad
from commands.CRUDs.domain.displayDomain     import DisplayDomain   as dd
from commands.CRUDs.domain.deleteDomain      import DeleteDomain    as deld
from commands.CRUDs.domain.updateDomain      import UpdateDomain    as ud
from commands.CRUDs.domain.setDomain	     import SetDomain	    as sd
from commands.CRUDs.domain.unsetDomain	     import UnsetDomain     as usd
from commands.CRUDs.path.addPath	     import AddPath         as ap
from commands.CRUDs.path.displayPath         import DisplayPath     as dp
from commands.CRUDs.path.updatePath	     import UpdatePath	    as up
from commands.CRUDs.path.deletePath	     import DeletePath	    as delp
import os
def execute(IN):
	command = ''
	if IN != '':
		command = IN.split()[0]
		
	match command:

		# Workshop!
		case "setworkshop" | "setw" | "sw":		sw.execute(IN)
		case "unsetworkshop" | "unsetw" | "usw":	usw.execute(IN)
		case "addworkshop" | "addw" | "aw":		aw.execute(IN)
		case "displayworkshop" | "displayw" | "dw":	dw.execute(IN)
		case "updateworkshop" | "updatew" | "uw":	uw.execute(IN)
		case "deleteworkshop" | "deletew" | "delw":	delw.execute(IN)
		# Domain
		case "adddomain" | "addd" | "ad":		ad.execute(IN)
		case "displaydomain" | "displayd" | "dd":	dd.execute(IN)
		case "updatedomain" | "updated" | "ud":		ud.execute(IN)
		case "deletedomain" | "deleted" | "deld":	deld.execute(IN)
		case "setdomain" | "setd" | "sd":		sd.execute(IN)
		case "unsetdomain" | "unsetd"| "usd":		usd.execute(IN)
		# PATH
		case "addpath" | "addp" | "ap":			ap.execute(IN)
		case "displaypath" | "displayp" | "dp":		dp.execute(IN)
		case "updatepath" | "updatep" | "up":		up.execute(IN)
		case "deletepath" | "deletep" | "delp":		delp.execute(IN)
		# Parameter
		case "addvariable" | "addv" | "av":		print('EXECUTING add parameter..')
		case "displayvariable" | "displayv" | "dv":	print('EXECUTING display parameter..')
		case "updatevariable" | "updatev" | "uv":	print('EXECUTING update parameter..')
		case "deletevariable" | "deletev" | "delv":	print('EXECUTING delete parameter..')
		# Cookie
		case "addcookie" | "addc" | "ac":		print('EXECUTING add cookie..')
		case "displaycookie" | "displayc" | "dc":	print('EXECUTING display cookie..')
		case "updatecookie" | "updatec" | "uc":		print('EXECUTING update cookie..')
		case "deletecookie" | "deletec" | "delc":	print('EXECUTING delete cookie..')
		# Capture
		case "addcapture" | "addcap" | "acap":		print('EXECUTING add capture..')
		case "displaycapture" | "displaycap" | "dcap":	print('EXECUTING display capture..')
		case "updatecapture" | "updatecap" | "ucap":	print('EXECUTING update capture..')
		case "deletecapture" | "deletecap" | "dcap":	print('EXECUTING delete capture..')
		# Transaction
		case "addtransaction" | "addt" | "at":		print('EXECUTING add transaction..')
		case "displaytransaction" | "displayt" | "dt":	print('EXECUTING display transaction..')
		case "updatetransaction" | "updatet" | "ut":	print('EXECUTING update transaction..')
		case "deletetransaction" | "deletet" | "delt":	print('EXECUTING delete transaction..')
		#quitting
		case "quit" | "q":				return False
		#clear
		case "clear" | "c":				os.system('clear')
		#Invalid Command
		case _:
			print('Invalid Command')
	return True
			
			
