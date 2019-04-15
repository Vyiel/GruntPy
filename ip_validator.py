
def ipValidation(raw_ip_dirty):
    global clean_ip

    # raw_ip_dirty = raw_input("enter ip address: ")
    raw_ip = raw_ip_dirty.lstrip(",<.>/?':;-*/")
    # print "raw IP"
    # print raw_ip #debug
    dots = 0

    # FUNCTIONS

    def StringCleaner(clean_ip):
        try:
            for i in range(len(clean_ip)):
                clean_ip[i] = int(clean_ip[i])
            return 1
        except:
            return 0

    # FUNCTIONS END


    dots = raw_ip.count(".")

    if dots != 3:
        valid_dots = 0
    else:
        valid_dots = 1
    # print valid_dots #DEBUG

    # COUNTING OF DOT SEPARATORS IS DONE #

    clean_ip = raw_ip.split(".")
    # print clean_ip #DEBUG

    # IP IS NOW SPLIT INTO 4 OCTETS #

    if StringCleaner(clean_ip) != 1:
        # print StringCleaner(clean_ip) #DEBUG
        # print "Invalid IP address Format 1"
        error_code = 1
        return error_code

    # IP ADDRESS CHECKED FOR POSSIBLE STRING POLLUTION AND BRANCHED ACCORDING TO RESULTS #

    else:

        if len(clean_ip) != 4:
            # print "Invalid IP address Format 2"
            error_code = 2
            return error_code

    # CHECKED IF THE NUMBER OF OCTETS ARE 4 AND BRANCHED ACCORDINGLY #

        else:

            for i in range(len(clean_ip)):
                if clean_ip[i] <= 255 and clean_ip[i] >= 0:
                    valid_octets = 1
                else:
                    valid_octets = 0

    # CHECKED IF EACH OCTET IS LESSER THAN OR EQUAL TO 255 and more than 0 #

            # print valid_octets #DEBUG

            if valid_dots and valid_octets == 1:
                # print ('IP Address is Valid')
                # print clean_ip #debug
                error_code = 0
                return error_code

            else:
                # print ('Invalid IP address Format 3')
                error_code = 3
                return error_code
                # print clean_ip #debug


def make_ip():
    for i in range(len(clean_ip)):
        clean_ip[i] = str(clean_ip[i])
    return clean_ip



