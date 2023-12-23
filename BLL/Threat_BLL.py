from Data.Threat import *

def get_all_threat():
    """
    read threat.txt and return all threats where action_taken = false
    return a list of Threat
    """
    threats = []
    with open("threats.txt","r") as file:
        lines = file.readlines()
        for i in range(1,len(lines)):
            # src_IP, dst_IP, protocol, occur, action_taken
            #   0       1         2       3         4
            line = lines[i].strip()
            temp = line.split(",")
            threats.append(Threat(temp[0],temp[1],temp[2],int(temp[3]),temp[4]=="True"))
    return threats

def ignore_threat(number):
    threats = get_all_threat()
    threats[number].ignore()
    return

def block_threat(number):
    threats = get_all_threat()
    threats[number].ignore()

def update_threat_list():
    markline = 0
    with open("threats.txt","r") as file:
        lines = file.readlines()
        markline = int(lines[0])
    
    with open("threats.txt","w") as file:
        file.write(str(markline)+"\n")
        for i in range(len(threats)):
            file.write(threats[i].to_csv_form()+"\n")

threats = get_all_threat()
print(len(threats))
for threat in threats:
    print(threat.to_csv_form())