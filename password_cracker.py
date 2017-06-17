#!/usr/bin/env python
# This program will take a /etc/shadow file's passwords and run them
# against the words in dictonary.txt
import crypt


def testPass(cryptpass):
    dictfile = open('dictionary.txt','r')
    # Detect if the password is using sha512 or older style unix
    if '$' in cryptpass:
		salt = "$%s$%s$" % (cryptpass.split('$')[1],cryptpass.split('$')[2])
    else:
        salt = cryptpass[0:2]
    #reads every word in the dictionary file, encrypts it with the salt
    #from above and then compares it to the hash from the password file
    for word in dictfile.readlines():
        word = word.strip()
        cryptword = crypt.crypt(word,salt)
        if cryptword == cryptpass:
            print "[+] Found Password: %s\n" % word
            return
    print "[-] Password Not Found.\n"
    return


def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip()
            print "[+] Cracking Password For: " + user
            testPass(cryptPass)
if __name__ == "__main__":
    main()
