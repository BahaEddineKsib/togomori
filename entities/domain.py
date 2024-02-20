import json
import os
import GlobalVars as TopG
import entities.workshop as W
import pprint
class Domain:
	def __init__(self, workshop_id,
			   domain_text     ="", 
			   tags            =[],
			   techs_list      =[],
			   whois_file      ="",
			   ip              ="", 
			   ports_map       ={},
			   server_file     ="",
			   robots_txt_file ="",
			   js_files_list   =[]):
		self.workshop_id     = workshop_id
		self.domain_text     = domain_text
		self.tags            = tags
		self.techs_list      = techs_list
		self.whois_file      = whois_file
		self.ip              = ip 
		self.ports_map       = ports_map
		self.server_file     = server_file
		self.robots_txt_file = robots_txt_file
		self.js_files_list   = js_files_list

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
		elif(Domain.searchInWorkshop(self.domain_text,wrk) != "DomainNotFound"):
			return "DomainExist"
		else:
			wrk.domains.append(self)
			wrk.update()
			return "DomainAdded"
	
	@staticmethod
	def delete(domain_text,workshop_id):
		wrk = W.Workshop.search(workshop_id)
		if( wrk == "WorkshopNotFound"):
			return "WorkshopNotFound"
		elif(Domain.searchInWorkshop(domain_text,wrk) == "DomainNotFound"):
			return "DomainNotFound"
		else:
			wrk.domains = [d for d in wrk.domains if d.domain_text != domain_text]
			wrk.update()
			return "DomainDeleted"

	def display(self,toDisplay=['ALL']):
		dmn={}
		if "ALL" in toDisplay or "workshop_id" in toDisplay:     dmn["workshop_id"]     =self.workshop_id
		if "ALL" in toDisplay or "domain_text" in toDisplay:     dmn["domain_text"]     =self.domain_text 
		if "ALL" in toDisplay or "tags" in toDisplay:            dmn["tags"]            =self.tags 
		if "ALL" in toDisplay or "techs_list" in toDisplay:      dmn["techs_list"]      =self.techs_list 
		if "ALL" in toDisplay or "whois_file" in toDisplay:      dmn["whois_file"]      =self.whois_file 
		if "ALL" in toDisplay or "ip" in toDisplay:              dmn["ip"]              =self.ip 
		if "ALL" in toDisplay or "ports_map" in toDisplay:       dmn["ports_map"]       =self.ports_map 
		if "ALL" in toDisplay or "server_file" in toDisplay:     dmn["server_file"]     =self.server_file 
		if "ALL" in toDisplay or "robots_txt_file" in toDisplay: dmn["robots_txt_file"] =self.robots_txt_file 
		if "ALL" in toDisplay or "js_files_list" in toDisplay:   dmn["js_files_list"]   =self.js_files_list 

		pp = pprint.PrettyPrinter(indent=4)
		pp.pprint(dmn)

	@staticmethod
	def getDomainsByWorkshop(wrk):
		return wrk.domains
	@staticmethod
	def searchInWorkshop(domain_text,wrk):
		for dmn in wrk.domains:
			if(dmn.domain_text==domain_text):
				return dmn
		return "DomainNotFound"

	@staticmethod
	def searchBy(      workshop_id,
		           domain_text     =False, 
			   tags            =False,
			   techs_list      =False,
			   whois_file      =False,
			   ip              =False, 
			   ports_map       =False,
			   server_file     =False,
			   robots_txt_file =False,
			   js_files_list   =False):
		
		domainsList=[]

		domainsList= domainsList if not workshop_id	else Domain.getDomainsByWorkshop(W.Workshop.search(workshop_id))
		domainsList= domainsList if not domain_text	else [d for d in domainsList if d.domain_text == domain_text]
		domainsList= domainsList if not tags		else [d for d in domainsList if any(tag  in d.tags              for tag  in tags)]
		domainsList= domainsList if not ports_map	else [d for d in domainsList if any(port in d.ports_map.items() for port in ports_map.items())]
		domainsList= domainsList if not techs_list	else [d for d in domainsList if any(tech in d.techs_list        for tech in techs_list)]
		domainsList= domainsList if not whois_file	else [d for d in domainsList if d.whois_file == whois_file]
		domainsList= domainsList if not ip		else [d for d in domainsList if d.ip == ip]
		domainsList= domainsList if not server_file     else [d for d in domainsList if d.server_file == server_file]
		domainsList= domainsList if not robots_txt_file else [d for d in domainsList if d.robots_txt_file== robots_txt_file]
		domainsList= domainsList if not js_files_list   else [d for d in domainsList if any(js_file in d.js_files_list  for js_file in js_files_list)]
		return domainsList








