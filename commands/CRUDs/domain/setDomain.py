from entities.domain   import Domain
from entities.workshop import Workshop
from commands.CRUDs    import DRY as c
import json
import GlobalVars as gv
from personalizedPrint import pp

class SetDomain:
	@staticmethod
	def execute(IN):
		IN      = c.short_command(IN,"sd")
		domain  = c.option("sd",True, False,IN)
		
		if("UserNeedsHelp" in [domain]):
			SetDomain.help()
		else:
			if( gv.CURRENT_WORKSHOP != ""):
				cw = gv.CURRENT_WORKSHOP
				if(not Domain.exist(cw,domain)):
					pp("❌ Domain ["+domain+"] Not Found.")
				else:
					gv.CURRENT_DOMAIN = domain
					pp("✅ Domain "+domain+" Setted")
					
			else:
				pp("❌: Can't set Domain without setting a workshop.")

	@staticmethod
	def help():
		pp("""
	command: setdomain | setd | sd
	option		required	Description

	<domain>	  YES		workshop name to set
	""")
