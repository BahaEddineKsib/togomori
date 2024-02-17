from entities.workshop import Workshop
from entities.domain   import Domain
from commands          import DRYFFC as c
import GlobalVars as TopG


class AddDomain:
	@staticmethod
	def execute(IN):
		IN       = c.short_command(IN,"ad")
		ad       = c.option("ad",    False,IN)
		domain   = c.option("-d",    True, IN)
		w_id     = c.option("-w",    True, IN)
		tag      = c.option("--tag", True,IN)
		for_sure = c.option("-s",    False,IN)
		


		if("UserNeedsHelp" in [ad, domain, for_sure, tag] or (not domain)):
			AddDomain.help()
		elif(not w_id and TopG.CURRENT_WORKSHOP == ""):
			print("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")

		else:
			w_id = TopG.CURRENT_WORKSHOP if not w_id else w_id
			tag  = "" if not tag else tag
			dmn = Domain(workshop_id=w_id, domain_text=domain, tag=tag)
			print("\ndomain:")
			dmn.display()
			result = c.questionToExecute(for_sure,dmn.save,{},"Save domain ["+domain+"] ?")
			if(result == "WorkshopNotFound"):
				print("❌ Workshop ["+w_id+"] Not Found.")
			elif(result == "DomainExist"):
				print("❌ Domain ["+domain+"] already exist.")
			elif(result == "DomainAdded"):
				print("✅ Domain ["+domain+"] is Added.")

	@staticmethod	
	def help():
		print("help -AddDomain")


