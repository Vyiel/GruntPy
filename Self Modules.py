# def ipValidation(ip):


raw_ip_dirty = raw_input("enter ip address: ")
raw_ip = raw_ip_dirty.lstrip(",<.>/?':;-*/")
print "raw IP"
print raw_ip
dots = 0
meta_chars = [",", "/"]

# def badCheck():
# BAD CHARACTER CHECK WILL BE DONE HERE BECAUSE THE SEPARATOR COMES NEXT

# FUNCTIONS


def checkInt(clean_ip):
    try:
        for i in range(len(clean_ip)):
            clean_ip[i] = int(clean_ip[i])
            return 1
    except:
        return 0

# FUNCTIONS END


dots = raw_ip.count(".");
    
if dots != 3:
    valid_dots = 1
else:
    valid_dots = 0

# print valid_dots

# WHEN THE SEPARATION AND DOT VALIDATION IS DONE, THE IP WILL BE CLEANED AND BROKEN DOWN TO CHECK FOR INTEGERS ONLY

clean_ip = raw_ip.split(".")
print "just splitted"
print clean_ip

if checkInt(clean_ip) != 1:
    intFree == 0
else:
    intFree = 1

print "clean IP:"
print clean_ip
print intFree

if len(clean_ip) != 4:

    print clean_ip
    print "Invalid IP address Format"
else:
    for i in range(len(clean_ip)):
        if clean_ip[i] <= 255 and len(clean_ip[i]) >= 1:
            valid_octets = 1
        else:
            valid_octets = 0

    # print valid_octets

    if valid_dots and valid_octets == 1:
        print ('IP Address is Valid')
    else:
        print ('Invalid IP address Format')

