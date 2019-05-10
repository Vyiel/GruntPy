from memory_profiler import profile

from scapy.all import *
import colorama
from termcolor import *
colorama.init()
popen = []
pclosed = []
result = []


def synScan(ip, ports):
    popen[:] = []
    pclosed[:] = []
    # cprint("Scanning IP: " + str(ip) + " for open ports: ", "blue")

    for port in ports:

        cprint("Scanning IP: " + str(ip) + " for port: " + str(port), "blue")

        target = IP(dst=ip)/TCP(dport=port,flags="S")
        reset_target = IP(dst=ip)/TCP(dport=port,flags="R")

        response = sr1(target,timeout=0.5,verbose=0)
        if response is None:
            pclosed.append(str(port))
        else:
            if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                sr(reset_target, timeout=0.2, verbose=0)
                popen.append(str(port))
            else:
                pclosed.append(str(port))

    return [popen, pclosed]

def pingScan(ip):
    target = IP(dst=ip)/ICMP()
    ping =sr1(target,timeout=1,verbose=0)
    if ping == None:
        return 0
    else:
        return 1

def udpScan(ip, ports):
    popen[:] = []
    pclosed[:] = []

    for port in ports:

        cprint("Scanning IP: " + str(ip) + " for port: " + str(port), "blue")

        target = IP(dst=ip)/UDP(dport=port)
        response = sr1(target,timeout=1,verbose=0)
        if response is None:
            popen.append(str(port))
        elif response.haslayer(ICMP):
            pclosed.append(str(port))
    print popen, pclosed
    return [popen, pclosed]


# #TESTING FUNCTION
# iprange = ['192.168.1.0', '192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5', '192.168.1.6', '192.168.1.7']
# portrange = [21, 80, 8080, 82, 5000, 22, 23, 25, 533, 544, 8090, 6070]
#
# for ips in iprange:
#     a = synScan(ips, portrange)
#     print a
# #TESTING FUNCTION



