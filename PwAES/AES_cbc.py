''' AES 256 encryption/decryption 

script args 
===========
* encrypt_or_decrypt {string} : string "d" or "e" 
* password {string} : password for encryption, use > 20 random characters
* path {string} : path to text file to be encrypted or decrypted 
* outpath (optional) {string} : path to save encrypted or decrypted file

'''
import sys 
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
 
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def encrypt(raw, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode("utf8")))

def decrypt(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))

if __name__ == '__main__':
  
    if len(sys.argv) not in [4,5] or sys.argv[1] in ["-h","-H","--help"]:
        print(__doc__)
        input("hit any key to exit")
        sys.exit()
        
      
    encrypt_or_decrypt = sys.argv[1]
    password = sys.argv[2]
    


    if (encrypt_or_decrypt == "e"): 
        with open(sys.argv[3], "r") as infile: 
            text = ""
            for l in infile.readlines():
                text += l
        output = encrypt(text, password)
        #print(output)
    elif (encrypt_or_decrypt == "d"):
        with open(sys.argv[3], "rb") as infile: 
            text = b""
            for l in infile.readlines():
                text += l
        output = decrypt(text, password)
        #print(bytes.decode(output))
    else:
        print("Arg 1 should be 'e' or 'd'")
        print(__doc__)
        input("hit any key to exit")
        sys.exit()
        
    if len(sys.argv) == 5:
        outpath = sys.argv[4]
        with open(outpath, "wb") as outfile: 
            outfile.write(output)
    if input ('Display ouput in terminal (y/n)').lower() in ["y","yes"]
        print(output)
        input('hit any key to exit')
