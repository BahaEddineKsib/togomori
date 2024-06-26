import json
import os
import GlobalVars as gv
import entities.domain as D
import pprint
import shutil
from personalizedPrint import pp

class Workshop:
	def __init__(self, ID, domains = []):
		self.ID      = ID

	def toJson(self):
		jsnWorkshop = self.__dict__
		return jsnWorkshop
	
	@staticmethod
	def jsonToWorkshop(wrk):
		Wor = Workshop(**wrk)
		return Wor

	@staticmethod
	def getPath(ID):
		return os.path.join(gv.DATABASE,"workshops", ID)

	@staticmethod
	def getDomainsPath(ID):
		return os.path.join(Workshop.getPath(ID),"domains")
	def save(self):
		if(Workshop.exist(self.ID)):
			return "WorkshopExist"
		else:
			workshop_path = Workshop.getPath(self.ID)
			domains_path  = Workshop.getDomainsPath(self.ID)
			os.mkdir(workshop_path)
			os.mkdir(  domains_path)
			return "WorkshopAdded"
	@staticmethod
	def exist(ID):
		return os.path.exists(Workshop.getPath(ID))

	@staticmethod
	def get(ID,expand = False):
		if Workshop.exist(ID):
			if not expand:
				return Workshop(ID)
			else:
				wrk = Workshop(ID)
				wrk.domains = sorted(os.listdir(Workshop.getDomainsPath(ID)))
				return wrk
		else:
			return Workshop("WorkshopNotFound")
	

	def display(self, expand = False):
		pprnt = pprint.PrettyPrinter(indent=4)
		if expand:
			pprnt.pprint(self.toJson())
			pp(msg=self.toJson(),print_it=False)
		else:
			pprnt.pprint(self.ID)
			pp(msg=self.ID,print_it=False)



	@staticmethod
	def delete(ID):
		if(ID == gv.CURRENT_WORKSHOP):
			return "WorkshopIsSet"
		elif(Workshop.exist(ID)):
			shutil.rmtree(Workshop.getPath(ID))
			return "WorkshopDeleted"
		else:
			return "WorkshopNotFound"

	@staticmethod
	def update(oldId,newId):
		if( not Workshop.exist(oldId)):
			return "WorkshopNotFound"
		elif(Workshop.exist(newId)):
			return "NewWorkshopIdExist"
		else:
			cw = gv.CURRENT_WORKSHOP
			gv.CURRENT_WORKSHOP = newId if cw == oldId else cw
			os.rename(Workshop.getPath(oldId), Workshop.getPath(newId))
			return "WorkshopUpdated"


	@staticmethod
	def getAll(expand=False):
		workshop_ids = sorted(os.listdir(os.path.join(gv.DATABASE,"workshops")))
		workshops    = []
		for ID in workshop_ids:
			wrk = Workshop.get(ID,expand)
			workshops.append(wrk)
		return workshops

