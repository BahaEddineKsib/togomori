from entities.workshop import Workshop
from commands import DRYFFC as c
import json
class DisplayWorkshop:
	@staticmethod
	def execute(IN):
		IN  = c.short_command(IN,"dw")
		dw  = c.option("dw",False,False, IN)
		id  = c.option("-w",True, False, IN)
		all = c.option("-A",False,False, IN)
		
		if("UserNeedsHelp" in [dw,id,all] or (not id and not all)):
			DisplayWorkshop.help()
		else:
			if(id):
				wrkshop = Workshop.search(id)
				if(wrkshop != "WorkshopNotFound"):
					print("\n✔️:WORKSHOP:")
					Workshop.search(id).display()
				else:
					print("❌: Workshop Not Found")
			if(all):
				print("\n✔️WORKSHOPS:")
				for wrk in Workshop.getAllWorkshops():
					print("\t•"+wrk.id)
			
	@staticmethod
	def help():
		print("help -DisplayWorkshop")

