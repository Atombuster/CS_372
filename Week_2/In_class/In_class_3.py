

def subnet (ip,subnet_mask):
    split_ip = ip#.split('.')
    split_subnet_mask = subnet_mask#.split('.')
    a = [0,0,0,0]
    b = [0,0,0,0]
    inverted_split_subnet_mask = [0,0,0,0]
    #print(split_ip)
    #print(split_subnet_mask)
    for x in range(len(split_ip)):
        #print(x)
        a[x] = split_ip[x] & split_subnet_mask[x]
        inverted_split_subnet_mask[x] = ~split_subnet_mask[x] & 0xff
        b[x] = split_ip[x] & inverted_split_subnet_mask[x]
    
    return a, b

print(subnet([192,168,17,2], [255,0,0,0]))
print(subnet([192,168,17,2], [255,255,0,0]))
print(subnet([192,168,17,2], [255,255,255,0]))
print(subnet([192,168,17,2], [255,192,0,0]))
print(subnet([192,168,17,2], [255,255,248,0]))