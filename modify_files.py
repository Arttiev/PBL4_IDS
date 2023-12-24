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
    
def reload_service(service):
    # os.popen("systemctl reload <service>")
    return

def ufw_execute(cmd):
    try:
        var = os.popen(cmd).read()
        return var
    except PermissionError:
        return "Require permission"