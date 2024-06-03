from entities.workshop import Workshop
from entities.domain   import Domain
from commands.CRUDs    import DRY as c
import GlobalVars as TopG
from personalizedPrint import pp

class DeleteDomain:
	@staticmethod
	def execute(IN):
		IN         = c.short_command(IN,"deld")
		deld         = c.option("deld",       True, False,IN)
		w_id       = c.option("-w",           True, False,IN)
		for_sure   = c.option("-s",           False,False,IN)
		


		if("UserNeedsHelp" in [ deld, w_id, for_sure]):
			DeleteDomain.help()
			return "UserNeedsHelp"
		elif(not w_id and TopG.CURRENT_WORKSHOP == ""):
			pp("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
			return "NoWorkshopSetted"
		else:
			cw         = TopG.CURRENT_WORKSHOP
			if not w_id:        w_id        = cw 

			result = c.questionToExecute(for_sure,Domain.delete,{'domain':deld, 'workshop_id':w_id},"Delete domain ["+deld+"] ?")
			
			if(result == "WorkshopNotFound"):
				pp("❌ Workshop ["+w_id+"] Not Found.")
			elif(result == "DomainNotFound"):
				pp("❌ Domain ["+deld+"] Not Found.")
			elif(result == "DomainDeleted"):
				pp("✅ Domain ["+deld+"] is Deleted.")
			return result
	@staticmethod	
	def help():
		pp("""
	command: deldomain | deleted | deld
	option			required	Description

	<domain>		  YES		New Domain 
						exemple: deld www.example.com

	-w <workshop>		  Y/N		select a workshop to add the domain in it
						required when there is no workshop setted

	-s			  NO		skip the saving question , and save changes
	""")


