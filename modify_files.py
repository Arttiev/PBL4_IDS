import os

"""
This package modify local.rules and ufw rules, with sudo permission
"""

dir_rules = "/usr/local/etc/rules/local.rules"

def add_local_rules(new_rule):
    try:
        with open(dir_rules,"a") as file:
            # to append a new rule to local.rules
            file.write("\n"+new_rule+"\n")
        return "Rule added"
    except PermissionError:
        return "Require permission"
    
def reload_ufw():
    try:
        os.system("ufw disable")
        os.system("ufw enable")
    except PermissionError:
        return "Require permission"
    return "Ufw reloaded"

def reload_service(service):
    # should be used to reload snort-nids
    try:
        os.popen("systemctl stop snort3-nids") 
        var = os.popen("systemctl start snort3-nids").read()
    except PermissionError:
        return "Require permission"
    return "Snort reloaded"

def ufw_execute(cmd):
    # run ufw_execute("ufw reload") to reload firewall and apply new rules
    try:
        var = os.popen(cmd).read()
        return var
    except PermissionError:
        return "Require permission"