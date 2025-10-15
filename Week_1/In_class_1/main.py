#Austen T 9/29/25
#CS372

print_bytes = lambda s: print(' '.join(f'{b:02x}' for b in s))
some_bytes = b'hello'

my_string = '"Hi 🙂"'.encode('utf-8')
decode_thing = my_string.decode('utf-8')
print_bytes(my_string)
print(decode_thing)


#4. It errors out
#error UnicodeEncodeError: 'ascii' codec can't encode character '\U0001f642' in position 4: ordinal not in range(128)
#my_string_2 = '"Hi 🙂"'.encode('ascii')
#decode_thing_2 = my_string_2.decode('ascii')
#print_bytes(my_string_2)
#print(decode_thing_2)

#6. there is 2X amount of bytes
my_string_3 = '"Hi 🙂"'.encode('utf-16')
decode_thing_3 = my_string_3.decode('utf-16')
print_bytes(my_string_3)
print(decode_thing_3)

#7. The Program won't do that it gives an error.
#error UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
my_string_4 = '"Hi 🙂"'.encode('utf-16')
#decode_thing_4 = my_string_4.decode('utf-8')
decode_thing_5 = my_string_4.decode('utf-16')
print_bytes(my_string_4)
#print(decode_thing_4)
print(decode_thing_5)
