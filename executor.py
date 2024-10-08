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
from commands.CRAFTs.getTechs		     import GetTechs
from commands.CRAFTs.getWhois		     import GetWhois
from commands.CRAFTs.getIp		     import GetIp
from commands.CRAFTs.getOpenPorts	     import GetOpenPorts
from commands.CRAFTs.getSubDomains	     import GetSubDomains
from commands.CRAFTs.getJavascripts	     import GetJavascripts
from commands.CRAFTs.getPaths		     import GetPaths
from commands.CRAFTs.getRobotsTxt	     import GetRobotsTxt
from commands.CRAFTs.getGithub		     import GetGithub
from commands.CRAFTs.fullscan		     import Fullscan
from commands.help			     import Help
from commands.CRUDs			     import DRY as c
from personalizedPrint			     import clear
from personalizedPrint			     import pp
import os
import sys
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
		case "addvariable" | "addv" | "av":		pp('EXECUTING add parameter..')
		case "displayvariable" | "displayv" | "dv":	pp('EXECUTING display parameter..')
		case "updatevariable" | "updatev" | "uv":	pp('EXECUTING update parameter..')
		case "deletevariable" | "deletev" | "delv":	pp('EXECUTING delete parameter..')
		# Cookie
		case "addcookie" | "addc" | "ac":		pp('EXECUTING add cookie..')
		case "displaycookie" | "displayc" | "dc":	pp('EXECUTING display cookie..')
		case "updatecookie" | "updatec" | "uc":		pp('EXECUTING update cookie..')
		case "deletecookie" | "deletec" | "delc":	pp('EXECUTING delete cookie..')
		# Capture
		case "addcapture" | "addcap" | "acap":		pp('EXECUTING add capture..')
		case "displaycapture" | "displaycap" | "dcap":	pp('EXECUTING display capture..')
		case "updatecapture" | "updatecap" | "ucap":	pp('EXECUTING update capture..')
		case "deletecapture" | "deletecap" | "dcap":	pp('EXECUTING delete capture..')
		# Transaction
		case "addtransaction" | "addt" | "at":		pp('EXECUTING add transaction..')
		case "displaytransaction" | "displayt" | "dt":	pp('EXECUTING display transaction..')
		case "updatetransaction" | "updatet" | "ut":	pp('EXECUTING update transaction..')
		case "deletetransaction" | "deletet" | "delt":	pp('EXECUTING delete transaction..')
		case "fullscan" | "fs" : Fullscan.execute(IN)
		case "get":
			asset = ''
			if len(IN.split()) >= 2:
				asset = IN.split()[1]
			match asset:
				case "techs"  : GetTechs.execute(IN)
				case "whois"  : GetWhois.execute(IN)
				case "ip"     : GetIp.execute(IN)
				case "ports"  : GetOpenPorts.execute(IN)
				case "subs"   : GetSubDomains.execute(IN)
				case "js"     : GetJavascripts.execute(IN)
				case "paths"  : GetPaths.execute(IN)
				case "robots" : GetRobotsTxt.execute(IN)
				case "github" : GetGithub.execute(IN)
				case _        : Help.execute("help get")
		case 'run':
			from APIs.app import run_apis
			c.questionToExecute( False,run_apis,{},"running APIs will prevent executing commands in this terminal \n you can execute < python3 APIs/app.py > in another terminal \n run APIs here (y/n)")
		case '':					return True
		case "quit" | "q":				return False
		case "clear" | "c":				clear()
		case "pwd":					pp(os.getcwd())
		case "help":					Help.execute(IN)
		case _:						pp('Invalid Command')
	return True
			
			
