from entities.workshop			import Workshop
from entities.domain			import Domain
from entities.path			import Path
from commands.CRUDs			import DRY as c
from get_assets.getTechsByWebanalyzer	import GetTechsByWebanalyzer
import GlobalVars as TopG
from personalizedPrint import pp

class GetTechs:
	@staticmethod
	def execute(IN):
		IN	     = c.concat_getasset(IN)
		IN	     = c.short_command(IN,"techs")
		cmnd	     = c.option("techs",False, False,IN)
		workshop     = c.option("-w"   ,True,  False,IN)
		domain	     = c.option("-d"   ,True,  False,IN)
		all_domains  = c.option("-a"	,False, False,IN)
		domains_list = c.option("-l"	,True,  True ,IN)
		show_balance = c.option("-b"   ,False, False,IN)
		no_save	     = c.option("-no"  ,False, False,IN)



		if("UserNeedsHelp" in [ cmnd, domain, no_save, workshop, show_balance, all_domains, domains_list]):
			GetTechs.help()
			return "UserNeedsHelp"
		elif(not workshop and TopG.CURRENT_WORKSHOP == "" and not no_save):
			pp("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
			return "NoWorkshopSetted"
		elif(c.segmentUrl(domain)["domain"]=="NoDomain" and not TopG.CURRENT_DOMAIN and not all_domains and not domains_list):
			pp("❌ Set a Domain or specify a domain with [-d <domain>] or in the beginning of the path.")
			return "NoDomainSetted"
		else:
			cw	 = TopG.CURRENT_WORKSHOP
			workshop = cw if not workshop else workshop
			if all_domains:
				if workshop and Workshop.exist(workshop):
					dmns = Domain.getAll(workshop)
					for d in dmns:
						pp("TECHNOLOGIESS: "+d.domain)
						result = GetTechsByWebanalyzer(workshop, d.domain, no_save, show_balance)
						GetTechs.outputting(result, show_balance)
				else:
					pp("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
					return "NoWorkshopSetted"
			elif domains_list:
				for domain in domains_list:
					if c.segmentUrl(domain)['domain'] != "NoDomain":
						result = GetTechsByWebanalyzer(workshop, domain, no_save, show_balance)
						GetWhois.outputting(result, show_balance)
					else:
						pp(domain+" is not a good domain")
			else:
				domain   = c.segmentUrl(domain)['domain'] if domain else TopG.CURRENT_DOMAIN
				result = GetTechsByWebanalyzer(workshop, domain, no_save, show_balance)
				GetTechs.outputting(result, show_balance)
			return result
	
	@staticmethod	
	def help():
		pp("""
	command: get techs
	option			required	Description

	-d <domain>		  YES		insert a domain to get its technologies
						required when there is no domain setted

	-a			  NO		get the technologies of all the domain
						a workshop

	-l <[domains]>		  NO		insert a list of domains to get their techs

	-w <workshop>		  Y/N		select a workshop
						required when there is no workshop setted

	-b			  NO		get the credit (how many scan left)

	-no			  NO		do NOT save the ip address we got.
		""")
	
	@staticmethod
	def outputting(result, show_balance):
		match result:
			case 400               : pp("400	There was an error with the request")
			case 403               : pp("403	Authorisation failure (incorrect API key, invalid method or resource or insufficient credits)\n Write your API KEY in config.json")
			case 429               : pp("429	Rate limit exceeded")
			case 'WorkshopNotFound': pp("Workshop Not Found")
			case _  :
				for t in result['techs']:
					pp(t)
				if show_balance :
					pp("You have "+str(result['balance'])+" requests left")



