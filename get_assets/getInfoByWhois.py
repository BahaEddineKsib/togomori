from entities.domain import Domain
import whois
import json

def GetInfoByWhois(workshop, domain,no_save):
	info = whois.whois(domain)
	info['creation_date'] = str(info['creation_date'])
	if info['domain_name'] == None:
		return 'DomainNotInWhois'
	if not no_save:
		dmn = Domain(workshop_id=workshop, domain=domain, whois=info)
		r   = dmn.save()
		if r == 'WorkshopNotFound':
			return r
		if r == 'DomainExist':
			dmn.domain = ''
			dmn.whois = info
			r = Domain.update(domain, workshop, dmn, False)

	return info

