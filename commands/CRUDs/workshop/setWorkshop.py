from entities.workshop import Workshop
from commands.CRUDs    import DRY as c
import json
import GlobalVars as gv
from personalizedPrint import pp

class SetWorkshop:
	@staticmethod
	def execute(IN):
		IN  = c.short_command(IN,"sw")
		ID  = c.option("sw",True, False,IN)
		
		if("UserNeedsHelp" in [ID]):
			SetWorkshop.help()
		else:
			if(Workshop.exist(ID)):
				gv.CURRENT_WORKSHOP=ID
				gv.CURRENT_DOMAIN  =""
				pp("✅ Workshop "+ID+" Setted")
			else:
				pp("❌: Workshop Not Found")

	@staticmethod
	def help():
		pp("""
	command: setworkshop | setw | sw
	option		required	Description

	<workshop>	  Y/N		workshop name to set
	""")



