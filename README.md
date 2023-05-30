# AES document encryption

This is a commandline tool for password based aes encryption of text documents. 

## PW generation
You can encrypt the file with your ethereum private key by signing the filename to create the password. You could also just have a randomly generated password, or for lower security, a memorable word or phrase. 


## Run as script 

You can runn the following command to decrypt or encrypt a file: 

```
python3 -m PwAES PATH_TO_FILE
```

## Quickstart 

```shell
python3 aes.py "path_to_file"
```