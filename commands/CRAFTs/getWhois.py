from entities.workshop			import Workshop 
from entities.domain			import Domain
from entities.path			import Path
from commands.CRUDs			import DRY as c
from get_assets.getInfoByWhois	 	import GetInfoByWhois
import GlobalVars as TopG
from personalizedPrint import pp

class GetWhois:
	@staticmethod
	def execute(IN):
		IN	     = c.concat_getasset(IN)
		IN	     = c.short_command(IN,"whois")
		cmnd	     = c.option("whois",False, False,IN)
		workshop     = c.option("-w"   ,True,  False,IN)
		domain	     = c.option("-d"   ,True,  False,IN)
		no_save	     = c.option("-no"  ,False, False,IN)



		if("UserNeedsHelp" in [ cmnd, domain, no_save, workshop]):
			GetTechs.help()
			return "UserNeedsHelp"
		elif(not workshop and TopG.CURRENT_WORKSHOP == "" and not no_save):
			pp("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
			return "NoWorkshopSetted"
		elif(c.segmentUrl(domain)["domain"]=="NoDomain" and not TopG.CURRENT_DOMAIN):
			pp("❌ Set a Domain or specify a domain with [-d <domain>] or in the beginning of the path.")
			return "NoDomainSetted"
		else:
			domain   = c.segmentUrl(domain)['domain'] if domain else TopG.CURRENT_DOMAIN
			cw	 = TopG.CURRENT_WORKSHOP
			workshop = cw if not workshop else workshop
			
			result = GetInfoByWhois(workshop,domain,no_save)
			match result:
				case "DomainNotInWhois": pp("Can't get this domain's information with whois")
				case "WorkshopNotFound": pp("workshop not found")
				case _  :
					for key in result:
						pp(key+': '+str(result[key]))
	
			return result
	@staticmethod	
	def help():
		pp("""
	command: get whois
	option			required	Description

	-d <domain>		  YES		insert a domain to get its technologies
						required when there is no domain setted

	-w <workshop>		  Y/N		select a workshop
						required when there is no workshop setted

	-no			  NO		do NOT save the ip address we got.
		""")















