import socket
import ip_validator as check_ip
import scanners as sc



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def scan(ipAdd):

    for ports in portRange:
        print ('Scanning IP: ' + str(ipAdd) + ' on Port -> ' + str(ports))


        try:
            sock.connect((ipAdd, ports))
            print 'Port Open'
        except socket.error as e:
            print e

# openPorts = []
# closedPorts = []
portRange = []


raw_ip = raw_input("Enter valid IP Address: ")
ip_ok = check_ip.ipValidation(raw_ip)

if ip_ok == 0:
    ip = check_ip.make_ip()
else:
    print "IP Invalid" #debug


cidr = input("Enter CIDR Value '0 for single ip' : ")

option = raw_input("Host Discovery or Port scan? Reply with 'pn' or 'sc'. ")
if option == "pn":
    choice = 1
elif option == "sc":
    choice = 2

ipRange = []
init = 0
start_cap = []
end_cap = []
host_range = []

if cidr == 0:
    ipRange.append(ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3])

elif cidr >= 24:
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

else:
    print ("Program is prototype. Classes A and B hasn't been developed yet")

if choice == 2:
    Df_ports = raw_input("Default '21, 22, 23, 80, 137, 139, 445, 3306, 8080'? y/n: ")

    if Df_ports == 'y':
        portRange = [21, 22, 23, 53, 80, 137, 139, 445, 3306, 5000, 8080]
    elif Df_ports == 'n':
        start_port = raw_input("enter start port: ")
        end_port = raw_input("enter end port: ")

        for ports in range(int(start_port), int(end_port + 1)):
            portRange.append(str(ports))

    else:
        print "Invalid Choice"

    for ips in ipRange:
        scan = sc.synScan(ips, portRange)
        print scan[0]
        print scan[1]

elif choice == 1:
    for ips in ipRange:
        ping = sc.pingScan(ips)
        if ping == 1:
            print "Host is up"
        else:
            print "Host is down"





