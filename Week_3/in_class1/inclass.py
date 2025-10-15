

def encode_data(message, value):
    
    encoded_message = message.encode('utf-8')
    value_in_bytes = value.to_bytes(4, "big")
    total_encoded_length = len(encoded_message) + len(value_in_bytes)
    output = total_encoded_length.to_bytes(2, "big") + encoded_message + value_in_bytes
    return output

def decode_data(data):
    length = int.from_bytes(data[0:2], "big")
    value = data[(length - 2): length + 2 ]
    message = data[2:(length - 2)]
    return (message.decode('utf-8'), int.from_bytes(value, "big"))

encoded = encode_data("hello world", 26)

print(decode_data(encoded))
