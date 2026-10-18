from parsing import valid_cidr
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

def print_usable_range(network_id, broadcast_id):
    

if __name__ == "__main__":
    try:
        ip, mask = valid_cidr(sys.argv)
        network_id = get_network_id(ip, mask)
        print_id(network_id, "network")
        broadcast_id = get_broadcast_id(ip, mask)
        print_id(broadcast_id, "broadcast")
    except Exception as e:
        sys.exit(f"{e}")
