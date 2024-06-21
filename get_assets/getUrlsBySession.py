from seleniumwire			import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui	import WebDriverWait
from selenium.webdriver.support		import expected_conditions as EC
from selenium.webdriver.common.by	import By
from selenium.common.exceptions		import WebDriverException
from commands.CRUDs			import DRY as c
from entities.domain			import Domain
from entities.path			import Path
from personalizedPrint import pp
import tldextract	 as domain_parts
import requests
import os
import time

def GetUrlsBySession(workshop, domain, look_for=['all'], no_save=True, strict=True, ignore_those=[]):
	if ignore_those == []:
		ignore_those = ["mozilla", "google", "facebook", "weglot", "polyfill.io", "fonts.gstatic.com"]
	elif "disable" in ignore_those:
		ignore_those = []

	#look_for = ["all"]
	print("looking for :")
	print(look_for)
	# Path to your GeckoDriver executable
	geckodriver_path = '/home/kali/Desktop/geckodriver'  # Adjust path as per your installation


	# Configure Firefox options
	firefox_options = webdriver.FirefoxOptions()
	firefox_options.headless = True  # Run Firefox in headless mode

	service = FirefoxService(executable_path=geckodriver_path)
	driver = webdriver.Firefox(service=service, options=firefox_options)

	is_session_closed(driver)
	main    = domain_parts.extract(domain).domain
	pp("main: "+main)
	pp("GET "+domain)
	driver.get("https://"+domain)
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
	pp("waiting for the site to fully load...")
	#time.sleep(10)
	reqs = []
	len_reqs = 0
	keep_wait = 0
	while keep_wait != 4:
		len_urls = len(reqs)
		start_from = len_reqs
		len_reqs = len(driver.requests)
		for r in range(start_from,len_reqs):
			wait_res = 3
			while not driver.requests[r].response and wait_res >0:
				time.sleep(0.5)
				wait_res = wait_res - 0.5

			if driver.requests[r].response:
				ignore = url_is_ignored(main, driver.requests[r].url, ignore_those, strict)
				if not ignore :
					if 'all' in look_for:
						pp(
							str(driver.requests[r].method)+"       "+
							str(driver.requests[r].response.headers['Content-Type'])+"             "+
							str(driver.requests[r].response.status_code)+" "+
							str(driver.requests[r].url)
						)
						reqs.append(driver.requests[r])
					else:
						get_it = to_look_for(str(driver.requests[r].response.headers['Content-Type']), look_for)
						if ( get_it ):
							pp(
							str(driver.requests[r].method)+"       "+
							str(driver.requests[r].response.headers['Content-Type'])+"             "+
							str(driver.requests[r].response.status_code)+" "+
							str(driver.requests[r].url)
							)
							reqs.append(driver.requests[r])
		#print("wait")
		time.sleep(1)
		if len_urls != len(reqs):
			keep_wait = 0
		else:
			keep_wait = keep_wait + 1

			
	if not no_save:
		for req in reqs:

			url       = c.segmentUrl(req.url)["domain"]
			path	  = c.segmentUrl(req.url)["path"]
			variables = c.segmentUrl(req.url)["variables"]
			if url != "NoDomain":
				dmn = Domain(workshop_id=workshop, domain=url)
				r   = dmn.save()
				if r == 'DomainExist':
					dmn.domain = ''
					dmn.workshop_id=''
					r = Domain.update(url, workshop, dmn, False)

			
			if req.response.headers['Content-Type'].find('javascript') != -1:
				dmn.domain	=''
				dmn.workshop_id	=''
				dmn.js_files	=['+', url+''+path]
				r = Domain.update(url, workshop, dmn, False)

			elif path != "InvalidPath" and path != "NoPath":
				pth = Path(domain=url, path=path)
				r   = pth.save(workshop)
				if r == "PathExist":
					pth.domain = ""
					pth.path   = ""
					r = Path.update(workshop, url, path, pth)

	driver.quit()
	is_session_closed(driver)
	return reqs

def to_look_for(res_type, look_for):
	for t in look_for:
		if res_type.find(t) != -1:
			return True
	return False

def url_is_ignored(main, url, wordlist, strict):

	if strict and url.find(main) == -1:
		return True

	for w in wordlist:
		if url.find(w) != -1:
			return True
	return False

def is_session_closed(driver):
	try:
		# Try to access window handles or any other property/method
		driver.window_handles
		pp("session is OPEN.")
		return False  # If no exception is raised, the session is still open
	except Exception:
		pp("session is CLOSED")
		return True  # If an exception is raised, the session is closed
