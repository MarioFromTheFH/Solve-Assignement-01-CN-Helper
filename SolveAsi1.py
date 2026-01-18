import json 
import yaml 
import re 
import sys

BITCNT=8

def find_period(message, pattern_rep=9):
    for i in range(1, len(message) // 2):
            pattern = message[:i]
            if message[i:i*10] == pattern * pattern_rep:
                return pattern
    return None

# Source - https://stackoverflow.com/a/36394050
# Posted by Joe T. Boka
# Retrieved 2026-01-14, License - CC BY-SA 3.0

def split_string(string, split_string):
    return [string[i:i+split_string] for i in range(0, len(string), split_string)]

def do_decode(message, offset=8*8, sequence="10101011"):

    print("Removing the first %d characters" % offset)

    #str_prae = message[:offset]
    #message=message[offset:]    

    print("The sequence "+sequence+" appears in the input-string: "+str(message.count(sequence))+" times")
    
    pattern = find_period(message)

    end_of_periodicity = 0

    if not pattern:
        print("No periods included. Starting now")        
    else:
        p_len = len(pattern)
        for i in range(0, len(message), p_len):
            if message[i:i+p_len] != pattern:
                end_of_periodicity = i
                break
    
        print(f"Periodizität bricht ab bei Index: {end_of_periodicity}")
        print(f"Fragment am Bruchpunkt: {message[end_of_periodicity:end_of_periodicity+10]}...")

    marker_index = message.find(sequence, end_of_periodicity)

    if marker_index == -1:
        marker_index = message.find(sequence)

    if marker_index != -1:
        payload = message[marker_index + len(sequence):]
        print(payload)
    else:
        print("No Marker found")

    print("Lenght of Payload: "+str(len(payload)))
    blocks = split_string(payload,BITCNT)
    
    decode = []
    for block in blocks:
        dec = int(block, 2)     
        print(block+": "+chr(dec))   
        decode.append(chr(dec))


    decoded_message=''.join(decode)
    print(decoded_message)    


if __name__ == "__main__":
    do_decode(sys.argv[1])
    

    