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
			return "UserNeedsHelp"
		else:
			result = c.questionToExecute(for_sure,Workshop.update,{'oldId':old_id,'newId':new_id },"update workshop ["+old_id+"] to ["+new_id+"] ? (y/n)")

			if(result == "WorkshopNotFound"):
				print("❌ Workshop ["+old_id+"] not found")
				return "WorkshopNotFound"
			elif(result == "NewWorkshopIdExist"):
				print("❌ Id ["+new_id+"] already exist.")
				return "NewWorkshopIdExist"
			elif(result == "WorkshopUpdated"):
				print("✅ Workshop ["+old_id+"] is Updated to ["+new_id+"]")
				return "WorkshopUpdated"
	@staticmethod
	def help():
		print("""
	command: updateworkshop | updatew | uw
	option		required	Description

	<workshop>	  YES		select a workshop to update

	-i <new_id>	  YES		give a new id

	-s		  NO		skip the saving question , and save changes
	""")




