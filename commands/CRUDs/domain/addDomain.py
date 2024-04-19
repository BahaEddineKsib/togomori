from entities.workshop import Workshop
from entities.domain   import Domain
from commands.CRUDs    import DRY as c
import GlobalVars as TopG


class AddDomain:
	@staticmethod
	def execute(IN):
		IN         = c.short_command(IN,"ad")
		ad         = c.option("ad",           False,False,IN)
		domain     = c.option("-d",           True, False,IN)
		w_id       = c.option("-w",           True, False,IN)
		tags       = c.option("--tag",        True, True, IN)
		techs      = c.option("--tech",       True, True, IN)
		whois = c.option("--whois",      True, False,IN)
		ip         = c.option("--ip",         True, False,IN)
		ports_map  = c.option("--port",       True, True, IN)
		server_file= c.option("--server",     True, False,IN)
		robots_file= c.option("--robots",     True, False,IN)
		js_files   = c.option("--js",         True, True, IN)
		for_sure   = c.option("-s",           False,False,IN)
		


		if("UserNeedsHelp" in [ ad,
					domain,
					for_sure,
					tags,
					techs,
					whois,
					ip,
					ports_map,
					server_file,
					robots_file,
					js_files,
					w_id] or (not domain)):
			AddDomain.help()
			return "UserNeedsHelp"
		elif(not w_id and TopG.CURRENT_WORKSHOP == ""):
			print("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
			return "NoWorkshopSetted"
		elif(ports_map and not c.canBeMap(ports_map)):
			print("❌Ports format: <[PORT_NAME]:[PORT]>")
			return "WrongPortFormat"
		else:
			toDisplay  = ["domain"]
			cw         = TopG.CURRENT_WORKSHOP
			if not w_id:        w_id        = cw 
			else: toDisplay.append("workshop_id")
			
			if not tags:        tags        = [] 
			else: toDisplay.append("tags")
			
			if not techs:       techs       = [] 
			else: toDisplay.append("techs")
			
			if not whois:  whois  = "" 
			else: toDisplay.append("whois")
			
			if not ip:          ip          = "" 
			else: toDisplay.append("ip")
			
			if not ports_map:   ports_map   = {} 
			else: toDisplay.append("ports"); ports_map = c.listToMap(ports_map)
			
			if not server_file: server_file = "" 
			else: toDisplay.append("server_file")
			
			if not robots_file: robots_file = "" 
			else: toDisplay.append("robots_file")
			
			if not js_files:    js_files    = [] 
			else: toDisplay.append("js_files")

			dmn   = Domain( workshop_id     =w_id,
					domain          =domain,
					tags            =tags,
					techs           =techs,
					whois      =whois,
					ip              =ip,
					ports           =ports_map,
					server_file     =server_file,
					robots_file     =robots_file,
					js_files        = js_files)
			dmn.display(toDisplay)
			result = c.questionToExecute( for_sure,dmn.save,{},"Save domain ["+domain+"] ?")
			if(result == "WorkshopNotFound"):
				print("❌ Workshop ["+w_id+"] Not Found.")
				return "WorkshopNotFound"
			elif(result == "DomainExist"):
				print("❌ Domain ["+domain+"] already exist.")
				return "DomainExist"
			elif(result == "DomainAdded"):
				print("✅ Domain ["+domain+"] is Added.")
				return "DomainAdded"

	@staticmethod	
	def help():
		print("help -AddDomain")




#TESTING COMMAND
#ad -d www.disc2.study -s --tag in-soup focus fromManual --tech react java --whois-file /whois/discord --ip 192.168.0.1 --port https:448 ssh:25 --server /nmap/scan --robots /disc/robots.txt --js /js1 /js2 /js3
