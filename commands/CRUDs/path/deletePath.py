from entities.workshop import Workshop
from entities.domain   import Domain
from entities.path     import Path
from commands.CRUDs    import DRY as c
import GlobalVars as TopG


class DeletePath:
	@staticmethod
	def execute(IN):
		IN      = c.short_command(IN,"delp")
		delp	= c.option("delp",True, False,IN)
		domain	= c.option("-d"  ,True, False,IN)
		w_id    = c.option("-w"  ,True, False,IN)
		for_sure= c.option("-s"	 ,False,False,IN)
		


		if("UserNeedsHelp" in [ delp, domain, w_id, for_sure]):
			DeletePath.help()
			return "UserNeedsHelp"
		elif(not w_id and TopG.CURRENT_WORKSHOP == ""):
			print("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
			return "NoWorkshopSetted"
		elif(not domain and c.segmentUrl(delp)["domain"]=="NoDomain" and not TopG.CURRENT_DOMAIN):
			print("❌ Set a Domain or specify a domain with [-d <domain>] or in the beginning of the path.")
			return "NoDomainSetted"
		else:
			path   = c.segmentUrl(delp)["path"]
			if path == 'NoPath' or path == 'InvalidPath':
				print("❌ Invalid Path. Path should contain at least one / and  start with /")
				return "InvalidPath"

			domain	= c.segmentUrl(delp)['domain'] if not domain		else domain
			domain	= TopG.CURRENT_DOMAIN	    if     domain == "NoDomain" else domain
			cw	= TopG.CURRENT_WORKSHOP
			if not w_id:w_id= cw 

			result = c.questionToExecute(for_sure,Path.delete,{'path':path, 'domain':domain, 'workshop_id':w_id},"Delete path ["+domain+path+"] ?")
			
			if(  result == "WorkshopNotFound"):
				print("❌ Workshop ["+w_id+"] Not Found.")
			elif(result == "DomainNotFound"):
				print("❌ Domain ["+domain+"] Not Found.")
			elif(result == "PathNotFound"):
				print("❌ Path ["+path+"] Not Found")
			elif(result == "PathDeleted"):
				print("✅ Path ["+path+"] is Deleted.")
			return result
	@staticmethod	
	def help():
		print("""
	command: deletepath | deletep | delp
	option			required	Description

	<path>			  YES		insert path to delete
						exemple: dp /path1/page.php

	-d <domain>		  Y/N		specify a domain where the path exist
						required when there is no domain setted

	-w <workshop>		  Y/N		select a workshop to add the domain in it
						required when there is no workshop setted

	-s			  NO		skip the saving question , and save changes
	""")

