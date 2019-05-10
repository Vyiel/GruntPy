from termcolor import *
import colorama
colorama.init()

def calculate_subnet(ip, cidr):
    init = 0
    start_cap = []
    end_cap = []
    host_range = []
    ipRange = []
    given_host = None
    seg = None
    start_host = 0
    end_host = 0
    subnetting_error = 0
    classes = [0, 8, 16, 24, 32]
    subnetting_error = int(0)

    try:
        cidr = int(cidr)
    except:
        return False

    if int(cidr) == 0:
        ipRange.append(ip[0] + '.' + ip[1] + '.' + ip[2] + '.' + ip[3])
        return ipRange

    else:

        try:
            for i in range(len(classes)):
                if cidr >= classes[i] and cidr < classes[i+1]:
                    seg = classes[i]
        except:
            return False


        if subnetting_error != 1:

            if seg == 24:
                given_host = int(ip[3])
            elif seg == 16:
                given_host = int(ip[2])
            # print given_host #DEBUG

            net_bits = cidr - seg
            subnets = 2 ** net_bits
            s_range = 256 / subnets

            try:
                for i in range(subnets):
                    start_cap.append(int(init))
                    init = init + s_range
                    end_cap.append(int(init) - 1)
            except:
                return False

            try:
                for j in range(subnets):
                    if (given_host) >= start_cap[j] and (given_host) <= end_cap[j]:
                        start_host = int(start_cap[j])
                        end_host = int(end_cap[j])
                    else:
                        sub_calc_error = 1
            except:
                return False

            for k in range(start_host, end_host+1):
                (host_range.append(k))

            if seg == 24:
                for l in host_range:
                    ipRange.append(ip[0] + "." + ip[1] + "." + ip[2] + "." + str(l))
                return ipRange

            elif seg == 16:
                for l in host_range:
                    for m in range(256):
                        ipRange.append(ip[0] + "." + ip[1] + "." + str(l) + "." + str(m))
                return ipRange

            else:
                cprint(
                    "Program is prototype. Classes A and B hasn't been developed yet. Develop it yourself from the above codes!!! ",
                    "red")
                return False






########## CODE EXAMINATION AND TESTING ###########


#
# raw_ip = '147.211.117.114'
# ip = raw_ip.split('.')
# cidr = raw_input("Enter CIDR: ")
# result = calculate_subnet(ip, cidr)
#
# print result
#
# # if result != None:
# #     for values in result:
# #         print values