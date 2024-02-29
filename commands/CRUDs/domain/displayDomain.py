from entities.workshop import Workshop
from entities.domain   import Domain
from commands.CRUDs    import DRY as c
import GlobalVars as TopG


class DisplayDomain:
	@staticmethod
	def execute(IN):
		IN         = c.short_command(IN,"dd")
		ad         = c.option("dd",      False,False,IN)
		domain     = c.option("-d",      True, False,IN)
		sub	   = c.option("--sub",   True, False,IN)
		main       = c.option("--main",  True, False,IN)
		tld        = c.option("--tld",   True, False,IN)
		w_id       = c.option("-w",      True, False,IN)
		tags       = c.option("--tag",   True, True, IN)
		techs      = c.option("--tech",  True, True, IN)
		whois_file = c.option("--whois", True, False,IN)
		ip         = c.option("--ip",    True, False,IN)
		ports_map  = c.option("--port",  True, True, IN)
		server_file= c.option("--server",True, False,IN)
		robots_file= c.option("--robots",True, False,IN)
		js_files   = c.option("--js",	 True, True, IN)
		show       = c.option("--show",  True, True, IN)
		expand     = c.option("-x",	 False,False,IN)
		all        = c.option("-A",      False,False,IN)


		if("UserNeedsHelp" in [ ad,
					domain,
					w_id,
					tags,
					techs,
					whois_file,
					ip,
					ports_map,
					server_file,
					robots_file,
					js_files,
					show,
					all] or (not domain and not all)):
			DisplayDomain.help()
			return "UserNeedsHelp"

		elif(not w_id and TopG.CURRENT_WORKSHOP == ""):
			print("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
			return "NoWorkshopSetted"
		elif(ports_map and not c.canBeMap(ports_map)):
			print("❌Ports format: <[PORT_NAME]:[PORT]>")
			return"WrongPortFormat"
		else:
			show       = [] if not show else show
			show.append("domain")
			cw         = TopG.CURRENT_WORKSHOP
			if not w_id:        w_id        = cw 
			if not sub:	    sub         = ""
			if not main:	    main        = ""
			if not tld:	    tld         = ""
			if not tags:        tags        = [] 
			if not techs:       techs       = [] 
			if not whois_file:  whois_file  = "" 
			if not ip:          ip          = "" 
			if not ports_map:   ports_map   = {} 
			if not server_file: server_file = "" 
			if not robots_file: robots_file = "" 
			if not js_files:    js_files    = [] 
			
			dmn   = Domain( workshop_id     =w_id,
					domain		=domain,
					tags            =tags,
					techs		=techs,
					whois_file      =whois_file,
					ip              =ip,
					ports		=ports_map,
					server_file     =server_file,
					robots_file	=robots_file,
					js_files	= js_files)
			wrk = Workshop.search(w_id)
			if(wrk == "WorkshopNotFound"):
				print("❌ Workshop ["+w_id+"] Not Found.")
				return "WorkshopNotFound"

			if(all):
				domainsList = Domain.getDomainsByWorkshop(wrk)
				
				domainsList = Domain.searchBy(  workshop_id=w_id,
								domain     =domain,
								sub        =sub,
								main       =main,
								tld	   =tld,
								tags	   =tags,
								techs      =techs,
								whois_file =whois_file,
								ip	   =ip,
								ports	   =ports_map,
								server_file=server_file,
								robots_file=robots_file,
								js_files   = js_files)
				dd = []
				for d in domainsList:
					d.display(show,expand)
					dd.append(d.domain)
				return dd
			elif(domain):
				d = Domain.searchInWorkshop(domain,wrk)
				if d == "DomainNotFound":
					print("No Domain have the name ["+domain+"] in workshop ["+w_id+"]")
					return "DomainNotFound"
				else:
					d.display(show,expand)
					return d.domain
				


	@staticmethod	
	def help():
		print("help -DisplayDomain")



