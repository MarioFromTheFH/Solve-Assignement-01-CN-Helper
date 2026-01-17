import json 
import yaml 
import re 
import sys

BITCNT=8

# Source - https://stackoverflow.com/a/36394050
# Posted by Joe T. Boka
# Retrieved 2026-01-14, License - CC BY-SA 3.0

def split_string(string, split_string):
    return [string[i:i+split_string] for i in range(0, len(string), split_string)]

def doEncode(message, offset=8*8, praeambel="10101011"):

    print("Removing the first %d characters" % offset)

    str_prae = message[:offset]
    message=message[offset:]

    print(str_prae+": "+str(len(str_prae))+" Zeichen")
    print(message)

    print("The sequence "+praeambel+" appears in the input-string: "+str(message.count(praeambel))+" times")

    message=message.split(praeambel,1)[1]

    print("Message after Präambel:")
    print(message)
    if len(message)%BITCNT!=0 :
        print(str(len(message))+" %"+str(BITCNT)+" = "+str(len(message)%BITCNT))
        return 0    
    
    blocks = split_string(message,BITCNT)
    
    decode = []
    for block in blocks:
        dec = int(block, 2)     
        print(block+": "+chr(dec))   
        decode.append(chr(dec))

    print(''.join(decode))


if __name__ == "__main__":
    doEncode(sys.argv[1])
    

    