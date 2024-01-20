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
		if(check_workshop_uniqeness(self.id)):
			
			savePath(self.path)
		else:
			print("This Workshop ID , already exist")
		
	def display(self):
		print("WORKSHOP:")
		print("\t id  : ",self.id)
		print("\t path: ",self.path)


def check_workshop_uniqeness(id):
	paths_file = open(os.getcwd()+'/data/paths', 'r')
	paths = paths_file.readlines()
	for path in paths:
		if(os.path.exists(path+''+id)):
			paths_file.close()
			return False
	paths_file.close()
	return True

def savePath(path):
	paths_file = open(os.getcwd()+'/data/paths', 'r')
	paths = paths_file.readlines()
	pathIsSaved = False
	for line in paths:
		print("\nline: ",line)
		if path+'\n' == line:
			pathIsSaved = True
			break 
	paths_file.close()
	
	if(not pathIsSaved):
		paths_file = open(os.getcwd()+'/data/paths', 'a')
		paths_file.writelines(path+'\n')
	
