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

	@staticmethod
	def update(domain_text, workshop_id, new_dmn):
		old_wrk = W.Workshop.search(workshop_id)
		new_wrk = W.Workshop.search(new_dmn.workshop_id)        if new_dmn.workshop_id           else ""
		old_dmn = Domain.searchInWorkshop(domain_text, old_wrk) if old_wrk != "WorkshopNotFound" else ""

		if( old_wrk == "WorkshopNotFound" ):
			return "OldWorkshopNotFound"
		elif(old_dmn == "DomainNotFound"):
			return "DomainNotFound"
		elif(new_wrk == "WorkshopNotFound"):
			return "NewWorkshopNotFound"
		elif(new_wrk and Domain.searchInWorkshop(new_dmn.domain_text, new_wrk) != "DomainNotFound"):
			return "DomainExist"
		else:
			old_dmn.domain_text	= new_dmn.domain_text	  if new_dmn.domain_text	else old_dmn.domain_text
			old_dmn.whois_file	= new_dmn.whois_file	  if new_dmn.whois_file		else old_dmn.whois_file
			old_dmn.ip		= new_dmn.ip		  if new_dmn.ip			else old_dmn.ip
			old_dmn.server_file	= new_dmn.server_file	  if new_dmn.server_file	else old_dmn.server_file
			old_dmn.robots_txt_file = new_dmn.robots_txt_file if new_dmn.robots_txt_file	else old_dmn.robots_txt_file
			old_dmn.workshop_id     = new_dmn.workshop_id     if new_wrk                    else old_dmn.workshop_id
			if new_dmn.js_files_list:	
				if(  '+' == new_dmn.js_files_list[0]	):
					old_dmn.js_files_list += new_dmn.js_files_list; old_dmn.js_files_list.remove('+')
				elif('_' == new_dmn.js_files_list[0]	):
					old_dmn.js_files_list = [ d for d in old_dmn.js_files_list if d not in new_dmn.js_files_list ]
				else:
					old_dmn.js_files_list  = new_dmn.js_files_list

			if new_dmn.tags:	
				if(  '+' == new_dmn.tags[0]	):
					old_dmn.tags+= new_dmn.tags; old_dmn.tags.remove('+')
				elif('_' == new_dmn.tags[0]	):
					old_dmn.tags= [ d for d in old_dmn.tags if d not in new_dmn.tags]
				else:
					old_dmn.tags= new_dmn.tags

			if new_dmn.techs_list:	
				if(  '+' == new_dmn.techs_list[0]	):
					old_dmn.techs_list+= new_dmn.techs_list; old_dmn.techs_list.remove('+')
				elif('_' == new_dmn.techs_list[0]	):
					old_dmn.techs_list= [ d for d in old_dmn.techs_list if d not in new_dmn.techs_list]
				else:
					old_dmn.techs_list= new_dmn.techs_list
			if new_dmn.ports_map:	
				if(  '+' == next(iter(new_dmn.ports_map.keys()))	):
					old_dmn.ports_map.update(new_dmn.ports_map); del old_dmn.ports_map['+']
				elif('_' == next(iter(new_dmn.ports_map.keys()))):
					old_dmn.ports_map.update(new_dmn.ports_map);
					for key in  new_dmn.ports_map.keys():
						del old_dmn.ports_map[key]
				else:
					old_dmn.ports_map= new_dmn.ports_map

			Domain.delete(domain_text,workshop_id)
			old_dmn.save()
			return "DomainUpdated"


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








