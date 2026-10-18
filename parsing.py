def prefix_to_mask(prefix):
    binary_str = ""
    rest = 32 - prefix

    binary_str += prefix * "1"
    binary_str += rest * "0"

    octet_1 = int(binary_str[0:8], 2)
    octet_2 = int(binary_str[8:16], 2)
    octet_3 = int(binary_str[16:24], 2)
    octet_4 = int(binary_str[24:32], 2)

    mask = [octet_1, octet_2, octet_3, octet_4]

    return mask


def validate_subnet_mask(subnet_mask: str) -> list:
    valid_mask_octets = [0, 128, 192, 224, 240, 248, 252, 254, 255]

    mask = subnet_mask.split('.')
    if len(mask) != 4:
        raise ValueError(
            "Error: Invalid subnet mask fromat\n"
            "Example: 255.255.255.0"
        )
    valid_mask = []
    for octet in mask:
        try:
            numerical_mask = int(octet)
        except:
            raise ValueError(
                "Error: Invalid subnet mask octect. Octet must be a number"
            )
        if numerical_mask not in valid_mask_octets:
            raise ValueError(
                f"Error: Subnet mask octets must be in this values {valid_mask_octets}"
            )
        valid_mask.append(numerical_mask)

    return valid_mask
    

def validate_ip_address(ip: str) -> list:
    octets = ip.split('.')
    if len(octets) != 4:
        raise ValueError(
            "Error: Invalid IP address format\n"
        )
    valid_ip = []
    for octet in octets:
        try:
            numerical_octet = int(octet)
        except:
            raise ValueError(
                "Error: Invalid IP address. Octet must be a digit"
            )
        if numerical_octet < 0 or numerical_octet > 255:
            raise ValueError(
                "Error: Invalid octet value. Octet valid range is 0-255"
            )
        valid_ip.append(numerical_octet)

    return valid_ip

def validate_prefix(prefix: str) -> int:
    try:
       numerical_prefix = int(prefix)
    except:
        raise ValueError(
            "Error: Invalid prefix. Prefix must be a / followed by digits"
        )
    if numerical_prefix < 0 or numerical_prefix > 32:
        raise ValueError(
            "Error: Invalid prefix value. Prefix must range from 0 to 32"
        )

    return numerical_prefix

def validate_ip_prefix(ip_prefix: str) -> tuple:
    pair = ip_prefix.split('/')
    if len(pair) != 2:
        raise ValueError(
            "Error: Invalid Address/Prefix format\n"
            "Example: python3 calculator.py 192.168.10.1/24"
        )
    ip_address, prefix = pair
    valid_ip = validate_ip_address(ip_address)
    valid_prefix = validate_prefix(prefix)

    return valid_ip, valid_prefix


def valid_cidr(cidr: list):
    args_len = len(cidr)
    if args_len == 1:
        raise ValueError(
            "Error: Error: Missing required arguments.\n\n"
            "Examples:\n"
            "python3 calculator.py 192.168.1.0/24\n"
            "python3 calculator.py 10.0.0.0 255.255.255.0\n"
        )
    if args_len > 3:
        raise ValueError(
            "Error: Only 2 arguments are required"
        )

    if args_len == 2:
        ip, prefix = validate_ip_prefix(cidr[1])
        mask = prefix_to_mask(prefix)
        return ip, mask

    ip = validate_ip_address(cidr[1])
    mask = validate_subnet_mask(cidr[2])

    return ip, mask
