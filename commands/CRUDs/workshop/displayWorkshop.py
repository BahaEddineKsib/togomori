from entities.workshop import Workshop
from commands.CRUDs    import DRY as c
import json
from personalizedPrint import pp


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
					pp("❌: Workshop Not Found")
					return "WorkshopNotFound"
			if(all):
				workshops_ids=[]
				for wrk in Workshop.getAll(expand):
					wrk.display(expand)
					workshops_ids.append(wrk.ID)

				return workshops_ids
			
	@staticmethod
	def help():
		pp("""
	command: displayworkshop | displayw | dw
	option		required	Description

	-w <workshop>	  Y/N		select a workshop to display 
					required when option -A is not added

	-A		  Y/N		display ALL the workshops
					required when option -w is not added

	-x		  NO		expand the display for more details
	""")

