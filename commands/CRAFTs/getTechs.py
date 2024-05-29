from entities.workshop			import Workshop
from entities.domain			import Domain
from entities.path			import Path
from commands.CRUDs			import DRY as c
from get_assets.getTechsByWebanalyzer	import GetTechsByWebanalyzer
import GlobalVars as TopG


class GetTechs:
	@staticmethod
	def execute(IN):
		IN	     = c.concat_getasset(IN)
		IN	     = c.short_command(IN,"techs")
		cmnd	     = c.option("techs",False, False,IN)
		workshop     = c.option("-w"   ,True,  False,IN)
		domain	     = c.option("-d"   ,True,  False,IN)
		show_balance = c.option("-b"   ,False, False,IN)
		no_save	     = c.option("-no"  ,False, False,IN)



		if("UserNeedsHelp" in [ cmnd, domain, no_save, workshop, show_balance]):
			GetTechs.help()
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
			
			result = GetTechsByWebanalyzer(workshop, domain, no_save, show_balance)
			match result:
				case 400               : print("400	There was an error with the request")
				case 403               : print("403	Authorisation failure (incorrect API key, invalid method or resource or insufficient credits)\n Write your API KEY in config.json")
				case 429               : print("429	Rate limit exceeded")
				case 'WorkshopNotFound': print("Workshop Not Found")
				case _  :
					for t in result['techs']:
						print(t)
					if show_balance :
						print("You have "+str(result['balance'])+" requests left")
			return result
	
	@staticmethod	
	def help():
		print("""
	command: get techs
	option			required	Description

	-d <domain>		  YES		insert a domain to get its technologies
						required when there is no domain setted

	-w <workshop>		  Y/N		select a workshop
						required when there is no workshop setted

	-b			  NO		get the credit (how many scan left)

	-no			  NO		do NOT save the ip address we got.
		""")



