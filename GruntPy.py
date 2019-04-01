import socket
import ip_validator as check_ip



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


raw_ip = raw_input("Enter valid IP Address: ")
ip_ok = check_ip.ipValidation(raw_ip)

if ip_ok == 0:
    ip = check_ip.make_ip()
else:
    print "IP Invalid" #debug


cidr = input("Enter CIDR Value '0 for single ip' : ")
# Df_ports = raw_input("Default '21, 22, 23, 80, 137, 139, 445, 3306, 8080'? y/n: ")

# if Df_ports == 'y':
#     portRange = [21, 22, 23, 80, 137, 139, 445, 3306, 8080]

# print ip

ipRange = []
init = 0
start_cap = []
end_cap = []
host_range = []

if cidr == 0:
    ip = raw_ip
    # scan(ip)
    print ips

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

    for k in range(start_host, end_host):
        (host_range.append(k))

    for l in host_range:
        print ipMod[0] + "." + ipMod[1] + "." + ipMod[2] + "." + str(l)

















#     for i in range(availHosts):
#         ipRange.append(ipMod[0]+"."+ipMod[1]+"."+ipMod[2]+"."+str(i))
#     # for ips in ipRange:
#     #     # scan(ips)
#     #     print
#
# elif cidr >= 16:
#     ipMod = ip[0:2]
#     # print ipMod
#     hostBits = 24 - cidr
#     availHosts = (2 ** hostBits)
#
#     for i in range(availHosts):
#         for j in range(256):
#             ipRange.append(ipMod[0]+"."+ipMod[1]+"."+str(i)+"."+str(j))
#     for ips in ipRange:
#         # scan(ips)
#         print ips
# else:
#     print ("Program is prototype. Classes A and B hasn't been developed yet")
#
#
