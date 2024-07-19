import entities.workshop as W
import entities.domain   as D
import os
import json
import shutil
from personalizedPrint import pp
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
		return path.replace("/","_BS_")
	@staticmethod
	def decode(path):
		return path.replace("_BS_","/")

	@staticmethod
	def jsonToPath(pth):
		return Path(**pth)

	@staticmethod
	def getPath(ID,domain,path):
		path = Path.encode(path)
		return os.path.join(D.Domain.getPathsPath(ID,domain),path)

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
			json_path = Path.getJsonPath(workshop_id, self.domain, self.path)
			os.mkdir(path_path)
			os.mknod(json_path)
			del self.domain
			del self.path
			try:
				with open(json_path,'w') as json_file:
					json.dump(self.toJson(), json_file)
				return "PathAdded"
			except Exception as e:
				print(e)
				return 

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
			return Path.jsonToPath(json_path)
		else:
			return "PathNotFound"

	def display(self,select=False, expand=False, very_expand=False):

		to_prnt = self.path
		if expand:
			to_prnt = self.domain+to_prnt
		if very_expand:
			to_prnt = self.toJson()
		pp(to_prnt)
		if(select and not very_expand):
			to_prnt = '_'*len(self.domain) + '~'*len(self.path) if expand else '~'*len(self.path)
			pp(to_prnt)


	@staticmethod
	def delete(path, domain, workshop_id):
		if(  not W.Workshop.exist(workshop_id)):
			return "WorkshopNotFound"
		elif(not D.Domain.exist(workshop_id, domain)):
			return "DomainNotFound"
		elif(not Path.exist(workshop_id,domain,path)):
			return "PathNotFound"
		else:
			shutil.rmtree(Path.getPath(workshop_id, domain, path))
			return "PathDeleted"

	
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
				if type(val) == dict:
					if val:
						path_vars_updated = True
						if(  next(iter(val.keys())) == "+"):
							del val['+']
							pth.__dict__[key].update(val)
						elif(next(iter(val.keys())) == "_"):
							del val['_']
							if len(val)!=0:
								for k in  val.keys():
									if k in pth.__dict__[key].keys():
										del pth.__dict__[key][k]
							else:
								pth.__dict__[key] = {}
						else:
							pth.__dict__[key]= val

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
				
