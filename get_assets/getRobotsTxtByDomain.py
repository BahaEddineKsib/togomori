from entities.domain import Domain
import requests as req
from personalizedPrint import pp

def GetRobotsTxtByDomain(workshop, domain, no_save):
	try:
		resp = req.get("https://"+domain+"/robots.txt", timeout=4)
		if resp.status_code == 200:
			pp("[+]	"+domain+"/robots.txt")
		else:
			#pp("can't get	"+domain+" robots.txt file")
			return "NoRobot"
	except Exception as e:
		#print(e)
		#pp("can't get	"+domain+" robots.txt file*")
		return "NoRobot"
		
	if not no_save:
		dmn = Domain(workshop_id=workshop, domain=domain, robots_file="/robots.txt")
		r   = dmn.save()
		if r == 'WorkshopNotFound':
			return r
		if r == 'DomainExist':
			dmn.domain = ''
			dmn.workshop_id=''
			r = Domain.update(domain, workshop, dmn, False)
	return "robTxtExist"
