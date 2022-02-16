import shodan
import socket
import sys
SHODAN_API_KEY = "your api key here"
api = shodan.Shodan(SHODAN_API_KEY)
try:
    results = api.search('OpenSSL/1.0.0')
    print ('Total Vulnerable servers: %s' % results['total'])
    for result in results['matches']:
        print ('%s' % result ['ip_str'])
        print ('%s' % socket.getfqdn(result['ip_str']))
        #print (result['data'])
    original_stdout = sys.stdout
    with open('shodan_output.txt', 'w') as f:
        for result in results['matches']:
            sys.stdout = f
            print ('%s' % result ['ip_str'])
            print ('%s' % socket.getfqdn(result['ip_str']))
            sys.stdout = original_stdout
except shodan.APIError as e:
    print ('Error: %s' % e)