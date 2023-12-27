# define class Alert

import modify_files as mf


class Alert:
    """
    Class Alert denote a specific traffic that is suspicious,
    thus can be block with a snort rule
    --- block <protocol> <sourceIP> any -> <destinationIP> any
    or a firewall rule
    --- ufw deny proto <protocol> from <sourceIP> to <destinationIP>
    """

    def __init__(self, timestamp, action, protocol, gid, sid, rev, msg, service, src_IP, src_Port, dst_IP, dst_Port, occur=1, action_taken=False):
        """
        A Alert consist of such fields
            src_IP (str): source IP
            dst_IP (str): destination IP
            proto (str): protocol
            occur (int): occurence in alert log
            action_taken (bool): is ignored/blocked, thus need no more concern
        """
        self.timestamp = timestamp
        self.action = action
        self.protocol =protocol
        self.gid = gid
        self.sid = sid
        self.rev = rev
        self.msg = msg
        self.service = service
        self.src_IP = src_IP
        self.src_Port = src_Port
        self.dst_IP = dst_IP
        self.dst_Port = dst_Port
        self.occur = occur
        self.action_taken = action_taken

    def __eq__(self, other):
        """
        Comparison between 2 Alerts
        """
        return (
            isinstance(other, Alert)
            and self.src_IP == other.src_IP
            and self.dst_IP == other.dst_IP
            and self.proto == other.proto
        )

    def to_csv_form(self):
        return (
            self.src_IP
            + ","
            + self.dst_IP
            + ","
            + self.protocol
            + ","
            + str(self.occur)
            + ","
            + str(self.action_taken)
        )

    def safe(self):
        """
        Need to add following rule to local.rules
        """
        new_rule = (
            "pass "
            + self.proto.lower()
            + " "
            + self.src_IP
            + " any -> "
            + self.dst_IP
            + " any"
        )
        result = mf.add_local_rules(new_rule)
        self.action_taken = True
        mf.reload_ufw()
        return result

    def ignore(self):
        self.action_taken = True
        return "Ignored"

    def limit(self):
        """
        Need to execute following firewall rule
        """
        new_rule = (
            "ufw route prepend limit proto "
            + self.proto.lower()
            + " from "
            + self.src_IP
            + " to "
            + self.dst_IP
        )
        result = mf.ufw_execute(new_rule)
        self.action_taken = True
        mf.reload_ufw()
        return result

    def block(self):
        """
        Need to execute following firewall rule
        """
        new_ufw = (
            "ufw route prepend deny proto "
            + self.proto.lower()
            + " from "
            + self.src_IP
            + " to "
            + self.dst_IP
        )
        result = mf.ufw_execute(new_ufw)
        self.action_taken = True
        mf.reload_ufw()
        return result
