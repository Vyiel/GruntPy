from random import randint
import subnet
import ip_validator as check_ip
import scanners as sc
import sys
from termcolor import *
import webbrowser
import colorama
colorama.init()



def main():

    portRange = []
    cidr = int()
    ipRange = []
    # init = 0
    # start_cap = []
    # end_cap = []
    # host_range = []
    scan_id = (randint(1, 1000))
    text_out_ip = []
    text_out_ping = []
    results = {}


    cprint("Your Scan ID for text output file is: "+str(scan_id), "red")

    raw_ip = raw_input("Enter valid IP Address: ")
    ip_ok = check_ip.ipValidation(raw_ip)

    if ip_ok == 0:
        ip = check_ip.make_ip()
    else:
        cprint('IP Invalid. Restarting!!!', 'red')
        main()
    try:
        cidr = int(input("Enter CIDR Value '0 for single ip' : "))
    except:
        cprint("Invalid CIDR Value. Restarting!!! ", 'red')
        main()


    subnet.calculate_subnet(ip, cidr)

    # option = raw_input("Host Discovery or Port scan? Reply with 'pn' or 'sc'. ")
    # if option == "pn":
    #     choice = 1
    # elif option == "sc":
    #     choice = 2
    # else:
    #     cprint("Invalid Choice. Restarting!!! ", 'red')
    #     main()
    #
    # if choice == 2:
    #     Df_ports = raw_input("Default '21, 22, 23, 80, 137, 139, 445, 3306, 8080'? y/n: ")
    #
    #     if Df_ports == 'y':
    #         portRange = [21, 22, 23, 53, 80, 137, 139, 445, 3306, 8080]
    #     elif Df_ports == 'n':
    #         rchoice = raw_input("Would you like a range or defined ports? Reply with 'rn' or 'df': ")
    #         if rchoice == "rn":
    #
    #             start_port = raw_input("enter start port: ")
    #             end_port = raw_input("enter end port: ")
    #             try:
    #                 start_port = int(start_port)
    #                 end_port = int(end_port)
    #             except:
    #                 cprint("Port invalid. Restarting!!! ", 'red')
    #                 main()
    #
    #             for ports in range(start_port, end_port + 1):
    #                 portRange.append(ports)
    #
    #         elif rchoice == "df":
    #             user_ports = raw_input("Enter ports separated with comma ',': ")
    #             def_ports = user_ports.split(",")
    #
    #             try:
    #                 for p in def_ports:
    #                     portRange.append(int(p))
    #             except:
    #                 cprint("Invalid Port exception caught!!! Restarting", "red")
    #
    #         else:
    #             cprint("Invalid Choice. Restarting!!! ", 'red')
    #             main()
    #     else:
    #         cprint("Invalid Choice. Restarting!!! ", 'red')
    #         main()
    #
    #     cprint("Only displaying open ports! ", "yellow")
    #
    #     for ips in ipRange:
    #         scan = sc.synScan(ips, portRange)
    #         if len(scan[0]) == 0:
    #             cprint("No open ports found on: "+ips, "red")
    #         else:
    #             cprint("On IP: "+ips, "cyan")
    #             text_out_ip = ips
    #             text_out_ports = []
    #             for open_port in scan[0]:
    #                 cprint("Port: "+open_port+" is open ", "green")
    #                 text_out_ports.append(open_port)
    #             results[text_out_ip] = text_out_ports
    #
    # elif choice == 1:
    #     for ips in ipRange:
    #         text_out_ip.append(ips)
    #         ping = sc.pingScan(ips)
    #         if ping == 1:
    #             cprint(ips+" is up!", "green")
    #             text_out_ping.append(ping)
    #         else:
    #             cprint(ips+" is down!", "red")
    #
    # if len(results) != 0:
    #     sys.stdout = open(str(scan_id)+".txt", "w")
    #     for keys in results.keys():
    #         print ""
    #         print "Open ports on IP "+str(keys)+": "
    #         for values in results[keys]:
    #             print values
    #     print "______________________ End of Scan Results ______________________ "
    #     print ""
    #     sys.stdout.close()
    #     webbrowser.open(str(scan_id)+".txt")
    #

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cprint("You have pressed an escape sequence. Quitting!!! ", "red")
        sys.exit(0)



