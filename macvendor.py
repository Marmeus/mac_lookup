#!/usr/bin/python3

import urllib.request as urllib2
import json
import codecs
import argparse

parser = argparse.ArgumentParser(description='Locate vendor from MAC Address')
gmandatory = parser.add_argument_group(title='Mandatory options', description='One of these options must be chosen.')
gexclusive = gmandatory.add_mutually_exclusive_group(required=True)
gexclusive.add_argument("-m", "--mac", type=str, help="MAC address to locate")
gexclusive.add_argument("-f", "--file", type=str, help="File path with MAC addresses to be located (One per line)")
parser.add_argument("-o", "--output",type=str, required=False, help="Store the output into a file")
parser.add_argument("-F", "--format", choices=['TEXT','JSON'], type=str, default='TEXT', required=False, help="Output format. Default: TEXT")
args = parser.parse_args()

#API base url,you can also use https if you need
url = "https://macvendors.co/api/"
mac_address = args.mac
mac_addresses_file = args.file
output_file = args.output
output_format = args.format
res = {}

def obtain_data(mac):
    request = urllib2.Request(url+mac, headers={'User-Agent' : "API Browser"})
    response = urllib2.urlopen( request )
    #Fix: json object must be str, not 'bytes'
    reader = codecs.getreader("utf-8")
    obj = json.load(reader(response))['result']
    return obj

def macs_from_file(file):
    res = {}
    f = open(file,'r')
    lines = f.readlines()
    for mac in lines:
        res[str(mac[:-1])]=obtain_data(mac[:-1])
    f.close()
    return res

def print_data(rjson):
    res = ""
    for k in rjson.keys():
        res += k+"\n"
        res += "=================\n"
        if 'error' in rjson[k]:
            res += "No results were found\n"
        else:
            result = rjson[k]
            if 'company' in result:
                res += "Company: "+result['company']+"\n"
            if 'country' in result:
                res += "Country: "+result['country']+"\n"
            if 'type' in result:
                res += "Type: "+result['type']+"\n"
            if 'address' in result:
                res += "Company address: "+result['address']+"\n\n"
    return res

# Checks if -m or -f is used
if mac_address != None:
    rjson = obtain_data(mac_address)
    res[mac_address]=rjson
else :
    res = macs_from_file(mac_addresses_file)

# Checks the format
if output_format == "TEXT":
    output = print_data(res)
else:
    output = json.dumps(res)

# Checks the output of the script
if output_file == None:
    print(output)
else:
    f = open(output_file, "w")
    f.write(output)
    f.close()
