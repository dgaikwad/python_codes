#!/usr/bin/python3
""" To validate emailid
    Usename contains any alphanumeric or dot or underscore
    Servername should have any alphanumeric
    Domain name contains only alphabets

"""
import re
def fun(mail):
    obj=re.match("^([\w\._]*)\@(\w+).([a-zA-Z]+)$",mail)
    if obj:
        print("Email Id: {}".format(obj.group(0)))
        print("User Name: {}".format(obj.group(1)))
        print("Server Name: {}".format(obj.group(2)))
        print("Domain Name: {}".format(obj.group(3)))
    else:
        print("Invalid EmailID: {}".format(mail))

email1="devi_das.gaikwad123@outlook.com"
email2="devidas.gaikwad123@outlook.com1"
fun(email1)
print()
fun(email2)
    
