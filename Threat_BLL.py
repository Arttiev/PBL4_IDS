from Threat import *

_instance = None
dir_threat = "threats.txt" # relative from PBL4_IDS

class Threat_BLL:
    threats = []

    def __init__(self):
        global _instance
        if _instance == None:
            _instance = self
            Threat_BLL.load_threat()

    def get_all_threat():
        return Threat_BLL.threats

    def load_threat():
        """
        read threat.txt and return all threats where action_taken = false
        initiates the Threat_BLL.threats
        """
        with open(dir_threat,"r") as file:
            lines = file.readlines()
            for i in range(1,len(lines)):
                # src_IP, dst_IP, protocol, occur, action_taken
                #   0       1         2       3         4
                line = lines[i].strip()
                temp = line.split(",")
                th = Threat(temp[0],temp[1],temp[2])
                Threat_BLL.threats.append(Threat(temp[0],temp[1],temp[2],int(temp[3]),temp[4]=="True"))
        return

    def ignore_threat(number):
        return Threat_BLL.threats[number].ignore()
        
    def safe_threat(number):
        return Threat_BLL.threats[number].safe()

    def limit_threat(number):
        return Threat_BLL.threats[number].limit()

    def block_threat(number):
        return Threat_BLL.threats[number].block()

    def update_threat_list():
        markline = 0
        with open("threats.txt","r") as file:
            lines = file.readlines()
            markline = int(lines[0])
        
        with open(dir_threat,"w") as file:
            file.write(str(markline)+"\n")
            for i in range(len(Threat_BLL.threats)):
                file.write(Threat_BLL.threats[i].to_csv_form()+"\n")
    def to_tuples():
        """
        convert list[Threat] to list(tuples)
        """
        d = []
        for th in Threat_BLL.threats:
            if not th.action_taken: # neu chua xu ly thi moi view
                d.append((th.src_IP,th.dst_IP,th.proto,th.occur))
        return d
# How to use
# bll = Threat_BLL()
# print(len(Threat_BLL.threats))
# for threat in Threat_BLL.threats:
#     print(threat.to_csv_form())