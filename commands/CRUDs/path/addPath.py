from entities.workshop import Workshop
from entities.domain   import Domain
from entities.path     import Path
from commands.CRUDs    import DRY as c
import GlobalVars as TopG


class AddPath:
	@staticmethod
	def execute(IN):
		IN         = c.short_command(IN,"ap")
		ap         = c.option("ap",           True, False,IN)
		domain     = c.option("-d",           True, False,IN)
		w_id       = c.option("-w",           True, False,IN)
		for_sure   = c.option("-s",           False,False,IN)
		


		if("UserNeedsHelp" in [ ap,domain,for_sure]):
			AddPath.help()
		elif(not w_id and TopG.CURRENT_WORKSHOP == ""):
			print("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
		elif(not domain and not c.segmentUrl(ap) and not TopG.CURRENT_DOMAIN):
			print("❌ Set a Domain or specify a domain with [-d <domain>] or in the beginning of the path.")
		else:
			domain = c.segmentUrl(ap)['domain'] if not domain else domain
			domain = TopG.CURRENT_DOMAIN	    if not domain else domain
			
			path   = ap if not c.segmentUrl(ap) else c.segmentUrl(ap)["path"]

			cw   = TopG.CURRENT_WORKSHOP
			w_id = cw if not w_id else w_id
			
			pth   = Path(domain = domain, path = path, variables = [])
			print("\npath:")
			pth.display()
			
			result = c.questionToExecute(for_sure,pth.save,{'workshop_id':w_id},"Save path ["+ap+"] ?")
			if(result == "WorkshopNotFound"):
				print("❌ Workshop ["+w_id+"] Not Found.")
			elif(result == "DomainNotFound"):
				print("❌ Domain ["+domain+"] Not Found.")
			elif(result == "PathExist"):
				print("❌ Path ["+path+"] Already Exist.")
			elif(result == "PathAdded"):
				print("✅ Path ["+path+"] is Added.")
	@staticmethod	
	def help():
		print("help -AddDomain")


