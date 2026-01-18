import sys
import binascii

# Source - https://stackoverflow.com/a/4859937
# Posted by Onedinkenedi, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-18, License - CC BY-SA 3.0
SCALE = 16 ## equals to hexadecimal
NUM_OF_BITS = 8

def do_mac_splitting(mac_address):
    mac_list=mac_address.split(":")
    print(mac_list)

    output_list=[]
    output_list6=[]
    for byte in mac_list:
        output_list.append(bin(int(byte, SCALE))[2:].zfill(NUM_OF_BITS))        
        output_list6.append(bin(int(byte[0], SCALE))[2:].zfill(NUM_OF_BITS)+bin(int(byte[1], SCALE))[2:].zfill(NUM_OF_BITS))

    print("BIN-MAC-ADR: "+':'.join([str(x) for x in output_list]))
    print("PLAIN-BIN:   "+"".join(output_list))
    print("BIN-SINGLE:  "+"".join(output_list6))


if __name__ == "__main__":
    do_mac_splitting(sys.argv[1])
    
