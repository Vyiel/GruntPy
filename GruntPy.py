import socket

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
cidr = input("Enter CIDR Value '0 for single ip' : ")
Df_ports = raw_input("Default '21, 22, 23, 80, 137, 139, 445, 3306, 8080'? y/n: ")

if Df_ports == 'y':
    portRange = [21, 22, 23, 80, 137, 139, 445, 3306, 8080]

ip = raw_ip.split(".")
# print ip

ipRange = []

if cidr == 0:
    ip = raw_ip
    scan(ip)

elif cidr >= 24:
    ipMod = ip[0:3]
    # print ipMod
    hostBits = 32 - cidr
    availHosts = (2 ** hostBits)

    for i in range(availHosts):
        ipRange.append(ipMod[0]+"."+ipMod[1]+"."+ipMod[2]+"."+str(i))
    for ips in ipRange:
        scan(ips)

elif cidr >= 16:
    ipMod = ip[0:2]
    # print ipMod
    hostBits = 24 - cidr
    availHosts = (2 ** hostBits)

    for i in range(availHosts):
        for j in range(256):
            ipRange.append(ipMod[0]+"."+ipMod[1]+"."+str(i)+"."+str(j))
    for ips in ipRange:
        scan(ips)

else:
    print ("Program is prototype. Classes A and B hasn't been developed yet")


