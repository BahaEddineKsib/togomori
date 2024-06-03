from entities.domain import Domain
import socket
import threading
import time
from personalizedPrint import pp



def scan_port(domain, port_name, port, open_ports):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(2)
		result = sock.connect_ex((domain, port))
		sock.close()
		if result == 0:
			open_ports[port_name] = port
			pp(""+port_name+":"+str(port)+" ✅",end='\n')
		else:

			#pp("|",end='')
			pp("\n"+port_name+":"+str(port)+" ❌",end='')
	except Exception as e:
		#pp(port_name+":"+str(port)+" ❌",end='')
		#pp("error: ")
		#pp(e)
		open_ports["NoPorts"] = 1
		return 0

def GetOpenPortsByDomain(workshop, domain, no_save,top_20=True, top_web=False, by_ports=[],interval=[]):

	open_ports	 = {}
	ports_to_scan	 = {}
	threads		 = []
	threads_interval = []

	if interval:
		try:
			num_of_sockets_to_relax = 30000
			relax_time = 5
			relax = 0
			for p in range(interval[0], interval[1]+1):
				t = threading.Thread(target=scan_port, args=(domain, str(p), p,  open_ports))
				t.start()
				threads_interval.append(t)
				#pp("##################################################################"+str(relax))
				relax = relax + 1
				if relax == num_of_sockets_to_relax:
					relax = 0
					for T in threads_interval:
						T.join()
					threads_interval=[]
					pp("--------------------------------------------------"+str((p/interval[1])*100)+"%")
			if threads_interval:
				for T in threads_interval:
					T.join()
				threads_interval=[]
				pp("--------------------------------------------------100%")



		except Exception as e:
			pp("ERROR: in interval")
			pp(e)
			open_ports["NoPorts"] = 1

	ports_to_scan = getPortsList(top_20, top_web, by_ports)
	translatePortsToNames(open_ports)
	if ports_to_scan:
		try: 
			for key, port in ports_to_scan.items():
				if not interval:
					t = threading.Thread(target=scan_port, args=(domain, key, port,  open_ports))
					t.start()
					threads.append(t)
				elif port < interval[0] or port > interval[1]:
					t = threading.Thread(target=scan_port, args=(domain, key, port,  open_ports))
					t.start()
					threads.append(t)

			for t in threads:
				t.join()
		except Exception as e:
			pp("ERROR: in ports to scan ")
			pp(e)
			open_ports["NoPorts"] = 1

	if not no_save:
		dmn = Domain(workshop_id=workshop, domain=domain, ports=open_ports)
		r   = dmn.save()
		if r == 'WorkshopNotFound':
			return r
		if r == 'DomainExist':
			dmn.domain = ''
			dmn.workshop_id=''
			r = Domain.update(domain, workshop, dmn, False)

	return open_ports

def translatePortsToNames(open_ports):
	key_update=[]
	RTWL = getReversedTopWebList()
	for key, port in open_ports.items():
		if key in RTWL.keys():
			key_update.append(key)
			#open_ports[RTWL[key]] = port
			#del open_ports[key]

	for k in key_update:
		open_ports[RTWL[k]] = port
		del open_ports[k]




def getPortsList(top_20=False, top_web=False, by_ports=[]):

	ports_to_scan={}

	top_20_list =  getTop20List()
	top_web_list = getTopWebList()

	if   top_web:
		ports_to_scan = top_web_list
	elif top_20:
		ports_to_scan = top_20_list

	if by_ports:
		rev = getReversedTopWebList()
		for p in by_ports:
			if str(p) in rev.keys():
				ports_to_scan[rev[str(p)]] = p
			else:
				ports_to_scan[str(p)] = p
	return ports_to_scan


def getTop20List():
	return {
        'ftp': 21,
        'ssh': 22,
        'telnet': 23,
        'smtp': 25,
        'dns': 53,
        'http': 80,
        'pop3': 110,
        'rpcbind': 111,
        'msrpc': 135,
        'netbios_ssn': 139,
        'imap': 143,
        'https': 443,
        'microsoft_ds': 445,
        'imaps': 993,
        'pop3s': 995,
        'pptp': 1723,
        'mysql': 3306,
        'ms_wbt_server': 3389,
        'vnc': 5900,
        'http_proxy': 8080
	}

def getTopWebList():
	return {
	'ftp': 21,
	'ssh': 22,
	'smtp': 25,
	'http': 80,
	'pop3': 110,
	'rpcbind': 111,
	'msrpc': 135,
	'netbios_ssn': 139,
	'imap': 143,
	'IIOP_Name_Service_over_TLS/SSL': 261,
	'IIOP_Name_Service': 271,
	'ocu-lm': 324,
	'https': 443,
	'microsoft_ds': 445,
	'ddi-tcp-1': 448,
	'smtps': 465,
	'nntp_over_TLS/SSL': 563,
	'sco-inetmgr': 614,
	'ipp': 631,
	'ldaps': 636,
	'asf-rmcp': 664,
	'corba-iiop': 684,
	'ieee-mms-ssl': 695,
	'netconf-ssh': 832,
	'dns-query-tls': 853,
	'dtls-device': 854,
	'ftps-data': 990,
	'imaps': 993,
	'ftps': 989,
	'telnets': 992,
	'ircs': 994,
	'pop3s': 995,
	'caspssl': 1129,
	'casp': 1131,
	'fopc-rc': 1184,
	'pptp': 1723,
	'radsec': 2083,
	'eli': 2087,
	'sep': 2089,
	'nbq': 2096,
	'rockwell-csp2': 2221,
	'njxos': 2252,
	'docker': 2376,
	'compaq-https': 2381,
	'ssrip': 2478,
	'ssmirnov': 2479,
	'polipo': 2482,
	'ttnc': 2484,
	'syncserver': 2679,
	'datatasmania1': 2762,
	'orbix-loc-ssl': 3077,
	'orbix-loc': 3078,
	'cxc': 3183,
	'csvr-proxy': 3191,
	'rtserv': 3220,
	'msft-gc-ssl': 3269,
	'mysql': 3306,
	'ms_wbt_server': 3389,
	'networklens': 3410,
	'xtrm': 3424,
	'jt400-ssl': 3471,
	'tsp': 3496,
	'vt-ssl': 3509,
	'jboss-iiop': 3529,
	'ibm-diradm': 3539,
	'ms-la': 3535,
	'can-nds-ssl': 3660,
	'can-nds': 36611,
	'tftps': 3713,
	'linktest': 3747,
	'listmgr-port': 3766,
	'asap-tcp': 3864,
	'asap-tls': 3885,
	'iss-mgmt-ssl': 3995,
	'sdo-tls': 3896,
	'suucp': 4031,
	'wap-push-http': 4036,
	'ice-location': 4062,
	'lorica-in': 4064,
	'chirp': 4081,
	'irdmi2': 4335,
	'irdmi': 4336,
	'eventsys': 4536,
	'rid': 4590,
	'ipfix': 4740,
	'opcua-tls': 4843,
	'appserv-http': 4849,
	'sbb-seclayer-tls': 5443,
	'wsm_server_ssl': 5007,
	'sips': 5061,
	'webservices': 5321,
	'stuns': 5349,
	'amqps': 5671,
	'3par-evts': 5783,
	'dyn-port': 5868,
	'vnc': 5900,
	'wsm_server_secure': 5986,
	'wbem-https': 5989,
	'wbem-http': 5990,
	'qmtps': 6209,
	'cdp-ssl': 6251,
	'pharos': 6443,
	'netconf-tls': 6513,
	'syslog-tls': 6514,
	'ovsdb-ssl': 6619,
	'ircs-u': 6697,
	'pt2-discover': 6771,
	'event-port': 7202,
	'swx-admin': 7443,
	'imqstompssl': 7673,
	'imqtunnelssl': 7674,
	'sun-user-https': 7677,
	'iana': 7775,
	'http_proxy': 8080,
	'qotps': 8243,
	'pcsync-https': 8443,
	'acap-ssl': 8991,
	'sunwebadmin': 8989,
	'sqlexec-ssl': 9089,
	'armcenterhttps': 9295,
	'gvpn': 9318,
	'tungsten-https': 9443,
	'iadt-tls': 9614,
	'dcmws-ssl': 9802,
	'snmpdtls': 10161,
	'snmpdtls-trap': 10162,
	'cmapport1': 11751,
	'vipera-ssl': 12013,
	'iqtelnet': 12109,
	'icpp': 14143,
	'oneconnect': 15002,
	'infiniswitchmgmt': 16995,
	'z-wave-s': 41230,
	'intel-rci-mgr': 16993,
	'commplex-main': 20003
	}
def getReversedTopWebList():
	return {
	'21': 'ftp',
	'22': 'ssh',
	'25': 'smtp',
	'80': 'http',
	'110': 'pop3',
	'111': 'rpcbind',
	'135': 'msrpc',
	'139': 'netbios_ssn',
	'143': 'imap',
	'261': 'IIOP_Name_Service_over_TLS/SSL',
	'271': 'IIOP_Name_Service',
	'324': 'ocu-lm',
	'443': 'https',
	'445': 'microsoft_ds',
	'448': 'ddi-tcp-1',
	'465': 'smtps',
	'563': 'nntp_over_TLS/SSL',
	'614': 'sco-inetmgr',
	'631': 'ipp',
	'636': 'ldaps',
	'664': 'asf-rmcp',
	'684': 'corba-iiop',
	'695': 'ieee-mms-ssl',
	'832': 'netconf-ssh',
	'853': 'dns-query-tls',
	'854': 'dtls-device',
	'990': 'ftps-data',
	'993': 'imaps',
	'989': 'ftps',
	'992': 'telnets',
	'994': 'ircs',
	'995': 'pop3s',
	'1129': 'caspssl',
	'1131': 'casp',
	'1184': 'fopc-rc',
	'1723': 'pptp',
	'2083': 'radsec',
	'2087': 'eli',
	'2089': 'sep',
	'2096': 'nbq',
	'2221': 'rockwell-csp2',
	'2252': 'njxos',
	'2376': 'docker',
	'2381': 'compaq-https',
	'2478': 'ssrip',
	'2479': 'ssmirnov',
	'2482': 'polipo',
	'2484': 'ttnc',
	'2679': 'syncserver',
	'2762': 'datatasmania1',
	'3077': 'orbix-loc-ssl',
	'3078': 'orbix-loc',
	'3183': 'cxc',
	'3191': 'csvr-proxy',
	'3220': 'rtserv',
	'3269': 'msft-gc-ssl',
	'3306': 'mysql',
	'3389': 'ms_wbt_server',
	'3410': 'networklens',
	'3424': 'xtrm',
	'3471': 'jt400-ssl',
	'3496': 'tsp',
	'3509': 'vt-ssl',
	'3529': 'jboss-iiop',
	'3539': 'ibm-diradm',
	'3535': 'ms-la',
	'3660': 'can-nds-ssl',
	'36611': 'can-nds',
	'3713': 'tftps',
	'3747': 'linktest',
	'3766': 'listmgr-port',
	'3864': 'asap-tcp',
	'3885': 'asap-tls',
	'3995': 'iss-mgmt-ssl',
	'3896': 'sdo-tls',
	'4031': 'suucp',
	'4036': 'wap-push-http',
	'4062': 'ice-location',
	'4064': 'lorica-in',
	'4081': 'chirp',
	'4335': 'irdmi2',
	'4336': 'irdmi',
	'4536': 'eventsys',
	'4590': 'rid',
	'4740': 'ipfix',
	'4843': 'opcua-tls',
	'4849': 'appserv-http',
	'5443': 'sbb-seclayer-tls',
	'5007': 'wsm_server_ssl',
	'5061': 'sips',
	'5321': 'webservices',
	'5349': 'stuns',
	'5671': 'amqps',
	'5783': '3par-evts',
	'5868': 'dyn-port',
	'5900': 'vnc',
	'5986': 'wsm_server_secure',
	'5989': 'wbem-https',
	'5990': 'wbem-http',
	'6209': 'qmtps',
	'6251': 'cdp-ssl',
	'6443': 'pharos',
	'6513': 'netconf-tls',
	'6514': 'syslog-tls',
	'6619': 'ovsdb-ssl',
	'6697': 'ircs-u',
	'6771': 'pt2-discover',
	'7202': 'event-port',
	'7443': 'swx-admin',
	'7673': 'imqstompssl',
	'7674': 'imqtunnelssl',
	'7677': 'sun-user-https',
	'7775': 'iana',
	'8080': 'http_proxy',
	'8243': 'qotps',
	'8443': 'pcsync-https',
	'8991': 'acap-ssl',
	'8989': 'sunwebadmin',
	'9089': 'sqlexec-ssl',
	'9295': 'armcenterhttps',
	'9318': 'gvpn',
	'9443': 'tungsten-https',
	'9614': 'iadt-tls',
	'9802': 'dcmws-ssl',
	'10161': 'snmpdtls',
	'10162': 'snmpdtls-trap',
	'11751': 'cmapport1',
	'12013': 'vipera-ssl',
	'12109': 'iqtelnet',
	'14143': 'icpp',
	'15002': 'oneconnect',
	'16995': 'infiniswitchmgmt',
	'41230': 'z-wave-s',
	'16993': 'intel-rci-mgr',
	'20003': 'commplex-main'
	}






#GetIpByDomain(workshop, domain, no_save,top_20=True, top_web=False, by_ports=[] interval=[]):

#GetIpByDomain('workshop', 'google.com', 'no_save', False, False, [], [1,1000])
