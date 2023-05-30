# AES document encryption

This is a commandline tool for password based aes encryption of text documents. 

## PW generation
You can encrypt the file with your ethereum private key by signing the filename to create the password. You could also just have a randomly generated password, or for lower security, a memorable word or phrase. 


## Scripts 
aes.py is reccomeneded as it has hidden pwinput. It uses EAX. The other AES_cbc.py uses CBC but still needs a little work.

## Quickstart 

```shell
python3 aes.py "path_to_file"
```