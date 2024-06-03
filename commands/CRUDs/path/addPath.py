from entities.workshop import Workshop
from entities.domain   import Domain
from entities.path     import Path
from commands.CRUDs    import DRY as c
import GlobalVars as TopG
from personalizedPrint import pp

class AddPath:
	@staticmethod
	def execute(IN):
		IN         = c.short_command(IN,"ap")
		ap         = c.option("ap"	,True, False,IN)
		domain     = c.option("-d"	,True, False,IN)
		tags       = c.option("--tag"	,True, True, IN)
		variables  = c.option("--var"	,True, True, IN)
		w_id       = c.option("-w"	,True, False,IN)
		for_sure   = c.option("-s"	,False,False,IN)



		if("UserNeedsHelp" in [ ap,domain, tags, for_sure]):
			AddPath.help()
			return "UserNeedsHelp"
		elif(not w_id and TopG.CURRENT_WORKSHOP == ""):
			pp("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
			return "NoWorkshopSetted"
		elif(not domain and c.segmentUrl(ap)["domain"]=="NoDomain" and not TopG.CURRENT_DOMAIN):
			pp("❌ Set a Domain or specify a domain with [-d <domain>] or in the beginning of the path.")
			return "NoDomainSetted"
		else:
			path   = c.segmentUrl(ap)["path"]
			if path == 'NoPath' or path == 'InvalidPath':
				pp("❌ Invalid Path. Path should contain at least one / and  start with /")
				return "InvalidPath"

			domain = c.segmentUrl(ap)['domain'] if not domain		else domain
			domain = TopG.CURRENT_DOMAIN	    if     domain == "NoDomain" else domain
			cw   = TopG.CURRENT_WORKSHOP
			w_id = cw if not w_id else w_id
			
			if not tags:
				tags = []
				very_expand = False
			else:
				very_expand = True

			if variables:
				variables = c.listToMap(variables, True)
			else:
				variables = c.segmentUrl(ap)['variables'] if c.segmentUrl(ap)['variables'] != 'NoVariables' else {}
			
			pth   = Path(domain = domain, path = path, tags=tags, variables=variables)

			pth.display(True,False,very_expand)
			
			result = c.questionToExecute(for_sure,pth.save,{'workshop_id':w_id},"Save path ["+ap+"] ?")
			if(result == "WorkshopNotFound"):
				pp("❌ Workshop ["+w_id+"] Not Found.")
			elif(result == "DomainNotFound"):
				pp("❌ Domain ["+domain+"] Not Found.")
			elif(result == "PathExist"):
				pp("❌ Path ["+path+"] Already Exist.")
			elif(result == "PathAdded"):
				pp("✅ Path ["+path+"] is Added.")
			return result



	@staticmethod	
	def help():
		pp("""
	command: addpath | addp | dp
	option			required	Description

	<path>			  YES		New path
						exemple: dp /path1/page.php
						Note: you can specify the domain and variables here 
						(dp www.ex.tn/path1/page.php?id=40)

	-d <domain>		  Y/N		specify a domain
						required when there is no domain setted

	-w <workshop>		  Y/N		select a workshop to add the domain in it
						required when there is no workshop setted

	--tag <[tags]>		  NO		Add a list of tags to add in the new domain
						exemple: --tag ex1 ex2 ex3 ex4

	--var <[variable:VALUE]>  NO		Add a list of variables and its value to add to the new path
						exemple: --var email:admin@m.com date:4-9-22

	-s			  NO		skip the saving question , and save changes
		""")
