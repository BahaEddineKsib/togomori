import threading
from flask import Flask, request
from flask_cors import CORS
import os
import subprocess
import json
import sys

def define_apis():
	
	app = Flask(__name__)
	
	CORS(app)

	sys.path.append(sys.argv[0].replace('APIs/app.py',''))
	sys.path.append(os.path.abspath(__file__).replace('/APIs/app.py',''))
	print(sys.path)

	@app.route('/', methods=['GET','POST','OPTION'])
	def index():
		testing = {}
		return testing
	@app.route('/command', methods=['GET', 'POST'])
	def command():
		cmnd = request.args.get('cmnd')
		cmnd = '' if cmnd == None else cmnd

		from executor import execute
		from commands.CRUDs    import DRY as c
		import GlobalVars as gv
		#execute = c.capture_prints(execute)
		#captured_prints, result = execute(cmnd)
		execute(cmnd)

		#print('\n'+captured_prints)
		
		return {'CURRENT_WORKSHOP':gv.CURRENT_WORKSHOP, 'CURRENT_DOMAIN':gv.CURRENT_DOMAIN, "LAST_OUTPUT":''}

	@app.route('/get_output',  methods=['GET','POST','OPTION'])
	def get_output():
		content = ''
		with open('output.txt', 'r') as f:
			for line in f:
				#print(line)
				content = content + line

			return content

	@app.route('/get_domain', methods=['GET','POST','OPTION'])
	def get_domain():
		from entities.workshop	import Workshop
		from entities.domain	import Domain
		from entities.path	import Path
		import GlobalVars	as     gv

		dmn = request.args.get('dmn')
		dmn = '' if dmn == None else dmn
		
		if gv.CURRENT_WORKSHOP == "":
			return {'domain':"set a workshop"}
		dmn_res = Domain.get(gv.CURRENT_WORKSHOP,dmn)
		return dmn_res.toJson()

		


	@app.route('/get_domains', methods=['GET','POST','OPTION'])
	def get_domains():
		from entities.workshop	import Workshop
		from entities.domain	import Domain
		from entities.path	import Path
		import GlobalVars	as     gv

		if gv.CURRENT_WORKSHOP == "":
			return {'data':['set a workshop']}
		domainsList = Domain.searchBy(workshop_id=gv.CURRENT_WORKSHOP)
		dd = []
		for d in domainsList:
			pathsCount = len(Path.getByDomain(d.domain,gv.CURRENT_WORKSHOP))
			jsCount	   = len(d.js_files)
			portsCount = len(list(d.ports.keys()))
			ip	   = "❌" if d.ip	   == "" else d.ip
			robots_file= "❌" if d.robots_file == "" else d.robots_file
			server_file= "❌" if d.server_file == "" else d.server_file
			tags	   = "❌" if len(d.tags)   == 0  else d.tags
			techs	   = len(d.techs)
			whois	   = "❌" if not d.whois         else "✅"

			dd.append({'domain':d.domain, 'ip':ip,'paths':pathsCount, 'js':jsCount, 'ports':portsCount, 'techs':techs,'whois':whois, 'server_file':server_file, 'robots_file':robots_file, 'tags':tags})
		return {'data':dd}

	@app.route('/get_setted_domain_infos', methods=['GET', 'POST', 'OPTION'])
	def get_setted_domain_infos():
		from entities.workshop	import Workshop
		from entities.domain	import Domain
		from entities.path	import Path
		import GlobalVars	as     gv

		if gv.CURRENT_WORKSHOP == "" or gv.CURRENT_DOMAIN == "":
			return {'data':['set a domain']}
		domainsList = Domain.searchBy(workshop_id=gv.CURRENT_WORKSHOP, domain=gv.CURRENT_DOMAIN)
		dd = []
		for d in domainsList:
			pathsCount = len(Path.getByDomain(d.domain,gv.CURRENT_WORKSHOP))
			jsCount	   = len(d.js_files)
			portsCount = len(list(d.ports.keys()))
			ip	   = "❌" if d.ip	   == "" else d.ip
			robots_file= "❌" if d.robots_file == "" else d.robots_file
			server_file= "❌" if d.server_file == "" else d.server_file
			tags	   = "❌" if len(d.tags)   == 0  else d.tags
			techs	   = len(d.techs)
			whois	   = "❌" if not d.whois         else "✅"

			dd.append({'domain':d.domain, 'ip':ip,'paths':pathsCount, 'js':jsCount, 'ports':portsCount, 'techs':techs,'whois':whois, 'server_file':server_file, 'robots_file':robots_file, 'tags':tags})
		return {'data':dd}

	@app.route('/get_setted_domain_whois', methods=['GET', 'POST', 'OPTION'])
	def get_setted_domain_whois():
		from entities.workshop	import Workshop
		from entities.domain	import Domain
		from entities.path	import Path
		import GlobalVars	as     gv

		if gv.CURRENT_WORKSHOP == "" or gv.CURRENT_DOMAIN == "":
			return {'data':['set a domain']}
		domainsList = Domain.searchBy(workshop_id=gv.CURRENT_WORKSHOP, domain=gv.CURRENT_DOMAIN)
		dd = []
		for d in domainsList:
			if not d.whois:
				whois = "SCAN WHOIS with 'get whois -d <domain> -w <workshop>'"
			else:
				whois = d.whois
				for w in whois.keys():
					dd.append({"asset":w,"value":whois[w]})
		return {'data':dd}


	@app.route('/get_setted_domain_js_files', methods=['GET', 'POST', 'OPTION'])
	def get_setted_domain_js_files():
		from entities.workshop	import Workshop
		from entities.domain	import Domain
		from entities.path	import Path
		import GlobalVars	as     gv

		if gv.CURRENT_WORKSHOP == "" or gv.CURRENT_DOMAIN == "":
			return {'data':['set a domain']}
		domainsList = Domain.searchBy(workshop_id=gv.CURRENT_WORKSHOP, domain=gv.CURRENT_DOMAIN)
		dd = []
		for d in domainsList:
			for j in d.js_files:
				dd.append({'javascript':j})
		return {'data':dd}

	@app.route('/get_setted_domain_paths', methods=['GET', 'POST', 'OPTION'])
	def get_setted_domain_paths():
		from entities.workshop	import Workshop
		from entities.domain	import Domain
		from entities.path	import Path
		import GlobalVars	as     gv

		if gv.CURRENT_WORKSHOP == "" or gv.CURRENT_DOMAIN == "":
			return {'data':['set a domain']}
		domainsList = Domain.searchBy(workshop_id=gv.CURRENT_WORKSHOP, domain=gv.CURRENT_DOMAIN)
		dd = []
		for d in domainsList:
			for p in Path.getByDomain(d.domain,gv.CURRENT_WORKSHOP):
				path = p.path
				tags = p.tags
				dd.append({'path':path, 'tags':tags})
		return {'data':dd}


	@app.route('/get_setted_domain_techs', methods=['GET', 'POST', 'OPTION'])
	def get_setted_domain_techs():
		from entities.workshop	import Workshop
		from entities.domain	import Domain
		from entities.path	import Path
		import GlobalVars	as     gv

		if gv.CURRENT_WORKSHOP == "" or gv.CURRENT_DOMAIN == "":
			return {'data':['set a domain']}
		domainsList = Domain.searchBy(workshop_id=gv.CURRENT_WORKSHOP, domain=gv.CURRENT_DOMAIN)
		dd = []
		for d in domainsList:
			for t in d.techs:
				dd.append({'technology':t})
		return {'data':dd}




	@app.route('/get_setted_domain_ports', methods=['GET', 'POST', 'OPTION'])
	def get_setted_domain_ports():
		from entities.workshop	import Workshop
		from entities.domain	import Domain
		from entities.path	import Path
		import GlobalVars	as     gv

		if gv.CURRENT_WORKSHOP == "" or gv.CURRENT_DOMAIN == "":
			return {'data':['set a domain']}
		domainsList = Domain.searchBy(workshop_id=gv.CURRENT_WORKSHOP, domain=gv.CURRENT_DOMAIN)
		dd = []
		for d in domainsList:
			for p in d.ports.keys():
				portname   = p
				portnumber = d.ports[p]

				dd.append({'name':portname,'number':portnumber})
		return {'data':dd}



	@app.route('/get_github_search', methods=['GET','POST','OPTION'])
	def get_github_search():
		import GlobalVars as gv

		if gv.CURRENT_WORKSHOP == "":
			return {'data':['set a workshop']}
		with open('data/workshops/'+gv.CURRENT_WORKSHOP+'/github_search') as f:
			d = json.load(f)
			
			return {'data':d}

	@app.route('/get_github_search_stats', methods=['GET','POST','OPTION'])
	def get_github_search_stats():
		import GlobalVars as gv

		if gv.CURRENT_WORKSHOP == "":
			return [{"name":"set a workshop","value":0}]

		res = []
		with open('data/workshops/'+gv.CURRENT_WORKSHOP+'/github_search') as f:
			d = json.load(f)
			
			for s in d:
				res.append({"name":s['repository'], "value":s['founds']})
			
			return res




	@app.route('/get_numberDomainsByWorkshop', methods=['GET','POST','OPTION'])
	def get_numberDomainsByWorkshop():
		from entities.workshop	import	Workshop
		from entities.domain	import	Domain
		import GlobalVars	as	gv

		if gv.CURRENT_WORKSHOP == "":
			return {"nb":0}
		domainsList = Domain.searchBy(workshop_id=gv.CURRENT_WORKSHOP)
		res = {"nb":len(domainsList)}
		return res

	@app.route("/get_ipStat", methods=['GET','POST','OPTION'])
	def get_ipStat():
		from entities.workshop	import	Workshop
		from entities.domain	import	Domain
		import GlobalVars	as	gv
		import ipaddress
		from collections import defaultdict


		if gv.CURRENT_WORKSHOP == "":
			return [{"name":"set a workshop","value":0}]
		dl = Domain.searchBy(workshop_id=gv.CURRENT_WORKSHOP)
		ip_addresses=[]
		for d in dl:
			if(d.ip):
				ip_addresses.append(d.ip)

		#guess 1
		guess ={}
		def guessing(itr):
			for ip in ip_addresses:
				net = ip.split('.')
				if itr == 1: net = net[0]+"."+net[1]+"."+net[2]+".0"
				if itr == 2: net = net[0]+"."+net[1]+".0.0"
				if itr == 3: net = net[0]+".0.0.0"
				if not(net in guess.keys()):
					guess[net] = []
				guess[net].append(ip)
			#clean
			to_delete=[]
			for key in guess.keys():
				if len(guess[key]) == 1:
					to_delete.append(key)
				else:
					for ip in guess[key]:
						while ip in ip_addresses:
							ip_addresses.remove(ip)
			if itr != 3:
				for k in to_delete:
					del guess[k]
		guessing(1)
		guessing(2)
		guessing(3)

		rslt = []
		for k in guess.keys():
			rslt.append({"name":k, "value":len(guess[k])})


		return rslt

	@app.route('/get_domain_names', methods=['GET','POST','OPTION'])
	def get_domain_names():
		from entities.workshop	import Workshop
		from entities.domain	import Domain
		from entities.path	import Path
		import GlobalVars	as     gv
		import tldextract	as domain_parts
 
		if gv.CURRENT_WORKSHOP == "":
			return [{"name":"set a workshop","value":0}]

		domainsList = Domain.searchBy(workshop_id=gv.CURRENT_WORKSHOP)
		hosts = []
		for d in domainsList:
			host = domain_parts.extract(d.domain).domain + '.' + domain_parts.extract(d.domain).suffix
			names = [i["name"] for i in hosts]
			if not (host in names):
				hosts.append({"name":host, "value":0})
			for h in range(0,len(hosts)):
				if hosts[h]["name"] == host:
					hosts[h]["value"] = hosts[h]["value"] + 1
		return hosts
	
	@app.route('/get_portsStat', methods=['GET','POST','OPTION'])
	def get_portsStat():
		from entities.workshop	import Workshop
		from entities.domain	import Domain
		from entities.path	import Path
		import GlobalVars	as     gv
		import tldextract	as domain_parts
 
		if gv.CURRENT_WORKSHOP == "":
			return [{"name":"set a workshop","value":0}]

		domainsList = Domain.searchBy(workshop_id=gv.CURRENT_WORKSHOP)
		ports = []
		for d in domainsList:
			for p in d.ports.keys():
				p = p +":"+str(d.ports[p])
				ports_names = [i["name"] for i in ports]
				if not (p in ports_names):
					ports.append({"name":p, "value":0})
				for i in range(0,len(ports)):
					if ports[i]["name"] == p:
						ports[i]["value"] = ports[i]["value"] + 1
		return ports

	@app.route('/get_pathsStat', methods=['GET','POST','OPTION'])
	def get_pathsStat():
		from entities.workshop	import Workshop
		from entities.domain	import Domain
		from entities.path	import Path
		import GlobalVars	as     gv

		if gv.CURRENT_WORKSHOP == "":
			return [{"name":"set a workshop","value":0}]

		domainsList = Domain.searchBy(workshop_id=gv.CURRENT_WORKSHOP)
		dd = []
		for d in domainsList:
			pathsCount = len(Path.getByDomain(d.domain,gv.CURRENT_WORKSHOP))
			if pathsCount != 0:
				dd.append({"name":d.domain,"value":pathsCount})
		return dd




	return app


def run_apis():
	subprocess.Popen(["python3", "APIs/app.py"])


if __name__ == '__main__':
	app = define_apis()
	app.run(debug=True)







