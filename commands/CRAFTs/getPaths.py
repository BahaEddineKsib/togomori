from entities.workshop			import Workshop
from entities.domain			import Domain
from entities.path			import Path
from commands.CRUDs			import DRY as c
from get_assets.getUrlsBySession 	import GetUrlsBySession
import GlobalVars as TopG
from personalizedPrint import pp

class GetPaths:
	@staticmethod
	def execute(IN):
		IN	     = c.concat_getasset(IN)
		IN	     = c.short_command(IN,"paths")
		cmnd	     = c.option("paths"	,False, False,IN)
		workshop     = c.option("-w"	,True,  False,IN)
		domain	     = c.option("-d"	,True,  False,IN)
		no_save	     = c.option("-no"	,False, False,IN)
		ig_list	     = c.option("-ig"	,True,  True ,IN)
		not_strict   = c.option("-ns"	,False, False,IN)



		if("UserNeedsHelp" in [ cmnd, domain, no_save, workshop, ig_list, not_strict]):
			GetPaths.help()
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

			if not ig_list:
				ig_list = []
				
			
			#result = GetUrlsBySession(workshop,domain,no_save)
			result = GetUrlsBySession(workshop, domain, ["all"], no_save, not not_strict, ig_list)
			#(workshop, domain, look_for=['all'], no_save=True, strict=True, ignore_those=[])
			match result:
				case "error": pp("Can't get this domain's paths")
				case _  :		 pp("done")
	
			return result
	@staticmethod
	def help():
		pp("""
	command: get paths
	option			required	Description

	-d <domain>		  YES		insert a domain to get its javascripts
						required when there is no domain setted

	-w <workshop>		  Y/N		select a workshop to add the domain in it
						required when there is no workshop setted

	-no			  NO		do NOT save the paths we got.

	-ig			  NO		give it a list of words/domains to ignore
						you can also give it the word disable , to 
						disable the default ignoring list
						
	-ns			  NO		ns for not stricted , it doesn't get only 
						the urls with the word you provide in the domain
						EX: default mode: for ex.com, it takes only urls
						with ex in it.
		""")
