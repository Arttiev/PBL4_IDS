import os
import ufw

print("Hello world!")

dir_rule = "/usr/local/etc/rules/local.rules"
dir_log = "/var/log/snort/alert_csv.txt"
dir_config = "/usr/local/etc/snort/snort.lua"

# os.system("snort -c /usr/local/etc/snort/snort.lua")

# executable
# variable = os.popen("snort -c /usr/local/etc/snort/snort.lua").read()
# print(variable)

# executable
# rules = []
# with open("/usr/local/etc/rules/local.rules","r") as file:
#     lines = file.readlines()
#     for line in lines:
#         if line.strip() != "":
#             rules.append(line)
# print(rules)

# executable after changing permission:
# run: sudo chmod 777 /usr/local/etc/rules/local.rules
# with open("/usr/local/etc/rules/local.rules","a") as file:
#     # to append a new rule to local.rules
#     file.write("\nthis line has no idea\n")

# executable after changing permission:
# run: sudo chmod 777 /var/log/snort/alert_csv.txt
# temp = []
# with open("/var/log/snort/alert_csv.txt","r") as file:
#     lines = file.readlines()
#     for j in range(0,min(100,len(lines))): # print first 100 lines of alert_csv.txt
#         lines[j] = lines[j].strip()
#         split = lines[j].split(",")
#         temp.append(split)

# for record in temp:
#     print(record)

# another approach:
# last_ = os.popen("tail -10 /var/log/snort/alert_csv.txt").read()
# print(last_)

from Threat_BLL import *

bll = Threat_BLL()
for t in bll.threats:
    print(t.to_csv_form())