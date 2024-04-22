import threading
from flask import Flask, request
from flask_cors import CORS
import os
import subprocess
import json
import sys
global LAST_OUTPUT
LAST_OUTPUT = '-'


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
		execute = c.capture_prints(execute)
		captured_prints, result = execute(cmnd)
		print('\n'+captured_prints)
		
		return {'CURRENT_WORKSHOP':gv.CURRENT_WORKSHOP, 'CURRENT_DOMAIN':gv.CURRENT_DOMAIN, "LAST_OUTPUT":captured_prints}
	return app
def run_apis():
	subprocess.Popen(["python3", "APIs/app.py"])


if __name__ == '__main__':
	app = define_apis()
	app.run(debug=True)

