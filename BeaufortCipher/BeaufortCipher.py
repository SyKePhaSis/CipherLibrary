import sys
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text:str,key:str) -> str:
    enc = []
    for i,v in enumerate(text):
        if v != ' ':
            ind_m = ALPHABET.find(v.upper())
            ind_k = ALPHABET.find(key[i % len(key)].upper())
            c = ALPHABET[(ind_k - ind_m) % 26]
        else:
            c = ' '
        enc.append(c)
    return ''.join(enc)

def decrypt(text,key):
    dec = []
    for i,v in enumerate(text):
        if v != ' ':
            ind_c = ALPHABET.find(v.upper())
            ind_k = ALPHABET.find(key[i % len(key)].upper())
            c = ALPHABET[(ind_k - ind_c) % 26]
        else:
            c = ' '
        dec.append(c)
    return ''.join(dec)

def main():
    if len(sys.argv) == 4:  
        match sys.argv[1].lower():
            case 'encrypt':
                print(encrypt(sys.argv[2],sys.argv[3]))
            case 'decrypt':
                print(decrypt(sys.argv[2],sys.argv[3]))
            case default:
                print('''
                The mode you entered could not be recognised!
                To encrypt or decrypt the text enter the following command:

                - BeaufordCipher.py encrypt text key

                - BeaufordCipher.py decrypt text key
                
                ''')
    else:
        print('''
        To encrypt or decrypt the text enter the following command:\n
        - BeaufordCipher.py encode text key\n
        - BeaufordCipher.py decode text key
        ''')

main()