from entities.workshop import Workshop
from entities.domain   import Domain
from commands          import DRYFFC as c
import GlobalVars as TopG


class DeleteDomain:
	@staticmethod
	def execute(IN):
		IN         = c.short_command(IN,"deld")
		deld         = c.option("deld",       True, False,IN)
		w_id       = c.option("-w",           True, False,IN)
		for_sure   = c.option("-s",           False,False,IN)
		


		if("UserNeedsHelp" in [ deld, w_id, for_sure]):
			DeleteDomain.help()
		elif(not w_id and TopG.CURRENT_WORKSHOP == ""):
			print("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
		else:
			cw         = TopG.CURRENT_WORKSHOP
			if not w_id:        w_id        = cw 

			result = c.questionToExecute(for_sure,Domain.delete,{'domain_text':deld, 'workshop_id':w_id},"Delete domain ["+deld+"] ?")
			
			if(result == "WorkshopNotFound"):
				print("❌ Workshop ["+w_id+"] Not Found.")
			elif(result == "DomainNotFound"):
				print("❌ Domain ["+deld+"] Not Found.")
			elif(result == "DomainAdded"):
				print("✅ Domain ["+deld+"] is Added.")

	@staticmethod	
	def help():
		print("help -DeleteDomain")

