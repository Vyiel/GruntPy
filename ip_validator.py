
def ipValidation(raw_ip_dirty):
    global clean_ip

    # raw_ip_dirty = raw_input("enter ip address: ")
    raw_ip = raw_ip_dirty.lstrip(",<.>/?':;-*/")

    dots = 0
    def StringCleaner(clean_ip):
        try:
            for i in range(len(clean_ip)):
                clean_ip[i] = int(clean_ip[i])
            return 1
        except:
            return 0


    dots = raw_ip.count(".")

    if dots != 3:
        valid_dots = 0
    else:
        valid_dots = 1

    clean_ip = raw_ip.split(".")

    if StringCleaner(clean_ip) != 1:
        error_code = 1
        return error_code
    else:
        if len(clean_ip) != 4:
            error_code = 2
            return error_code
        else:
            for i in range(len(clean_ip)):
                if clean_ip[i] <= 255 and clean_ip[i] >= 0:
                    valid_octets = 1
                else:
                    valid_octets = 0
                    break

            if valid_dots and valid_octets == 1:
                error_code = 0
                return error_code
            else:
                error_code = 3
                return error_code


def make_ip():
    for i in range(len(clean_ip)):
        clean_ip[i] = str(clean_ip[i])
    return clean_ip

def make_ip_composit():
    ip = make_ip()
    joiner = "."
    composite_ip = joiner.join(ip)
    return composite_ip


