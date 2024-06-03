from entities.workshop import Workshop
from entities.domain   import Domain
from commands.CRUDs    import DRY as c
import GlobalVars as TopG
from personalizedPrint import pp

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
		whois = c.option("--whois"	,True, False,IN)
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
					whois,
					ip,
					ports_map,
					server_file,
					robots_file,
					js_files,
					w_id,
					new_w_id]):
			UpdateDomain.help()
			return "UserNeedsHelp"

		elif(not w_id and TopG.CURRENT_WORKSHOP == ""):
			pp("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
			return "NoWorkshopSetted"

		elif(ports_map and not c.canBeMap(ports_map, updating=True)):
			pp("❌Ports format: <[PORT_NAME]:[PORT]>")
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
			
			if not whois:  whois  = "" 
			else: toDisplay.append("whois")
			
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
					whois      =whois,
					ip              =ip,
					ports		=ports_map,
					server_file     =server_file,
					robots_file	=robots_file,
					js_files	= js_files)
			dmn.display(toDisplay)
			result = c.questionToExecute(for_sure,Domain.update,{'domain':ud, 'workshop_id':w_id, 'new_dmn':dmn},"Update domain ["+ud+"] ?")
			if(result ==   "NewWorkshopNotFound"):
				pp("❌ Workshop ["+new_w_id+"] Not Found.")
			elif(result == "OldWorkshopNotFound"):
				pp("❌ Workshop ["+w_id+"] Not Found.")
			elif(result == "DomainNotFound"):
				pp("❌ Domain ["+ud+"] Not Found.")
			elif(result == "DomainExist"):
				pp("❌ Domain ["+domain+"] already exist.")
			elif(result == "DomainUpdated"):
				pp("✅ Domain ["+ud+"] is Updated.")
			return result

	@staticmethod
	def help():
		pp("""
	command: updatedomain | updated | ud
	option			required	Description
	
	<domain>		  YES		Select a domain to update
						exemple: ud www.exemple.com

	-d <domain>		  YES		Insert a New Domain
						exemple: -d www.example_updated.com

	-w <workshop>		  Y/N		Select a workshop which the domain exist
						required when there is no workshop setted

	--tag   <[tags]>	  NO		Update tags. ( ERASE all the old tags and replace it with the new list.)
	      + <[tags]>			adding + before the tags list will add tags to the already existed tags 
	      _ <[tags]>			adding _ before the tags list will remove the tags you listed if they exist
						exemple: --tag _ tag1 tag2 tag3

	--tech   <[techs]>	  NO		Update technologies.( ERASE all the old techs and replace it with the new list.)
	       + <[techs]>			adding + before the techs list will add tags to the already existed tags
	       _ <[techs]>			adding _ before the techs list will remove the tags you listed if they exist
						exemple: --tech + react bootstrap nodejs

	--whois  <[COLUMN:VALUE]> NO		Update whois columns. (ERASE all the columns and replace them with your input)
	       + <[COLUMN:VALUE]>		adding + before the whois columns will add columns to the already existed columns
	       _ <[COLUMN:VALUE]>		adding _ before the column:value list will remove the columns you listed if they exist
						exemple: --whois + admin_email:admin@m.com org:techCompany

	--ip <ip>		  NO		Update the ip address

	--port   <[PORT:VALUE]>	  NO		Update the ports ( ERASE all the old ports and replace it with the new list.)
	       + <[PORT:VALUE]>			adding + before the ports list will add ports to the already existed ports
	       _ <[PORT:VALUE]>			adding _ before the ports list will remove the ports you listed if they exist
						exemple: --port http:443 ssh:22

	--robots <file_path>	  NO		Update the robots.txt file path

	--js <[file_path]>	  NO		Update the list of js file's paths (-/+)

	-s			  NO		skip the saving question , and save changes
	""")
