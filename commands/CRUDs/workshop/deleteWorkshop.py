from entities.workshop import Workshop
from commands.CRUDs    import DRY as c

class DeleteWorkshop:
	@staticmethod
	def execute(IN):
		IN       = c.short_command(IN,"delw")
		id       = c.option("delw",True, False,IN)
		for_sure = c.option("-s",  False,False,IN)
		
		if("UserNeedsHelp" in [id,for_sure]):
			DeleteWorkshop.help()
		else:
			result = c.questionToExecute(for_sure,Workshop.deleteById,{'id':id},"Delete workshop ["+id+"] ?")
			if(result == "WorkshopNotFound"):
				print("❌ Workshop ["+id+"] not found")
			elif(result == "WorkshopIsSet"):
				print("❌ Workshop ["+id+"] is set - can't delete workshop when setted as current workshop")
			elif(result == "WorkshopDeleted"):
				print("✅ Workshop ["+id+"] is Deleted")
	@staticmethod
	def help():
		print("help -AddWorkshop")


