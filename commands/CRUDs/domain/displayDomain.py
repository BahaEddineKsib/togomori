from entities.workshop import Workshop
from entities.domain   import Domain
from commands          import DRYFFC as c
import GlobalVars as TopG


class DisplayDomain:
	@staticmethod
	def execute(IN):
		IN         = c.short_command(IN,"dd")
		ad         = c.option("dd",           False,False,IN)
		domain     = c.option("-d",           True, False,IN)
		w_id       = c.option("-w",           True, False,IN)
		tags       = c.option("--tag",        True, True, IN)
		techs      = c.option("--tech",       True, True, IN)
		whois_file = c.option("--whois-file", True, False,IN)
		ip         = c.option("--ip",         True, False,IN)
		ports_map  = c.option("--port",       True, True, IN)
		server_file= c.option("--server-file",True, False,IN)
		robots_file= c.option("--robots-file",True, False,IN)
		js_files   = c.option("--js-file",    True, True, IN)
		show       = c.option("--show",       True, True, IN)
		all        = c.option("-a",           False,False,IN)


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
			AddDomain.help()
		elif(not w_id and TopG.CURRENT_WORKSHOP == ""):
			print("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
		elif(ports_map and not c.canBeMap(ports_map)):
			print("❌Ports format: <[PORT_NAME]:[PORT]>")
		else:
			toDisplay  = ["domain_text"]
			show       = [] if not show else show
			
			cw         = TopG.CURRENT_WORKSHOP
			if not w_id:        w_id        = cw 
			else:toDisplay.append("workshop_id")
			if "workshop_id" in  show:toDisplay.append("workshop_id")

			
			if not tags:        tags        = [] 
			else:toDisplay.append("tags")
			if "tags" in  show:toDisplay.append("tags")

			
			if not techs:       techs       = [] 
			else:toDisplay.append("techs_list")
			if "techs_list" in  show:toDisplay.append("techs_list")

			
			if not whois_file:  whois_file  = "" 
			else:toDisplay.append("whois_file")
			if "whois_file" in  show:toDisplay.append("whois_file")

			
			if not ip:          ip          = "" 
			else:toDisplay.append("ip")
			if "ip" in  show:toDisplay.append("ip")

			
			if not ports_map:   ports_map   = {} 
			else:toDisplay.append("ports_map"); ports_map = c.listToMap(ports_map)
			if "ports_map " in  show:toDisplay.append("ports_map")

			
			if not server_file: server_file = "" 
			else:toDisplay.append("server_file")
			if "server_file" in  show:toDisplay.append("server_file")

			
			if not robots_file: robots_file = "" 
			else:toDisplay.append("robots_txt_file")
			if "robots_txt_file" in  show:toDisplay.append("robots_txt_file")

			
			if not js_files:    js_files    = [] 
			else:toDisplay.append("js_files_list")
			if "js_files_list" in  show:toDisplay.append("js_files_list")


			dmn   = Domain( workshop_id     =w_id,
					domain_text     =domain,
					tags            =tags,
					techs_list      =techs,
					whois_file      =whois_file,
					ip              =ip,
					ports_map       =ports_map,
					server_file     =server_file,
					robots_txt_file =robots_file,
					js_files_list   = js_files)
			if(all):
				wrk = Workshop.search(w_id)
				if(wrk == "WorkshopNotFound"):
					print("❌ Workshop ["+w_id+"] Not Found.")
				else:
					domainsList = Domain.getDomainsByWorkshop(wrk)
					
					domainsList = Domain.searchBy(  workshop_id     =w_id,
									domain_text     =domain,
									tags            =tags,
									techs_list      =techs,
									whois_file      =whois_file,
									ip              =ip,
									ports_map       =ports_map,
									server_file     =server_file,
									robots_txt_file =robots_file,
									js_files_list   = js_files)
					for d in domainsList:
						d.display(toDisplay)

	@staticmethod	
	def help():
		print("help -AddDomain")



