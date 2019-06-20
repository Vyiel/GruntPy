from collections import OrderedDict
from random import randint
import subnet
import ip_validator as check_ip
import scanners as sc
import basicFunctions as bf
import sys
from termcolor import *
import webbrowser
import time
import colorama
colorama.init()


def main():

    portRange = []
    cidr = int()
    ipRange = []
    scan_id = (randint(1, 1000))
    text_out_ip = []
    text_out_ports = []
    text_out_ping = []
    results = OrderedDict()
    portPerIp = []
    ip = []
    sdict = {}

    def basicFuncSelect():
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

            action1 = input("Enter selection: ")
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
        return portRange

    def save(results, scan_id):

        if len(results) != 0:
            sys.stdout = open(str(scan_id) + ".html", "w")
            print ("""
            <!DOCTYPE html>
            <html>
            <head>
                <title> GruntPy : IP and Port status </title>
            </head>
            <body style="background-color: black">
                <center> <h2 style="color: #009432"> GruntPy : Open Ports/Alive or dead Status on IPs </h2> </center>
                <br>     
                   """)

            for keys in results.keys():

                print ("""
                
	            <div id="container" 
	            style="border: solid 1px; border-radius: 5px; height: 40px; width: 80%; 
	            display: block; position: relative;	left: 10%; margin: 5px; border-color: #009432;">
                    <div id="IP" style="display: inline-block; height: 100%; width: 20%; left: 0px; 
                    text-align: center; padding: 0px; margin: 0px">
			            <p style="margin: 10px; padding: 1px; position: relative; color: #009432;"> """ +str(keys) + """ </p> 
                    </div>    """)
                portPerIp = []
                for values in results[keys]:
                    portPerIp.append(str(values))

                toHtml = ",".join(portPerIp)

                print ("""
                    <div id="ports" style="display: inline-block; height: 100%; width: 78%; 
                    left: 0px; text-align: center; padding: 0px; margin: 0px; ">
			            <p style="margin: 10px; padding: 1px; position: relative; color: #009432;"> """ + toHtml + """ </p>
		            </div>
                    
                </div>""")

            print ("<br> <br>")
            print ('<center > <p style="color: #009432"> End of Scan Results </p> </center>')
            sys.stdout.close()
            webbrowser.open(str(scan_id) + ".html")
        else:
            sys.stdout = open(str(scan_id) + ".html", "w")
            print ("")
            print ('<p style="color: #009432" No viable results to display!!! ')
            print ('<center > <p style="color: #009432"> End of Scan Results </p> </center>')
            sys.stdout.close()
            webbrowser.open(str(scan_id) + ".txt")


    if len(sys.argv) > 1:

        while True:
            try:
                file_name = sys.argv[1]
                file = open(file_name, "r").read()
                break
            except:
                cprint("Invalid argument or content detected!!! ", "red")
                time.sleep(3)
                sys.exit()

        ipList = file.split(",")

        for ips in ipList:
            ip_ok = check_ip.ipValidation(ips)
            if ip_ok == 0:
                ipRange.append(check_ip.make_ip_composit())
            else:
                cprint("Invalid IP list detected!!! ", "red")
                sys.exit()
    cprint("Your Scan ID for text output file is: "+str(scan_id), "red")

    if len(ipRange) == 0:
        while True:

            raw_ip = input("Enter valid IP Address: ")
            ip_ok = check_ip.ipValidation(raw_ip)
            if ip_ok == 0:
                ip = check_ip.make_ip()
                break
            else:
                cprint("Invalid IP detected!!! ", "red")
                continue


        while True:

            cidr = input("Enter CIDR Value. Press '0' for Single IP: ")

            sn_result = subnet.calculate_subnet(ip, cidr)
            if sn_result != False:
                ipRange = subnet.calculate_subnet(ip, cidr)
                break
            else:
                cprint("Invalid CIDR detected!!! ", "red")
                continue

    sdict = {
        1: 'synScan',
        2: 'pingScan',
        3: 'udpScan',
        4: 'banner',
        5: 'whois'
            }

    cprint("""    
        1) For half connect scan (SYN)
        2) For scanning alive hosts/host in a range
        3) For scanning UDP ports.
        4) For Banner grabbing on (if) open ports
        5) For WhoIs Domain Name resolve
    """,
           "blue")

    while True:

        action2 = input("Enter selection: ")
        try:
            action2 = int(action2)
        except:
            cprint("Unavilable selection detected!!! ", "red")
            continue
        if action2 > 5 or action2 < 1:
            cprint("Unavilable selection detected!!! ", "red")
            continue
        else:
            break

    selection2 = sdict.get(action2, "False")

    if selection2 == 'synScan':
        portRange = basicFuncSelect()

        for ips in ipRange:
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

    if selection2 == 'pingScan':
        for ips in ipRange:
            text_out_ip = ips
            ping = sc.pingScan(ips)
            text_out_ping = []
            if ping == 1:
                cprint(ips + " is up!", "green")
                status = 'alive'
                text_out_ping.append(status)
                results[text_out_ip] = [status]
            else:
                cprint(ips + " is down!", "red")

    if selection2 == 'udpScan':
        portRange = basicFuncSelect()

        for ips in ipRange:
            scan = sc.udpScan(ips, portRange)
            if len(scan[0]) == 0:
                cprint("Closed ports found on: " + ips, "red")
            else:
                cprint("On IP: " + ips, "cyan")
                text_out_ip = ips
                text_out_ports = []
                for open_port in scan[0]:
                    cprint("Port: " + open_port + " is probably open or filtered ", "green")
                    text_out_ports.append(open_port)
                results[text_out_ip] = text_out_ports

    if selection2 == 'banner':
        portRange = basicFuncSelect()

        for ips in ipRange:
            scan = sc.banner(ips, portRange)
            if len(scan) == 0:
                cprint("Couldn't find any banners", "red")
            else:
                for banners in scan.keys():
                    cprint("Banner Grabbed for IP "+ str(ips) + ":"+ str(banners) + ": " + scan[banners], "green")


    if selection2 == 'whois':
        for ips in ipRange:
            cprint("Name resolved for: " + str(ips), "blue")
            if sc.whois(ips) != 0:
                result = (str(sc.whois(ips)))
                cprint(result, "green")
                results[ips] = [result]
            else:
                cprint("Couldn't resolve domain name for this IP", "red")



    while True:
        if len(results) != 0:
            if_save = input("Do you want to save the results into current directory? (y/n) ")
            if if_save == "y":
                save(results, scan_id)
                cprint("Thank you for using GruntPy. Quitting!!! ", "red")
                time.sleep(3)
                break
            elif if_save == "n":
                cprint("Thank you for using GruntPy. Quitting!!! ", "red")
                time.sleep(3)
                sys.exit()
                break
            else:
                cprint("Invalid selection detected", "red")
                continue
        break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cprint("You have pressed an escape sequence. Quitting!!! ", "red")
        time.sleep(3)
        sys.exit(0)



