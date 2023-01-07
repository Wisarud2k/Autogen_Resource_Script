from pymetasploit3.msfrpc import MsfRpcClient
from pymetasploit3.msfrpc import JobManager

import json
import time
import os
import sys

import pyfiglet

import nmap_module
import exploit_module
import rc_module

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

    text = "HOME"

# Use the `figlet_format` function to generate the banner
    banner = pyfiglet.figlet_format(text)
    # Get the list of running jobs
    
    # extracting all of excellent module
    # exploit_list_extract(client,exploitlist)
    while True:
        print(banner)
        print('press [1] to go to Nmap module')
        print('press [2] to go to Exploit module')
        print('press [3] to go to Resource Script module')
        print('press [4] to exit')
        command = input('Input Command Here: ')

        if(command == '1'):
            # print('go to Nmap')
            os.system('cls' if os.name == 'nt' else 'clear')
            nmap_module.nmap_scan()
        elif(command == '2'):
            # print('go to Exploit')
            os.system('cls' if os.name == 'nt' else 'clear')
            exploit_module.exploit(client)
        elif(command == '3'):
            # print('Resource ')
            os.system('cls' if os.name == 'nt' else 'clear')
            rc_module.main(client)
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

def wait_jobs():
    # for i in range(5):
    #     print(".", end="", flush=True)
    #     time.sleep(1)
    # os.system('cls' if os.name == 'nt' else 'clear')
    for i in progressbar(range(15), "Running an Exploit: ", 40):
        time.sleep(0.1)

def progressbar(it, prefix="", size=60, out=sys.stdout): # Python3.3+
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] ".format(prefix, "#"*x, "."*(size-x)), 
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    # print("\n", flush=True, file=out)


if __name__ == '__main__':
    main()
