import json
import os
import GlobalVars as TopG
import entities.workshop as W
import pprint
import tldextract as domain_parts
class Domain:
	def __init__(self, workshop_id,
			   domain     ="", 
			   sub        ="",
			   main       ="",
			   tld        ="",
			   tags       =[],
			   techs      =[],
			   whois_file ="",
			   ip         ="", 
			   ports      ={},
			   server_file="",
			   robots_file="",
			   js_files   =[]):
		self.workshop_id     = workshop_id
		self.domain	     = domain
		self.sub	     = domain_parts.extract(domain).subdomain if sub  !="" else ""
		self.main	     = domain_parts.extract(domain).domain    if main !="" else ""
		self.tld	     = domain_parts.extract(domain).suffix    if tld  !="" else ""
		self.tags            = tags
		self.techs           = techs
		self.whois_file      = whois_file
		self.ip              = ip 
		self.ports           = ports
		self.server_file     = server_file
		self.robots_file     = robots_file
		self.js_files        = js_files

	def toJson(self):
		return self.__dict__

	@staticmethod
	def jsonToDomain(dmn):
		Dom = Domain(**dmn)
		return Dom

	def save(self):
		wrk = W.Workshop.search(self.workshop_id)
		if( wrk == "WorkshopNotFound" ):
			return "WorkshopNotFound"
		elif(Domain.searchInWorkshop(self.domain,wrk) != "DomainNotFound"):
			return "DomainExist"
		else:
			wrk.domains.append(self)
			wrk.update()
			return "DomainAdded"
	
	@staticmethod
	def delete(domain,workshop_id):
		wrk = W.Workshop.search(workshop_id)
		if( wrk == "WorkshopNotFound"):
			return "WorkshopNotFound"
		elif(Domain.searchInWorkshop(domain,wrk) == "DomainNotFound"):
			return "DomainNotFound"
		else:
			wrk.domains = [d for d in wrk.domains if d.domain != domain]
			wrk.update()
			return "DomainDeleted"

	@staticmethod
	def update(domain, workshop_id, new_dmn):
		old_wrk = W.Workshop.search(workshop_id)
		new_wrk = W.Workshop.search(new_dmn.workshop_id)        if new_dmn.workshop_id           else ""
		old_dmn = Domain.searchInWorkshop(domain, old_wrk) if old_wrk != "WorkshopNotFound" else ""

		if( old_wrk == "WorkshopNotFound" ):
			return "OldWorkshopNotFound"
		elif(old_dmn == "DomainNotFound"):
			return "DomainNotFound"
		elif(new_wrk == "WorkshopNotFound"):
			return "NewWorkshopNotFound"
		elif(new_wrk and Domain.searchInWorkshop(new_dmn.domain, new_wrk) != "DomainNotFound"):
			return "DomainExist"
		else:
			old_dmn.domain	= new_dmn.domain	  if new_dmn.domain	else old_dmn.domain
			old_dmn.whois_file	= new_dmn.whois_file	  if new_dmn.whois_file		else old_dmn.whois_file
			old_dmn.ip		= new_dmn.ip		  if new_dmn.ip			else old_dmn.ip
			old_dmn.server_file	= new_dmn.server_file	  if new_dmn.server_file	else old_dmn.server_file
			old_dmn.robots_file = new_dmn.robots_file if new_dmn.robots_file	else old_dmn.robots_file
			old_dmn.workshop_id     = new_dmn.workshop_id     if new_wrk                    else old_dmn.workshop_id
			if new_dmn.js_files:	
				if(  '+' == new_dmn.js_files[0]	):
					old_dmn.js_files += new_dmn.js_files; old_dmn.js_files.remove('+')
				elif('_' == new_dmn.js_files[0]	):
					old_dmn.js_files = [ d for d in old_dmn.js_files if d not in new_dmn.js_files ]
				else:
					old_dmn.js_files  = new_dmn.js_files

			if new_dmn.tags:	
				if(  '+' == new_dmn.tags[0]	):
					old_dmn.tags+= new_dmn.tags; old_dmn.tags.remove('+')
				elif('_' == new_dmn.tags[0]	):
					old_dmn.tags= [ d for d in old_dmn.tags if d not in new_dmn.tags]
				else:
					old_dmn.tags= new_dmn.tags

			if new_dmn.techs:	
				if(  '+' == new_dmn.techs[0]	):
					old_dmn.techs+= new_dmn.techs; old_dmn.techs.remove('+')
				elif('_' == new_dmn.techs[0]	):
					old_dmn.techs= [ d for d in old_dmn.techs if d not in new_dmn.techs]
				else:
					old_dmn.techs= new_dmn.techs
			if new_dmn.ports:	
				if(  '+' == next(iter(new_dmn.ports.keys()))	):
					old_dmn.ports.update(new_dmn.ports); del old_dmn.ports['+']
				elif('_' == next(iter(new_dmn.ports.keys()))):
					old_dmn.ports.update(new_dmn.ports);
					for key in  new_dmn.ports.keys():
						del old_dmn.ports[key]
				else:
					old_dmn.ports= new_dmn.ports

			Domain.delete(domain,workshop_id)
			old_dmn.save()
			return "DomainUpdated"


	def display(self,toDisplay=['ALL']):
		dmn={}
		if "ALL" in toDisplay or "workshop_id"	in toDisplay:dmn["workshop_id"] =self.workshop_id
		if "ALL" in toDisplay or "domain"	in toDisplay:dmn["domain"]	=self.domain
		if "ALL" in toDisplay or "sub"		in toDisplay:dmn["sub"]		=self.sub
		if "ALL" in toDisplay or "main"		in toDisplay:dmn["main"]	=self.main
		if "ALL" in toDisplay or "tld"		in toDisplay:dmn["tld"]		=self.tld
		if "ALL" in toDisplay or "tags"		in toDisplay:dmn["tags"]        =self.tags 
		if "ALL" in toDisplay or "techs"	in toDisplay:dmn["techs"]	=self.techs 
		if "ALL" in toDisplay or "whois_file"	in toDisplay:dmn["whois_file"]  =self.whois_file 
		if "ALL" in toDisplay or "ip"		in toDisplay:dmn["ip"]          =self.ip 
		if "ALL" in toDisplay or "ports"	in toDisplay:dmn["ports"]       =self.ports 
		if "ALL" in toDisplay or "server_file"	in toDisplay:dmn["server_file"] =self.server_file 
		if "ALL" in toDisplay or "robots_file"	in toDisplay:dmn["robots_file"] =self.robots_file 
		if "ALL" in toDisplay or "js_files"	in toDisplay:dmn["js_files"]	=self.js_files 

		pp = pprint.PrettyPrinter(indent=4)
		pp.pprint(dmn)

	@staticmethod
	def getDomainsByWorkshop(wrk):
		return wrk.domains
	@staticmethod
	def searchInWorkshop(domain,wrk):
		for dmn in wrk.domains:
			if(dmn.domain==domain):
				return dmn
		return "DomainNotFound"

	@staticmethod
	def searchBy(      workshop_id,
		           domain	=False,
			   sub		=False,
			   main		=False,
			   tld		=False,
			   tags		=False,
			   techs	=False,
			   whois_file   =False,
			   ip           =False, 
			   ports	=False,
			   server_file  =False,
			   robots_file	=False,
			   js_files	=False):
		
		domainsList=[]

		domainsList= domainsList if not workshop_id	else Domain.getDomainsByWorkshop(W.Workshop.search(workshop_id))
		domainsList= domainsList if not domain		else [d for d in domainsList if d.domain == domain]
		domainsList= domainsList if not sub		else [d for d in domainsList if d.sub == sub]
		domainsList= domainsList if not main		else [d for d in domainsList if d.main == main]
		domainsList= domainsList if not tld		else [d for d in domainsList if d.tld == tld]
		domainsList= domainsList if not tags		else [d for d in domainsList if any(tag  in d.tags              for tag  in tags)]
		domainsList= domainsList if not ports		else [d for d in domainsList if any(port in d.ports.items() for port in ports.items())]
		domainsList= domainsList if not techs		else [d for d in domainsList if any(tech in d.techs        for tech in techs)]
		domainsList= domainsList if not whois_file	else [d for d in domainsList if d.whois_file == whois_file]
		domainsList= domainsList if not ip		else [d for d in domainsList if d.ip == ip]
		domainsList= domainsList if not server_file     else [d for d in domainsList if d.server_file == server_file]
		domainsList= domainsList if not robots_file	else [d for d in domainsList if d.robots_file== robots_file]
		domainsList= domainsList if not js_files	else [d for d in domainsList if any(js_file in d.js_files  for js_file in js_files)]
		return domainsList








