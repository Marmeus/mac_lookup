# Introduction

During a WIFI pentest, sometimes you must obtain information about your target's devices. Some initial data can be obtained through the MAC address of the access points.

This script allows you to retrieve all the information in JSON format, using [macvendors](https://macvendors.co/api/) API, for later processing to gather more information about the device.

# Usage

The options are the following:

```bash
kali@kali:mac_lookup$ python3 macvendor.py  --help
usage: macvendor.py [-h] (-m MAC | -f FILE) [-o OUTPUT] [-F {TEXT,JSON}]

Locate vendor from MAC Address

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Store the output into a file
  -F {TEXT,JSON}, --format {TEXT,JSON}
                        Output format. Default: TEXT

Mandatory options:
  One of these options must be chosen.

  -m MAC, --mac MAC     MAC address to locate
  -f FILE, --file FILE  File path with MAC addresses to be located (One per line)
```

Then, the results can be shown as more "graphical" (by default) or in JSON.

```bash
kali@kali:mac_lookup$ python3 macvendor.py -m 00:11:22:33:44:00
00:11:22:33:44:00
=================
Company: CIMSYS Inc
Country: KR
Type: MA-L
Company address: #301,Sinsung-clean BLDG,140, Nongseo-Ri,Kiheung-Eup,Yongin-City  Kyunggi-Do  449-711,KR

kali@kali:/media/sf_GitHub/mac_lookup$ python3 macvendor.py -F JSON -m 00:11:22:33:44:00 
{"00:11:22:33:44:00": {"company": "CIMSYS Inc", "mac_prefix": "00:11:22", "address": "#301,Sinsung-clean BLDG,140, Nongseo-Ri,Kiheung-Eup,Yongin-City  Kyunggi-Do  449-711,KR", "start_hex": "001122000000", "end_hex": "001122FFFFFF", "country": "KR", "type": "MA-L"}}
```

