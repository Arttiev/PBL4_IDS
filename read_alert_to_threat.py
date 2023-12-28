from Threat import *

dir_log = "/var/log/snort/alert_csv.txt"
# dir_log = "alert_csv.txt" # for testing on windows


def read_alert_to_threat():
    # open threats.txt, append all into threats
    """
    This function browse the alert_csv.txt file, read the logs and convert into threats
    The function MUST be called before loading Threat_BLL.get_all_threat()
    """
    threats = []
    markline = 0
    with open("threats.txt", "r") as file:
        lines = file.readlines()
        if len(lines) > 0:
            markline = int(lines[0])
        for i in range(1, len(lines)):
            # src_IP, dst_IP, protocol, occur, action_taken
            #   0       1         2       3         4
            line = lines[i].strip()
            if line == "":
                continue
            temp = line.split(",")
            threats.append(
                Threat(temp[0], temp[1], temp[2], int(temp[3]), temp[4] == "True")
            )

    # open alert_fast.txt, look for new threats
    with open(dir_log, "r") as file:
        lines = file.readlines()  # Read all lines into a list
        for i in range(markline, len(lines)):
            # timestamp, action, protocol, gid, sid, rev, msg, service, src_IP, src_port, dst_IP, dst_port
            #     0         1       2       3    4    5    6      7        8        9       10      11
            line = lines[i].strip()  # Remove trailing newline characters
            temp = line.split(",")  # Split the line using comma as the separator
            threat = Threat(temp[8], temp[10], temp[2])
            if (
                threat.src_IP == "unknown"
                or threat.src_IP == ""
                or threat.dst_IP == ""
                or threat.dst_IP == "unknown"
                or threat.proto == ""
                or threat.proto == "unknown"
            ):
                continue
            check = 0
            for j in range(len(threats)):
                if threats[j] == threat:
                    threats[j].occur += 1
                    check = 1
                    break
            if check == 0:
                threats.append(threat)

        markline = len(lines) - 1

    with open("threats.txt", "w") as file:
        file.write(str(markline) + "\n")
        for i in range(len(threats)):
            file.write(threats[i].to_csv_form() + "\n")
