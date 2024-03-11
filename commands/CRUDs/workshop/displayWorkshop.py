from entities.workshop import Workshop
from commands.CRUDs    import DRY as c
import json
class DisplayWorkshop:
	@staticmethod
	def execute(IN):
		IN	= c.short_command(IN,"dw")
		dw	= c.option("dw",False,False, IN)
		ID	= c.option("-w",True, False, IN)
		ALL	= c.option("-A",False,False, IN)
		expand  = c.option("-x",False,False, IN)
		
		if("UserNeedsHelp" in [dw,ID,ALL,expand] or (not ID and not ALL)):
			DisplayWorkshop.help()
			return "UserNeedsHelp"
		else:
			if(ID):
				if( Workshop.exist(ID)):
					wrk = Workshop.get(ID,expand)
					wrk.display(expand)
					return wrk.ID
				else:
					print("❌: Workshop Not Found")
					return "WorkshopNotFound"
			if(all):
				workshops_ids=[]
				for wrk in Workshop.getAll(expand):
					wrk.display(expand)
					workshops_ids.append(wrk.ID)

				return workshops_ids
			
	@staticmethod
	def help():
		print("help -DisplayWorkshop")

