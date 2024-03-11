from entities.workshop import Workshop
from entities.domain   import Domain
from entities.path     import Path
from commands.CRUDs    import DRY as c
import GlobalVars as TopG


class UpdatePath:
	@staticmethod
	def execute(IN):
		IN         = c.short_command(IN,"up")
		up         = c.option("up",     True, False,IN)
		domain     = c.option("-d",	True, False,IN)
		new_path   = c.option("--p",	True, False,IN)
		tags       = c.option("--tag",  True, True, IN)
		new_d	   = c.option("--d",	True, False,IN)
		w_id       = c.option("-w",     True, False,IN)
		for_sure   = c.option("-s",     False,False,IN)


		if("UserNeedsHelp" in [ up,domain, new_path, tags, new_d, w_id, for_sure]):
			AddPath.help()
			return "UserNeedsHelp"
		elif(not w_id and TopG.CURRENT_WORKSHOP == ""):
			print("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
			return "NoWorkshopSetted"
		elif(not domain and c.segmentUrl(up)["domain"]=="NoDomain" and not TopG.CURRENT_DOMAIN):
			print("❌ Set a Domain or specify a domain with [-d <domain>] or in the beginning of the path.")
			return "NoDomainSetted"
		else:
			path   = c.segmentUrl(up)["path"]
			if path == 'NoPath' or path == 'InvalidPath':
				print("❌ Invalid Path. Path should contain at least one / and  start with /")
				return "InvalidPath"

			if new_path:
				new_p = c.segmentUrl(new_path)["path"]
				d     = c.segmentUrl(new_path)["domain"]
				if new_p == 'NoPath' or new_p == "InvalidPath":
					print("❌ Invalid Path. Path should contain at least one / and  start with /")
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
			
			new_pth	= Path(domain = new_d, path = new_p, tags=tags)

			new_pth.display(True,False)
			
			result = c.questionToExecute(for_sure,Path.update,{'workshop_id':w_id,'domain':domain,'path':path,'new_pth':new_pth},"Update path ["+path+"] ?")
			if(result == "WorkshopNotFound"):
				print("❌ Workshop ["+w_id+"] Not Found.")
			elif(result == "DomainNotFound"):
				print("❌ Domain ["+domain+"] Not Found.")
			elif(result == "PathNotFound"):
				print("❌ path ["+path+"] Not Found")
			elif(result == "NewPathExist"):
				print("❌ Path ["+new_p+"] Already Exist.")
			elif(result == "NewDomainNotFound"):
				print("❌ domain ["+new_d+"] Not Found.")
			elif(result == "PathUpdated"):
				print("✅ Path ["+path+"] is Updated.")
			return result



	@staticmethod	
	def help():
		print("help -AddDomain")


