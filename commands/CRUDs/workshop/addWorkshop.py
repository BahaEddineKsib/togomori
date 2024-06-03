from entities.workshop import Workshop
from commands.CRUDs    import DRY as c
from personalizedPrint import pp


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
			#pp("\nWORKSHOP:")
			#wrk.display()
			result = c.questionToExecute(for_sure,wrk.save,{},"Save workshop ["+id+"] ?")
			if(result == "WorkshopExist"):
				pp("❌ Workshop ["+id+"] already exist")
				return "WorkshopExist"
			elif(result == "WorkshopAdded"):
				pp("✅ Workshop is ["+id+"] Added")
				return "WorkshopAdded"

	@staticmethod	
	def help():
		pp("""
	command: addworkshop | addw | aw
	option		required	Description

	<workshop>	  YES		the name of the new workshop

	-s		  NO		skip the saving question , and save changes
	""")







		
