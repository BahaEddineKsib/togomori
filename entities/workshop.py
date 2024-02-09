import json
import os



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
				
			print("✅:",self.id,"is Added")
		else:
			print("❌: This Workshop ID , already exist")
	
	def display(self):
		print(self.toJson())


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






	#yeeyy
