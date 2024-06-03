from entities.workshop import Workshop
from commands.CRUDs    import DRY as c
import json
import GlobalVars as TopG
from personalizedPrint import pp

class UnsetWorkshop:
	@staticmethod
	def execute(IN):
		IN  = c.short_command(IN,"usw")
		unset  = c.option("usw",False,False,IN)
		
		if("UserNeedsHelp" in [unset]):
			UnsetWorkshop.help()
		else:
			TopG.CURRENT_WORKSHOP=""
			TopG.CURRENT_DOMAIN  =""
			pp("✅ Workshop  Unsetted")
			
	@staticmethod
	def help():
		pp("""
	command: unsetworkshop | unsetw | sw  [CONTAIN NO OPTIONS]
	""")



