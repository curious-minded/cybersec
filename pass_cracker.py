import hashlib

def read_text(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def crack_password(target_hash, word_list):
    for word in word_list:
        hashed_word = hash_password(word)
        if hashed_word == target_hash:
            return word
    return None

if __name__ == "__main__":
    with open("dictionary.txt", 'w') as file:
        string = "apple\norange\negg\nlemon\ngrapes\nsecret\nstrawberry\npassword\nhashcat\n"
        file.write(string)

    target_hash = input("Enter the hash value (SHA-256, 64 hex characters): ")

    if len(target_hash) != 64 or not all(c in '0123456789abcdefABCDEF' for c in target_hash):
        print("Error: Invalid SHA-256 hash. Please enter a valid 64-character hexadecimal hash.")
    else:
        dictionary_file = "dictionary.txt"
        word_list = read_text(dictionary_file)

        cracked_password = crack_password(target_hash, word_list)

        if cracked_password:
            print(f"Password cracked! The password is: {cracked_password}")
        else:
            print("Password not found in the dictionary.")
