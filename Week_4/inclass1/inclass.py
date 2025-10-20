

ip = "1.2.3.255"
def ipfour (ip):
    ip_split = ip.split(".")

    if len(ip_split) > 4:
        return print("not a valid IP4 address")
    byte = b""
    i = 0
    while i < len(ip_split):
        byte += int(ip_split[i]).to_bytes(1)
        i = i + 1 

    print(byte)

ipfour(ip)