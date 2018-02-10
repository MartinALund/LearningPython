alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_mode():
    while 1:
        text = get_text()
        mode = set_mode()
        if mode == "encrypt":
            key = get_key()
            print(encrypt(text, key))
        elif mode == "decrypt":
            key = get_key()
            print(decrypt(text, key))
        elif mode == "bruteforce":
            bruteforce(text)
        else:
            print("You need to select a method")


def get_text():
    text = input("Enter cipher text here: ")
    return text.upper()


def get_key():
    key = int(input("Enter key here: "))
    return key


def set_mode():
    mode = input("Enter mode: encrypt, decrypt, bruteforce: ")
    return mode.lower()


def encrypt(text, key):
    return cipher(text, key)


def decrypt(text, key):
    return cipher(text, -key)


def bruteforce(text):
    for i in range(len(alfabet)):
        print("{}:{}".format(i, decrypt(text,i)))


def cipher(text, key):
    result = ""
    for chars in text:
        if chars in alfabet:
            pos = alfabet.index(chars)
            pos = pos + key
            pos = (pos + len(alfabet)) % len(alfabet)
            result += alfabet[pos]
        else:
            result = result + chars
    return result


get_mode()