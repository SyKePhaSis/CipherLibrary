import math 
import random
import sys

ALPHABET = "ABCDEFFGHIJKLMNOPQRSTUVWXYZ "

def lcm(a,b):
    return (abs(a*b)/math.gcd(a,b))

def isPrime(n: int) -> bool:
    x = 2
    while x <= math.ceil(n/2):
        if (n % x) == 0:
            return False
        else:
            x += 1
    return True
            

def PhiPrime(n: int) -> int:
    #Because P,Q prime then Phi(Q) and Phi(P) where Phi is the euler Totent function
    return (n - 1)

def genD(P:int,Q:int,e:int)-> int:
    d = 1
    while True:
        num = (d*e) % (PhiPrime(Q)*PhiPrime(P))
        if num == 1:
            return d
        d += 1

def genE(N,phiN):
    for i in range(3,phiN,2):
        if N%i != 0 and phiN%i != 0 and isPrime(i):
            print(N)
            print(i)
            return i
    print("Regen")
    genKeys()

def genKeys(bound:int):
    Q = 4
    P = 4
    while not isPrime(Q):
        Q = random.randint(1,bound)
    while not isPrime(P):
        P = random.randint(1,bound)
    N = P*Q
    e = genE(N,(P-1)*(Q-1))
    d = genD(P,Q,e)
    return (P,Q,N,e),d 

def encrypt(N,e,text):
    t = list(text)
    for i in range(len(t)):
        index = ALPHABET.find(t[i].upper())
        t[i] = str((pow(int(index), int(e)) % int(N)))
    t = ' '.join(t)
    print(t)


def decrypt(N,d,text:str):
    t = text.split(' ')
    for i in range(len(t)): 
        n = (pow(int(t[i]),int(d)) % int(N))
        t[i] = ALPHABET[n]
    t = ''.join(t)
    print(t)

if len(sys.argv) >= 3:
    if(sys.argv[1].lower() == 'generate'):
        KeyPub,KeyPriv = genKeys(int(sys.argv[2]))
        print(f"Public Keys Are: [N = {KeyPub[2]}, e = {KeyPub[3]}, P = {KeyPub[0]}, Q={KeyPub[1]}]\nPrivateKey is: [d = {KeyPriv}]")
    elif len(sys.argv) == 5:
        if(sys.argv[1].lower() == 'encrypt'):
            print(encrypt(sys.argv[2],sys.argv[3],sys.argv[4]))
            sys.exit(0)
        elif(sys.argv[1].lower() == 'decrypt'):
            print(decrypt(sys.argv[2],sys.argv[3],sys.argv[4]))
            sys.exit(0)
        else:
            print("Mode not recognised! Please supply the desired mode(generate,encrypt,decrypt) by supplying it as an argument. \nFor example:\n-RSAPython.py generate\n-RSAPython.py encode\n-RSAPython.py decode")
            sys.exit(0)
    else:
        print("Please supply the following:\n\nFor generation: \n-Bounds \n\nFor encryption: \n-N \n-e \n-text\n\nFor decryption: \n-N \n-d \n-text")
else:
    print("Please supply the desired mode(generate,encrypt,decrypt) by supplying it as an argument. \nFor example:\n-RSAPython.py generate \n-RSAPython.py encode\n-RSAPython.py decode")
    sys.exit(0)