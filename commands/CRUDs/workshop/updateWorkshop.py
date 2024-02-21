from entities.workshop import Workshop
from commands.CRUDs    import DRY as c

class UpdateWorkshop:
	@staticmethod
	def execute(IN):
		IN       = c.short_command(IN,"uw")
		old_id   = c.option("uw",True, False,IN)
		new_id   = c.option("-i",True, False,IN)
		for_sure = c.option("-s",False,False,IN)
		
		if("UserNeedsHelp" in [old_id,new_id,for_sure] or (not new_id)):
			UpdateWorkshop.help()
		else:
			result = c.questionToExecute(for_sure,Workshop.updateId,{'id':old_id,'newId':new_id },"update workshop ["+old_id+"] to ["+new_id+"] ? (y/n)")
			if(result == "WorkshopNotFound"):
				print("❌ Workshop ["+old_id+"] not found")
			elif(result == "NewWorkshopIdExist"):
				print("❌ Id ["+new_id+"] already exist.")
			elif(result == "WorkshopUpdated"):
				print("✅ Workshop ["+old_id+"] is Updated to ["+new_id+"]")
	@staticmethod
	def help():
		print("help -UpdateWorkshop")


