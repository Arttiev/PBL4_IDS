from Alert import *

_instance = None
dir_Alert = "alert_csv.txt"  # relative from PBL4_IDS
#dir_Alert = "/var/log/snort/alert_csv.txt"

class Alert_BLL:
    alerts = []

    def __init__(self):
        global _instance
        if _instance == None:
            _instance = self
            Alert_BLL.load_Alert()

    def get_all_Alert():
        return Alert_BLL.alerts

    def load_Alert():
        """
        read Alert.txt and return all alerts where action_taken = false
        initiates the Alert_BLL.alerts
        """
        with open(dir_Alert, "r") as file:
            lines = file.readlines()
            for i in range(1, len(lines)):
                # src_IP, dst_IP, protocol, occur, action_taken
                #   0       1         2       3         4
                line = lines[i].strip()
                temp = line.split(",")
                Alert_BLL.alerts.append(
                    Alert(temp[0], temp[1], temp[2], int(temp[3]), temp[4], temp[5], temp[6], temp[7], temp[8], temp[9], temp[10], temp[11])
                )
        return

    def ignore_Alert(number):
        return Alert_BLL.alerts[number].ignore()

    def safe_Alert(number):
        return Alert_BLL.alerts[number].safe()

    def limit_Alert(number):
        return Alert_BLL.alerts[number].limit()

    def block_Alert(number):
        return Alert_BLL.alerts[number].block()

    def update_Alert_list():
        markline = 0
        with open("alerts.txt", "r") as file:
            lines = file.readlines()
            markline = int(lines[0])

        with open(dir_Alert, "w") as file:
            file.write(str(markline) + "\n")
            for i in range(len(Alert_BLL.alerts)):
                file.write(Alert_BLL.alerts[i].to_csv_form() + "\n")

    def to_tuples(month = "all"):
        """
        convert list[Alert] to list(tuples)
        """
        d = []
        for alert in Alert_BLL.alerts:
            if (month == "all"):
                d.append((alert.timestamp, alert.action, alert.protocol, alert.gid, alert.sid, alert.rev, alert.msg, alert.service, alert.src_IP, alert.src_Port, alert.dst_IP, alert.dst_Port))
            else:
                temp_month = alert.timestamp[0:2]
                if (temp_month == month):
                    d.append((alert.timestamp, alert.action, alert.protocol, alert.gid, alert.sid, alert.rev, alert.msg, alert.service, alert.src_IP, alert.src_Port, alert.dst_IP, alert.dst_Port))
        return d

    def protocol_count(month = "all") -> dict:
        dict = {}
        alert_List = Alert_BLL.to_tuples(month)
        alert_List = [list(alert_item) for alert_item in alert_List]
        for item in alert_List:
            if (str(item[2]) not in dict.keys()):
                dict[str(item[2])] = 1
            else:
                dict[str(item[2])] += 1
        return dict


# How to use
# bll = Alert_BLL()
# print(len(Alert_BLL.alerts))
# for Alert in Alert_BLL.alerts:
#     print(Alert.to_csv_form())
