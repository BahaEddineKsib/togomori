import json
import os
import GlobalVars as TopG
import entities.domain as D
import pprint
class Workshop:
	def __init__(self, id, domains:[D.Domain] = []):
		self.id      = id
		self.domains = domains

	def toJson(self):
		jsnWorkshop = self.__dict__
		jsnWorkshop['domains'] = [ dmn.toJson() for dmn in self.domains]
		return jsnWorkshop
	
	@staticmethod
	def jsonToWorkshop(wrk):
		Wor = Workshop(**wrk)
		Wor.domains = [D.Domain.jsonToDomain(dmn) for dmn in Wor.domains]
		return Wor


	def save(self):
		if(Workshop.search(self.id) == "WorkshopNotFound"):

			wrkList = Workshop.getAllWorkshops()
			
			wrkList.append(self)

			jsnList = [w.toJson() for w in wrkList]
			json_data = {"workshops": jsnList}
			with open(TopG.JSON_DATABASE, 'w') as workshops_file:
				json.dump(json_data, workshops_file)
				
			return "WorkshopAdded"
		else:
			return "WorkshopExist"
	
	def display(self, expand = False):
		pp = pprint.PrettyPrinter(indent=4)
		if expand:
			pp.pprint(self.toJson())
		else:
			self.domains = [ d.domain for d in self.domains]
			pp.pprint(self.__dict__)


	@staticmethod
	def deleteById(id, temporary_delete=0):
		
		if(id == TopG.CURRENT_WORKSHOP and temporary_delete == 0 ):
			return "WorkshopIsSet"
		elif(Workshop.search(id) == "WorkshopNotFound"):
			return "WorkshopNotFound"
		else:
			wrkList = Workshop.getAllWorkshops()
			jsnList = [w.toJson() for w in wrkList if w.id != id]

			json_data = {"workshops": jsnList}
			with open(TopG.JSON_DATABASE, 'w') as workshops_file:
				json.dump(json_data, workshops_file)

			return "WorkshopDeleted"

	@staticmethod
	def updateId(oldId,newId):
		wrk = Workshop.search(oldId)
		if(wrk == "WorkshopNotFound"):
			return "WorkshopNotFound"
		elif(Workshop.search(newId) != "WorkshopNotFound"):
			return "NewWorkshopIdExist"
		else:
			cw = TopG.CURRENT_WORKSHOP
			TopG.CURRENT_WORKSHOP = newId if cw == oldId else cw
			Workshop.deleteById(oldId, temporary_delete=1)
			wrk.id = newId
			for dmn in wrk.domains:
				dmn.workshop_id = newId
			wrk.save()
			return "WorkshopUpdated"

	def update(self):
		Workshop.deleteById(self.id, temporary_delete=1)
		self.save()

	@staticmethod
	def getAllWorkshops():
		listObj = []
		with open(TopG.JSON_DATABASE, 'r') as workshops_file:
			listObj = json.load(workshops_file)

		wrkList = []
		for wrk in listObj.get("workshops", []):
			wrkList.append(Workshop.jsonToWorkshop(wrk))

		return wrkList
	
	@staticmethod
	def search(id):
		for wrk in Workshop.getAllWorkshops():
			if(id == wrk.id):
				return wrk
		return "WorkshopNotFound"
