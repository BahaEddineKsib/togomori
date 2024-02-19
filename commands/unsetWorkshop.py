from entities.workshop import Workshop
from commands import DRYFFC as c
import json
import GlobalVars as TopG


class UnsetWorkshop:
	@staticmethod
	def execute(IN):
		IN  = c.short_command(IN,"usw")
		unset  = c.option("usw",False,False,IN)
		
		if("UserNeedsHelp" in [unset]):
			UnsetWorkshop.help()
		else:
			TopG.CURRENT_WORKSHOP=""
			
	@staticmethod
	def help():
		print("help -UnsetWorkshop")


