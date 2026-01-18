import sys


def do_aufgabe(name):
    resultstr_dec=""
    resultstr_bin=""
    resultstr_bin_plain=""

    for c in name:
        dec_c=ord(c)
        resultstr_dec+=str(dec_c)+"-"
        resultstr_bin+=str("{0:b}".format(dec_c)+"-")
        resultstr_bin_plain+=str("{0:b}".format(dec_c))

    print("DEC: "+resultstr_dec[:-1])
    print("BIN: "+resultstr_bin[:-1])
    print("Plain: "+resultstr_bin_plain)
    

if __name__ == "__main__":
    do_aufgabe(sys.argv[1])
    
