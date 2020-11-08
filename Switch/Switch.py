import pyAesCrypt
import time
import urllib3
from bs4 import BeautifulSoup
from secure_delete import secure_delete

# This is the payload - It will encrypt whatever file we specified.
def FirePayload(filePath, encryptPass):
    print("ACTIVATED PAYLOAD!!!!!")
    bufferSize = 64 * 1024 # encryption/decryption buffer size - 64K
    pyAesCrypt.encryptFile(filePath, (filePath+'.aes'), encryptPass, bufferSize) # encrypt
    secure_delete.secure_random_seed_init()
    secure_delete.secure_delete(filePath) # Erases the plaintext file
    print("SWITCH ACTIVATED - LOCKDOWN MODE ENTERED")
    exit()

def DecryptPayload(filePath, directory, password):
    bufferSize = 64 * 1024  # encryption/decryption buffer size - 64K
    print(filePath)
    filename = filePath[:-4]
    print(filename)
    try:
        pyAesCrypt.decryptFile(filePath, filename, password, bufferSize)
        secure_delete.secure_random_seed_init()
        secure_delete.secure_delete(filePath)  # Erases the plaintext file
    except:
        print("Cant encrypt")
        exit()


# Checks for the keyphrase on Pastebin
def CheckKey(url, filePath, password, phrase, directory, decrypt):
    if decrypt == "X":
        print("Starting decrypting")
        DecryptPayload(filePath,directory,password)
    else:
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        soup = BeautifulSoup(r.data, "html.parser")
        findings = soup.find_all('div', {'class': 'de1'})
        for switch in findings:
            switch_string = switch.text
            print(switch_string)
            if switch_string == phrase:
                FirePayload(filePath, password)
            else:
                time.sleep(10)
                CheckKey(url, filePath, password)
