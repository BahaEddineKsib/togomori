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
from GlobalVars				     import DATABASE      as db
import unittest
import json
import sys
import shutil
import os

class UTT(unittest.TestCase):

	def test_1111_AddWorkshop(self):
		self.assertEQUAL(AddWorkshop.execute,"addw workshop1 -s","WorkshopAdded",PAUSE)
		self.assertEQUAL(AddWorkshop.execute,"addw workshop2 -s","WorkshopAdded")
		self.assertEQUAL(AddWorkshop.execute,"addw workshop3 -s","WorkshopAdded")
		self.assertEQUAL(AddWorkshop.execute,"addw workshop1 -s","WorkshopExist",PAUSE)
		self.assertEQUAL(AddWorkshop.execute,"addw -s"		,"UserNeedsHelp",PAUSE)
		self.assertEQUAL(AddWorkshop.execute,"addw"		,"UserNeedsHelp",PAUSE)


	def test_1112_AddDomain(self):
		self.assertEQUAL(AddDomain.execute,"ad -d www.domain1.tn -w workshop1"+
						   " -s --tag tag1  tag2 tag3 --tech"+
						   " java react --whois /data/whois.txt"+
						   " --ip 192.168.0.1 --port https:448 ssh:25"+
						   " --server /nmap/scan --robots /data/robots.txt --js /js1 /js2 /js3"	,"DomainAdded"		,PAUSE)
		self.assertEQUAL(AddDomain.execute,"ad -d www.domain2.tn --tag tag2 -w workshop1 -s"			,"DomainAdded"		,PAUSE)
		self.assertEQUAL(AddDomain.execute,"ad -d www.domain3.tn --tag tag3 -w workshop1 -s"			,"DomainAdded"		,PAUSE)
		self.assertEQUAL(AddDomain.execute,"ad -d www.domain1.tn -w workshop1 -s"				,"DomainExist"		,PAUSE)
		self.assertEQUAL(AddDomain.execute,"ad -d www.t.tn    -w TTTTTT -s"					,"WorkshopNotFound"	,PAUSE)
		self.assertEQUAL(AddDomain.execute,"ad -d www.t.tn    -w workshop1 --port https:8585 :85 -s"		,"WrongPortFormat"	,PAUSE)
		self.assertEQUAL(AddDomain.execute,"ad -d www.t.tn    -w workshop1 --port https: -s"			,"WrongPortFormat"	,PAUSE)
		self.assertEQUAL(AddDomain.execute,"ad -d www.t.tn    -w"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain.execute,"ad -d www.t.tn --tag"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain.execute,"ad -d www.t.tn --tech"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain.execute,"ad -d www.t.tn --whois"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain.execute,"ad -d www.t.tn --ip"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain.execute,"ad -d www.t.tn --port"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain.execute,"ad -d www.t.tn --server"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain.execute,"ad -d www.t.tn --robots"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain.execute,"ad -d www.t.tn --js"						,"UserNeedsHelp")
		self.assertEQUAL(AddDomain.execute,"ad"									,"UserNeedsHelp")
	'''
	def test_1113_AddPath(self):
		self.assertEQUAL(AddPath.execute,"ap www.domain1.tn/path/1 -w workshop1 -s"	,"PathAdded"	   ,PAUSE)
		self.assertEQUAL(AddPath.execute,"ap /path/2 -d www.domain1.tn -w workshop1 -s"	,"PathAdded"	   ,PAUSE)
		self.assertEQUAL(AddPath.execute,"ap  www.watever.tn/ -w workshop1 -s"		,"DomainNotFound"  ,PAUSE)
		self.assertEQUAL(AddPath.execute,"ap  www.domain1.tn/    -w whatever -s"	,"WorkshopNotFound",PAUSE)
		self.assertEQUAL(AddPath.execute,"ap /path/1          -w workshop1 -s"		,"NoDomainSetted"  ,PAUSE)
		self.assertEQUAL(AddPath.execute,"ap  www.domain1.tn/p -s"			,"NoWorkshopSetted",PAUSE)
		print('setworkshop workshop1 \n setdomain www.domain1.tn')
		SetWorkshop.execute("setw workshop1")
		SetDomain.execute("setd www.domain1.tn")
		self.assertEQUAL(AddPath.execute,"ap /path/3  -s"			,"PathAdded"	,PAUSE)
		self.assertEQUAL(AddPath.execute,"ap /path/4/dmn2 -d www.domain2.tn -s"	,"PathAdded"	,PAUSE)
		self.assertEQUAL(AddPath.execute,"ap /path/1  -s"			,"PathExist"	,PAUSE)
		self.assertEQUAL(AddPath.execute,"ap  path/1  -s"			,"InvalidPath"	,PAUSE)
		self.assertEQUAL(AddPath.execute,"ap /path/1/ -s"			,"PathAdded"	,PAUSE)
		self.assertEQUAL(AddPath.execute,"ap"					,"UserNeedsHelp")
		#print('unsetworkshop')
		#UnsetWorkshop.execute("usw")
	'''
	def test_1114_DisplayWorkshop(self):
		self.assertEQUAL(DisplayWorkshop.execute,"dw -w workshop1"   ,"workshop1"				,PAUSE)
		self.assertEQUAL(DisplayWorkshop.execute,"dw -w workshop1 -x","workshop1"				,PAUSE)
		self.assertEQUAL(DisplayWorkshop.execute,"dw -w workshop "   ,"WorkshopNotFound"			,PAUSE)
		self.assertEQUAL(DisplayWorkshop.execute,"dw -A"	     ,["workshop1","workshop2","workshop3"]	,PAUSE)
		self.assertEQUAL(DisplayWorkshop.execute,"dw -A -x"	     ,["workshop1","workshop2","workshop3"]	,PAUSE)

	def test_1115_DisplayDomain(self):
		SetWorkshop.execute("setw workshop1")
		self.assertEQUAL(DisplayDomain.execute,"dd -d www.domain1.tn"		     , "www.domain1.tn"					  ,PAUSE)
		self.assertEQUAL(DisplayDomain.execute,"dd -d www.domain1.tn --show paths"   , "www.domain1.tn"					  ,PAUSE)
		self.assertEQUAL(DisplayDomain.execute,"dd -d www.domain1.tn --show paths -x", "www.domain1.tn"					  ,PAUSE)
		self.assertEQUAL(DisplayDomain.execute,"dd -A "				     ,["www.domain1.tn","www.domain2.tn","www.domain3.tn"],PAUSE)
		self.assertEQUAL(DisplayDomain.execute,"dd -A --show ALL"		     ,["www.domain1.tn","www.domain2.tn","www.domain3.tn"],PAUSE)
		self.assertEQUAL(DisplayDomain.execute,"dd -A --port https:8585 :85"	     ,"WrongPortFormat"					  ,PAUSE)
		self.assertEQUAL(DisplayDomain.execute,"dd -A --port https: -s"		     ,"WrongPortFormat"					  ,PAUSE)
		self.assertEQUAL(DisplayDomain.execute,"dd -d  www.t.tn"		     ,"DomainNotFound")
		self.assertEQUAL(DisplayDomain.execute,"dd -A --tag tag2"		     ,["www.domain1.tn","www.domain2.tn"]		  ,PAUSE)
		self.assertEQUAL(DisplayDomain.execute,"dd -A --tag"			     ,"UserNeedsHelp")
		self.assertEQUAL(DisplayDomain.execute,"dd -A -w whatever"		     ,"WorkshopNotFound")
	'''
	def test_1116_DisplayPath(self):
		UnsetDomain.execute("usd")
		self.assertEQUAL(DisplayPath.execute,"dp -p www.domain1.tn/path/1"	,"/path/1"						  ,True)
		self.assertEQUAL(DisplayPath.execute,"dp -d www.domain1.tn -a"		,["/path/1","/path/2","/path/3","/path/1/"]		  ,True)
		self.assertEQUAL(DisplayPath.execute,"dp -A"				,["/path/4/dmn2","/path/1","/path/2","/path/3","/path/1/"],True)
		self.assertEQUAL(DisplayPath.execute,"dp -p www.domain1.tn"		,"NoPath"						  ,True)
		self.assertEQUAL(DisplayPath.execute,"dp -p my/path   -d www.domain1.tn","InvalidPath"						  ,True)
		self.assertEQUAL(DisplayPath.execute,"dp -p /whatever -d www.whatever.t","DomainNotFound"					  ,True)
		self.assertEQUAL(DisplayPath.execute,"dp -p /whatever -d www.domain1.tn","PathNotFound"						  ,True)
		self.assertEQUAL(DisplayPath.execute,"dp -A -w whatever"		,"WorkshopNotFound"					  ,True)
		self.assertEQUAL(DisplayPath.execute,"dp -a"				,"NoDomainSetted"					  ,True)
		UnsetWorkshop.execute("usw")
		self.assertEQUAL(DisplayPath.execute,"dp -A"				,"NoWorkshopSetted"					  ,True)
		'''

	def test_1117_UpdateDomain(self):
		self.assertEQUAL(UpdateDomain.execute,"updatedomain www.domain1.tn -d www.updated_domain.tn -s"				,"DomainUpdated"	,PAUSE)
		self.assertEQUAL(UpdateDomain.execute,"updated www.updated_domain.tn --w workshop2 -s"					,"DomainUpdated"	,PAUSE)
		self.assertEQUAL(UpdateDomain.execute,"updated www.updated_domain.tn -d www.u_domain.tn -w workshop2 --w workshop1 -s"	,"DomainUpdated"	,PAUSE)
		self.assertEQUAL(UpdateDomain.execute,"updated www.u_domain.tn --js + /u_js -s"						,"DomainUpdated"	,PAUSE)
		self.assertEQUAL(UpdateDomain.execute,"updated www.u_domain.tn --tag u_tag1 u_tag2 u_tag3 u_tag4 -s"			,"DomainUpdated"	,PAUSE)
		self.assertEQUAL(UpdateDomain.execute,"updated www.u_domain.tn --tag _ u_tag1 whatever -s"				,"DomainUpdated"	,PAUSE)
		self.assertEQUAL(UpdateDomain.execute,"updated www.u_domain.tn --tech _ -s"						,"DomainUpdated"	,PAUSE)
		self.assertEQUAL(UpdateDomain.execute,"updated www.u_domain.tn --port + p1:80 p2:60 -s"					,"DomainUpdated"	,PAUSE)
		self.assertEQUAL(UpdateDomain.execute,"updated www.u_domain.tn --port _ p2:80 -s"					,"DomainUpdated"	,PAUSE)
		self.assertEQUAL(UpdateDomain.execute,"updated www.u_domain.tn --port _ -s"						,"DomainUpdated"	,PAUSE)
		self.assertEQUAL(UpdateDomain.execute,"updated www.u_domain.tn --port u_ssh:25 u_https:448 -s"				,"DomainUpdated"	,PAUSE)
		
	def test_1118_UpdateWorkshop(self):
		self.assertEQUAL(UpdateWorkshop.execute,"updatew workshop1   -i updated_workshop1 -s"	   ,"WorkshopUpdated"	,PAUSE)
		self.assertEQUAL(UpdateWorkshop.execute,"updatew workshop1   -i updated_workshop1 -s"	   ,"WorkshopNotFound"	,PAUSE)
		self.assertEQUAL(UpdateWorkshop.execute,"updatew updated_workshop1 -i updated_workshop1 -s","NewWorkshopIdExist",PAUSE)
		self.assertEQUAL(UpdateWorkshop.execute,"updatew -i TESTTTT -s"				   ,"UserNeedsHelp"	,PAUSE)
		self.assertEQUAL(UpdateWorkshop.execute,"updatew updated_workshop1 -s"			   ,"UserNeedsHelp"	,PAUSE)
		
	def test_1119_DeleteDomain(self):
		self.assertEQUAL(DeleteDomain.execute,"deletedomain www.domain2.tn -s"	  ,"DomainDeleted"	,PAUSE)
		self.assertEQUAL(DeleteDomain.execute,"deld www.domain3.tn -s -w whatever","WorkshopNotFound"	,PAUSE)
		self.assertEQUAL(DeleteDomain.execute,"deld www.whatever.tn -s","DomainNotFound"		,PAUSE)




	def test_1120_DeleteWorkshop(self):
		self.assertEQUAL(DeleteWorkshop.execute,"deletew workshop3 -s","WorkshopDeleted" ,PAUSE)
		self.assertEQUAL(DeleteWorkshop.execute,"deletew whatever  -s","WorkshopNotFound",PAUSE)
		SetWorkshop.execute("sw workshop2")
		self.assertEQUAL(DeleteWorkshop.execute,"deletew workshop2 -s","WorkshopIsSet"	 ,PAUSE)
		self.assertEQUAL(DeleteWorkshop.execute,"deletew -s"	      ,"UserNeedsHelp"	 ,PAUSE)
		
	'''
	#def test_1118_UpdateDomain(self):
		#self.assertEQUAL(UpdateDomain.execute,"ud ")
	'''
	def assertEQUAL(self,executor,command,result,pause=False):
		print("\n",command)
		self.assertEqual(executor(command), result)
		if pause:
			p = input()


if __name__ == "__main__":
	db = sys.argv[0].replace("test_togomori.py","")+"test_data/"
	global PAUSE
	inp   =input("make pauses ?[<enter>:no][<y>:yes]")
	PAUSE =True if inp == 'y' else False

	unittest.main(exit=False)


	del_test_json = input()
	shutil.rmtree(os.path.join(db,"workshops"))
	os.mkdir(os.path.join(db,"workshops"))
