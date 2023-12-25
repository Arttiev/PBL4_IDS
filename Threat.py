# define class Threat

import modify_files as mf

class Threat:
    """
    Class Threat denote a specific traffic that is suspicious,
    thus can be block with a snort rule
    --- block <protocol> <sourceIP> any -> <destinationIP> any 
    or a firewall rule
    --- ufw deny proto <protocol> from <sourceIP> to <destinationIP> 
    """
    def __init__(self, src_IP, dst_IP, proto, occur = 1, action_taken = False):
        """
        A threat consist of such fields
            src_IP (str): source IP
            dst_IP (str): destination IP
            proto (str): protocol
            occur (int): occurence in alert log
            action_taken (bool): is ignored/blocked, thus need no more concern
        """
        self.src_IP = src_IP
        self.dst_IP = dst_IP
        self.proto = proto
        self.occur = occur
        self.action_taken = action_taken
    
    def __eq__(self, other):
        """
        Comparison between 2 threats
        """
        return (
            isinstance(other,Threat) 
            and self.src_IP == other.src_IP
            and self.dst_IP == other.dst_IP
            and self.proto == other.proto
        )
    
    def to_csv_form(self):
        return self.src_IP + "," + self.dst_IP + "," + self.proto + "," + str(self.occur) + "," + str(self.action_taken)
    
    def safe(self):
        """
        Need to add following rule to local.rules
        """
        new_rule = "pass " + self.proto.lower() + " " + self.src_IP + " any -> " + self.dst_IP + " any"
        result = mf.add_local_rules(new_rule)
        self.action_taken=True
        return result
    
    def ignore(self):
        self.action_taken=True
        return "Ignored"

    def limit(self):
        """
        Need to execute following firewall rule
        """
        new_rule = "ufw --dry-run prepend limit proto " + self.proto.lower() + " from " + self.src_IP + " to " + self.dst_IP 
        result = mf.ufw_execute(new_rule)
        self.action_taken=True
        return result

    def block(self):
        """
        Need to execute following firewall rule
        """
        new_ufw = "ufw --dry-run prepend deny proto " + self.proto.lower() + " from " + self.src_IP + " to " + self.dst_IP 
        result = mf.ufw_execute(new_ufw)
        self.action_taken=True
        return result
    