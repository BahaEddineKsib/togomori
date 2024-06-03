from entities.workshop import Workshop
from commands.CRUDs    import DRY as c
from personalizedPrint import pp

class DeleteWorkshop:
	@staticmethod
	def execute(IN):
		IN       = c.short_command(IN,"delw")
		ID       = c.option("delw",True, False,IN)
		for_sure = c.option("-s",  False,False,IN)
		
		if("UserNeedsHelp" in [ID,for_sure]):
			DeleteWorkshop.help()
			return "UserNeedsHelp"
		else:
			result = c.questionToExecute(for_sure,Workshop.delete,{'ID':ID},"Delete workshop ["+ID+"] ?")
			if(result == "WorkshopNotFound"):
				pp("❌ Workshop ["+ID+"] not found")
			elif(result == "WorkshopIsSet"):
				pp("❌ Workshop ["+ID+"] is set - can't delete workshop when setted as current workshop")
			elif(result == "WorkshopDeleted"):
				pp("✅ Workshop ["+ID+"] is Deleted")
			return result
	@staticmethod
	def help():
		pp("""
	command: deleteworkshop | deletew | delw
	option		required	Description

	<workshop>	  YES		workshop name to delete

	-s		  NO		skip the saving question , and save changes
	""")


