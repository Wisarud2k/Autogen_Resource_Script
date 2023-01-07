from pymetasploit3.msfrpc import MsfRpcClient
from pymetasploit3.msfrpc import JobManager

import json
import time
import os
import sys
import nmap_module

excellentExplotis = []
# excellentExplotis = ['unix/ftp/vsftpd_234_backdoor','windows/fileformat/activepdf_webgrabber', 'windows/fileformat/djvu_imageurl', 'windows/fileformat/mcafee_hercules_deletesnapshot', 'windows/fileformat/msworks_wkspictureinterface', 'windows/fileformat/sascam_get', 'windows/smb/ms04_007_killbill', 'windows/ftp/sami_ftpd_list']
greatExploits = []
goodExploits = []
normalExploits = []
averageExploits = []
lowExploits = []
manualExplots = []


def main():
    client = MsfRpcClient('test',port=55553)

    exploitlist = client.modules.exploits
    # Get the list of running jobs
    jobs = JobManager(client)
    # extracting all of excellent module
    # exploit_list_extract(client,exploitlist)
    while True:
        print('press [1] to go to Nmap module')
        print('press [2] to go to Exploit module')
        print('press [3] to go to Resource Script module')
        print('press [4] to exit')
        command = input('Input Command Here: ')
        if(command == '1'):
            print('go to Nmap')
            nmap_module.nmap_scan()
        elif(command == '2'):
            print('go to Exploit')
        elif(command == '3'):
            print('Resource ')
        elif(command == '4'):
            print('exiting ..')
            break
        else:
            print('Error: No command found')

    
def exploit_list_extract(client,exploitlist):
    for exploit in exploitlist:
        rank = client.modules.use('exploit',exploit).rank
        if(rank == 600): # Excellent modules
            excellentExplotis.append(exploit)
        elif(rank == 500): # great modules
            greatExploits.append(exploit)
        elif(rank == 400): # good modules
            goodExploits.append(exploit)
        elif(rank == 300): # normal modules
            normalExploits.append(exploit)
        elif(rank == 200): # average modules
            averageExploits.append(exploit)
        elif(rank == 100): # low modules
            lowExploits.append(exploit)
        else:
            manualExplots.append(exploit)

if __name__ == '__main__':
    main()
