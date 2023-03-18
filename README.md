# Auto Generate Metasploit Resouce Script

This Program can run an exploit with automate search for open port with excellent rank in Metasploit Module.
Generate shell / bash scripts to use in security automate test  

## Getting Started
### Prerequisites
~~~
- Python >= 3.10
- python3-nmap
- pymetasploit3
- etc..
~~~

### Installing

~~~
1. Clone the repository.
2. Navigate to the project directory.
3. Run 'pip install -r requirements.txt' to install dependencies.
4. Start program wiht python3 autogen.py
~~~

MSFRPC Installing

~~~
This project use msfrpc api and msfconsole you may need to install and start rpc server or in case of you don't have msfrpc instance
1.install docker desktop or cli (both can use)
2.use docker pull on my ubuntu-metasploit image at url:.....
	with command docker pull ....
3. start docker with command .....
	which will create a docker container that use port 55553 and 443
run autogen.py wiht msfrpc password "test"

~~~
## Usage

~~~
run exploit in program:
xxx

create shell or bash script for running exploit
~~~

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.