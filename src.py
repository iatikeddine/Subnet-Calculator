from parsing import valid_cidr
import ipaddress
import sys

def get_broadcast_id(ip, mask):
    broadcast_id = []
    not_mask = []

    for octect in mask:
        not_mask.append(~octect & 255)

    for ip_octet, not_mask_octet in zip(ip, not_mask):
        broadcast_id.append(ip_octet | not_mask_octet)
    
    return broadcast_id

def get_network_id(ip, mask):
    network_id = []

    for ip_octet, mask_octet in zip(ip, mask):
        network_id.append(ip_octet & mask_octet)
    
    return network_id

def print_id(network_id, type):
    if type == "network":
        print("Network ID: ", end="")
    if type == "broadcast":
        print("Broadcast ID: ", end="")

    for x in range(4):
        if x == 3:
            print(network_id[x])
            break
        print(f"{network_id[x]}.", end="")

def get_usable_range(network_id, broadcast_id):
    no1, no2, no3, no4 = network_id
    bo1, bo2, bo3, bo4 = broadcast_id

    first_usable = ((no1 << 24) | (no2 << 16) | (no3 << 8) | no4) + 1
    last_usable = ((bo1 << 24) | (bo2 << 16) | (bo3 << 8) | bo4) - 1

    first_usable = str(ipaddress.IPv4Address(first_usable))
    last_usable = str(ipaddress.IPv4Address(last_usable))

    return first_usable, last_usable

def print_range(first_usable, last_usable):
    print("Usable IP address range: ", end="")
    print(f"{first_usable} - {last_usable}")

def print_ip(ip):
    for x in range(4):
        if x == 3:
            print(ip[x])
            break
        print(f"{ip[x]}.", end="")

if __name__ == "__main__":
    try:
        ip, mask = valid_cidr(sys.argv)
        if mask[3] == 255:
            print(f"IP address: ", end="")
            print_ip(ip)
        else:
            network_id = get_network_id(ip, mask)
            broadcast_id = get_broadcast_id(ip, mask)
            if mask[3] == 254:
                print("This is a point-to-point network")
                print("First ip address: ", end="")
                print_ip(network_id)
                print("Second ip address: ", end="")
                print_ip(broadcast_id)
            else:
                print_id(network_id, "network")
                print_id(broadcast_id, "broadcast")
                first_usable, last_usable = get_usable_range(network_id, broadcast_id)
                print_range(first_usable, last_usable)
    except Exception as e:
        sys.exit(f"{e}")
