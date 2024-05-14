import sys








#This file contain all global variables.

global CURRENT_WORKSHOP
global CURRENT_DOMAIN
global DATABASE

CURRENT_WORKSHOP = ""
CURRENT_DOMAIN   = ""
DATABASE	 = ""
PATH		 = ""
print("are in "+sys.argv[0])
if "test_togomori.py" in sys.argv[0] :
	PATH	 = sys.argc[0].replace("test_togomori.py","")
	DATABASE = sys.argv[0].replace("test_togomori.py","")+"test_data/"

elif "APIs/app.py" in sys.argv[0]:
	PATH	 = sys.argv[0].replace('APIs/app.py','')
	DATABASE = sys.argv[0].replace('APIs/app.py','')+"data/"

elif "togomori.py"    in sys.argv[0]:
	PATH	 = sys.argv[0].replace('togomori.py','')
	DATABASE = sys.argv[0].replace('togomori.py','')+"data/"

print('Our data is '+DATABASE)
