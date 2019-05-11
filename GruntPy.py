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


def main():

    portRange = []
    cidr = int()
    ipRange = []
    scan_id = (randint(1, 1000))
    text_out_ip = []
    text_out_ports = []
    text_out_ping = []
    results = {}
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
        return portRange

    def save(results, scan_id):

        if len(results) != 0:
            sys.stdout = open(str(scan_id) + ".html", "w")
            print ("""
            <!DOCTYPE html>
            <html>
            <head>
                <title> IP and Port status </title>
            </head>
            <body>
                <center> <h2> Open Ports/Alive or dead Status on IPs </h2> </center>
                <br>     
                   """)

            for keys in results.keys():

                print ("""
                
	            <div id="container" 
	            style="border: solid 1px; border-radius: 5px; height: 40px; width: 80%; 
	            display: block; position: relative;	left: 10%">
                    <div id="IP" style="display: inline-block; height: 100%; width: 20%; left: 0px; 
                    text-align: center; padding: 0px; margin: 0px">
			            <p style="margin: 10px; padding: 1px; position: relative;"> """ +str(keys) + """ </p> 
                    </div>    """)
                portPerIp = []
                for values in results[keys]:
                    portPerIp.append(str(values))

                toHtml = ",".join(portPerIp)

                print ("""
                    <div id="ports" style="display: inline-block; height: 100%; width: 78%; 
                    left: 0px; text-align: center; padding: 0px; margin: 0px; ">
			            <p style="margin: 10px; padding: 1px; position: relative; color: green;"> """ + toHtml + """ </p>
		            </div>
                    
                </div>""")

            print "<br> <br>"
            print "<center>______________________ End of Scan Results ______________________  </center>"
            sys.stdout.close()
            webbrowser.open(str(scan_id) + ".html")
        else:
            sys.stdout = open(str(scan_id) + ".html", "w")
            print ""
            print "No viable results to display!!! "
            print "______________________ End of Scan Results ______________________ "
            sys.stdout.close()
            webbrowser.open(str(scan_id) + ".txt")


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

    sdict = {
        1: 'synScan',
        2: 'pingScan',
        3: 'udpScan'
            }

    cprint("""    
        1) For half connect scan (SYN)
        2) For scanning alive hosts/host in a range
        3) For scanning UDP ports
    """,
           "blue")

    while True:

        action2 = raw_input("Enter selection: ")
        try:
            action2 = int(action2)
        except:
            cprint("Unavilable selection detected!!! ", "red")
            continue
        if action2 > 3 or action2 < 1:
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

    while True:
        if_save = raw_input("Do you want to save the results into current directory? (y/n) ")
        if if_save == "y":
            save(results, scan_id)
            break
        elif if_save == "n":
            cprint("Thank you for using GruntPy. Quitting!!! ", "red")
            sys.exit()
            break
        else:
            cprint("Invalid selection detected", "red")
            continue


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cprint("You have pressed an escape sequence. Quitting!!! ", "red")
        sys.exit(0)



