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
from commands.CRUDs import DRY as c


class Help:

	@staticmethod
	def execute(IN):
		HL = c.option("help", True, True,IN)

		if("UserNeedsHelp" in [HL]):
			Help.help()
			return "UserNeedsHelp"
		else:
			if( "commands" in HL or "all" in HL):
				print("""
					COMMANDS:
					setworkshop	| setw		| sw
					unsetworkshop	| unsetw	| usw
					addworkshop	| addw		| aw
					displayworkshop	| displayw	| dw
					deleteworkshop	| deletew	| delw
					updateworkshop	| updatew	| uw
					adddomain	| addd		| ad
					displaydomain	| displayd	| dd
					deletedomain	| deleted	| deld
					updatedomain	| updated	| ud
					setdomain	| setd		| sd
					unsetdomain	| unsetd	| usd
					addpath		| addp		| ap
					displaypath	| displayp	| dp
					updatepath	| updatep	| up
					deletepath	| deletep	| delp
					get techs
					get whois
					get ip
					get ports
					get subs""")
			if("all" in HL or "workshop" 	in HL or "set"		in HL or "setworkshop"       in HL):sw.help()
			if("all" in HL or "domain"	in HL or "set"		in HL or "setdomain"         in HL):sd.help()
			if("all" in HL or "workshop"	in HL or "unset"	in HL or "unsetworkshop"     in HL):usw.help()
			if("all" in HL or "domain"	in HL or "unset"	in HL or "unsetdomain"       in HL):usd.help()
			if("all" in HL or "workshop"	in HL or "add"		in HL or "addworkshop"       in HL):aw.help()
			if("all" in HL or "domain"	in HL or "add"		in HL or "adddomain"	     in HL):ad.help()
			if("all" in HL or "path"	in HL or "add"		in HL or "addpath"	     in HL):ap.help()
			if("all" in HL or "workshop"	in HL or "display"	in HL or "displayworkshop"   in HL):dw.help()
			if("all" in HL or "domain"	in HL or "display"	in HL or "displaydomain"     in HL):dd.help()
			if("all" in HL or "path"	in HL or "display"	in HL or "displaypath"	     in HL):dp.help()
			if("all" in HL or "workshop"	in HL or "update"	in HL or "updateworkshop"    in HL):uw.help()
			if("all" in HL or "domain"	in HL or "update"	in HL or "updatedomain"      in HL):ud.help()
			if("all" in HL or "path"	in HL or "update"	in HL or "updatepath"	     in HL):up.help()
			if("all" in HL or "workshop"	in HL or "delete"	in HL or "deleteworkshop"    in HL):delw.help()
			if("all" in HL or "domain"	in HL or "delete"	in HL or "deletedomain"	     in HL):deld.help()
			if("all" in HL or "path"	in HL or "delete"	in HL or "deletepath"	     in HL):delp.help()
			if("all" in HL or "get"		in HL or "get_techs"	in HL or "techs"	     in HL):GetTechs.help()
			if("all" in HL or "get"		in HL or "get_whois"	in HL or "whois"	     in HL):GetWhois.help()
			if("all" in HL or "get"		in HL or "get_ip"	in HL or "ip"		     in HL):GetIp.help()
			if("all" in HL or "get"		in HL or "get_ports"	in HL or "ports"	     in HL):GetOpenPorts.help()
			if("all" in HL or "get"		in HL or "get_subs"	in HL or "subs"		     in HL):GetSubDomains.help()
	@staticmethod
	def help():
		print("""
	command: help
	option			required	Description

	<COMMAND_HELP>		  YES		With help command you should insert a target
	

	COMMANDS_HELP:
		all			help for all the commands
		commands

		set			help for the commands sw, sd
		setworkshop		help for the command setworkshop     | setw       | sw
                setdomain		help for the command setdomain       | setd       | sd

		unset			help for the commands usd, usd
                unsetworkshop		help for the command unsetworkshop   | unsetw     | usw
                unsetdomain		help for the command unsetdomain     | unsetd     | usd

		add			help for the commands aw, ad, ap
	        addworkshop		help for the command addworkshop     | addw       | aw
                adddomain		help for the command adddomain       | addd       | ad
                addpath			help for the command addpath         | addp       | ap

		display			help for the commands dw, dd, dp
                displayworkshop		help for the command displayworkshop | displayw   | dw
                displaydomain		help for the command displaydomain   | displayd	  | dd
                displaypath		help for the command displaypath     | displayp	  | dp

		update			help for the commands uw, ud, up
                updateworkshop		help for the command updateworkshop  | updatew	  | uw
                updatedomain		help for the command updatedomain    | updated	  | ud
                updatepath		help for the command updatepath	     | update     | up

		delete			help for the commands delw, deld, delp
                deleteworkshop		help for the command deleteworkshop  | deletew    | delw
                deletedomain		help for the command deletedomain    | deleted	  | deld
                deletepath		help for the command deletepath	     | deletep	  | delp

		workshop		help for the CRUD commands of workshop
		domain			help for the CRUD commands of domain
		path			help for the CRUD commands of path

		get			help for the commands get [techs, whois, ip, ports, subs]
                techs			help for the command get techs
                whois			help for the command get whois
                ip			help for the command get ip
                ports			help for the command get ports
                subs			help for the command get subs
		
		all			list all the commands help
		commands		listing all the existing commands


		exemple: help domain tech

		""")
