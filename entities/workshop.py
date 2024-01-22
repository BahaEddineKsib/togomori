import json
import os


	
class Workshop:
	default_path=os.getcwd()+"/data"
	def __init__(self, id, path):
		self.id  = id
		self.path= path
	
	def toJson(self):
		return json.dumps(self.__dict__,indent=4)
	
	def save(self):
		if(check_workshop_uniqeness(self.id)):
			if(savePath(self.path)):
				workshopDirectory = self.path+'/'+self.id
				workshopJsonFile  = workshopDirectory+'/'+self.id
				os.mkdir(workshopDirectory)
				os.mknod(workshopJsonFile)
				saveJson(workshopJsonFile, self.toJson())
				print("✅:",self.id,"is Added")
			else:
				print("❌: this path doesn't exist")
			
		else:
			print("❌: This Workshop ID , already exist")
		
	def display(self):
		print("\nWORKSHOP:")
		print(self.toJson())


def check_workshop_uniqeness(id):
	paths_file = open(os.getcwd()+'/data/paths', 'r')
	paths = paths_file.readlines()
	for path in paths:
		path=path[0:len(path)-1:1]
		if(os.path.exists(path+'/'+id)):
			paths_file.close()
			return False
	paths_file.close()
	return True

def savePath(path):
	if(os.path.exists(path)):
		paths_file = open(os.getcwd()+'/data/paths', 'r')
		paths = paths_file.readlines()
		pathIsSaved = False
		for line in paths:
			if path+'\n' == line:
				pathIsSaved = True
				break
		paths_file.close()
	
		if(not pathIsSaved):
			paths_file = open(os.getcwd()+'/data/paths', 'a')
			paths_file.writelines(path+'\n')
		return True
	else:
		return False

def saveJson(path, jsonObj):
		jsonObj_file = open(path, 'a')
		jsonObj_file.writelines(jsonObj+'\n')
