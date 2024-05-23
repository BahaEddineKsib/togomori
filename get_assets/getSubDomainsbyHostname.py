from entities.domain		import Domain
import GlobalVars		as gv
import socket
import threading


def GetSubDomainsByHostname(workshop, domain, no_save, by_wordlist=True):
	socket.setdefaulttimeout(100)
	founded_subs = {}
	if by_wordlist :
		#wordlist_file = gv.PATH+"wordlists/subs.txt"
		wordlist_file = "wordlists/subs.txt"

		with open(wordlist_file,'r') as file:
			name = file.read()
			subsList = name.splitlines()
		threads = []
		num_of_sockets_to_relax = 10001
		relax_time = 5
		relax = 0
		subNum=0
		for sub in subsList:
			subNum = subNum+1
			t = threading.Thread(target=domainExist, args=(workshop, sub+'.'+domain, no_save, founded_subs))
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
	return founded_subs

def domainExist(workshop, domain, no_save, founded_subs):
	save_it = False
	try:
		ip = socket.gethostbyname(domain)

		if ip not in list(founded_subs.values()):
			founded_subs[domain] = ip
			print("[+] "+ip+" "+domain)
			save_it = True
	except Exception as e:
		#print(e)
		#print("***********"+domain)
		return "NoIp"

	if (not no_save) and save_it:
		dmn = Domain(workshop_id=workshop, domain=domain, ip=ip)
		r   = dmn.save()
		if r == 'WorkshopNotFound':
			return r
		if r == 'DomainExist':
			dmn.domain = ''
			dmn.workshop_id=''
			r = Domain.update(domain, workshop, dmn, False)
	return ip




#GetSubDomainsByHostname("workshop", "esprit-tn.com", True, by_wordlist=True)
