import json
import os
class Workshop:
	default_path=os.getcwd()+"/data"
	def __init__(self, id, path):
		self.id  = id
		self.path= path
	
	def toJSON(self):
		return json.dumps(wrkshp.__dict__)
	
	def save(self):
		cwd = os.getcwd()
		print(cwd)
		
	def display(self):
		print("WORKSHOP:")
		print("\t id  : ",self.id)
		print("\t path: ",self.path)
		
		
		
#wrkshp = Workshop("pfeEsprit","/azer/azer/azer")
#print(wrkshp.toJSON())
