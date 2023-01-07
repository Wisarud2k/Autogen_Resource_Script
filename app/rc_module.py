from pymetasploit3.msfrpc import AuthManager
import base
import os

def main(client):
    print('Resource Script Module')
    while True:
        print('press [1] to see current rc file') # might change to show and select availabe rc
        print('press [2] to run a rc file')
        print('press [0] to go back')
        command = input('Input RC Command Here: ')
        if command == '1':
            print('working in progress')
        elif command == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Executing rc file via msfconsole')
            run_resource_script(client)
        elif command == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print('Error: Command Not Found..')

# This line runs the main function
if __name__ == "__main__":
    main()

def generate_resource_script(commands):
  with open(base.LOCAL_PATH +'resource_script.rc', 'w') as f:
    for command in commands:
      f.write(command + '\n')

def run_resource_script(msf_client):
    # result = msf_client.modules.execute('resource', constant.resouce_path)
    console_id = msf_client.call('console.create')['id']
    # Run the commands in the console
    # result = msf_client.call('console.run')
    # msf_client.call('console.write', [console_id, 'help\n'])
    msf_client.call('console.write', [console_id, 'resource '+ base.RESOURCE_PATH + 'resource_script.rc\n'])
    # output = msf_client.call('console.read', [console_id])

    while True:
        try:
            output = msf_client.call('console.read', [console_id])
            # msf_client.call('console.write', [console_id, 'exit -y\n'])
            if output['data'] != '':
                print(output['data'])
        except:
            print('exiting resource output')
            msf_client.call('console.destroy',[console_id])
            break
