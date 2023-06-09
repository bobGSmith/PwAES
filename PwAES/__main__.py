'''PASSWORD BASED AES ENCRYPTION

This allows password based AES encrypton of strings and text files. It can be imported as a module or ran as a script

To run as script, pass the following args: 
    * path (str) : file path to the text file to be encrypted or decrypted

This module contains the following functions: 
    * get_extension - returns the file extension of a path
    * anykey_exit - promps user to hit any key then exits the script
    * help_disply - displays doc string if incorrect number of args is passed or -h is passed
    * gen_pw_privatekey - generates a AES private key from a password string
    * write_cyphertext_file - takes path to text file and saves a encrypted version in the same directory
    * decrypt_cyphertext_file - decrypts a cyphertext file generated by write_cyphertext_file 
'''

from PwAES import *
import sys

help_display(sys.argv,1,__doc__)
path = sys.argv[1]
encrypt = input('Encrypt or Decrypt (e/d) > ') 
private_key = gen_pw_privatekey()

if encrypt.lower() in ['e','encrypt']:
    write_cyphertext_file(path,private_key)
    anykey_exit()
        
elif encrypt.lower() in ['d','decrypt']:
    display_or_save = input('Dispaly or save output (d/s) > ')
    decrypted = decrypt_cyphertext_file(path,private_key)
    if display_or_save in ['d','display']:
        print(decrypted)
        anykey_exit()
    elif display_or_save in ['s','save']:
        with open(path.replace('encrypted.txt','decrypted.txt'),'w') as outfile:
            outfile.write(decrypted)   
        anykey_exit()

    
input('selection not recognised, hit any key to exit')
exit()