import sys

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def CaesarEncrypt(s: str,shift: int, reps: int = 1):
    str = list(s.upper())
    for z in range(reps):
        for i in range(len(str)):
            if str[i] != ' ':
                j = ALPHABET.find(str[i])
                print(j)
                str[i] = ALPHABET[abs((j + shift + 26))%26]
    print(''.join(str))
    sys.exit(0)

def CaesarDecrypt(s: str,shift: int, reps: int = 1):
    str = list(s.upper())
    for z in range(reps):
        for i in range(len(str)):
            if str[i] != ' ':
                j = ALPHABET.find(str[i])
                print(j)
                str[i] = ALPHABET[abs((j - shift + 26))%26]
    print(''.join(str))
    sys.exit(0)

if len(sys.argv) >= 5:
    if(sys.argv[1].lower() == "encrypt"):
        CaesarEncrypt(sys.argv[2], int(sys.argv[3]),int(sys.argv[4]))
    elif(sys.argv[1].lower() == "decrypt"):
        CaesarDecrypt(sys.argv[2], int(sys.argv[3]),int(sys.argv[4]))
    else:
        print("Mode not Recognised! Please Enter One of the following modes: \n -Encrypt \n -Decrypt")
else:
    print("CaesarPython usage: \n --mode Encrypt,Decrypt \n --text 'Encode This text' \n --shift 'shif-tnumber' \n --reps 'repetitions' \n Example: CaesarPython.py Encrypt 'Encode This Text' 4 2")
    sys.exit(0)


