from entities.workshop import Workshop
from commands import DRYFFC as c

class AddWorkshop:
	@staticmethod
	def execute(IN):
		IN   = c.short_command(IN,"aw")
		id   = c.option("aw",True,IN)
		save = c.option("-s",False,IN)
		
		if("UserNeedsHelp" in [id,save]):
			AddWorkshop.help()
		else:
			wrk = Workshop(id)
			print("\nWORKSHOP:")
			wrk.display()
			S_return = c.saveIt(save,wrk.save)



	@staticmethod	
	def help():
		print("help -AddWorkshop")













		
