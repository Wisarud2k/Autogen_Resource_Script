import nmap3
import json

def nmap_scan():
    nmap = nmap3.Nmap()
    # results = nmap.scan_top_ports("192.168.184.129")
    # ressults = nmap.nmap_version_detection("host", args="--script vulners --script-args mincvss+5.0")
    # print(results)
    # os_results = nmap.nmap_os_detection("192.168.178.2")
    ip_address = input('Please Input Target Address: ')
    try:
        version_result = nmap.nmap_version_detection(ip_address)
    except:
        print('Error: Please try again')

    # json_formatted_str = json.dumps(version_result, indent=4)

    # print(json_formatted_str)
    json_formatted_str = json.dumps(version_result, indent=4,sort_keys=True)
    jj = json.loads(json_formatted_str)
    formated = json.dumps(jj['192.168.184.129']['ports'],indent=4,sort_keys=True)
    data = jj['192.168.184.129']['ports']
    for port in data:
        # 4 case 
        # have all information
        # print(port)
        if(port['state'] == 'open' and 'version' in port['service'].keys() and 'product' in port['service'].keys()):
            print('PORT: ' +port['portid']+'/'+port['protocol'] +' SERVICE: '+port['service']['name'] + ' VERSION: ' + port['service']['product'] + ' ' + port['service']['version'])
        elif(port['state'] == 'open' and 'version' in port['service'].keys()): # have only version keys
            # print('Im only have version key!!')
            print('PORT: ' +port['portid']+'/'+port['protocol']+' SERVICE: '+port['service']['name']+ ' VERSION: ' + port['service']['version'])
        elif(port['state'] == 'open' and 'product' in port['service'].keys()): # have only product keys 
            # print('Im only have product key!!')
            print('PORT: ' +port['portid']+'/'+port['protocol']+' SERVICE: '+port['service']['name']+ ' VERSION: ' + port['service']['product'])
        elif(port['state'] == 'open'): # dont have version and product keys
            # print('Im dont have both extras keys!!')
            print('PORT: ' +port['portid']+'/'+port['protocol']+' SERVICE: '+port['service']['name'] + ' VERSION: ')

def main():
    print('nmap module')
# This line runs the main function
if __name__ == "__main__":
    main()