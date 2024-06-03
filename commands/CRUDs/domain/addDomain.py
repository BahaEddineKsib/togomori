from entities.workshop import Workshop
from entities.domain   import Domain
from commands.CRUDs    import DRY as c
import GlobalVars as TopG
from personalizedPrint import pp

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
			pp("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
			return "NoWorkshopSetted"
		elif(ports_map and not c.canBeMap(ports_map)):
			pp("❌Ports format: <[PORT_NAME]:[PORT]>")
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
			
			if not whois:  whois		= {} 
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
					whois		=whois,
					ip              =ip,
					ports           =ports_map,
					server_file     =server_file,
					robots_file     =robots_file,
					js_files        = js_files)
			dmn.display(toDisplay)
			result = c.questionToExecute( for_sure,dmn.save,{},"Save domain ["+domain+"] ?")
			if(result == "WorkshopNotFound"):
				pp("❌ Workshop ["+w_id+"] Not Found.")
				return "WorkshopNotFound"
			elif(result == "DomainExist"):
				pp("❌ Domain ["+domain+"] already exist.")
				return "DomainExist"
			elif(result == "DomainAdded"):
				pp("✅ Domain ["+domain+"] is Added.")
				return "DomainAdded"

	@staticmethod	
	def help():
		pp("""
	command: adddomain | addd | dd
	option			required	Description

	-d <domain>		  YES		New Domain 
						exemple: -d www.example.com

	-w <workshop>		  Y/N		select a workshop to add the domain in it
						required when there is no workshop setted

	--tag <[tags]>		  NO		Add a list of tags to add in the new domain
						exemple: --tag ex1 ex2 ex3 ex4

	--tech <[techs]>	  NO		Add a list of techs to add in the new domain
						exemple: --tech react bootstrap nodejs

	--whois <[COLUMN:VALUE]>  NO		Add a list of whois colums and its value to add to the new domain
						exemple: --whois admin_email:admin@m.com org:techCompany

	--ip <ip>		  NO		add an ip address to the new domain

	--port <[PORT:VALUE]>	  NO		Add a list of ports to add to the new domain
						exemple: --port http:443 ssh:22

	--robots <file_path>	  NO		Add a robots.txt file path

	--js <file_path>	  NO		Add a list of js file's paths

	-s			  NO		skip the saving question , and save changes
	""")


#TESTING COMMAND
#ad -d www.disc2.study -s --tag in-soup focus fromManual --tech react java --whois-file /whois/discord --ip 192.168.0.1 --port https:448 ssh:25 --server /nmap/scan --robots /disc/robots.txt --js /js1 /js2 /js3
