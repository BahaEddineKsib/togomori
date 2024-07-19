from entities.workshop			import Workshop
from entities.domain			import Domain
from entities.path			import Path
from commands.CRUDs			import DRY as c
from get_assets.getSubDomainsbyHostname	import GetSubDomainsByHostname
import GlobalVars as TopG
from personalizedPrint import pp
import tldextract	 as domain_parts

#GetSubDomainsByHostname("workshop", "esprit-tn.com", True, by_wordlist=True)
class GetSubDomains:
	@staticmethod
	def execute(IN):
		IN	     = c.concat_getasset(IN)
		IN	     = c.short_command(IN,"subs")
		cmnd	     = c.option("subs"	,False, False,IN)
		workshop     = c.option("-w"	,True,  False,IN)
		domain	     = c.option("-d"	,True,  False,IN)
		all_domains  = c.option("-a"	,False, False,IN)
		domains_list = c.option("-l"	,True,  True ,IN)
		no_save	     = c.option("-no"	,False, False,IN)
		by_wordlist  = c.option("-W"	,False, False,IN)
		by_crt_sh    = c.option("-C"	,False, False,IN)



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

			if not by_wordlist and not by_crt_sh:
				by_wordlist = True

			if all_domains:
				if workshop and Workshop.exist(workshop):
					dmns = Domain.getAll(workshop)
					hosts= []
					for d in dmns:
						host = domain_parts.extract(d.domain).domain + '.' + domain_parts.extract(d.domain).suffix
						if not (host in hosts):
							hosts.append(host)
					for h in hosts:
						pp("SUBS OF "+h)
						result = GetSubDomainsByHostname(workshop,h, no_save, by_wordlist) 
				else:
					pp("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
					return "NoWorkshopSetted"
			elif domains_list:
				for d in domains_list:
					if c.segmentUrl(d)['domain'] != "NoDomain":
						result = GetUrlsBySession(workshop, d, no_save, by_wordlist)
					else:
						pp(d+" is not a good domain")
			else:
				domain   = c.segmentUrl(domain)['domain'] if domain else TopG.CURRENT_DOMAIN
				result = GetSubDomainsByHostname(workshop,domain,no_save, by_wordlist)

			match result:
				case {} : pp("No subdomains are found.")
				case _  : pp(result)
	
			return result
	@staticmethod
	def help():
		pp("""
	command: get subs
	option			required	Description

	-d <domain>		  YES		insert a domain to get its subdomains
						required when there is no domain setted

	-w <workshop>		  Y/N		select a workshop
						required when there is no workshop setted

	-W			  NO		scan by the wordlist

	-C			  NO		get subs from crt.sh

	-no			  NO		do NOT save the ip address we got.
		""")

