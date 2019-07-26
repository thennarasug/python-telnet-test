#usage --> python telnet.py replace_ip_or_host_here replace_input_port_number_here
import sys
import telnetlib

host=sys.argv[1]
portno=sys.argv[2]

try:
    conn = telnetlib.Telnet(host,portno)
    response = host+' ' + portno +' - Success'
except:
    response = host+' ' + portno +' - Failed'
finally:
    print(response)
