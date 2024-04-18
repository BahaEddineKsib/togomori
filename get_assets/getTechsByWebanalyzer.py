from entities.domain import Domain
import requests
import json
def GetTechsByWebanalyzer(workshop, domain, no_save, show_balance):

	with open('configs.json', 'r') as json_file:
		json_configs = json.load(json_file)
	api_key = json_configs["webanalyzer_API"]
	headers = {"x-api-key":api_key}
	result = {}
	res1 = requests.get('https://api.wappalyzer.com/v2/lookup/?urls=https://'+domain,headers=headers)

	if show_balance:
		res2    = requests.get('https://api.wappalyzer.com/v2/credits/balance/',headers=headers)
		if res2.status_code != 200:
			return balance.status_code
		result['balance'] = res2.json()['credits'] 

	if res1.status_code != 200:
		return res1.status_code
	json_res = res1.json()

	result['techs'] = [tech["name"] for tech in json_res[0]["technologies"]]
	#result['techs'] = ['tech1','tech2','tech3']
	#result['techs'] = []
	if not no_save:
		dmn = Domain(workshop_id=workshop, domain=domain, techs=result['techs'])
		r   = dmn.save()
		if r == 'WorkshopNotFound':
			return r
		if r == 'DomainExist':
			dmn.domain = ''

			dmn.techs = ['_']+dmn.techs
			r = Domain.update(domain, workshop, dmn, False)

			dmn.techs = ['+']+dmn.techs
			r = Domain.update(domain, workshop, dmn, False)

	return result
 
















