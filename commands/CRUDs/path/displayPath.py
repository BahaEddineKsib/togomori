from entities.workshop import Workshop
from entities.domain   import Domain
from entities.path     import Path
from commands.CRUDs    import DRY as c
import GlobalVars as gv


class DisplayPath:
	@staticmethod
	def execute(IN):
		IN		= c.short_command(IN,"dp")
		dp		= c.option("dp",      False,False,IN)
		path		= c.option("-p",      True, False,IN)
		domain		= c.option("-d",      True, False,IN)
		w_id		= c.option("-w",      True, False,IN)
		all_in_domain   = c.option("-a",      False,False,IN)
		all_in_workshop = c.option("-A",      False,False,IN)
		select          = c.option("--select",False,False,IN)


		if("UserNeedsHelp" in [ dp,domain,path,w_id, all_in_domain,all_in_workshop] or (not path and not all_in_domain and not all_in_workshop) ):
			DisplayPath.help()
			return "UserNeedsHelp"
		elif(not w_id and gv.CURRENT_WORKSHOP == ""):
			print("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
			return "NoWorkshopSetted"
		elif(not domain and c.segmentUrl(path)["domain"] == "NoDomain" and not gv.CURRENT_DOMAIN and not all_in_workshop):
			print("❌ Set a Domain or specify a domain with [-d <domain>] or in the beginning of the path.")
			return "NoDomainSetted"
		else:
			cw   = gv.CURRENT_WORKSHOP
			w_id = cw if not w_id else w_id

			if not Workshop.exist(w_id):
				print("❌ Workshop ["+w_id+"] Not Found.")
				return"WorkshopNotFound"

			if(all_in_workshop):
				pp = []
				paths = Path.getAll(w_id)
				for p in paths:
					p.display(select)
					pp.append(p.path)
				return pp
			
			domain = c.segmentUrl(path)['domain']	if not domain		  else domain
			domain = gv.CURRENT_DOMAIN		if     domain=="NoDomain" else domain

			if not Domain.exist(w_id,domain):
				print("❌ Domain ["+domain+"] Not Found.")
				return   "DomainNotFound"
			if(all_in_domain):
				pp = []
				paths = Path.getByDomain(domain, w_id)
				for p in paths:
					p.display(select)
					pp.append(p.path)
				return pp

			path   = c.segmentUrl(path)["path"]
			if path == 'InvalidPath':
				print("❌ Invalid Path. Path should contain at least one / and  start with /")
				return "InvalidPath"
			if(path == "NoPath"):
				print("❌ No Path entered.")
				return "NoPath"
			
			if not Path.exist(w_id,domain,path):
				print("❌ Path ["+path+"] Not Found.")
				return "PathNotFound"
			else:
				pth = Path.get(w_id,domain,path)
				pth.display(select)
				return pth.path


			
	@staticmethod
	def help():
		print("help -AddDomain")


