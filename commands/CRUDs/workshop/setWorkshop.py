from entities.workshop import Workshop
from commands.CRUDs    import DRY as c
import json
import GlobalVars as gv


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
				print("✅ Workshop "+ID+" Setted")
			else:
				print("❌: Workshop Not Found")

	@staticmethod
	def help():
		print("help -SetWorkshop")

