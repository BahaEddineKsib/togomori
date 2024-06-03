from entities.workshop import Workshop
from entities.domain   import Domain
from commands.CRUDs    import DRY as c
import GlobalVars as gv
from personalizedPrint import pp

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
		whois = c.option("--whois", True, False,IN)
		ip         = c.option("--ip",    True, False,IN)
		ports_map  = c.option("--port",  True, True, IN)
		server_file= c.option("--server",True, False,IN)
		robots_file= c.option("--robots",True, False,IN)
		js_files   = c.option("--js",	 True, True, IN)
		show       = c.option("--show",  True, True, IN)
		expand     = c.option("-x",	 False,False,IN)
		ALL        = c.option("-A",      False,False,IN)


		if("UserNeedsHelp" in [ ad,
					domain,
					w_id,
					tags,
					techs,
					whois,
					ip,
					ports_map,
					server_file,
					robots_file,
					js_files,
					show,
					ALL] or (not domain and not ALL)):
			DisplayDomain.help()
			return "UserNeedsHelp"

		elif(not w_id and gv.CURRENT_WORKSHOP == ""):
			pp("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
			return "NoWorkshopSetted"
		elif(ports_map and not c.canBeMap(ports_map)):
			pp("❌Ports format: <[PORT_NAME]:[PORT]>")
			return"WrongPortFormat"
		else:
			show       = [] if not show else show
			show.append("domain")
			cw         = gv.CURRENT_WORKSHOP
			if not w_id:        w_id        = cw 
			if not sub:	    sub         = ""
			if not main:	    main        = ""
			if not tld:	    tld         = ""
			if not tags:        tags        = [] 
			if not techs:       techs       = [] 
			if not whois:  whois		= {}
			if not ip:          ip          = "" 
			if not ports_map:   ports_map   = {} 
			if not server_file: server_file = "" 
			if not robots_file: robots_file = "" 
			if not js_files:    js_files    = [] 
			
			dmn   = Domain( workshop_id     =w_id,
					domain		=domain,
					tags            =tags,
					techs		=techs,
					whois		=whois,
					ip              =ip,
					ports		=ports_map,
					server_file     =server_file,
					robots_file	=robots_file,
					js_files	= js_files)
			if(not Workshop.exist(w_id)):
				pp("❌ Workshop ["+w_id+"] Not Found.")
				return "WorkshopNotFound"

			if(ALL):
				domainsList = Domain.searchBy(  workshop_id=w_id,
								domain     =domain,
								sub        =sub,
								main       =main,
								tld	   =tld,
								tags	   =tags,
								techs      =techs,
								whois      =whois,
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
				if not Domain.exist(w_id,domain):
					pp("No Domain have the name ["+domain+"] in workshop ["+w_id+"]")
					return "DomainNotFound"
				else:
					d = Domain.get(w_id,domain)
					d.display(show,expand)
					return d.domain
				


	@staticmethod
	def help():
		pp("""
	command: displaydomain | displayd | dd
	option			required	Description

	-d <domain>		  Y/N		Select a domain to display
						required when -A option is absent

	-A			  Y/N		Display all the domains in a workshop
						required when -d option id absent

	--show <[VARs]>		  NO		Choose variables to display. variables are:
						[domain, tag, tech, ip, port, robots, js, whois, ALL]
						exemple: --show whois port
						note: the variable ALL , means display all the variables

	-x			  NO		Expand the display

	-w <workshop>		  Y/N		select a workshop
						required when there is no workshop setted

	--tag <[tags]>		  NO		Search by a list of tags to add in the new domain
						exemple: --tag ex1 ex2 ex3 ex4

	--tech <[techs]>	  NO		Search by a list of techs to add in the new domain
						exemple: --tech react bootstrap nodejs

	--whois <[COLUMN:VALUE]>  NO		Search by a list of whois colums and its value to add to the new domain
						exemple: --whois admin_email:admin@m.com org:techCompany

	--ip <ip>		  NO		Search by an ip address to the new domain

	--port <[PORT:VALUE]>	  NO		Search by a list of ports to add to the new domain
						exemple: --port http:443 ssh:22

	--robots <file_path>	  NO		Search by a robots.txt file path

	--js <file_path>	  NO		Search by a list of js file's paths

	""")


