from entities.workshop import Workshop
from commands import DRYFFC as c

class AddWorkshop:
	@staticmethod
	def execute(IN):
		IN   = c.short_command(IN,"aw")
		id   = c.option("aw",True,IN)
		path = c.option("-f",True,IN) if c.option("-f",True,IN) else Workshop.default_path
		save = c.option("-s",False,IN)
		
		if("UserNeedsHelp" in [id,path]):
			AddWorkshop.help()
		else:
			wrk = Workshop(id,path)
			print("\nWORKSHOP:")
			wrk.display()
			S_return = c.saveIt(save,wrk.save)



	@staticmethod	
	def help():
		print("help -AddWorkshop")













		
