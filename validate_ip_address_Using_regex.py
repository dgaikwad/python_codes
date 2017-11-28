#!/usr/bin/python3
""" Program to validate the valid ip address.

Following are the some example of ip address:

IPAddress is valid : 1.1.1.1 , true
IPAddress is valid : 255.255.255.255 , true
IPAddress is valid : 192.168.1.1 , true
IPAddress is valid : 10.10.1.1 , true
IPAddress is valid : 132.254.111.10 , true
IPAddress is valid : 26.10.2.10 , true
IPAddress is valid : 127.0.0.1 , true
IPAddress is valid : 10.10.10 , false
IPAddress is valid : 10.10 , false
IPAddress is valid : 10 , false
IPAddress is valid : a.a.a.a , false
IPAddress is valid : 10.0.0.a , false
IPAddress is valid : 10.10.10.256 , false
IPAddress is valid : 222.222.2.999 , false
IPAddress is valid : 999.10.10.20 , false
IPAddress is valid : 2222.22.22.22 , false
IPAddress is valid : 22.2222.22.2 , false

"""


import re

def validate_ip(ip):
    pattern="^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-5][0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-5][0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-5][0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-5][0-5])$"
    # Number Separated by . using group
    # Every group is divided by 4 part
    # Number can be between 0-9 or
    # Number can be between 10-99 or
    # Number can be between 100-199 or
    # Number can be between 200-256
    obj=re.match(pattern, ip)
    if obj:
        print("Valid IP : {}".format(ip))
    else:
        print("Invalid IP: {}".format(ip))



if __name__ == "__main__":
    data= ['1.1.1.1', '255.255.255.255', '192.168.1.1', '10.10.1.1', '132.254.111.10', '26.10.2.10', '127.0.0.1', '10.10.10', '10.10', '10', 'a.a.a.a', '10.0.0.a', '10.10.10.256', '222.222.2.999', '999.10.10.20', '2222.22.22.22', '22.2222.22.2']
    for ip in data:
        validate_ip(ip)


