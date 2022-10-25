from cryptography.fernet import Fernet
import os

def cargar_key():
    return open("key.key", "rb").read()

def decrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, "rb") as file:
            file_data = file.read()
        print(item)
        print(file_data)
        encrypted_data = f.decrypt(file_data)
        with open(item, "wb") as file:
            file.write(encrypted_data)

if __name__ == "__main__":

    user = os.environ.get('USERNAME')
    print("Username is: " + user)

    path_to_decrypt = "C:\\hello"
    items = os.walk(path_to_decrypt)

    # full_path = [path_to_encrypt+"\\"+item for item in items]
    full_path = [os.path.join(root, name)
                 for root, dirs, files in os.walk(path_to_decrypt)
                 for name in files
                 if name != "readme.txt"]

    print(full_path)

    key = cargar_key()

    decrypt(full_path, key)