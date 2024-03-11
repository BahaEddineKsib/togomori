from commands.CRUDs.workshop.setWorkshop     import SetWorkshop 
from commands.CRUDs.workshop.unsetWorkshop   import UnsetWorkshop
from commands.CRUDs.workshop.addWorkshop     import AddWorkshop 
from commands.CRUDs.workshop.displayWorkshop import DisplayWorkshop
from commands.CRUDs.workshop.deleteWorkshop  import DeleteWorkshop
from commands.CRUDs.workshop.updateWorkshop  import UpdateWorkshop
from commands.CRUDs.domain.addDomain         import AddDomain
from commands.CRUDs.domain.displayDomain     import DisplayDomain
from commands.CRUDs.domain.deleteDomain      import DeleteDomain
from commands.CRUDs.domain.updateDomain      import UpdateDomain
from commands.CRUDs.domain.setDomain	     import SetDomain
from commands.CRUDs.domain.unsetDomain	     import UnsetDomain
from commands.CRUDs.path.addPath	     import AddPath
from commands.CRUDs.path.displayPath	     import DisplayPath
from commands.CRUDs.path.updatePath	     import UpdatePath
from executor import execute
from GlobalVars				     import DATABASE      as db
import unittest
import json
import sys
import shutil
import os

class UTT(unittest.TestCase):

	def test_1111_AddWorkshop(self):
		self.assertEQUAL(AddWorkshop,"addw workshop1 -s","WorkshopAdded",PAUSE)
		self.assertEQUAL(AddWorkshop,"addw workshop2 -s","WorkshopAdded")
		self.assertEQUAL(AddWorkshop,"addw workshop3 -s","WorkshopAdded")
		self.assertEQUAL(AddWorkshop,"addw workshop1 -s","WorkshopExist",PAUSE)
		self.assertEQUAL(AddWorkshop,"addw -s"		,"UserNeedsHelp",PAUSE)
		self.assertEQUAL(AddWorkshop,"addw"		,"UserNeedsHelp",PAUSE)


	def test_1112_AddDomain(self):
		self.assertEQUAL(AddDomain,"ad -d www.domain1.tn -w workshop1"+
						   " -s --tag tag1  tag2 tag3 --tech"+
						   " java react --whois /data/whois.txt"+
						   " --ip 192.168.0.1 --port https:448 ssh:25"+
						   " --server /nmap/scan --robots /data/robots.txt --js /js1 /js2 /js3"	,"DomainAdded"		,PAUSE)
		self.assertEQUAL(AddDomain,"ad -d www.domain2.tn --tag tag2 -w workshop1 -s"			,"DomainAdded"		,PAUSE)
		self.assertEQUAL(AddDomain,"ad -d www.domain3.tn --tag tag3 -w workshop1 -s"			,"DomainAdded"		,PAUSE)
		self.assertEQUAL(AddDomain,"ad -d www.domain1.tn -w workshop1 -s"				,"DomainExist"		,PAUSE)
		self.assertEQUAL(AddDomain,"ad -d www.t.tn    -w TTTTTT -s"					,"WorkshopNotFound"	,PAUSE)
		self.assertEQUAL(AddDomain,"ad -d www.t.tn    -w workshop1 --port https:8585 :85 -s"		,"WrongPortFormat"	,PAUSE)
		self.assertEQUAL(AddDomain,"ad -d www.t.tn    -w workshop1 --port https: -s"			,"WrongPortFormat"	,PAUSE)
		self.assertEQUAL(AddDomain,"ad -d www.t.tn    -w"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain,"ad -d www.t.tn --tag"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain,"ad -d www.t.tn --tech"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain,"ad -d www.t.tn --whois"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain,"ad -d www.t.tn --ip"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain,"ad -d www.t.tn --port"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain,"ad -d www.t.tn --server"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain,"ad -d www.t.tn --robots"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain,"ad -d www.t.tn --js"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain,"ad"									,"UserNeedsHelp")
	
	def test_1113_AddPath(self):
		self.assertEQUAL(AddPath,"ap www.domain1.tn/path/1 -w workshop1 --tag tag1 tag2 tag3 -s","PathAdded"	   ,PAUSE)
		self.assertEQUAL(AddPath,"ap /path/2 -d www.domain1.tn -w workshop1 -s"			,"PathAdded"	   ,PAUSE)
		self.assertEQUAL(AddPath,"ap  www.watever.tn/ -w workshop1 -s"				,"DomainNotFound"  ,PAUSE)
		self.assertEQUAL(AddPath,"ap  www.domain1.tn/    -w whatever -s"			,"WorkshopNotFound",PAUSE)
		self.assertEQUAL(AddPath,"ap /path/1          -w workshop1 -s"				,"NoDomainSetted"  ,PAUSE)
		self.assertEQUAL(AddPath,"ap  www.domain1.tn/p -s"					,"NoWorkshopSetted",PAUSE)
		print('setworkshop workshop1 \n setdomain www.domain1.tn')
		SetWorkshop.execute("setw workshop1")
		SetDomain.execute("setd www.domain1.tn")
		self.assertEQUAL(AddPath,"ap /path/3  -s"			,"PathAdded"	,PAUSE)
		self.assertEQUAL(AddPath,"ap /path/4/dmn2 -d www.domain2.tn -s"	,"PathAdded"	,PAUSE)
		self.assertEQUAL(AddPath,"ap /path/1  -s"			,"PathExist"	,PAUSE)
		self.assertEQUAL(AddPath,"ap  path/1  -s"			,"InvalidPath"	,PAUSE)
		self.assertEQUAL(AddPath,"ap /path/1/ -s"			,"PathAdded"	,PAUSE)
		self.assertEQUAL(AddPath,"ap"					,"UserNeedsHelp")
		#print('unsetworkshop')
		UnsetWorkshop.execute("usw")
		UnsetDomain.execute("usd")
	
	def test_1114_DisplayWorkshop(self):
		self.assertEQUAL(DisplayWorkshop,"dw -w workshop1"   ,"workshop1"				,PAUSE)
		self.assertEQUAL(DisplayWorkshop,"dw -w workshop1 -x","workshop1"				,PAUSE)
		self.assertEQUAL(DisplayWorkshop,"dw -w workshop "   ,"WorkshopNotFound"			,PAUSE)
		self.assertEQUAL(DisplayWorkshop,"dw -A"	     ,["workshop1","workshop2","workshop3"]	,PAUSE)
		self.assertEQUAL(DisplayWorkshop,"dw -A -x"	     ,["workshop1","workshop2","workshop3"]	,PAUSE)

	def test_1115_DisplayDomain(self):
		SetWorkshop.execute("setw workshop1")
		self.assertEQUAL(DisplayDomain,"dd -d www.domain1.tn"		     , "www.domain1.tn"					  ,PAUSE)
		self.assertEQUAL(DisplayDomain,"dd -d www.domain1.tn --show paths"   , "www.domain1.tn"					  ,PAUSE)
		self.assertEQUAL(DisplayDomain,"dd -d www.domain1.tn --show paths -x", "www.domain1.tn"					  ,PAUSE)
		self.assertEQUAL(DisplayDomain,"dd -A "				     ,["www.domain1.tn","www.domain2.tn","www.domain3.tn"],PAUSE)
		self.assertEQUAL(DisplayDomain,"dd -A --show ALL"		     ,["www.domain1.tn","www.domain2.tn","www.domain3.tn"],PAUSE)
		self.assertEQUAL(DisplayDomain,"dd -A --port https:8585 :85"	     ,"WrongPortFormat"					  ,PAUSE)
		self.assertEQUAL(DisplayDomain,"dd -A --port https: -s"		     ,"WrongPortFormat"					  ,PAUSE)
		self.assertEQUAL(DisplayDomain,"dd -d  www.t.tn"		     ,"DomainNotFound")
		self.assertEQUAL(DisplayDomain,"dd -A --tag tag2"		     ,["www.domain1.tn","www.domain2.tn"]		  ,PAUSE)
		self.assertEQUAL(DisplayDomain,"dd -A --tag"			     ,"UserNeedsHelp")
		self.assertEQUAL(DisplayDomain,"dd -A -w whatever"		     ,"WorkshopNotFound")
	
	def test_1116_DisplayPath(self):
		#UnsetDomain.execute("usd")
		self.assertEQUAL(DisplayPath,"dp -p www.domain1.tn/path/1"	,"/path/1"						  ,PAUSE)
		self.assertEQUAL(DisplayPath,"dp -d www.domain1.tn -a"		,["/path/1","/path/1/","/path/2","/path/3"]		  ,PAUSE)
		self.assertEQUAL(DisplayPath,"dp -A"				,['/path/1','/path/1/','/path/2','/path/3','/path/4/dmn2'],PAUSE)
		self.assertEQUAL(DisplayPath,"dp -p www.domain1.tn"		,"NoPath"						  ,PAUSE)
		self.assertEQUAL(DisplayPath,"dp -p my/path   -d www.domain1.tn","InvalidPath"						  ,PAUSE)
		self.assertEQUAL(DisplayPath,"dp -p /whatever -d www.whatever.t","DomainNotFound"					  ,PAUSE)
		self.assertEQUAL(DisplayPath,"dp -p /whatever -d www.domain1.tn","PathNotFound"						  ,PAUSE)
		self.assertEQUAL(DisplayPath,"dp -A -w whatever"		,"WorkshopNotFound"					  ,PAUSE)
		self.assertEQUAL(DisplayPath,"dp -a"				,"NoDomainSetted"					  ,PAUSE)
		UnsetWorkshop.execute("usw")
		self.assertEQUAL(DisplayPath,"dp -A"				,"NoWorkshopSetted"					  ,PAUSE)
		SetWorkshop.execute("sw workshop1")

	def test_1117_UpdatePath(self):
		self.assertEQUAL(UpdatePath,"updatepath /path/2 -d www.domain1.tn --p /path/two -s"		,"PathUpdated",PAUSE)
		self.assertEQUAL(UpdatePath,"updatepath www.domain1.tn/path/1 --p www.domain2.tn/path/1/ -s"	,"PathUpdated",PAUSE)

	def test_1118_UpdateDomain(self):
		self.assertEQUAL(UpdateDomain,"updatedomain www.domain1.tn -d www.updated_domain.tn -s"				,"DomainUpdated",PAUSE)
		self.assertEQUAL(UpdateDomain,"updated www.updated_domain.tn --w workshop2 -s"					,"DomainUpdated",PAUSE)
		self.assertEQUAL(UpdateDomain,"updated www.updated_domain.tn -d www.u_domain.tn -w workshop2 --w workshop1 -s"	,"DomainUpdated",PAUSE)
		self.assertEQUAL(UpdateDomain,"updated www.u_domain.tn --js + /u_js -s"						,"DomainUpdated",PAUSE)
		self.assertEQUAL(UpdateDomain,"updated www.u_domain.tn --tag u_tag1 u_tag2 u_tag3 u_tag4 -s"			,"DomainUpdated",PAUSE)
		self.assertEQUAL(UpdateDomain,"updated www.u_domain.tn --tag _ u_tag1 whatever -s"				,"DomainUpdated",PAUSE)
		self.assertEQUAL(UpdateDomain,"updated www.u_domain.tn --tech _ -s"						,"DomainUpdated",PAUSE)
		self.assertEQUAL(UpdateDomain,"updated www.u_domain.tn --port + p1:80 p2:60 -s"					,"DomainUpdated",PAUSE)
		self.assertEQUAL(UpdateDomain,"updated www.u_domain.tn --port _ p2:80 -s"					,"DomainUpdated",PAUSE)
		self.assertEQUAL(UpdateDomain,"updated www.u_domain.tn --port _ -s"						,"DomainUpdated",PAUSE)
		self.assertEQUAL(UpdateDomain,"updated www.u_domain.tn --port u_ssh:25 u_https:448 -s"				,"DomainUpdated",PAUSE)
		
	def test_1119_UpdateWorkshop(self):
		self.assertEQUAL(UpdateWorkshop,"updatew workshop1   -i updated_workshop1 -s"	   ,"WorkshopUpdated"	,PAUSE)
		self.assertEQUAL(UpdateWorkshop,"updatew workshop1   -i updated_workshop1 -s"	   ,"WorkshopNotFound"	,PAUSE)
		self.assertEQUAL(UpdateWorkshop,"updatew updated_workshop1 -i updated_workshop1 -s","NewWorkshopIdExist",PAUSE)
		self.assertEQUAL(UpdateWorkshop,"updatew -i TESTTTT -s"				   ,"UserNeedsHelp"	,PAUSE)
		self.assertEQUAL(UpdateWorkshop,"updatew updated_workshop1 -s"			   ,"UserNeedsHelp"	,PAUSE)
		
	def test_1120_DeleteDomain(self):
		self.assertEQUAL(DeleteDomain,"deletedomain www.domain2.tn -s"	  ,"DomainDeleted"	,PAUSE)
		self.assertEQUAL(DeleteDomain,"deld www.domain3.tn -s -w whatever","WorkshopNotFound"	,PAUSE)
		self.assertEQUAL(DeleteDomain,"deld www.whatever.tn -s","DomainNotFound"		,PAUSE)




	def test_1121_DeleteWorkshop(self):
		self.assertEQUAL(DeleteWorkshop,"deletew workshop3 -s","WorkshopDeleted" ,PAUSE)
		self.assertEQUAL(DeleteWorkshop,"deletew whatever  -s","WorkshopNotFound",PAUSE)
		SetWorkshop.execute("sw workshop2")
		self.assertEQUAL(DeleteWorkshop,"deletew workshop2 -s","WorkshopIsSet"	 ,PAUSE)
		self.assertEQUAL(DeleteWorkshop,"deletew -s"	      ,"UserNeedsHelp"	 ,PAUSE)
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


	def assertEQUAL(self,executor,command,result,pause=False):
		print("\n",command)
		self.assertEqual(executor.execute(command), result)
		if pause:
			p = input()
			os.system("clear")
		


if __name__ == "__main__":
	db = sys.argv[0].replace("test_togomori.py","")+"test_data/"
	global PAUSE
	inp   =input("make pauses ?[<enter>:no][<y>:yes]")
	PAUSE =True if inp == 'y' else False

	unittest.main(exit=False)


	del_test_json = input()
	shutil.rmtree(os.path.join(db,"workshops"))
	os.mkdir(os.path.join(db,"workshops"))
