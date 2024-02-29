from entities.workshop import Workshop
from commands.CRUDs    import DRY as c

class AddWorkshop:
	@staticmethod
	def execute(IN):
		IN       = c.short_command(IN,"aw")
		id       = c.option("aw",True  ,False,IN)
		for_sure = c.option("-s",False, False,IN)
		
		if("UserNeedsHelp" in [id,for_sure]):
			AddWorkshop.help()
			return "UserNeedsHelp"
		else:
			wrk = Workshop(id)
			#print("\nWORKSHOP:")
			#wrk.display()
			result = c.questionToExecute(for_sure,wrk.save,{},"Save workshop ["+id+"] ?")
			if(result == "WorkshopExist"):
				print("❌ Workshop ["+id+"] already exist")
				return "WorkshopExist"
			elif(result == "WorkshopAdded"):
				print("✅ Workshop is ["+id+"] Added")
				return "WorkshopAdded"

	@staticmethod	
	def help():
		print("help -AddWorkshop")













		
