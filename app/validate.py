import ipaddress
def validate_ip_address(ip_string):
   try:
       ip_object = ipaddress.ip_address(ip_string)
       return True
   except ValueError:
       return False