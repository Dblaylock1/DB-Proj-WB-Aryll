import sys
import base64
import time
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

# Do not change this salt
mysalt = b'J>\xbav\xc5\xa6\xa01Sg\xa7\xb3,\xc3\xa3\x02'

#global lists
mainmenu = ['main menu', 'explain commands', 'explain', 'command list', 'cd list', 'commands', 'go back', 'commandz']
helpme = ['helpme', 'help', 'help me', 'i need help', '--help', '-help', 'help me', 'wfes help', 'please help']
dande = ['dande', 'decryptthenencrypt', 'decrypt then encrypt', 'd and encrypt', 'dandencrypt', 'decenc', 'dec&enc', 'dec+enc', 'decrypt&encrypt', 'decrypt+encrypt', 'dec2enc', 'd2e', 'de2e', 'decrypt2encrypt', 'decodeencode', 'processfile', 'doubleprocess', 'doublecrypto', 'recrypto', 'redecryptencrypt']
generate = ['g', 'generate', 'hash', 'create hash', 'generate hash']
write = ['w', 'write', 'write file']
read = ['r', 'read', 'read file']
encrypt = ['e', 'encrypt', 'encrypt a file', 'file encrypt']
decrypt = ['d', 'decrypt', 'decrypt file', 'decrypt a file']
delete = ['del', 'delete', 'delete a file', 'delete file']

def generate_key(password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=mysalt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))
print('''
What would you like to do?
(D)ecrypt a file
(Del)ete a file
(E)ncrypt a file
(G)enerate a hash
(R)ead a file
(W)rite a new text file
(H)elp me


⠀⠀⠀⠀⠀⠀ ⠀⠀⣀⣤⣴⠶⠾⠿⠛⠛⠻⠿⠶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀ ⠀⢠⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀ ⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀⠀
⠀⠀⠀ ⠀⠀⣿⠇⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡈⣿⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⣿⡆⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⣿⠀⠀⠀⠀⠀
⠀⠀ ⠀⠀⠀⠸⣧⢸⡆⢀⣀⣀⣤⡀⠀⠀⢀⣤⣀⣀⡀⠀⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣿⠁⣿⣿⣿⣿⡟⠀⠀⠸⣿⣿⣿⣿⠆⣿⠟⠀⠀⠀⣀⠀⠀
⠀⢰⡟⢿⣆⠀⠀⣿⠀⠙⢿⣿⠟⠀⣠⣄⠀⠹⣿⣿⠟⠀⢹⠀⠀⣠⡿⢻⣇⠀
⣠⡾⠃⠈⠻⢷⣦⣽⣄⡀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⢀⣠⣿⣤⡶⠟⠁⠘⢿⣆
⠻⠷⠶⠶⣶⣤⣈⠙⠻⣿⣷⣦⠀⠸⠋⠙⠟⠀⣠⣾⣿⠟⠋⣁⣠⣴⠶⠶⠾⠟
⠀⠀⠀⠀⠀⠉⠛⠿⣶⣼⠿⣿⣲⡤⡤⡤⢤⢰⣿⡏⣿⣶⠿⠛⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⡄⠻⣹⡟⡟⡟⣻⣻⠽⠁⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⣶⠾⠶⠾⠟⠋⣁⣼⣷⡀⠀⠉⠉⠉⠉⠀⢀⣼⣧⣀⠉⠛⠷⠶⠿⣶⡄⠀
⠀⠀⠙⣷⡄⢀⣴⠿⠛⠁⠀⠙⠳⠶⠤⠴⠶⠞⠋⠀⠈⠙⠻⣶⡄⠀⣾⠟⠁⠀
⠀⠀⠀⢸⣷⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣶⡿⠀⠀⠀

''')  
    
def main():
    x1 = input('Write Command Here: ')
    if x1.lower() in generate:
        password = input("Please tell me the password you want to base the hash off of: ")
        if password in mainmenu:
            return main()
        elif password not in mainmenu:
            key = generate_key(password)
            print('Please copy generated hash:', key.decode())
            return main()
    elif x1.lower() in encrypt:
        filename = input("\nEnter the name of the file to encrypt: ")
        if filename in mainmenu:
            return main()
        elif filename not in mainmenu:
            if not os.path.isfile(filename):
                print("File is not found.")
                return main()
            key_input = input("\nEnter the hash to encrypt this file with: ")
            if key_input in mainmenu:
                return main()
            elif key_input not in mainmenu:
                try:
                    cipher = Fernet(key_input)
                    with open(filename, 'rb') as f:
                        data = f.read()
                    encrypted = cipher.encrypt(data)
                    with open(filename, 'wb') as f:
                        f.write(encrypted)
                    print("File encrypted successfully. ")
                    return main()
                except Exception as e:
                    print("Operation has failed: ", e)
                return main()
    elif x1.lower() in decrypt:
        key_input = input("\nEnter the hash used to encrypt the file: ")
        if key_input in mainmenu:
            return main()
        elif key_input not in mainmenu:
            filename = input('Please tell me the name of the file. (With extention)')
            if not os.path.isfile(filename):
                print("File not found.")
                return main()
            try:
                cipher = Fernet(key_input)
                with open(filename, 'rb') as f:
                    encrypted_data = f.read()
                decrypted_data = cipher.decrypt(encrypted_data)
                with open(filename, 'wb') as f:
                    f.write(decrypted_data)
                print("File decrypted successfully.")
                print(decrypted_data.decode('utf-8', errors='ignore'))
                return main()
            except Exception as e:
                print("Decryption failed: ", e)
            return main()
    elif x1.lower() in delete:
        filename = input("\nEnter the name of the file to delete: ")
        if filename in mainmenu:
            return main()
        if filename not in mainmenu:
            if os.path.isfile(filename):
                os.remove(filename)
                print("File deleted.")
                return main()
            elif not os.path.isfile(filename):
                print("File not found.")
                return main()
            else:
                print('Error message, returning to menu')
                return main()
    elif x1.lower() in write:
        content = input("\nEnter content for the new file: ")
        if content in mainmenu:
            return main()
        elif content not in mainmenu:
            filename = input("\nEnter the filename (no extension): ") + ".txt"
            with open(filename, 'w') as f:
                f.write(content)
            print(f"File '{filename}' created.")
            return main()
    elif x1.lower() in read:
        filename = input("\nEnter the name of the file to read: ")
        if filename in mainmenu:
            return main()
        elif filename not in mainmenu:
            if not os.path.isfile(filename):
                print("File not found.")
                return main()
            with open(filename, 'rb') as f:
                print(f.read())
                return main()
    elif x1.lower() in dande:
        filename = input("\nEnter the name of the file to read. ")
        if filename in mainmenu:
            return main()
        elif filename not in mainmenu:
            key_input = input("Tell me the hash that this file is currently encrypted with: ")
            if not os.path.isfile(filename):
                print("File not found.")
                return main()
            try:
                cipher = Fernet(key_input)
                with open(filename, 'rb') as f:
                    encrypted_data = f.read()
                decrypted_data = cipher.decrypt(encrypted_data)
                print(decrypted_data.decode('utf-8', errors='ignore'))
                print("You currently have 10 seconds before the file is re-encrypted. ")
                time.sleep(10)
                re_encrypted = cipher.encrypt(decrypted_data)
                with open(filename, 'wb') as f:
                    f.write(re_encrypted)
                print("File re-encrypted successfully. ")
                return main()
            except Exception as e:
                print("Operation Failed. ", e)
            return main()
    elif x1.lower() in helpme:
        print('''
        
What would you like to do?
(D)ecrypt a file
(Del)ete a file
(E)ncrypt a file
(G)enerate a hash
(R)ead a file
(W)rite a new text file
(H)elp me


⠀⠀⠀⠀⠀⠀ ⠀⠀⣀⣤⣴⠶⠾⠿⠛⠛⠻⠿⠶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀ ⠀⢠⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀ ⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀⠀
⠀⠀⠀ ⠀⠀⣿⠇⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡈⣿⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⣿⡆⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⣿⠀⠀⠀⠀⠀
⠀⠀ ⠀⠀⠀⠸⣧⢸⡆⢀⣀⣀⣤⡀⠀⠀⢀⣤⣀⣀⡀⠀⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣿⠁⣿⣿⣿⣿⡟⠀⠀⠸⣿⣿⣿⣿⠆⣿⠟⠀⠀⠀⣀⠀⠀
⠀⢰⡟⢿⣆⠀⠀⣿⠀⠙⢿⣿⠟⠀⣠⣄⠀⠹⣿⣿⠟⠀⢹⠀⠀⣠⡿⢻⣇⠀
⣠⡾⠃⠈⠻⢷⣦⣽⣄⡀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⢀⣠⣿⣤⡶⠟⠁⠘⢿⣆
⠻⠷⠶⠶⣶⣤⣈⠙⠻⣿⣷⣦⠀⠸⠋⠙⠟⠀⣠⣾⣿⠟⠋⣁⣠⣴⠶⠶⠾⠟
⠀⠀⠀⠀⠀⠉⠛⠿⣶⣼⠿⣿⣲⡤⡤⡤⢤⢰⣿⡏⣿⣶⠿⠛⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⡄⠻⣹⡟⡟⡟⣻⣻⠽⠁⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⣶⠾⠶⠾⠟⠋⣁⣼⣷⡀⠀⠉⠉⠉⠉⠀⢀⣼⣧⣀⠉⠛⠷⠶⠿⣶⡄⠀
⠀⠀⠙⣷⡄⢀⣴⠿⠛⠁⠀⠙⠳⠶⠤⠴⠶⠞⠋⠀⠈⠙⠻⣶⡄⠀⣾⠟⠁⠀
⠀⠀⠀⢸⣷⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣶⡿⠀⠀⠀

This is a fairly simplistic fernet encryption system for python specifically for .txt files, you will not be able to encrypt files with this
nor use it as ransomware, so dont even try if you have your grubby hands on it somehow. Command lsit is above, write a file does not mean edit a file, it will create an entirely
new file, or it will add its contents on top of the preexisting contents. It is not like nano for linux or something.

any other questions? Shoot me an email at kyatpentesting@protonmail.com and ill see if I can get back to you.
        
thanks again for using my file encryption system, and check out my other projects!
        
        ''')
        return main()
    else:
        print("\nInvalid command. Use one of the listed commands.")
        return main()

if __name__ == "__main__":
    print('''\nWelcome to W.R.E.D - the encryption file management system.''')
    main()
