from entities.workshop import Workshop
from commands import DRYFFC as c

class AddWorkshop:
	@staticmethod
	def execute(IN):
		IN       = c.short_command(IN,"aw")
		id       = c.option("aw",True  ,False,IN)
		for_sure = c.option("-s",False, False,IN)
		
		if("UserNeedsHelp" in [id,for_sure]):
			AddWorkshop.help()
		else:
			wrk = Workshop(id)
			print("\nWORKSHOP:")
			wrk.display()
			result = c.questionToExecute(for_sure,wrk.save,{},"Save workshop ["+id+"] ?")
			if(result == "WorkshopExist"):
				print("❌ Workshop ["+id+"] already exist")
			elif(result == "WorkshopAdded"):
				print("✅ Workshop is ["+id+"] Added")

	@staticmethod	
	def help():
		print("help -AddWorkshop")













		
