from entities.workshop import Workshop
from commands import DRYFFC as c
import json
import GlobalVars as TopG


class SetWorkshop:
	@staticmethod
	def execute(IN):
		IN  = c.short_command(IN,"sw")
		id  = c.option("sw",True,IN)
		
		if("UserNeedsHelp" in [id]):
			SetWorkshop.help()
		else:
			wrkshop = Workshop.search(id)
			if(wrkshop != "WorkshopNotFound"):
				TopG.CURRENT_WORKSHOP=id
			else:
				print("❌: Workshop Not Found")

	@staticmethod
	def help():
		print("help -SetWorkshop")

