from cryptography.fernet import Fernet

def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
        return key


master_pwd = input("what is the master password?: ").lower()
key = load_key() + master_pwd.encode()
fer = Fernet(key)

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()'''

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passd = data.split("|")
            print("user:" + user, "Password:" + fer.decrypt(passd.encode())


while True:
    mode = input("would you like to add a new pwd or view existing (add or view or q to quit)?: ").lower()
    if mode == "q":
        break

    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Enter the required response")
        continue
