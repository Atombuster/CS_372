a = "192.168.1.2"
b = "10.20.30.40"
c = "127.0.0.1"
d = 3325256824
e = 3405803976
f = 3221225987
print_bytes = lambda s: print(' '.join(f'{b:02x}' for b in s))

def iptodecimal(string):
    numbers = string.split(".")
    i = 0
    hexnumber = 0
    while i <= 3:
        if hexnumber == 0:
            hexnumber = int(numbers[i])
        else:
            hexnumber = hexnumber << 8 | int(numbers[i])  
        i += 1
    return int(hexnumber)


def decimaltiip (number):
    i = 0
    array = []
    output = ''

    while i <= 3:
        
        array.append(number & 0xff)
        number = (number >> 8) 
        i += 1
    #print(array)
    output = str(array[3]) + '.' + str(array[2]) +'.'+ str(array[1]) +'.'+ str(array[0])
    return output

print("Part 1")
print(iptodecimal(a))
print(iptodecimal(b))
print(iptodecimal(c))
print("Part 2")
print(decimaltiip(d))
print(decimaltiip(e))
print(decimaltiip(f))