import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

scans = []
headers = {'X-ApiKeys': 'accessKey={ACCESSKEY}; secretKey={SECRETKEY}'}

def FindScans():
	url = 'https://localhost:8834/scans'
	r = requests.get(url,headers=headers,verify=False)
	parsed = json.loads(r.text)
	print parsed

	print "{0} {1:40} {2:20}".format('ID', 'Scan Name', 'Status')
	print "_"*60
	for element in parsed['scans']:
		id = element['id']
		name = element['name']
		status = element['status']
		print "{0} {1:40} {2:20}".format('['+str(id)+']', name, status)

def StartScan():
	print '\n\n'
	startscan = raw_input('What scan would you like to run? ')
	url = 'https://localhost:8834/scans/'+str(startscan)+'/launch'
	r = requests.post(url,headers=headers,verify=False)

def StopScan():
	print '\n\n'
        startscan = raw_input('What scan would you like to quit? ')
        url = 'https://localhost:8834/scans/'+str(startscan)+'/stop'
        r = requests.post(url,headers=headers,verify=False)

def NewScan():
	print '\n\n'
	range = raw_input('What range would you like to scan? ')
	url = 'https://localhost:8834/scans/'
	body = {"uuid": "9999","settings": {"name": "API TEST","description": "testing","emails": "<email>","enabled": "true","launch": "ON_DEMAND","folder_id": "1","policy_id": "1","scanner_id": "1","text_targets": "127.0.0.1"}}
        r = requests.post(url,headers=headers,data=body,verify=False)
	print r.text

def Choose():
	print '\n\n'
	startstop = raw_input("Would you like to (S)tart or (Q)uit a scan? ")
	if startstop == 'S':
		StartScan()
	else:
		if startstop == 'Q':
			StopScan()

		else:
			pass
while True:
	FindScans()
	NewScan()
	Choose()
