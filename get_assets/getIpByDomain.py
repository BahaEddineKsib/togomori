from entities.domain import Domain
import socket
from personalizedPrint import pp

def GetIpByDomain(workshop, domain, no_save):
	try:
		ip = socket.gethostbyname(domain)
		pp("[+]  "+ip+"	"+domain)
	except:
		pp("can't get	"+domain)
		return "NoIp" 
		
	if not no_save:
		dmn = Domain(workshop_id=workshop, domain=domain, ip=ip)
		r   = dmn.save()
		if r == 'WorkshopNotFound':
			return r
		if r == 'DomainExist':
			dmn.domain = ''
			dmn.workshop_id=''
			r = Domain.update(domain, workshop, dmn, False)
	return ip
