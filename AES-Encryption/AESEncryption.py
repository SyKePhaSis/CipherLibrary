import random

#TABLES AND CONSTANTS WE ARE USING

#Rihndael S-box
sbox = [['0x63','0x7c','0x77','0x7b','0xf2','0x6b','0x6f','0xc5','0x30','0x01','0x67','0x2b','0xfe','0xd7','0xab','0x76'],
['0xca','0x82','0xc9','0x7d','0xfa','0x59','0x47','0xf0','0xad','0xd4','0xa2','0xaf','0x9c','0xa4','0x72','0xc0'],
['0xb7','0xfd','0x93','0x26','0x36','0x3f','0xf7','0xcc','0x34','0xa5','0xe5','0xf1','0x71','0xd8','0x31','0x15'],
['0x04','0xc7','0x23','0xc3','0x18','0x96','0x05','0x9a','0x07','0x12','0x80','0xe2','0xeb','0x27','0xb2','0x75'],
['0x09','0x83','0x2c','0x1a','0x1b','0x6e','0x5a','0xa0','0x52','0x3b','0xd6','0xb3','0x29','0xe3','0x2f','0x84'],
['0x53','0xd1','0x00','0xed','0x20','0xfc','0xb1','0x5b','0x6a','0xcb','0xbe','0x39','0x4a','0x4c','0x58','0xcf'],
['0xd0','0xef','0xaa','0xfb','0x43','0x4d','0x33','0x85','0x45','0xf9','0x02','0x7f','0x50','0x3c','0x9f','0xa8'],
['0x51','0xa3','0x40','0x8f','0x92','0x9d','0x38','0xf5','0xbc','0xb6','0xda','0x21','0x10','0xff','0xf3','0xd2'],
['0xcd','0x0c','0x13','0xec','0x5f','0x97','0x44','0x17','0xc4','0xa7','0x7e','0x3d','0x64','0x5d','0x19','0x73'],
['0x60','0x81','0x4f','0xdc','0x22','0x2a','0x90','0x88','0x46','0xee','0xb8','0x14','0xde','0x5e','0x0b','0xdb'],
['0xe0','0x32','0x3a','0x0a','0x49','0x06','0x24','0x5c','0xc2','0xd3','0xac','0x62','0x91','0x95','0xe4','0x79'],
['0xe7','0xc8','0x37','0x6d','0x8d','0xd5','0x4e','0xa9','0x6c','0x56','0xf4','0xea','0x65','0x7a','0xae','0x08'],
['0xba','0x78','0x25','0x2e','0x1c','0xa6','0xb4','0xc6','0xe8','0xdd','0x74','0x1f','0x4b','0xbd','0x8b','0x8a'],
['0x70','0x3e','0xb5','0x66','0x48','0x03','0xf6','0x0e','0x61','0x35','0x57','0xb9','0x86','0xc1','0x1d','0x9e'],
['0xe1','0xf8','0x98','0x11','0x69','0xd9','0x8e','0x94','0x9b','0x1e','0x87','0xe9','0xce','0x55','0x28','0xdf'],
['0x8c','0xa1','0x89','0x0d','0xbf','0xe6','0x42','0x68','0x41','0x99','0x2d','0x0f','0xb0','0x54','0xbb','0x16']]

#CONSTANT MATRIX
c = [['0x02','0x03','0x01','0x01'],
    ['0x01','0x02','0x03','0x01'],
    ['0x01','0x01','0x02','0x03'],
    ['0x03','0x01','0x01','0x02']]

invC = [["0x0e","0xb","0x0d","0x09"],
        ["0x09","0x0e","0x0b","0x0d"],
        ["0x0d","0x09","0x0e","0x0b"],
        ["0x0b","0x0d","0x09","0x0e"]]

invSBox =   [["0x52","0x09","0x6a","0xd5","0x30","0x36","0xa5","0x38","0xbf","0x40","0xa3","0x9e","0x81","0xf3","0xd7","0xfb"],
            ["0x7c","0xe3","0x39","0x82","0x9b","0x2f","0xff","0x87","0x34","0x8e","0x43","0x44","0xc4","0xde","0xe9","0xcb"],
            ["0x54","0x7b","0x94","0x32","0xa6","0xc2","0x23","0x3d","0xee","0x4c","0x95","0x0b","0x42","0xfa","0xc3","0x4e"],
            ["0x08","0x2e","0xa1","0x66","0x28","0xd9","0x24","0xb2","0x76","0x5b","0xa2","0x49","0x6d","0x8b","0xd1","0x25"],
            ["0x72","0xf8","0xf6","0x64","0x86","0x68","0x98","0x16","0xd4","0xa4","0x5c","0xcc","0x5d","0x65","0xb6","0x92"],
            ["0x6c","0x70","0x48","0x50","0xfd","0xed","0xb9","0xda","0x5e","0x15","0x46","0x57","0xa7","0x8d","0x9d","0x84"],
            ["0x90","0xd8","0xab","0x00","0x8c","0xbc","0xd3","0x0a","0xf7","0xe4","0x58","0x05","0xb8","0xb3","0x45","0x06"],
            ["0xd0","0x2c","0x1e","0x8f","0xca","0x3f","0x0f","0x02","0xc1","0xaf","0xbd","0x03","0x01","0x13","0x8a","0x6b"],
            ["0x3a","0x91","0x11","0x41","0x4f","0x67","0xdc","0xea","0x97","0xf2","0xcf","0xce","0xf0","0xb4","0xe6","0x73"],
            ["0x96","0xac","0x74","0x22","0xe7","0xad","0x35","0x85","0xe2","0xf9","0x37","0xe8","0x1c","0x75","0xdf","0x6e"],
            ["0x47","0xf1","0x1a","0x71","0x1d","0x29","0xc5","0x89","0x6f","0xb7","0x62","0x0e","0xaa","0x18","0xbe","0x1b"],
            ["0xfc","0x56","0x3e","0x4b","0xc6","0xd2","0x79","0x20","0x9a","0xdb","0xc0","0xfe","0x78","0xcd","0x5a","0xf4"],
            ["0x1f","0xdd","0xa8","0x33","0x88","0x07","0xc7","0x31","0xb1","0x12","0x10","0x59","0x27","0x80","0xec","0x5f"],
            ["0x60","0x51","0x7f","0xa9","0x19","0xb5","0x4a","0x0d","0x2d","0xe5","0x7a","0x9f","0x93","0xc9","0x9c","0xef"],
            ["0xa0","0xe0","0x3b","0x4d","0xae","0x2a","0xf5","0xb0","0xc8","0xeb","0xbb","0x3c","0x83","0x53","0x99","0x61"],
            ["0x17","0x2b","0x04","0x7e","0xba","0x77","0xd6","0x26","0xe1","0x69","0x14","0x63","0x55","0x21","0x0c","0x7d"]]
             

#THE ALPHABET AND HEX NUMBERS AND LETTERS 
ALPHABET = "ABCDEFFGHIJKLMNOPQRSTUVWXYZ"
HEX = "0123456789ABCDEF"

def hexToBin(hex:str) -> str:   
    string = str(hex).split('0x')
    binar = str(bin(int(string[1], 16)))[2:].zfill(8)
    return binar

def binToHex(binary:str)->str:
    hexa = hex(int(str(binary),2))
    if len(hexa) < 4:
        hexa = f"0x0{hexa[2]}"
    return hexa

def galoisMult(b1:str,b2:str) -> str:
    b1 , b2= list(b1), list(b2)
    b1_l = []
    b2_l = []
    sum_l = []
    for i,v in enumerate(b1):
        if v == '1':
            b1_l.append((len(b1))-i-1)
    for i,v in enumerate(b2):
        if v == '1':
            b2_l.append((len(b2))-i)
    for i in b1_l:
        for j in b2_l:
            sum_l.append(i+j)
    sum_l.sort()
    if sum_l:
        for i in range(sum_l[-1]):
            if sum_l.count(i) >= 2:
                t = sum_l.count(i) % 2
                while sum_l.count(i) > t:
                    sum_l.pop(sum_l.index(i))
        out = []
        for i in range(sum_l[-1]):
            if (i+1) in sum_l:
                out.append('1')
            else:
                out.append('0')
        out = out[::-1]
        while len(out) > 8:       
            s = out[:9]
            s = XOR(''.join(s),'100011011')
            for i in range(9):
                out[i] = s[i]
            while out[0] == '0':
                out.pop(0)
        out = binToHex(''.join(out).zfill(8))
        return out
    return binToHex('00000000')


def matrixMult(m1: list, m2: list)->list:
    fm = randomHexMatrixGen(len(m1),1,0,0)
    for row in range(len(m1)):
        for index in range(4):
            # print(f'({hexToBin(m1[row][index])} x {hexToBin(m2[index])}) + {hexToBin(fm[row][0])} => {hexToBin(galoisMult(hexToBin(m1[row][index]),hexToBin(m2[index])))} + {hexToBin(fm[row][0])} => {XOR(hexToBin(galoisMult(hexToBin(m1[row][index]),hexToBin(m2[index]))),hexToBin(fm[row][0]))} => {binToHex(XOR(hexToBin(galoisMult(hexToBin(m1[row][index]),hexToBin(m2[index]))),hexToBin(fm[row][0])))}\n-----------------------------------------------')
            fm[row][0] = binToHex(XOR(hexToBin(galoisMult(hexToBin(m1[row][index]),hexToBin(m2[index]))),hexToBin(fm[row][0])))
    return(fm)

def subBoxTrans(byte:str,sbox) -> str:
    indexes = (list(byte)[2].upper(), list(byte)[3].upper())
    out = sbox[HEX.find(indexes[0])][HEX.find(indexes[1])]
    return out

def randomHexMatrixGen(rows: int,columns: int,upperNum: int, lowerNum: int)->list:
    mat = []
    for row in range(rows):
        mat.append([])
        for column in range(columns):
            mat[row].append(str(hex(random.randint(upperNum,lowerNum))))
    return mat    
    # For Printing The keys:
     
    #  co = 0
    
    # for i in range(len(w)):
    #     co += 1
    #     print(w[i])
    #     if co == 4:
    #         co = 0
    #         print('---------------------------')

def randomNumMatrixGen(rows:int,columns:int,upperNum: int, lowerNum: int)->list:
    mat = []
    for row in range(rows):
        mat.append([])
        for column in range(columns):
            mat[row].append(str(random.randint(upperNum,lowerNum)))
    return(mat)

def XOR(byte1: str,byte2: str) -> str:
    b1 = list(byte1)
    b2 = list(byte2)
    b3 = []
    for i in range(len(b1)):
        if b1[i] == '1' and b2[i] == '1':
            b3.append('0')
        elif b1[i] == '0' and b2[i] == '0':
            b3.append('0')
        else:
            b3.append('1')
    return((''.join(b3)))

def splitText(text:str,c: int):
    temp = []
    if (len(text) // 16*c) >= 0:
        for i in range(0, (len(text) // 16) - (c-1), c):
            temp.append(text[(16*(i)):(16*(i+c))])
            if(len(text) % 16) > 0:
                temp.append(text[(len(text) // 16)*16:])
    return temp
        

def createMatrixFromText(text:str):
    out = []
    for j in range(len(text)):
        val = list(text[j])
        temp = randomNumMatrixGen(4,4,0,0)
        for i in range(len(val)):
            temp[(i//4)][(i%4)] = hex(ord(val[i]))
        out.append(temp)
    return out

def createMatrixFromHex(text:str):
    out = []
    for j in range(len(text)):
        val = []
        for i in range(0,len(text[j]),2):
            val.append(text[j][i:(i+2)])
        temp = randomNumMatrixGen(4,4,0,0)
        for i in range(len(val)):
            temp[(i//4)][(i%4)] = val[i]
        out.append(temp)
    return out

def addKeyRound(state:list, key:list):
    for i in range(len(state)):
        for j in range(len(state[0])):
            state[i][j] = binToHex(XOR(hexToBin(state[i][j]),hexToBin(key[i][j])))
    return state

def subBytes(state:list) -> list:
    for column in range(len(state)):
        for row in range(len(state[0])):
            state[column][row] = subBoxTrans(state[column][row],sbox)
    return state

def invSubBytes(state:list) -> list:
    for column in range(len(state)):
        for row in range(len(state[0])):
            state[column][row] = subBoxTrans(state[column][row],invSBox)
    return state

def shiftRows(state:list) -> list:
    for row in range(1,len(state)):
        tmp = ['','','','']
        i = 0
        j = 0
        while j < 4:
            tmp[(3*row + i)%4] = state[i][row]
            i += 1
            j += 1
        for i in range(4):
            state[i][row] = tmp[i]       
    return state

def invShiftRows(state: list) -> list:
    for row in range(1,len(state)):
        tmp = ['','','','']
        i = 0
        j = 0
        while j < 4:
            tmp[(row + i)%4] = state[i][row]
            i += 1
            j += 1
        for i in range(4):
            state[i][row] = tmp[i]
    return state

def mixColumns(state:list) -> list:
    for i in range(4):
        out = matrixMult(c,state[i])
        for j in range(4):
            state[i][j] = out[j][0]
    return state

def invMixColumns(state:list) -> list:
    for i in range(4):
        out = matrixMult(invC,state[i])
        for j in range(4):
            state[i][j] = out[j][0]
    return state

def printState(state:list):
    t = randomNumMatrixGen(4,4,0,0)
    for i in range(len(state)):
        for j in range(len(state[i])):
            t[i][j] = state[j][i]
    for i in range(len(state)):
        print('|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|')
        print(f"| {' '.join(t[i])} |")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def keyTransform(w:list,w_3:list,const:int)->list:
    out = ['','','','']
    tmp = ['','','','']
    i = 0
    j = 0
    while j < 4:
        tmp[(3 + i)%4] = w[i]
        i += 1
        j += 1
    for i in range(4):
        out[i] = subBoxTrans(tmp[i],sbox)
    out[0] = binToHex(XOR(hexToBin(out[0]),hexToBin(galoisMult(bin(int(const)).split('0b')[1].zfill(8),'00000001'))))
    for i in range(len(out)):
        out[i] = binToHex(XOR(hexToBin(out[i]),hexToBin(w_3[i])))
    return out

def keyGenerate(encryptKey: str) -> list:
    encryptKey = list(encryptKey)
    for i,v in enumerate(encryptKey):
        encryptKey[i] = hex(ord(v)) 
    w = randomNumMatrixGen(44,4,0,0)
    for i in range(4):
        w[i] = encryptKey[(0 + 4*i):(4*(i+1))]  
    w[4] = keyTransform(w[3],w[0],1)
    for i in range(5,44):
        for j in range(len(w[i-1])):
            if i % 4 != 0:
                w[i][j] = binToHex(XOR(hexToBin(w[i-1][j]),hexToBin(w[i-4][j])))
            else:
                w[i] = keyTransform(w[i-1],w[i-4],pow(2,(i-4)//4))
    
    # For Printing The keys:
     
    #  co = 0
    
    # for i in range(len(w)):
    #     co += 1
    #     print(w[i])
    #     if co == 4:
    #         co = 0
    #         print('---------------------------')
    
    return w

def addPadding(cipher):
    return "".join(list(cipher) + list(("0" + str(16 - len(cipher)/2))*(16 - len(cipher)/2)))

def readyHex(state):
    for table in range(len(state)):
        for column in range(len(state[table])):
            for row in range(len(state[table][column])):
                state[table][column][row] = "".join(["0","x"] + list(state[table][column][row]))
    return state

def stateToText(state):
    out = []
    for column in range(len(state)):
        for row in range(len(state[column])):
            out.append(state[column][row].split('x')[1])
    return out

def encrypt(text:str,encryptKey:str,rounds:int):
    out = ""
    w = keyGenerate(encryptKey)
    text = createMatrixFromText(splitText(text,1))
    for j in range(len(text)):
        state = addKeyRound(text[j],w[0:4])
        for i in range(rounds):
            state = subBytes(state)
            state = shiftRows(state)
            if i != (rounds-1):
                state = mixColumns(state)
            state = addKeyRound(state, w[(4*(i+1)):(4*(i+2))])
        printState(state)
        out = out + "".join(stateToText(state))
    print(out)

def decrypt(cipher:str, decryptKey:str, rounds: int):
    w = keyGenerate(decryptKey)
    cipher = splitText(cipher,2)
    for i in range(len(cipher)):
        if len(cipher[i]) < 32:
            cipher[i] = addPadding(cipher[i])
    cipher = createMatrixFromHex(cipher)
    cipher = readyHex(cipher)
    for j in range(len(cipher)):
        
        state = addKeyRound(cipher[j], w[40:44])
        for i in range(rounds):
            state = invShiftRows(state)
            state = invSubBytes(state)
            state = addKeyRound(state, w[(44 - ((i+2)* 4)): (44 - ((i+1)*4))])
            if i != (rounds-1):
                state = invMixColumns(state)
        printState(state)
        print(''.join(stateToText(state)))

encrypt("Two One Nine Two","Thats my Kung Fu",10)
decrypt("29c3505f571420f6402299b31a02d73a","Thats my Kung Fu", 10)
# m = createMatrixFromText(splitText("Two One Nine Two",1))[0]
# printState(m)
# m = shiftRows(m)
# printState(m)
# m = invShiftRows(m)
# printState(m)
# print(splitText("29c3505f571420f6402299b31a02d73af98548c55877cc3bc891e429a4094dbbe2e152c30302cda1b007f3ad8ac050cb",2))
# 
