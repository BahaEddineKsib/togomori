from entities.workshop import Workshop 
import requests
import pprint
import json
import time
import os
from personalizedPrint import pp


def GetGithubByDomain(workshop, keyword, no_save, clear=False):

	if clear:
		if Workshop.exist(workshop):
			file_path = Workshop.getPath(workshop)+'/github_search'
			if os.path.isfile(file_path):
				open(file_path, 'w').close()
				pp("Clear.")
			return 'clear'
		else:
			pp("workshop don't exist.")
			return 'WorkshopNotFound'

	time.sleep(5)
	with open('configs.json', 'r') as json_file:
		json_configs = json.load(json_file)
	github_token = json_configs["github_token"]
	items = []
	repositories = []
	page = 1
	slow_down(github_token)
	while page<10:
		items = []
		query = f"{keyword}"
		
		slow_down(github_token)

		url = f"https://api.github.com/search/code?q={query}&page={page}"
		headers = {"Authorization": f"token {github_token}"}
		response = requests.get(url, headers=headers)
		pp('Get: '+url)
		#slow_down(github_token)
		if response.status_code != 200:
			pp("F:"+keyword+" page "+str(page))
			#pp(f"Failed to retrieve data: {response.status_code}")
			#pp(response.text)
			break

		result = response.json()
		if not result['items']:
			break

		for item in result['items']:
			pp(f"Repository: {item['repository']['full_name']}")
			time.sleep(0.02)
			#pprint.pp(item)
			it = {"domain":keyword, "repository":item['repository']['full_name'], "filename":item['name'], "url":"https://github.com/"+item['repository']['full_name']}
			if not any(d.get("repository") == it["repository"] for d in repositories):
				repositories.append({'repository':it['repository'], 'domain':keyword, 'founds':0, 'url':it['url']})
			items.append(it)

		for i in range(0, len(repositories)):
			for it in items:
				if repositories[i]['repository'] == it['repository']:
					repositories[i]['founds'] = repositories[i]['founds'] + 1

		page += 1
	for rep in repositories:
		pp("repository: "+rep['repository'])
		pp("founds    : "+str(rep['founds']))
		pp("domain    : "+rep['domain'])
		pp("url       : "+rep['url']+'\n')
	
	if not no_save:
		if Workshop.exist(workshop):
			file_path = Workshop.getPath(workshop)+'/github_search'
			#data = {"key1": "value1", "key2": "value2"}
	
			# Check if the file exists
			if not os.path.isfile(file_path):
				pp("ne: CREATING "+file_path)
				#Create the file and write the dictionary
				with open(file_path, 'w') as file:
					json.dump(repositories, file)  # Serialize the dictionary as JSON and write it to the file
				pp("Saved. in "+ file_path)
			else:
				pp("e: Saving in " +file_path)
				with open(file_path, 'r') as file:
					json_list = json.load(file)
				for rep in repositories:
					in_search = False
					for i in range(0, len(json_list)):
						if json_list[i]['repository'] == rep['repository'] and json_list[i]['domain'] == rep['domain']:
							json_list[i]['founds'] = rep['founds']
							in_search = True
							break
					if not in_search:
						json_list.append(rep)
				with open(file_path, 'w') as file:
					json.dump(repositories, file)
		else:
			pp("workshop "+workshop+" not found")

def slow_down(key):
	# Your personal access token
	access_token = key
	
	# GitHub API URL for rate limit status
	url = "https://api.github.com/rate_limit"
	
	# Headers with authentication
	headers = {
	    "Authorization": f"token {access_token}"
	}
	
	# Send the GET request to check rate limits
	response = requests.get(url, headers=headers)
	
	if response.status_code == 200:
		rate_limit_info = response.json()
		core_limits = rate_limit_info['resources']['core']
		limit = core_limits['limit']
		remaining = core_limits['remaining']
		reset_time = core_limits['reset']
		
		# Calculate the time remaining until reset
		current_time = time.time()
		time_until_reset = reset_time - current_time
		
		# Calculate the delay needed between requests
		if remaining > 0:
			delay_between_requests = time_until_reset / remaining +1
		else:
			# If no requests are remaining, wait until the reset time
			delay_between_requests = time_until_reset +1
			
		#print(f"Rate Limit: {limit}")
		#print(f"Remaining: {remaining}")
		#print(f"Time until reset (seconds): {time_until_reset}")
		#print(f"Delay between requests (seconds): {delay_between_requests}")
		
		# Example usage: wait between requests
		if delay_between_requests > 0:
			#print(f"Waiting {delay_between_requests:.2f} seconds before the next request.")
			time.sleep(delay_between_requests)
		else:
			#pp(f"Failed to retrieve rate limits: {response.status_code}")
			#pp(response.json())  # Print the error message from GitHub
			pp(f"Failed to retrieve rate limits")



# Example usage
#GetGithubByDomain('w','pfe.esprit.tn', False)
