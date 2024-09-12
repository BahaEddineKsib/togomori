from entities.workshop			import Workshop 
from entities.domain			import Domain
from entities.path			import Path
from commands.CRUDs			import DRY as c
from get_assets.getGithubByDomain	import GetGithubByDomain
import GlobalVars as TopG
from personalizedPrint import pp
import tldextract	 as domain_parts
class GetGithub:
	@staticmethod
	def execute(IN):
		IN	     = c.concat_getasset(IN)
		IN	     = c.short_command(IN,"github")
		cmnd	     = c.option("github",False, False,IN)
		workshop     = c.option("-w"	,True,  False,IN)
		domain	     = c.option("-d"	,True,  False,IN)
		all_domains  = c.option("-a"	,False, False,IN)
		domains_list = c.option("-l"	,True,  True ,IN)
		clear	     = c.option("-c"	,False, False,IN)
		no_save	     = c.option("-no"	,False, False,IN)



		if("UserNeedsHelp" in [ cmnd, domain, no_save, workshop, all_domains, domains_list, clear]):
			GetGithub.help()
			return "UserNeedsHelp"
		elif(not workshop and TopG.CURRENT_WORKSHOP == "" and not no_save):
			pp("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
			return "NoWorkshopSetted"
		elif(c.segmentUrl(domain)["domain"]=="NoDomain" and not TopG.CURRENT_DOMAIN and not all_domains and not domains_list and not clear):
			pp("❌ Set a Domain or specify a domain with [-d <domain>] or in the beginning of the path.")
			return "NoDomainSetted"
		else:
			cw	 = TopG.CURRENT_WORKSHOP
			workshop = cw if not workshop else workshop

			if clear:
				result = GetGithubByDomain(workshop, '', False,clear)
				return result
			
			elif all_domains:
				if workshop and Workshop.exist(workshop):
					dmns = Domain.getAll(workshop)
					DMNS = []
					hosts= []
					for d in dmns:
						result = GetGithubByDomain(workshop,d.domain, False)
						DMNS.append(d.domain)
						host = domain_parts.extract(d.domain).domain + '.' + domain_parts.extract(d.domain).suffix
						if not (host in hosts):
							hosts.append(host)
					for h in hosts:
						if h not in DMNS:
							result = GetGithubByDomain(workshop,h, False)
				else:
					pp("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
					return "NoWorkshopSetted"
			elif domains_list:
				for d in domains_list:
					if c.segmentUrl(d)['domain'] != "NoDomain":
						result = GetGithubByDomain(workshop,d, False)
					else:
						pp(d+" is not a good domain")
			else:
				domain   = c.segmentUrl(domain)['domain'] if domain else TopG.CURRENT_DOMAIN
				result = GetGithubByDomain(workshop,domain, False)
	
			return result
	@staticmethod	
	def help():
		pp("""
	command: get github
	option			required	Description

	-d <domain>		  YES		insert a domain to search for github repos
						required when there is no domain setted

	-a			  NO		search for all the domains in a workshop
						in github

	-l [<domain>]		  NO		search for a list of domains in github

	-w <workshop>		  Y/N		select a workshop
						required when there is no workshop setted

	-c			  NO		clear the search history

	-no			  NO		do NOT save the ip address we got.
		""")


