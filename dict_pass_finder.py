from crypto import crypt
def test_pass(crypt_pass):
    salt = crypt_pass[:2]
    dict_file = open("dictionary.txt",'r')
    for word in dict_file.readlines():
        crypt_word = crypt(word.strip('\n'),salt)

        if crypt_word == crypt_pass:
            print(f'[+] Found password : {word}\n')
            return
        else:
            print('[-] Password not found.\n')
            return
if __name__ == '__main__':
    pass_file = open("passwords.txt")
    for line in pass_file.readlines():
        if ':' in line:
            user = line.split(':')[0]
            _crypt_pass = line.split(':')[1].strip()
            print(f'[*] Cracking password for : {user}')
            test_pass(crypt_pass)
