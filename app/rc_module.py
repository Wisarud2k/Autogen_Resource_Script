from pymetasploit3.msfrpc import AuthManager
import base

def main():
    print('rc module')
# This line runs the main function
if __name__ == "__main__":
    main()

def generate_resource_script(commands):
  with open(base.LOCAL_PATH +'resource_script.rc', 'w') as f:
    for command in commands:
      f.write(command + '\n')