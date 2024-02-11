import json
import os
import GlobalVars as TopG


class Workshop:
	def __init__(self, id):
		self.id  = id

	def toJson(self):
		return json.dumps(self.__dict__)

	def save(self):
		if(Workshop.search(self.id) == "WorkshopNotFound"):

			listObj = Workshop.getAllWorkshops()
			listObj.append(self.__dict__)
	                
			json_data = {"workshops": listObj}
			with open(os.getcwd()+'/data/workshops.json', 'w') as workshops_file:
				json.dump(json_data, workshops_file)
				
			return "WorkshopAdded"
		else:
			return "WorkshopExist"
	
	def display(self):
		print(self.toJson())


	@staticmethod
	def deleteById(id):
		
		if(id == TopG.CURRENT_WORKSHOP):
			return "WorkshopIsSet"
		elif(Workshop.search(id) == "WorkshopNotFound"):
			return "WorkshopNotFound"
		else:
			wlist = Workshop.getAllWorkshops()
			wlist = [w for w in wlist if w["id"] != id]

			json_data = {"workshops": wlist}
			with open(os.getcwd()+'/data/workshops.json', 'w') as workshops_file:
				json.dump(json_data, workshops_file)

			return "WorkshopDeleted"

	@staticmethod
	def getAllWorkshops():
		listObj = []
		with open(os.getcwd()+'/data/workshops.json', 'r') as workshops_file:
			listObj = json.load(workshops_file)
		
		return listObj.get("workshops", [])
	
	@staticmethod
	def search(id):
		for wrk in Workshop.getAllWorkshops():
			if(id == wrk['id']):
				return Workshop(wrk['id'])
		return "WorkshopNotFound"
