#cracking password of a zip file using a pre defined list.
import zipfile
from tqdm import tqdm
wordlist = "rockyou.txt"#Pre-defined list of passwords
zip_file = input("Enter the zip file :")#User defined program.
obj = zipfile.ZipFile(zip_file)
n_words = len(list(open(wordlist,"rb")))
print("Total words to test:",n_words)

with open(wordlist,"rb")as wordlist:
    for word in tqdm(wordlist,total = n_words,unit = "word"):
        try:
            obj.extractall(pwd = word.strip())
        except:
            continue
        else:
            print("[+] Password found:",word.decode().strip())
            exit(0)
    print("[!] Password not found, try another wordlist.")
    
