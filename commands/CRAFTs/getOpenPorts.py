from entities.workshop			import Workshop
from entities.domain			import Domain
from entities.path			import Path
from commands.CRUDs			import DRY as c
from get_assets.getOpenPortsByDomain	 	import GetOpenPortsByDomain 
import GlobalVars as TopG


#GetIpByDomain('workshop', 'google.com', 'no_save', False, False, [], [1,1000])
class GetOpenPorts:
	@staticmethod
	def execute(IN):
		IN	     = c.concat_getasset(IN)
		IN	     = c.short_command(IN,"ports")
		cmnd	     = c.option("ports"	    ,False, False,IN)
		workshop     = c.option("-w"	    ,True,  False,IN)
		domain	     = c.option("-d"	    ,True,  False,IN)
		top_20	     = c.option("--t20"	    ,False, False,IN)
		top_web	     = c.option("--tweb"    ,False,False ,IN)
		by_ports     = c.option("-p"	    ,True, True  ,IN)
		interval     = c.option("--interval",True, True  ,IN)
		no_save	     = c.option("-no"	    ,False, False,IN)



		if("UserNeedsHelp" in [ cmnd, 
					domain, 
					no_save, 
					workshop,
					top_20,
					top_web,
					by_ports,
					interval]):
			GetOpenPorts.help()
			return "UserNeedsHelp"
		elif(not workshop and TopG.CURRENT_WORKSHOP == "" and not no_save):
			print("❌ Set a Workshop or specify a workshop with [-w <workshop id>]")
			return "NoWorkshopSetted"
		elif(c.segmentUrl(domain)["domain"]=="NoDomain" and not TopG.CURRENT_DOMAIN):
			print("❌ Set a Domain or specify a domain with [-d <domain>] or in the beginning of the path.")
			return "NoDomainSetted"
		elif(interval):
			if(len(interval) != 2):
				print("❌ interval is wrong")
				return "WrongInterval"
			if not c.canBeNumber(interval[0]) or not c.canBeNumber(interval[1]):
				print("❌ interval is wrong")
				return "WrongInterval"
			else:
				interval[0] = int(interval[0])
				interval[1] = int(interval[1])
			if interval[0]>= interval[1]:
				print("❌ interval is wrong")
				return "WrongInterval"
		elif(by_ports):
			for p in range(0,len(by_ports)):
				if not c.canBeNumber(by_ports[p]):
					print("❌ port is wrong")
					return "WrongPort"
				else:
					by_ports[p] = int(by_ports[p])


		domain   = c.segmentUrl(domain)['domain'] if domain else TopG.CURRENT_DOMAIN
		cw	 = TopG.CURRENT_WORKSHOP
		workshop = cw if not workshop else workshop

		result = GetOpenPortsByDomain(workshop, domain, no_save, top_20, top_web, by_ports, interval)
		match result:
			case "NoIp": print("Can't get this domain's ip")
			case _  :		 print(result)
	
		return result




	@staticmethod
	def help():
		print("""
	command: get ports
	option			required	Description

	-d <domain>		  YES		insert a domain to get its ip address
						required when there is no domain setted

	-w <workshop>		  Y/N		select a workshop to add the domain in it
						required when there is no workshop setted

	--t20			  NO		scan the top 20 scanned ports

	--tweb			  NO		scan the top scanned ports for web applications

	-p			  NO		specify a one or list of ports to scan

	--interval		  NO		specify an interval of ports to scan

	-no			  NO		do NOT save the ip address we got.
		""")

#GetIpByDomain('workshop', 'google.com', 'no_save', False, False, [], [1,1000])
