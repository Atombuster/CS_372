import sys
import json
import math  # If you want to use math.inf for infinity

def ipv4_to_value(ipv4_addr):
    numbers = ipv4_addr.split(".")
    i = 0
    hexnumber = 0
    while i <= 3:
        if hexnumber == 0:
            hexnumber = int(numbers[i])
        else:
            hexnumber = hexnumber << 8 | int(numbers[i])  
        i += 1
    return int(hexnumber)

def value_to_ipv4(addr):

    i = 0
    array = []
    output = ''

    while i <= 3:
        
        array.append(addr & 0xff)
        addr = (addr >> 8) 
        i += 1
    #print(array)
    output = str(array[3]) + '.' + str(array[2]) +'.'+ str(array[1]) +'.'+ str(array[0])
    return output

def get_subnet_mask_value(slash):

    mask = 0
    
    mask_split = slash.split('/')
    i = 0
    mask_len = int(mask_split[1])

    while i < 32:
        if mask_len > 0:
            mask_len -= 1
            mask = mask << 1 | 1
        else:
            mask = mask << 1
        i += 1
    return(mask)

def ips_same_subnet(ip1, ip2, slash):

    ip1_value = ipv4_to_value(ip1)
    ip2_value = ipv4_to_value(ip2)
    mask = get_subnet_mask_value(slash)
    ip1_value = ip1_value & mask
    ip2_value = ip2_value & mask
    if ip1_value == ip2_value:
        return True
    else:
        return False


def find_router_for_ip(routers, ip):


    for subnet in routers:
        
        if ips_same_subnet(subnet, ip, routers[subnet]["netmask"]):
            return subnet
    return None

def dijkstras_shortest_path(routers, src_ip, dest_ip):
    """
    This function takes a dictionary representing the network, a source
    IP, and a destination IP, and returns a list with all the routers
    along the shortest path.

    The source and destination IPs are **not** included in this path.

    Note that the source IP and destination IP will probably not be
    routers! They will be on the same subnet as the router. You'll have
    to search the routers to find the one on the same subnet as the
    source IP. Same for the destination IP. [Hint: make use of your
    find_router_for_ip() function from the last project!]

    The dictionary keys are router IPs, and the values are dictionaries
    with a bunch of information, including the routers that are directly
    connected to the key.

    This partial example shows that router `10.31.98.1` is connected to
    three other routers: `10.34.166.1`, `10.34.194.1`, and `10.34.46.1`:

    {
        "10.34.98.1": {
            "connections": {
                "10.34.166.1": {
                    "netmask": "/24",
                    "interface": "en0",
                    "ad": 70
                },
                "10.34.194.1": {
                    "netmask": "/24",
                    "interface": "en1",
                    "ad": 93
                },
                "10.34.46.1": {
                    "netmask": "/24",
                    "interface": "en2",
                    "ad": 64
                }
            },
            "netmask": "/24",
            "if_count": 3,
            "if_prefix": "en"
        },
        ...

    The "ad" (Administrative Distance) field is the edge weight for that
    connection.

    **Strong recommendation**: make functions to do subtasks within this
    function. Having it all built as a single wall of code is a recipe
    for madness.
    """

    source_router = find_router_for_ip(routers, src_ip)
    destination_router = find_router_for_ip(routers, dest_ip)
    #print(source_router)
    #print(destination_router)
    if source_router == destination_router:
        return []
    
    distance = {}
    to_vist = set()
    parent = {}

    for router in routers:
        distance[router] = math.inf
        parent[router] = None
        to_vist.add(router)

    distance[source_router] = 0

    while to_vist:
        #print('new loop')
        current_node = None
        for router in to_vist:
            if current_node is None or distance[router] < distance[current_node]:
                current_node = router
        to_vist.remove(current_node)
        #print(current_node)
        for neighbor, data in routers[current_node]["connections"].items(): 

            alt = distance[current_node] + data["ad"]
            #print('{')
            #print(alt)
            #print(distance[neighbor]) 
            #print('}')

            if alt < distance[neighbor]:
                distance[neighbor] = alt
                parent[neighbor] = current_node

    if parent[destination_router] is None:
        return []
    path = []
    current = destination_router

    while current != source_router:
        path.append(current)
        current = parent[current]
    #this next line of code broke my brain I could not figure out this out for the life of me 
    path.append(source_router)
    #

    path.reverse()


    return path
    


#------------------------------
# DO NOT MODIFY BELOW THIS LINE
#------------------------------
def read_routers(file_name):
    with open(file_name) as fp:
        data = fp.read()

    return json.loads(data)

def find_routes(routers, src_dest_pairs):
    for src_ip, dest_ip in src_dest_pairs:
        path = dijkstras_shortest_path(routers, src_ip, dest_ip)
        print(f"{src_ip:>15s} -> {dest_ip:<15s}  {repr(path)}")

def usage():
    print("usage: dijkstra.py infile.json", file=sys.stderr)

def main(argv):
    try:
        router_file_name = argv[1]
    except:
        usage()
        return 1

    json_data = read_routers(router_file_name)

    routers = json_data["routers"]
    routes = json_data["src-dest"]

    find_routes(routers, routes)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    
