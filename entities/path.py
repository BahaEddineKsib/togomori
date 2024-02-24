import entities.workshop as W
import entities.domain   as D

class Path:
	def __init__(self, domain="", path="",variables=[]):
		self.domain		= domain
		self.path		= path
		self.variables		= variables
	
	def toJson(self):
		jsnPath	= self.__dict__
		return jsnPath

	@staticmethod
	def jsonToPath(pth):
		return Path(**pth)

	def save(self,workshop_id):
		wrk = W.Workshop.search(workshop_id)
		dmn = D.Domain.searchInWorkshop(self.domain,wrk) if wrk != "WorkshopNotFound" else ""
		if(  wrk == "WorkshopNotFound" ):
			return "WorkshopNotFound"
		elif(dmn == "DomainNotFound"):
			return "DomainNotFound"
		elif(Path.searchInDomain(self.path, dmn)  != "PathNotFound"):
			return "PathExist"
		else:

			dmn.paths.append(self)
			dmn.update()
			return "PathAdded"
	def display(self):
		print(self.domain+self.path)
		print(' '*len(self.domain) + '~'*len(self.path))
	

	@staticmethod
	def searchInDomain(path,dmn):
		for pth in dmn.paths:
			if(pth.path==path):
				return pth
		return "PathNotFound"


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
