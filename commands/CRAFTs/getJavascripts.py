from entities.workshop			import Workshop
from entities.domain			import Domain
from entities.path			import Path
from commands.CRUDs			import DRY as c
from get_assets.getUrlsBySession 	import GetUrlsBySession
import GlobalVars as TopG
from personalizedPrint import pp

class GetJavascripts:
	@staticmethod
	def execute(IN):
		IN	     = c.concat_getasset(IN)
		IN	     = c.short_command(IN,"js")
		cmnd	     = c.option("js",False, False,IN)
		workshop     = c.option("-w"   ,True,  False,IN)
		domain	     = c.option("-d"   ,True,  False,IN)
		no_save	     = c.option("-no"  ,False, False,IN)



		if("UserNeedsHelp" in [ cmnd, domain, no_save, workshop]):
			GetJavascript.help()
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
			
			#result = GetUrlsBySession(workshop,domain,no_save)
			result = GetUrlsBySession(workshop, domain, ["script"], False)
			#(workshop, domain, look_for=['all'], no_save=True)
			match result:
				case "error": pp("Can't get this domain's js files")
				case _  :		 pp("done")
	
			return result
	@staticmethod
	def help():
		pp("""
	command: get ip
	option			required	Description

	-d <domain>		  YES		insert a domain to get its javascripts
						required when there is no domain setted

	-w <workshop>		  Y/N		select a workshop to add the domain in it
						required when there is no workshop setted

	-no			  NO		do NOT save the js files we got.
		""")
