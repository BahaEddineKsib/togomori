from entities.domain   import Domain
from entities.workshop import Workshop
from commands.CRUDs    import DRY as c
import json
import GlobalVars as TopG
from personalizedPrint import pp

class UnsetDomain:
	@staticmethod
	def execute(IN):
		IN      = c.short_command(IN,"usd")
		domain  = c.option("usd",False, False,IN)
		
		if("UserNeedsHelp" in [domain]):
			UnsetDomain.help()
		else:
			TopG.CURRENT_DOMAIN = ""
			pp("✅ Domain Unsetted")

	@staticmethod
	def help():
		pp("""
	command: unsetdomain | unsetd | usd [CONTAIN NO OPTIONS]
	""")



