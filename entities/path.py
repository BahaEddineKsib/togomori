import entities.workshop as W
import entities.domain   as D
import os
import json
import shutil

class Path:
	def __init__(self, domain="", path="", tags=[], variables={}):
		self.domain	= domain
		self.path	= path
		self.tags	= tags
		self.variables	= variables
	
	def toJson(self):
		jsnPath	= self.__dict__
		return jsnPath

	@staticmethod
	def encode(path):
		return path.replace("/","[BS]")
	@staticmethod
	def decode(path):
		return path.replace("[BS]","/")

	@staticmethod
	def jsonToPath(pth):
		return Path(**pth)

	@staticmethod
	def getPath(ID,domain,path):
		path = Path.encode(path)
		return os.path.join(D.Domain.getPathsPath(ID,domain),path)

	@staticmethod
	def getVariablesPath(ID,domain,path):
		return os.path.join(Path.getPath(ID,domain,path),"variables")

	@staticmethod
	def getJsonPath(ID, domain, path):
		return os.path.join(Path.getPath(ID,domain,path),"path.json")

	def save(self,workshop_id):
		if(  not W.Workshop.exist(workshop_id) ):
			return "WorkshopNotFound"
		elif(not D.Domain.exist(workshop_id,self.domain)):
			return "DomainNotFound"
		elif(Path.exist(workshop_id, self.domain, self.path)):
			return "PathExist"
		else:
			path_path = Path.getPath(workshop_id, self.domain, self.path)
			vars_path = Path.getVariablesPath(workshop_id,self.domain,self.path)
			json_path = Path.getJsonPath(workshop_id, self.domain, self.path)
			os.mkdir(path_path)
			os.mkdir(vars_path)
			os.mknod(json_path)
			del self.domain
			del self.path
			del self.variables
			with open(json_path,'w') as json_file:
				json.dump(self.toJson(), json_file)
			return "PathAdded"

	@staticmethod
	def exist(ID, domain, path):
		return os.path.exists(Path.getPath(ID, domain, path))

	@staticmethod
	def get(ID, domain, path, expand=False):
		if Path.exist(ID,domain,path):
			with open(Path.getJsonPath(ID,domain,path), 'r') as json_file:
				json_path = json.load(json_file)
			json_path["domain"]		= domain
			json_path["path"]		= path
			#if expand: json_domain["paths"] =sorted(os.listdir(Domain.getPathsPath(ID,domain)))
			return Path.jsonToPath(json_path)
		else:
			return "PathNotFound"

	def display(self,select=False, expand=False, very_expand=False):

		to_prnt = self.path
		if expand:
			to_prnt = self.domain+to_prnt
		if very_expand:
			to_prnt = self.toJson()
		print(to_prnt)
		if(select and not very_expand):
			to_prnt = '_'*len(self.domain) + '~'*len(self.path) if expand else '~'*len(self.path)
			print(to_prnt)
	
	
	@staticmethod
	def update(workshop_id, domain, path, new_pth):
		if(  not W.Workshop.exist(workshop_id) ):
			return "WorkshopNotFound"
		elif(not D.Domain.exist(workshop_id, domain)):
			return "DomainNotFound"
		elif(not Path.exist(workshop_id,domain,path)):
			return "PathNotFound"
		elif(new_pth.domain and not D.Domain.exist(workshop_id, new_pth.domain)):
			return "NewDomainNotFound"
		elif(new_pth.path and Path.exist(workshop_id, new_pth.domain,new_pth.path)):
			return "NewPathExist"
		else:
			dir_updated=False
			path_vars_updated=False
			pth = Path.get(workshop_id, domain, path)
			for key,val in new_pth.__dict__.items():
				if type(val) == str:
					if   val:
						if   key in ["domain","path"] : dir_updated = True
						else:path_vars_updated = True
						if   val == "_":
							pth.__dict__[key] = ""
						elif val:
							pth.__dict__[key] = val
				if type(val) == list:
					if val:
						path_vars_updated = True
						if   val[0] == "+":
							del val[0]
							pth.__dict__[key] += val
						elif val[0] == "_":
							del val[0]
							pth.__dict__[key]  = [p for p in pth.__dict__[key] if p not in val] if len(val) !=0 else []
						else:
							pth.__dict__[key]  = val

			if dir_updated:
				shutil.move(Path.getPath(workshop_id, domain, path),Path.getPath(workshop_id,pth.domain, pth.path))
			if path_vars_updated:	
				json_path = Path.getJsonPath(workshop_id,pth.domain, pth.path)
				del pth.path
				del pth.domain
				with open(json_path,'w') as json_file:
					json.dump(pth.toJson(),json_file)

			return "PathUpdated"



	@staticmethod
	def getByDomain(domain,workshop_id):
		if( not W.Workshop.exist(workshop_id) ):
			return "WorkshopNotFound"
		elif( not D.Domain.exist(workshop_id, domain) ):
			return "DomainNotFound"
		else:
			return [Path.get(workshop_id,domain,Path.decode(p)) for p in D.Domain.get(workshop_id,domain,True).paths]

			



	@staticmethod
	def getAll(workshop_id):
		if( not W.Workshop.exist(workshop_id) ):
			return "WorkshopNotFound"
		else:
			paths=[]
			for dmn in W.Workshop.get(workshop_id,True).domains:
				paths += Path.getByDomain(dmn,workshop_id)

			return paths
				



	'''
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


	@staticmethod
	def getDomainsByWorkshop(wrk):
		return wrk.domains

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
'''
