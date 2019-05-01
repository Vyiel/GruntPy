from random import randint
import subnet
import ip_validator as check_ip
import scanners as sc
import basicFunctions as bf
import sys
from termcolor import *
import webbrowser
import colorama
colorama.init()



def main():

    portRange = []
    cidr = int()
    ipRange = []
    scan_id = (randint(1, 1000))
    text_out_ip = []
    text_out_ping = []
    results = {}
    ip = []
    bfdict = {}


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
    def inputAction1():
        while True:
            try:
                action1 = raw_input("Enter selection ")
                action1 = int(action1)

                return action1
            except:
                cprint("Selection not integer!!! ", "red")
                continue

    ia1 = inputAction1()


    got = bfdict.get(ia1, False)()
    print got
















if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cprint("You have pressed an escape sequence. Quitting!!! ", "red")
        sys.exit(0)



