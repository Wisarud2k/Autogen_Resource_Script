import ipaddress
def validate_ip_address(ip_string):
   try:
       ip_object = ipaddress.ip_address(ip_string)
       return True
   except ValueError:
       return False

def setting_validate(fieldname,value):
    if(fieldname == 'target_ip'):
        return validate_ip_address(value)
    elif(fieldname == 'TTL'):
        return value.isdigit()