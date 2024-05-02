from entities.workshop			import Workshop
from entities.domain			import Domain
from entities.path			import Path
from commands.CRUDs			import DRY as c
from get_assets.getIpByDomain	 	import GetIpByDomain 
import GlobalVars as TopG


class GetIp:
	@staticmethod
	def execute(IN):
		IN	     = c.concat_getasset(IN)
		IN	     = c.short_command(IN,"ip")
		cmnd	     = c.option("ip",False, False,IN)
		workshop     = c.option("-w"   ,True,  False,IN)
		domain	     = c.option("-d"   ,True,  False,IN)
		no_save	     = c.option("-no"  ,False, False,IN)



		if("UserNeedsHelp" in [ cmnd, domain, no_save, workshop]):
			GetIp.help()
			return "UserNeedsHelp"
		elif(not workshop and TopG.CURRENT_WORKSHOP == "" and not no_save):
			print("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
			return "NoWorkshopSetted"
		elif(c.segmentUrl(domain)["domain"]=="NoDomain" and not TopG.CURRENT_DOMAIN):
			print("❌ Set a Domain or specify a domain with [-d <domain>] or in the beginning of the path.")
			return "NoDomainSetted"
		else:
			domain   = c.segmentUrl(domain)['domain'] if domain else TopG.CURRENT_DOMAIN
			cw	 = TopG.CURRENT_WORKSHOP
			workshop = cw if not workshop else workshop
			
			result = GetIpByDomain(workshop,domain,no_save)
			match result:
				case "NoIp": print("Can't get this domain's ip")
				case _  :		 print(result)
	
			return result
	@staticmethod
	def help():
		print("help")




