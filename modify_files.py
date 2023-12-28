import os

"""
This package modify files with sudo permission
"""

dir_rules = "/usr/local/etc/rules/local.rules"

def add_local_rules(new_rule):
    try:
        with open(dir_rules,"a") as file:
            # to append a new rule to local.rules
            file.write(new_rule+"\n")
        return "Rule added"
    except PermissionError:
        return "Require permission"

def read_sid():
    try:
        with open("settings.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                temp = line.split(":")
                if temp[0]=="sid":
                    return temp[1]
    except Exception:
        return "Error occured"    

def update_sid(newvalue):
    try:
        list = []
        with open("settings.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                temp = line.split(":")
                list.append(temp)
        with open("settings.txt","w") as file:
            for l in list:
                if l[0] == "sid":
                    file.write("sid:"+newvalue)
                else: 
                    file.write(l[0]+":"+l[1])
        return
    except Exception:
        return "Error occured"    

def reload_ufw():
    try:
        os.system("ufw disable")
        os.system("ufw enable")
    except PermissionError:
        return "Require permission"
    return "Ufw reloaded"

def reload_snort(service="snort3-nids"):
    # can provide service in case of different service name
    # should be used to reload snort-nids
    try:
        os.popen("systemctl stop "+service) 
        var = os.popen("systemctl start "+service).read()
    except PermissionError:
        return "Require permission"
    return var

def ufw_execute(cmd):
    # run ufw_execute("ufw reload") to reload firewall and apply new rules
    try:
        var = os.popen(cmd).read()
        return var
    except PermissionError:
        return "Require permission"