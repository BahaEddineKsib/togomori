from entities.workshop import Workshop
from entities.domain   import Domain
from commands          import DRYFFC as c
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
		whois_file = c.option("--whois-file", True, False,IN)
		ip         = c.option("--ip",         True, False,IN)
		ports_map  = c.option("--port",       True, True, IN)
		server_file= c.option("--server-file",True, False,IN)
		robots_file= c.option("--robots-file",True, False,IN)
		js_files   = c.option("--js-file",    True, True, IN)
		for_sure   = c.option("-s",           False,False,IN)
		


		if("UserNeedsHelp" in [ ad,
					domain,
					for_sure,
					tags,
					techs,
					whois_file,
					ip,
					ports_map,
					server_file,
					robots_file,
					js_files] or (not domain)):
			AddDomain.help()
		elif(not w_id and TopG.CURRENT_WORKSHOP == ""):
			print("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
		elif(ports_map and not c.canBeMap(ports_map)):
			print("❌Ports format: <[PORT_NAME]:[PORT]>")
		else:
			cw         = TopG.CURRENT_WORKSHOP
			w_id       = cw if not w_id        else w_id
			tags       = [] if not tags        else tags
			techs      = [] if not techs       else techs
			whois_file = "" if not whois_file  else whois_file
			ip         = "" if not ip          else ip
			ports_map  = {} if not ports_map   else c.listToMap(ports_map)
			server_file= "" if not server_file else server_file
			robots_file= "" if not robots_file else robots_file
			js_files   = [] if not js_files    else js_files

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
			print("\ndomain:")
			dmn.display()
			result = c.questionToExecute(for_sure,dmn.save,{},"Save domain ["+domain+"] ?")
			if(result == "WorkshopNotFound"):
				print("❌ Workshop ["+w_id+"] Not Found.")
			elif(result == "DomainExist"):
				print("❌ Domain ["+domain+"] already exist.")
			elif(result == "DomainAdded"):
				print("✅ Domain ["+domain+"] is Added.")

	@staticmethod	
	def help():
		print("help -AddDomain")







#TESTING COMMAND
#ad -d www.disc.study -s --tag in-soup focus fromManual --tech react java --whois-file /whois/discord --ip 192.168.0.1 --port https:448 ssh:25 --server-file /nmap/scan --robots-file /disc/robots.txt --js-file /js1 /js2 /js3