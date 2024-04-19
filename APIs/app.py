import threading
from flask import Flask
import os
import subprocess
def define_apis():

    app = Flask(__name__)


    @app.route('/')
    def index():
        return 'Hello, World!'

    return app

def run_apis():
	subprocess.Popen(["python3", "APIs/app.py"])

if __name__ == '__main__':
	app = define_apis()
	app.run(debug=True)


