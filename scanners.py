from scapy.all import *
from termcolor import colored


popen = []
pclosed = []
result = []
def synScan(ip, ports):
    for port in ports:
        print colored("Scanning IP: "+ str(ip) + " for port: " + str(port), "blue")
        target = IP(dst=ip)/TCP(dport=port,flags="S")
        reset_target = IP(dst=ip)/TCP(dport=port,flags="R")

        response = sr1(target,timeout=1,verbose=0)
        if response == None:
            pclosed.append(str(port))
        else:
            if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                popen.append(str(port))
            else:
                pclosed.append(str(port))
        sr(reset_target,timeout=0.5,verbose=0)
    return popen, pclosed

def pingScan(ip):
    target = IP(dst=ip)/ICMP()
    ping =sr1(target,timeout=1,verbose=0)
    if ping == None:
        return 0
    else:
        return 1



