from entities.workshop			import Workshop
from entities.domain			import Domain
from entities.path			import Path
from commands.CRUDs			import DRY as c
from get_assets.getIpByDomain	 	import GetIpByDomain 
import GlobalVars as TopG
from personalizedPrint import pp

class GetIp:
	@staticmethod
	def execute(IN):
		IN	     = c.concat_getasset(IN)
		IN	     = c.short_command(IN,"ip")
		cmnd	     = c.option("ip" ,False, False,IN)
		workshop     = c.option("-w" ,True,  False,IN)
		domain	     = c.option("-d" ,True,  False,IN)
		all_domains  = c.option("-a" ,False,  False,IN)
		domains_list = c.option("-l" ,True,  True ,IN)
		no_save	     = c.option("-no",False, False,IN)



		if("UserNeedsHelp" in [ cmnd, domain, no_save, workshop, all_domains, domains_list]): 
			GetIp.help()
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
						if d.ip =="":
							result = GetIpByDomain(workshop,d.domain,no_save) 
				else:
					pp("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
					return "NoWorkshopSetted"
			elif domains_list:
				for d in domains_list:
					if c.segmentUrl(d)['domain'] != "NoDomain":
						result = GetIpByDomain(workshop, d, no_save)
					else:
						pp(d+" is not a good domain")
			else:
				domain   = c.segmentUrl(domain)['domain'] if domain else TopG.CURRENT_DOMAIN

				result = GetIpByDomain(workshop,domain,no_save)
				'''
				match result:
					case "NoIp": pp("Can't get this domain's ip")
					case _  :		 pp("done.")
				'''
			return result

	@staticmethod
	def help():
		pp("""
	command: get ip
	option			required	Description

	-d <domain>		  Y/N		insert a domain to get its ip address
						required when there is no domain setted

	-a			  NO		get the ip address of all the domains 
						in the workshop that don't have an ip yet

	-l			  NO		insert a list of domains to get their ip

	-w <workshop>		  Y/N		select a workshop to add the domain in it
						required when there is no workshop setted

	-no			  NO		do NOT save the ip address we got.
		""")
