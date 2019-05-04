from random import randint
import subnet
import ip_validator as check_ip
import scanners as sc
import basicFunctions as bf
import sys
import time
from termcolor import *
import webbrowser
import colorama
colorama.init()
from memory_profiler import profile

@profile()
def main():

    portRange = []
    cidr = int()
    ipRange = []
    scan_id = (randint(1, 1000))
    text_out_ip = []
    text_out_ports = []
    text_out_ping = []
    results = {}
    ip = []
    bfdict = {}
    times = int(0)


    cprint("Your Scan ID for text output file is: "+str(scan_id), "red")

    while True:

        raw_ip = raw_input("Enter valid IP Address: ")
        ip_ok = check_ip.ipValidation(raw_ip)
        if ip_ok == 0:
            ip = check_ip.make_ip()
            break
        else:
            cprint("Invalid IP detected!!! ", "red")
            continue


    while True:

        cidr = raw_input("Enter CIDR Value. Press '0' for Single IP: ")

        sn_result = subnet.calculate_subnet(ip, cidr)
        if sn_result != False:
            ipRange = subnet.calculate_subnet(ip, cidr)
            break
        else:
            cprint("Invalid CIDR detected!!! ", "red")
            continue


    bfdict = {
        1: bf.preDefinedPorts,
        2: bf.manualPorts,
        3: bf.manualRange

            }

    cprint("""    
    1) For scanning with Common Pre Defined Ports!
    2) For scanning with ports manually entered!
    3) For scanning with port range entered!
    """,
           "blue")

    while True:

        action1 = raw_input("Enter selection: ")
        try:
            action1 = int(action1)
        except:
            cprint("Unavilable selection detected!!! ", "red")
            continue
        if action1 > 3 or action1 < 1:
            cprint("Unavilable selection detected!!! ", "red")
            continue
        else:
            break

    portRange = bfdict.get(action1, bf.unknownAction)()

    for ips in ipRange:
        # times = times + 1
        # if times == 5:
        #     cprint("resting for 15 seconds!!! ", "green")
        #     time.sleep(5)
        #     times = 0


        scan = sc.synScan(ips, portRange)
        if len(scan[0]) == 0:
            cprint("No open ports found on: " + ips, "red")
        else:
            cprint("On IP: " + ips, "cyan")
            text_out_ip = ips
            text_out_ports = []
            for open_port in scan[0]:
                cprint("Port: " + open_port + " is open ", "green")
                text_out_ports.append(open_port)
            results[text_out_ip] = text_out_ports




















if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cprint("You have pressed an escape sequence. Quitting!!! ", "red")
        sys.exit(0)



