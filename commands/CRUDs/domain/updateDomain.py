from entities.workshop import Workshop
from entities.domain   import Domain
from commands.CRUDs    import DRY as c
import GlobalVars as TopG


class UpdateDomain:
	@staticmethod
	def execute(IN):
		IN         = c.short_command(IN,"ud")
		ud         = c.option("ud"	,True, False,IN)
		domain     = c.option("-d"	,True, False,IN)
		w_id       = c.option("-w"	,True, False,IN)
		new_w_id   = c.option("--w"	,True, False,IN)
		tags       = c.option("--tag"	,True, True, IN)
		techs      = c.option("--tech"	,True, True, IN)
		whois_file = c.option("--whois"	,True, False,IN)
		ip         = c.option("--ip"	,True, False,IN)
		ports_map  = c.option("--port"	,True, True, IN)
		server_file= c.option("--server",True, False,IN)
		robots_file= c.option("--robots",True, False,IN)
		js_files   = c.option("--js"	,True, True, IN)
		for_sure   = c.option("-s"	,False,False,IN)
		


		if("UserNeedsHelp" in [ ud,
					domain,
					for_sure,
					tags,
					techs,
					whois_file,
					ip,
					ports_map,
					server_file,
					robots_file,
					js_files,
					w_id,
					new_w_id]):
			AddDomain.help()
			return "UserNeedsHelp"

		elif(not w_id and TopG.CURRENT_WORKSHOP == ""):
			print("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
			return "NoWorkshopSetted"

		elif(ports_map and not c.canBeMap(ports_map, updating=True)):
			print("❌Ports format: <[PORT_NAME]:[PORT]>")
			return "WrongPortFormat"

		else:
			toDisplay  = []
			cw         = TopG.CURRENT_WORKSHOP
			if not w_id:        w_id        = cw 

	
			if not new_w_id:    new_w_id    = ""
			else: toDisplay.append("workshop_id")

			if not domain:      domain      = ""
			else: toDisplay.append("domain")

			if not tags:        tags        = [] 
			else: toDisplay.append("tags")
			
			if not techs:       techs       = [] 
			else: toDisplay.append("techs")
			
			if not whois_file:  whois_file  = "" 
			else: toDisplay.append("whois_file")
			
			if not ip:          ip          = "" 
			else: toDisplay.append("ip")
			
			if not ports_map:   ports_map   = {} 
			else: toDisplay.append("ports"); ports_map = c.listToMap(ports_map,updating=True)
			
			if not server_file: server_file = "" 
			else: toDisplay.append("server_file")
			
			if not robots_file: robots_file = "" 
			else: toDisplay.append("robots_file")
			
			if not js_files:    js_files    = [] 
			else: toDisplay.append("js_files")

			dmn   = Domain( workshop_id     =new_w_id,
					domain		=domain,
					tags            =tags,
					techs		=techs,
					whois_file      =whois_file,
					ip              =ip,
					ports		=ports_map,
					server_file     =server_file,
					robots_file	=robots_file,
					js_files	= js_files)
			dmn.display(toDisplay)
			result = c.questionToExecute(for_sure,Domain.update,{'domain':ud, 'workshop_id':w_id, 'new_dmn':dmn},"Update domain ["+ud+"] ?")
			if(result ==   "NewWorkshopNotFound"):
				print("❌ Workshop ["+new_w_id+"] Not Found.")
			elif(result == "OldWorkshopNotFound"):
				print("❌ Workshop ["+w_id+"] Not Found.")
			elif(result == "DomainNotFound"):
				print("❌ Domain ["+ud+"] Not Found.")
			elif(result == "DomainExist"):
				print("❌ Domain ["+domain+"] already exist.")
			elif(result == "DomainUpdated"):
				print("✅ Domain ["+ud+"] is Updated.")
			return result

	@staticmethod	
	def help():
		print("help -AddDomain")


