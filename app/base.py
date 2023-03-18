import os
cwd = os.getcwd()
LOCAL_PATH = cwd + '/app/rc/'
RESOURCE_PATH = '/app/shared-vol/'
NMAP_REPORT_PATH =  cwd + '/app/nmap_report/'
REPORT_PATH = cwd + '/app/exploit_report/'

# setting dict for global setting
settings = {'TTL(s)':'30','LHOSTS':'172.17.0.2'}
# open port for exploit searching 
open_port = ['21']
exploit_and_port = {}
exploit_list = []