import json
import os
import GlobalVars as TopG
import entities.workshop as W

class Domain:
	def __init__(self, workshop_id,
			   domain_text     ="", 
			   tag             ="main",
			   techs_list      =[],
			   whois_file      ="",
			   ip              ="", 
			   ports_map       ={},
			   server_file     ="",
			   robots_txt_file ="",
			   js_files_list   =[]):
		self.workshop_id     = workshop_id
		self.domain_text     = domain_text
		self.tag             = tag
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
		elif(Domain.getMain(wrk) != "NoMainDomain"):
			return "MainDomainExist"
		else:
			wrk.domains.append(self)
			wrk.update()
			return "DomainAdded"

	def display(self):
		print(self.toJson())
	
	@staticmethod
	def getMain(wrk):
		mDom = [ wd for wd in wrk.domains if wd.tag == "main"]
		if(mDom):
			return mDom[0]
		else:
			return "NoMainDomain"

	@staticmethod
	def getDomainsByWorkshop(wrk):
		return wrk.domains
	@staticmethod
	def searchInWorkshop(domain_text,wrk):
		for dmn in wrk.domains:
			if(dmn.domain_text==domain_text):
				return dmn
		return "DomainNotFound"
