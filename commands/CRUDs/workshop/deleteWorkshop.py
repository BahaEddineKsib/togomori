from entities.workshop import Workshop
from commands.CRUDs    import DRY as c

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
				print("❌ Workshop ["+ID+"] not found")
			elif(result == "WorkshopIsSet"):
				print("❌ Workshop ["+ID+"] is set - can't delete workshop when setted as current workshop")
			elif(result == "WorkshopDeleted"):
				print("✅ Workshop ["+ID+"] is Deleted")
			return result
	@staticmethod
	def help():
		print("""
	command: deleteworkshop | deletew | delw
	option		required	Description

	<workshop>	  YES		workshop name to delete

	-s		  NO		skip the saving question , and save changes
	""")


