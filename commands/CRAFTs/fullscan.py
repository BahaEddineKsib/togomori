from commands.CRAFTs.getTechs		import GetTechs
from commands.CRAFTs.getWhois		import GetWhois
from commands.CRAFTs.getIp	        import GetIp
from commands.CRAFTs.getOpenPorts       import GetOpenPorts
from commands.CRAFTs.getSubDomains      import GetSubDomains
from commands.CRAFTs.getJavascripts     import GetJavascripts
from commands.CRAFTs.getPaths		import GetPaths
from commands.CRAFTs.getRobotsTxt	import GetRobotsTxt
from commands.CRAFTs.getGithub		import GetGithub
from commands.help			import Help
from commands.CRUDs			import DRY as c
from personalizedPrint			import clear
from personalizedPrint			import pp
from entities.workshop			import Workshop
from entities.domain			import Domain
from entities.path			import Path
import GlobalVars as TopG
import time

class Fullscan:
	@staticmethod
	def execute(IN):
		IN	= c.short_command(IN,"fs")
		cmnd	= c.option("fs", False, False, IN)
		workshop= c.option("-w", True , False, IN)
		domain  = c.option("-d", True , False, IN)
		
		workshop = "-w "+workshop if workshop else ""
		domain   = "-d "+domain   if domain   else ""
		msgs=[]
		msgs.append("Scanning Sub domains...")
		Fullscan.say_it(msgs)
		subs = GetSubDomains.execute("get subs "+workshop+" "+domain)

		msgs.append("☑ scan done: sub domains")
		Fullscan.say_it(msgs)

		for k in subs.keys():
			msgs.append("Scanning "+k+" paths")
			Fullscan.say_it(msgs)
			scan_url = GetPaths.execute("get paths "+workshop+" -d "+k)
		msgs.append("☑ scan done: domain's paths")
		Fullscan.say_it(msgs)
		for k in subs.keys():
			msgs.append("Scanning "+k+" open ports")
			Fullscan.say_it(msgs)
			scan_url = GetOpenPorts.execute("get ports "+workshop+" -d "+k)
		msgs.append("☑ scan done: domain's open ports")
		Fullscan.say_it(msgs)
		
		for k in subs.keys():
			msgs.append("Scanning Robots.txt: "+k)
			Fullscan.say_it(msgs)
			scan_robots = GetRobotsTxt.execute("get robots "+workshop+" -d "+k)
		msgs.append("☑ scan done: Robots.txt")
		Fullscan.say_it(msgs)
		
		for k in subs.keys():
			msgs.append("Scanning IP address: "+k)
			Fullscan.say_it(msgs)
			scan_robots = GetIp.execute("get ip "+workshop+" -d "+k)
		msgs.append("☑ scan done: IP addresses")
		Fullscan.say_it(msgs)

		msgs.append("Scanning WHOIS server")
		Fullscan.say_it(msgs)
		scan_robots = GetWhois.execute("get whois "+workshop+" -a")
		msgs.append("☑ scan done: Whois")
		Fullscan.say_it(msgs)

		msgs.append("Scanning Github Repositories: ")
		Fullscan.say_it(msgs)
		scan_robots = GetGithub.execute("get github "+workshop+" -a")
		msgs.append("☑ scan done: Github search")
		Fullscan.say_it(msgs)



	def say_it(msgs):
		clear()
		for msg in msgs:
			pp(msg)
		


		
