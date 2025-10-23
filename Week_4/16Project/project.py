#Austen Turbyne
print_bytes = lambda s: print(' '.join(f'{b:02x}' for b in s))
def ipfour (ip, size):
    source_dest = ip.split()
    SoureIp = source_dest[0].split('.')
    
    DestIP = source_dest[1].split('.')
    SoureIp.extend(DestIP)
    SoureIp.append("0")#Z
    SoureIp.append("6")#P

    ip_split = SoureIp

    byte = b""
    i = 0
    while i < len(ip_split):
        byte += int(ip_split[i]).to_bytes(1)
        i = i + 1 
    byte += size.to_bytes(2)
    return(byte)


def checksum(pseudo_header, tcp_data):
    data = pseudo_header + tcp_data

    total = 0
    offset = 0

    while offset < len(data):  

        word = int.from_bytes(data[offset:offset + 2], "big")
        total += word
        
        total = (total & 0xffff) + (total >> 16)  # carry around
        offset += 2
        #print(total)
    return (~total) & 0xffff




i = 0

while i < 10:
    tcp_data_file = open("./tcp_data/tcp_data_" + str(i)+".dat", "rb")
    data_file = tcp_data_file.read()
    #print(data_file)
    data_file_len = len(data_file)
    tcp_zero_cksum = data_file[:16] + b'\x00\x00' + data_file[18:]
    if len(tcp_zero_cksum) % 2 == 1:
        tcp_zero_cksum += b'\x00'


    tcp_addrs_file = open("./tcp_data/tcp_addrs_" + str(i)+".txt")
    address = tcp_addrs_file.read()
    #print(address)
    pseudo_header = ipfour(address, data_file_len)


    datachecksum = int.from_bytes(data_file[16:18], "big")
    #print(datachecksum)
    #print_bytes(pseudo_header)
    mychecksum = checksum(pseudo_header, tcp_zero_cksum)
    #print(mychecksum)

    if datachecksum == mychecksum:
        print("PASS")
    else:
        print("FAIL")



    tcp_addrs_file.close
    tcp_data_file.close



    i += 1

