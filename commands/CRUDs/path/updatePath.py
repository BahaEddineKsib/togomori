from entities.workshop import Workshop
from entities.domain   import Domain
from entities.path     import Path
from commands.CRUDs    import DRY as c
import GlobalVars as TopG
from personalizedPrint import pp

class UpdatePath:
	@staticmethod
	def execute(IN):
		IN         = c.short_command(IN,"up")
		up         = c.option("up",     True, False,IN)
		domain     = c.option("-d",	True, False,IN)
		new_path   = c.option("-p",	True, False,IN)
		tags       = c.option("--tag",  True, True, IN)
		variables  = c.option("--var",  True, True, IN)
		new_d	   = c.option("-D",	True, False,IN)
		w_id       = c.option("-w",     True, False,IN)
		for_sure   = c.option("-s",     False,False,IN)


		if("UserNeedsHelp" in [ up,domain, new_path, tags, variables, new_d, w_id, for_sure]):
			AddPath.help()
			return "UserNeedsHelp"
		elif(not w_id and TopG.CURRENT_WORKSHOP == ""):
			pp("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
			return "NoWorkshopSetted"
		elif(not domain and c.segmentUrl(up)["domain"]=="NoDomain" and not TopG.CURRENT_DOMAIN):
			pp("❌ Set a Domain or specify a domain with [-d <domain>] or in the beginning of the path.")
			return "NoDomainSetted"
		else:
			path   = c.segmentUrl(up)["path"]
			if path == 'NoPath' or path == 'InvalidPath':
				pp("❌ Invalid Path. Path should contain at least one / and  start with /")
				return "InvalidPath"

			if new_path:
				new_p = c.segmentUrl(new_path)["path"]
				d     = c.segmentUrl(new_path)["domain"]
				if new_p == 'NoPath' or new_p == "InvalidPath":
					pp("❌ Invalid Path. Path should contain at least one / and  start with /")
					return "InvalidPath"
				elif not new_d and d != 'NoDomain' :
					new_d = d
			else:
				new_p = ""
			
			new_d	= new_d if new_d else ""
			domain	= c.segmentUrl(up)['domain'] if not domain		else domain
			domain	= TopG.CURRENT_DOMAIN	    if     domain == "NoDomain" else domain
			cw	= TopG.CURRENT_WORKSHOP
			w_id	= cw if not w_id else w_id

			if variables:
				variables = c.listToMap(variables, True)
			else:
				variables = c.segmentUrl(new_path)['variables'] if c.segmentUrl(new_path)['variables'] != 'NoVariables' else {}

			new_pth	= Path(domain = new_d, path = new_p, tags=tags, variables=variables)

			new_pth.display(True,False)
			
			result = c.questionToExecute(for_sure,Path.update,{'workshop_id':w_id,'domain':domain,'path':path,'new_pth':new_pth},"Update path ["+path+"] ?")
			if(result == "WorkshopNotFound"):
				pp("❌ Workshop ["+w_id+"] Not Found.")
			elif(result == "DomainNotFound"):
				pp("❌ Domain ["+domain+"] Not Found.")
			elif(result == "PathNotFound"):
				pp("❌ path ["+path+"] Not Found")
			elif(result == "NewPathExist"):
				pp("❌ Path ["+new_p+"] Already Exist.")
			elif(result == "NewDomainNotFound"):
				pp("❌ domain ["+new_d+"] Not Found.")
			elif(result == "PathUpdated"):
				pp("✅ Path ["+path+"] is Updated.")
			return result



	@staticmethod	
	def help():
		pp("""
	command: updatepath | updatep | up
	option			required	Description

	<path>			  YES		select a path to update
						exemple: up /path1/page.php
						Note: you can specify the domain here
						(up www.ex.tn/path1/page.php)

	-d <domain>		  Y/N		specify a domain
						required when there is no domain setted

	-w <workshop>		  Y/N		select a workshop to add the domain in it
						required when there is no workshop setted

	-p <path>		  NO		insert a new url link

	-D <domain>		  NO		insert a new domain

	--tag  <[tags]>		  NO		Update tags (ERASE all the old tags and replace it with new list.)
	     + <[tags]>				adding + before the tags list will add to the already existed tags
	     - <[tags]>				adding _ before the tags list will remove the tags you listed if they exist
						exemple: --tag + ex1 ex2 ex3 ex4

	--var <[variable:VALUE]>  NO		Update variables (ERASE all the old variables and replace it with new list)
	     +<[variable:VALUE]>		adding + before the variables list will add to the already existed variables
	     -<[variable:VALUE]>		adding _ before the variables list will remove the variables you listed if they exist
						exemple: --var _ email:admin@m.com date:4-9-22

	-s			  NO		skip the saving question , and save changes
	""")
