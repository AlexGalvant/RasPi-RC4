import random, base64
from hashlib import sha1
from random import randint



"Implementation of RC4 Algorithm"
def crypt(data, key):
    x = 0
    box = range(256)
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        box[i], box[x] = box[x], box[i]
    x = y = 0
    out = []
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))
    
    return ''.join(out)


" Encryption function"
def encrypt(data, key, encode=base64.b64encode, salt_length=16):
    salt = ''
    for n in range(salt_length):
        salt += chr(random.randrange(256))
    data = salt + crypt(data, sha1(key + salt).digest())
    if encode:
        data = encode(data)
    return data


"Decryption function"
def decrypt(data, key, decode=base64.b64decode, salt_length=16):
    if decode:
        data = decode(data)
    salt = data[:salt_length]
    return crypt(data[salt_length:], sha1(key + salt).digest())



"main code"
if __name__ == '__main__':
    secretMessage='Alex is here'
    "Publicly Shared"
    p=353
    "Publicly Shared"
    g=3

    "Own Secret"
    "a = randint(2, p-1)"
    a=97
    A = (g ** a) % p
    
    "to be shared to otherside"
    print A

    "this will be shared to you by other side, 233 is example"
    b=233
    B = (g ** b) % p

    "calculation of key takes place without exchange of 'Own Secret'"
    key=(B ** a) % p

    print key
    "Got key from Diffie Hellman CODE"
    myKey=str(key)
    edata = encrypt(secretMessage, myKey)
    print edata
    
    " should get same on other side as well"
    myKey=str(key)
    ddata=decrypt(edata,myKey)
    print ddata