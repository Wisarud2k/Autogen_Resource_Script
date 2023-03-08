from pymetasploit3.msfrpc import MsfRpcClient
from pymetasploit3.msfrpc import JobManager

import signal
import json
import time
import os
import sys

import pyfiglet

import nmap_module
import exploit_module
import rc_module
import base
import validate

excellentExplotis = []
# excellentExplotis = ['unix/ftp/vsftpd_234_backdoor','windows/fileformat/activepdf_webgrabber', 'windows/fileformat/djvu_imageurl', 'windows/fileformat/mcafee_hercules_deletesnapshot', 'windows/fileformat/msworks_wkspictureinterface', 'windows/fileformat/sascam_get', 'windows/smb/ms04_007_killbill', 'windows/ftp/sami_ftpd_list']
greatExploits = []
goodExploits = []
normalExploits = []
averageExploits = []
lowExploits = []
manualExplots = []

# setting dict for global setting
settings = {'TTL':30}

def main():
    client = MsfRpcClient('test',port=55553)

    text = "HOME"
    augrs = "AugRS"
    # Use the `figlet_format` function to generate the banner
    banner = pyfiglet.figlet_format(text)
    # Get the list of running jobs
    
    # initialize require options
    print(pyfiglet.figlet_format(augrs,font = "slant"))
    print('Starting Program...')
    print('Please Specify Initial Input')
    ipaddr = input('Target Ip address: ')
    while validate.validate_ip_address(ipaddr) == False:
        print('Invalid Ip Address')
        ipaddr = input('Please Input New Target Ip address: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    base.settings['target_ip'] = ipaddr

    # settings['target_ip'] = input('Target Ip address: ')
    while True:
        try:
            print(banner)
            print('press [1] to go to Nmap module')
            print('press [2] to go to Exploit module')
            # print('press [3] to go to Resource Script module')
            print('press [3] to go to Options')
            print('press [0] to exit')
            command = input('Input Command Here: ')

            if(command == '1'):
                # print('go to Nmap')
                os.system('cls' if os.name == 'nt' else 'clear')
                nmap_module.nmap_scan()
            elif(command == '2'):
                # print('go to Exploit')
                os.system('cls' if os.name == 'nt' else 'clear')
                exploit_module.exploit(client)
            # elif(command == '3'):
            #     # print('Resource ')
            #     os.system('cls' if os.name == 'nt' else 'clear')
            #     rc_module.main(client)
            elif(command == '3'):
                os.system('cls' if os.name == 'nt' else 'clear')
                __options()
            elif(command == '0'):
                print('exiting ..')
                break
            else:
                print('Error: Command Not Found')
        except KeyboardInterrupt:
            break
        


def __options():
    # text = "OPTIONS"
    print(pyfiglet.figlet_format(text = "OPTIONS",font = "slant"))
    while True:
        try:
            for key in base.settings:
                print(key + ": " + str(base.settings[key]))
            print('')
            print('press [1] to edit options')
            print('press [0] to exit')
            command = input('Input Command Here: ')

            if(command == '1'):
                os.system('cls' if os.name == 'nt' else 'clear')
                __edit_options()
                print(pyfiglet.figlet_format(text = "OPTIONS",font = "slant"))
                # print('current Ip address is '+settings['target_ip']) 
            elif(command == '0'):
                print('exiting ..')
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(pyfiglet.figlet_format(text = "OPTIONS",font = "slant"))
                print('Error: Command Not Found')
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        # for key in base.settings:
        #     print(key + ": " + str(base.settings[key]))
        # print('')
        # print('press [1] to edit options')
        # print('press [0] to exit')
        # command = input('Input Command Here: ')

        # if(command == '1'):
        #     os.system('cls' if os.name == 'nt' else 'clear')
        #     __edit_options()
        #     print(pyfiglet.figlet_format(text = "OPTIONS",font = "slant"))
        #     # print('current Ip address is '+settings['target_ip']) 
        # elif(command == '0'):
        #     print('exiting ..')
        #     os.system('cls' if os.name == 'nt' else 'clear')
        #     break
        # else:
        #     os.system('cls' if os.name == 'nt' else 'clear')
        #     print(pyfiglet.figlet_format(text = "OPTIONS",font = "slant"))
        #     print('Error: Command Not Found')


def __edit_options():
    print(pyfiglet.figlet_format(text = "EDIT OPTIONS",font = "slant"))
    while True:
        try:
            settings = base.settings
            count = 0
            numkey = {}
            for key in settings:
                count+= 1
                print('['+ str(count) +'] ' + key + ": " + str(settings[key]))
                numkey[count] = key
            print('select option to edit')
            command = int(input('selected option: '))
            if(command in numkey.keys()):
                print('Current ' + str(numkey[command]) + ' is ' + str(settings[numkey[command]]))
                newvalue = input('Enter New Value: ')
                if(validate.setting_validate(numkey[command],newvalue)):
                    base.settings[numkey[command]] = newvalue
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(pyfiglet.figlet_format(text = "EDIT OPTIONS",font = "slant"))
                    print('Error: Invalid Input')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(pyfiglet.figlet_format(text = "EDIT OPTIONS",font = "slant"))
                print('Error: Invalid Input')
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            break







if __name__ == '__main__':
    main()
