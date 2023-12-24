import os

# set code_runner => executor map to use 'sudo python3 -u'
# run: sudo visudo 
# put this line below %sudo ALL=(ALL:ALL) ALL
# <username> ALL=(ALL) NOPASSWD: ALL

def ufw_status(mode=0):
    """
    View status:
    default 0: ufw status
    mode 1: ufw status verbose
    mode 2: ufw status numbered
    """
    cmd = "ufw status"
    if mode==1:
        cmd+= " verbose"
    elif mode==2:
        cmd+= " numbered"
    var = os.popen(cmd).read()
    return var

def ufw_add(protocol, src_IP, dst_IP, action, dry_run=False):
    """
    Add a rule:
    ufw [--dry-run] ACTION proto PROTOCOL from SRC_IP to DST_IP
    """
    cmd = "ufw "
    if dry_run: 
        # dry_run = True => test mode
        # dry_run = False => real action
        cmd+="--dry-run "
    cmd = cmd + action + " proto " + protocol + " from " + src_IP + " to " + dst_IP
    var = os.popen(cmd).read()
    return var

def ufw_delete(num, dry_run=False):
    """
    Delete a rule by number, using 
    ufw [--dry-run] --force delete NUM
    """
    cmd = "ufw "
    if dry_run:
        cmd+="--dry-run "
    cmd = cmd + "--force delete " + str(num)
    var = os.popen(cmd).read()
    return var

# print(ufw_add("tcp","192.168.1.0/24","192.168.199.0/24","allow",dry_run=False))
# print(ufw_delete(1,dry_run=False))
print(ufw_status(mode=1))