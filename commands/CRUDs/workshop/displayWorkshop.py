from entities.workshop import Workshop
from commands.CRUDs    import DRY as c
import json
class DisplayWorkshop:
	@staticmethod
	def execute(IN):
		IN	= c.short_command(IN,"dw")
		dw	= c.option("dw",False,False, IN)
		id	= c.option("-w",True, False, IN)
		all	= c.option("-A",False,False, IN)
		expand  = c.option("-x",False,False, IN)
		
		if("UserNeedsHelp" in [dw,id,all,expand] or (not id and not all)):
			DisplayWorkshop.help()
			return "UserNeedsHelp"
		else:
			if(id):
				wrk = Workshop.search(id)
				if(wrk != "WorkshopNotFound"):
					print("\n✔️:WORKSHOP:")
					wrk.display(expand)
					return wrk.id
				else:
					print("❌: Workshop Not Found")
					return "WorkshopNotFound"
			if(all):
				workshops_ids=[]
				print("\n✔️WORKSHOPS:")
				for wrk in Workshop.getAllWorkshops():
					print("\t•"+wrk.id)
					workshops_ids.append(wrk.id)

				return workshops_ids
			
	@staticmethod
	def help():
		print("help -DisplayWorkshop")

