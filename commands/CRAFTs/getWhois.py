from entities.workshop			import Workshop 
from entities.domain			import Domain
from entities.path			import Path
from commands.CRUDs			import DRY as c
from get_assets.getInfoByWhois	 	import GetInfoByWhois
import GlobalVars as TopG
from personalizedPrint import pp
import tldextract	 as domain_parts
class GetWhois:
	@staticmethod
	def execute(IN):
		IN	     = c.concat_getasset(IN)
		IN	     = c.short_command(IN,"whois")
		cmnd	     = c.option("whois",False, False,IN)
		workshop     = c.option("-w"   ,True,  False,IN)
		domain	     = c.option("-d"   ,True,  False,IN)
		all_domains  = c.option("-a"	,False, False,IN)
		domains_list = c.option("-l"	,True,  True ,IN)
		no_save	     = c.option("-no"  ,False, False,IN)



		if("UserNeedsHelp" in [ cmnd, domain, no_save, workshop, all_domains, domains_list]):
			GetWhois.help()
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
					hosts= []
					for d in dmns:
						host = domain_parts.extract(d.domain).domain + '.' + domain_parts.extract(d.domain).suffix
						if not (host in hosts):
							hosts.append(host)
					for h in hosts:
						pp("WHOIS: "+h)
						result = GetInfoByWhois(workshop,h, no_save, by_hostname=True)
						GetWhois.outputting(result)
				else:
					pp("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
					return "NoWorkshopSetted"
			elif domains_list:
				for d in domains_list:
					if c.segmentUrl(d)['domain'] != "NoDomain":
						result = GetInfoByWhois(workshop, d, no_save)
						GetWhois.outputting(result)
					else:
						pp(d+" is not a good domain")
			else:
				domain   = c.segmentUrl(domain)['domain'] if domain else TopG.CURRENT_DOMAIN
				result = GetInfoByWhois(workshop,domain,no_save)
				
				Get.Whoisoutputting(result)
	
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

	-a			  NO		get the WHOIS of all the domains 
						in the workshop that don't have a WHOIS scan yet

	-l			  NO		insert a list of domains to get their WHOIS



	-no			  NO		do NOT save the ip address we got.
		""")

	@staticmethod
	def outputting(result):
		match result:
			case "DomainNotInWhois": pp("Can't get this domain's information with whois")
			case "WorkshopNotFound": pp("workshop not found")
			case _  :
				for key in result:
					if  type(result[key]) != list:
						pp(key+':		'+result[key])
					else:
						first = True
						for i in result[key]:
							if first:
								pp(key+':		'+i)
								first = False
							else:
								pp('			'+i)
















