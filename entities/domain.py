import json
import os
import shutil
import pprint
import GlobalVars	 as gv
import entities.workshop as W
import entities.path	 as P
import tldextract	 as domain_parts
class Domain:
	def __init__(self, workshop_id,
			   domain	="", 
			   sub		="",
			   main		="",
			   tld		="",
			   tags		=[],
			   techs	=[],
			   whois_file	="",
			   ip		="", 
			   ports	={},
			   server_file	="",
			   robots_file	="",
			   js_files	=[],
			   paths	=[]):

		self.workshop_id= workshop_id
		self.domain	= domain
		if(domain):
			self.sub	= domain_parts.extract(domain).subdomain if sub  =="" else sub
			self.main	= domain_parts.extract(domain).domain    if main =="" else main
			self.tld	= domain_parts.extract(domain).suffix    if tld  =="" else tld
		else:
			self.sub = sub
			self.main= main
			self.tld = tld
		self.tags       = tags
		self.techs      = techs
		self.whois_file = whois_file
		self.ip         = ip
		self.ports      = ports
		self.server_file= server_file
		self.robots_file= robots_file
		self.js_files   = js_files
		self.paths	= paths       
	
	def setDomainParts(self):
		if(self.domain):
			self.sub  = domain_parts.extract(self.domain).subdomain 
			self.main = domain_parts.extract(self.domain).domain    
			self.tld  = domain_parts.extract(self.domain).suffix    


	def toJson(self):
		jsnDmn       = self.__dict__
		return jsnDmn

	@staticmethod
	def jsonToDomain(dmn):
		Dom	  = Domain(**dmn)
		return Dom

	@staticmethod
	def getPath(ID,domain):
		return os.path.join(W.Workshop.getDomainsPath(ID),domain)

	@staticmethod
	def getPathsPath(ID,domain):
		return os.path.join(Domain.getPath(ID,domain),"paths")

	@staticmethod
	def getJsonPath(ID,domain):
		return os.path.join(Domain.getPath(ID,domain),"domain.json")
	def save(self):
		if( not W.Workshop.exist(self.workshop_id )):
			return "WorkshopNotFound"
		elif(Domain.exist(self.workshop_id,self.domain)):
			return "DomainExist"
		else:
			domain_path = Domain.getPath(self.workshop_id,self.domain)
			paths_path  = Domain.getPathsPath(self.workshop_id,self.domain)
			json_path   = Domain.getJsonPath(self.workshop_id,self.domain)
			os.mkdir(domain_path)
			os.mkdir( paths_path)
			os.mknod(json_path)
			del self.workshop_id
			del self.domain
			with open(json_path,'w') as json_file:
				json.dump(self.toJson(),json_file)
			
			return "DomainAdded"

	@staticmethod
	def exist(ID,domain):
		return os.path.exists(Domain.getPath(ID,domain))

	@staticmethod
	def get(ID,domain,expand=False):
		if Domain.exist(ID,domain):
			with open(Domain.getJsonPath(ID,domain), 'r') as json_file:
				json_domain = json.load(json_file)
			json_domain["workshop_id"]	= ID
			json_domain["domain"]		= domain
			if expand: json_domain["paths"] =sorted([ P.Path.decode(p) for p in os.listdir(Domain.getPathsPath(ID,domain))])
			return Domain.jsonToDomain(json_domain)
		else:
			return "DomainNotFound"
			

	def display(self,toDisplay=['ALL'], expand=False):
		dmn={}
		if "ALL" in toDisplay or "workshop_id"	in toDisplay or expand:dmn["workshop_id"]  =self.workshop_id
		if "ALL" in toDisplay or "domain"	in toDisplay or expand:dmn["domain"]	 =self.domain
		if "ALL" in toDisplay or "sub"		in toDisplay or expand:dmn["sub"]		 =self.sub
		if "ALL" in toDisplay or "main"		in toDisplay or expand:dmn["main"]	 =self.main
		if "ALL" in toDisplay or "tld"		in toDisplay or expand:dmn["tld"]		 =self.tld
		if "ALL" in toDisplay or "tags"		in toDisplay or expand:dmn["tags"]         =self.tags 
		if "ALL" in toDisplay or "techs"	in toDisplay or expand:dmn["techs"]	 =self.techs 
		if "ALL" in toDisplay or "whois_file"	in toDisplay or expand:dmn["whois_file"]   =self.whois_file 
		if "ALL" in toDisplay or "ip"		in toDisplay or expand:dmn["ip"]           =self.ip 
		if "ALL" in toDisplay or "ports"	in toDisplay or expand:dmn["ports"]        =self.ports 
		if "ALL" in toDisplay or "server_file"	in toDisplay or expand:dmn["server_file"]  =self.server_file 
		if "ALL" in toDisplay or "robots_file"	in toDisplay or expand:dmn["robots_file"]  =self.robots_file 
		if "ALL" in toDisplay or "js_files"	in toDisplay or expand:dmn["js_files"]	 =self.js_files 
		if "ALL" in toDisplay or "paths"	in toDisplay or expand:dmn["paths"]	 = self.paths

		if len(dmn) == 1:
			dmn = next(iter(dmn.values()))
		pp = pprint.PrettyPrinter(indent=4)
		pp.pprint(dmn)


	@staticmethod
	def delete(domain,workshop_id):
		if( not W.Workshop.exist(workshop_id)):
			return "WorkshopNotFound"
		elif(not Domain.exist(workshop_id, domain)):
			return "DomainNotFound"
		else:
			shutil.rmtree(Domain.getPath(workshop_id,domain))
			if gv.CURRENT_DOMAIN == domain : gv.CURRENT_DOMAIN = ""
			return "DomainDeleted"

	@staticmethod
	def update(domain, workshop_id, new_dmn, hard_update = False):

		if(  not W.Workshop.exist(workshop_id) ):
			return "OldWorkshopNotFound"
		elif(not Domain.exist(workshop_id, domain)):
			return "DomainNotFound"
		elif(new_dmn.workshop_id and not W.Workshop.exist(new_dmn.workshop_id)):
			return "NewWorkshopNotFound"
		elif(new_dmn.domain and Domain.exist(new_dmn.workshop_id, new_dmn.domain)):
			return "DomainExist"
		else:
			dir_updated=False
			domain_vars_updated=False
			dmn = Domain.get(workshop_id, domain)
			for key,val in new_dmn.__dict__.items():
				if type(val) == str:
					if   val:
						if   key in ["workshop_id","domain"] : dir_updated = True
						elif key not in ["sub","main","tld"] : domain_vars_updated = True
						if   val == "_":
							dmn.__dict__[key] = ""
						elif val:
							dmn.__dict__[key] = val
				if type(val) == list:
					if val:
						domain_vars_updated = True
						if   val[0] == "+":
							del val[0]
							dmn.__dict__[key] += val
						elif val[0] == "_":
							del val[0]
							dmn.__dict__[key]  = [d for d in dmn.__dict__[key] if d not in val] if len(val) !=0 else []
						else:
							dmn.__dict__[key]  = val
				if type(val) == dict:
					if val:
						domain_vars_updated = True
						if(  next(iter(val.keys())) == "+"	):
							del val['+']
							dmn.__dict__[key].update(val)
						elif(next(iter(val.keys())) == "_"	):
							del val['_']
							if len(val)!=0:
								for k in  val.keys():
									if k in dmn.__dict__[key].keys():
										del dmn.__dict__[key][k]
							else:
								dmn.__dict__[key] = {}
						else:
							dmn.ports= val
			if dir_updated:
				shutil.move(Domain.getPath(workshop_id, domain),Domain.getPath(dmn.workshop_id, dmn.domain))
				dmn.setDomainParts()
			if dir_updated or domain_vars_updated:	
				json_path = Domain.getJsonPath(dmn.workshop_id,dmn.domain)
				del dmn.workshop_id
				del dmn.domain
				with open(json_path,'w') as json_file:
					json.dump(dmn.toJson(),json_file)

			return "DomainUpdated"

	@staticmethod
	def getAll(ID, expand=False):
		if W.Workshop.exist(ID):
			domain_names = sorted(os.listdir(W.Workshop.getDomainsPath(ID)))
			domains	     = []
			for d in domain_names:
				d = Domain.get(ID,d,expand)
				domains.append(d)
			return domains

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

		domainsList= Domain.getAll(workshop_id)
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








