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

	sys.path.append(sys.argv[0].replace('/APIs/app.py',''))

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
			return {'domains':['set a workshop']}
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
	return app
def run_apis():
	subprocess.Popen(["python3", "APIs/app.py"])


if __name__ == '__main__':
	app = define_apis()
	app.run(debug=True)







