from termcolor import *
import colorama
colorama.init()
portRange = []
default_ports = []
clean_range = []
split = []


def manualPorts():
    while True:

        user_ports = input("Enter ports separated with comma ',': ")
        def_ports = user_ports.split(",")
        try:
            for p in def_ports:
                portRange.append(int(p))
        except:
            cprint("Invalid Ports detected!!!", "red")
            portRange[:] = []

        for q in portRange:
            if q > 0 and q <= 65535:
                return portRange
                continue
            else:
                cprint("Invalid Ports detected!!!", "red")
                portRange[:] = []
                break


def preDefinedPorts():
    default_ports = [21, 22, 23, 25, 53, 80, 110, 137, 138, 139, 445, 443, 554, 8080]
    portRange = default_ports
    return portRange

def manualRange():
    while True:

        mrange = input("Enter Port range separated by '-' ")
        if mrange.count("-") == 1:
            split = mrange.split("-")
            if len(split) == 2:
                try:
                    for i in split:
                        clean_range.append(int(i))
                    for j in range(clean_range[0], clean_range[1]+1):
                        portRange.append(int(j))
                except:
                    cprint("Invalid Port range detected!!! ", "red")
                    clean_range[:] = []
                    portRange[:] = []
                    continue

                for q in portRange:
                    if q > 0 and q <= 65535:
                        return portRange
                        continue
                    else:
                        cprint("Invalid Ports detected!!!", "red")
                        portRange[:] = []
                        clean_range[:] = []
                        break

            else:
                cprint("Invalid Port range detected!!!", "red")
                continue
        else:
            cprint("Invalid Port range detected!!!", "red")
            continue


def unknownAction():
    return False



# print manualRange()




