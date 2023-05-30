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