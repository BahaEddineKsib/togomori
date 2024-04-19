from entities.domain import Domain
import whois
import json

def GetInfoByWhois(workshop, domain,no_save):
	info = whois.whois(domain)
	info['creation_date'] = str(info['creation_date'])
	json_info = {}

	json_info['admin_address']=info['admin_address']
	json_info['admin_address2']=info['admin_address2']
	json_info['admin_city']=info['admin_city']
	json_info['admin_country']=info['admin_country']
	json_info['admin_email']=info['admin_email']
	json_info['admin_fax']=info['admin_fax']
	json_info['admin_first_name']=info['admin_first_name']
	json_info['admin_name']=info['admin_name']
	json_info['admin_phone']=info['admin_phone']
	json_info['admin_state']=info['admin_state']
	json_info['admin_zip']=info['admin_zip']
	json_info['aregistrant_zip']=info['aregistrant_zip']
	json_info['creation_date']=info['creation_date']
	json_info['domain_name']=info['domain_name']
	json_info['name_servers']=info['name_servers']
	json_info['registrant_address']=info['registrant_address']
	json_info['registrant_address2']=info['registrant_address2']
	json_info['registrant_city']=info['registrant_city']
	json_info['registrant_country']=info['registrant_country']
	json_info['registrant_email']=info['registrant_email']
	json_info['registrant_fax']=info['registrant_fax']
	json_info['registrant_name']=info['registrant_name']
	json_info['registrant_phone']=info['registrant_phone']
	json_info['registrant_state']=info['registrant_state']
	json_info['registrar']=info['registrar']
	json_info['status']=info['status']
	json_info['tech_address']=info['tech_address']
	json_info['tech_address2']=info['tech_address2']
	json_info['tech_city']=info['tech_city']
	json_info['tech_country']=info['tech_country']
	json_info['tech_email']=info['tech_email']
	json_info['tech_fax']=info['tech_fax']
	json_info['tech_first_name']=info['tech_first_name']
	json_info['tech_name']=info['tech_name']
	json_info['tech_phone']=info['tech_phone']
	json_info['tech_state']=info['tech_state']
	json_info['tech_zip']=info['tech_zip']
	if json_info['domain_name'] == None:
		return 'DomainNotInWhois'
	if not no_save:
		dmn = Domain(workshop_id=workshop, domain=domain, whois=json_info)
		r   = dmn.save()
		if r == 'WorkshopNotFound':
			return r
		if r == 'DomainExist':
			dmn.domain = ''
			dmn.workshop_id=''
			r = Domain.update(domain, workshop, dmn, False)

	return json_info

