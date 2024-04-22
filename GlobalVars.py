import sys








#This file contain all global variables.

global CURRENT_WORKSHOP
global CURRENT_DOMAIN
global DATABASE

CURRENT_WORKSHOP = ""
CURRENT_DOMAIN   = ""
DATABASE	 = sys.argv[0].replace("togomori.py","")+"data/"
DATABASE	 = sys.argv[0].replace('APIs/app.py','')+"data/"
