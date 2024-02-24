import sys








#This file contain all global variables.

global CURRENT_WORKSHOP
global CURRENT_DOMAIN
global JSON_DATABASE

CURRENT_WORKSHOP = ""
CURRENT_DOMAIN   = ""
JSON_DATABASE    = sys.argv[0].replace("togomori.py","")+"data/workshops.json"
