import os
cwd = os.getcwd()
LOCAL_PATH = cwd + '/rc/'
RESOURCE_PATH = '/shared-vol/'
NMAP_REPORT_PATH =  cwd + '/nmap_report/'
REPORT_PATH = cwd + '/exploit_report'

# setting dict for global setting
settings = {'TTL':'30','LHOSTS':'172.17.0.2'}
# open port for exploit searching 
open_port = ['21']
exploit_and_port = {}
exploit_list = []