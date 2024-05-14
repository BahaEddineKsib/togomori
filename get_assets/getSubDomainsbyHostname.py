#from entities.domain		import Domain
#import GlobalVars		as gv
import socket
import threading


def GetSubDomainsByHostname(workshop, domain, no_save, by_wordlist=True):
	if by_wordlist :
		#wordlist_file = gv.PATH+"wordlists/subs.txt"
		wordlist_file = "wordlists/subs.txt"

		with open(wordlist_file,'r') as file:
			name = file.read()
			subsList = name.splitlines()
		threads = []
		founded_subs= {}
		num_of_sockets_to_relax = 10001
		relax_time = 5
		relax = 0
		subNum=0
		for sub in subsList:
			subNum = subNum+1
			t = threading.Thread(target=domainExist, args=(workshop, sub+'.'+domain, True, founded_subs))
			t.start()
			threads.append(t)
			relax = relax + 1
			if relax == num_of_sockets_to_relax:
				relax = 0
				for T in threads:
					T.join()
				threads=[]
				print("--------------------------------------------------"+str((subNum/10000)*100)+"%")
		if threads:
			for T in threads:
				T.join()
			threads=[]
			print("--------------------------------------------------100%    DONE")
	#print(founded_subs)

def domainExist(workshop, domain, no_save, founded_subs):
	try:
		ip = socket.gethostbyname(domain)
		founded_subs[domain] = ip
		print("[+] "+domain)
	except Exception as e:
		#print(e)
		#print("***********"+domain)
		return "NoIp" 
		"""
	if not no_save:
		dmn = Domain(workshop_id=workshop, domain=domain, ip=ip)
		r   = dmn.save()
		if r == 'WorkshopNotFound':
			return r
		if r == 'DomainExist':
			dmn.domain = ''
			dmn.workshop_id=''
			r = Domain.update(domain, workshop, dmn, False)
		"""
	return ip




GetSubDomainsByHostname("workshop", "esprit.tn", True, by_wordlist=True)
