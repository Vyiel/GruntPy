
import ip_validator as check_ip
import scanners as sc
import sys
from termcolor import colored

def main():

    portRange = []
    cidr = int()

    raw_ip = raw_input("Enter valid IP Address: ")
    ip_ok = check_ip.ipValidation(raw_ip)

    if ip_ok == 0:
        ip = check_ip.make_ip()
    else:
        print colored('IP Invalid. Restarting!!!', 'red')
        main()
    try:
        cidr = int(input("Enter CIDR Value '0 for single ip' : "))
    except:
        print colored("Invalid CIDR Value. Restarting!!! ", 'red')
        main()

    ipRange = []
    init = 0
    start_cap = []
    end_cap = []
    host_range = []

    if cidr == 0:
        ipRange.append(ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3])

    elif cidr >= 24 and cidr < 33:
        ipMod = ip[0:3]
        given_host = int(ip[3])

        hostBits = 32 - cidr
        availHosts = (2 ** hostBits)
        net_bits = cidr - 24
        subnets = 2 ** net_bits
        s_range = 256 / subnets

        for i in range(subnets):
            start_cap.append(init)
            init = init + s_range
            end_cap.append(init - 1)

        for j in range(subnets):
            if given_host >= start_cap[j] and given_host <= end_cap[j]:
                start_host = int(start_cap[j])
                end_host = int(end_cap[j])
                break
            else:
                sub_calc_error = 1

        for k in range(start_host, end_host+1):
            (host_range.append(k))


        for l in host_range:
            ipRange.append(ipMod[0] + "." + ipMod[1] + "." + ipMod[2] + "." + str(l))

        # for ips in ipRange:
        #     print ips
        #DEBUG#

    elif cidr >= 16 and cidr < 24:
        ipMod = ip[0:2]
        given_host = int(ip[2])

        hostBits = 24 - cidr
        availHosts = (2 ** hostBits)
        net_bits = cidr - 16
        subnets = 2 ** net_bits
        s_range = 256 / subnets

        for i in range(subnets):
            start_cap.append(init)
            init = init + s_range
            end_cap.append(init - 1)

        for j in range(subnets):
            if given_host >= start_cap[j] and given_host <= end_cap[j]:
                start_host = int(start_cap[j])
                end_host = int(end_cap[j])
                break
            else:
                sub_calc_error = 1

        for k in range(start_host, end_host+1):
            (host_range.append(k))

        for l in host_range:
            for m in range(256):
                ipRange.append(ipMod[0] + "." + ipMod[1] + "." + str(l) + "." + str(m))

        # for ips in ipRange:
        #     print ips
        # DEBUG#

    elif cidr < 16:
        print colored("Program is prototype. Classes A and B hasn't been developed yet. Develop it yourself from the above codes!!! ", "red")
        main()

    else:
        print colored("Invalid CIDR Value. Restarting!!! ", 'red')
        main()

    option = raw_input("Host Discovery or Port scan? Reply with 'pn' or 'sc'. ")
    if option == "pn":
        choice = 1
    elif option == "sc":
        choice = 2
    else:
        print colored("Invalid Choice. Restarting!!! ", 'red')
        main()

    if choice == 2:
        Df_ports = raw_input("Default '21, 22, 23, 80, 137, 139, 445, 3306, 8080'? y/n: ")

        if Df_ports == 'y':
            portRange = [21, 22, 23, 53, 80, 137, 139, 445, 3306, 8080]
        elif Df_ports == 'n':
            rchoice = raw_input("Would you like a range or defined ports? Reply with 'rn' or 'df': ")
            if rchoice == "rn":

                start_port = raw_input("enter start port: ")
                end_port = raw_input("enter end port: ")
                try:
                    start_port = int(start_port)
                    end_port = int(end_port)
                except:
                    print colored("Port invalid. Restarting!!! ", 'red')
                    main()

                for ports in range(start_port, end_port + 1):
                    portRange.append(ports)

            elif rchoice == "df":
                user_ports = raw_input("Enter ports separated with comma ',': ")
                def_ports = user_ports.split(",")
                for ports in def_ports:
                    portRange.append(int(ports))
            else:
                print colored("Invalid Choice. Restarting!!! ", 'red')
                main()
        else:
            print colored("Invalid Choice. Restarting!!! ", 'red')
            main()

        print colored("Only displaying open ports! ", "yellow")
        for ips in ipRange:
            scan = sc.synScan(ips, portRange)
            if not scan[0]:
                print colored("No open ports found on: "+ips, "red")
            else:
                print "On IP: "+ips
                for open_port in scan[0]:
                    print colored("Port: "+open_port+" is open ", "green")

    elif choice == 1:
        for ips in ipRange:
            ping = sc.pingScan(ips)
            if ping == 1:
                print colored(ips+" is up!", "green")
            else:
                print colored(ips+" is down!", "red")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print colored("You have pressed an escape sequence. Quitting!!! ", "red")
        sys.exit(0)


