import binascii

def XORBreak(h):
    en = binascii.unhexlify(h)
    for key in range(256):
        de = ''.join(chr(b ^ key) for b in en)
        if de.isprintable():
            print(de)

with open("four.txt") as f:
    for line in f:
        XORBreak(line.rstrip("\n"))
