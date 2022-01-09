import binascii

CRYPTO = '636c6970636c6970636c6970636c6970636c6970636c6970636c6970636c6970636c6970636c6970636c6970636c6970636c6970636c6970636c6970636c6970636c6970636c6970636c6970636c6970636c6970636c6970636c6970'
hex_list = [CRYPTO[i: i + 2] for i in range(0, len(CRYPTO), 2)]

for i in hex_list:
  print(binascii.unhexlify(i).decode('utf-8'), end='')