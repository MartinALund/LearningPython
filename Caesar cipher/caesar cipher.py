alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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
        elif mode == "frekvens":
            get_frequency(text)
        else:
            print("You need to select a method")


def get_text():
    text = input("Enter cipher text here: ")
    return text.upper()


def get_key():
    key = int(input("Enter key here: "))
    return key


def set_mode():
    mode = input("Enter mode: encrypt, decrypt, bruteforce, frekvens: ")
    return mode.lower()


def encrypt(text, key):
    return cipher(text, key)


def decrypt(text, key):
    return cipher(text, -key)


def bruteforce(text):
    for key in range(len(alphabet)):
        print("{}:{}".format(key, decrypt(text,key)))


def get_frequency(text):
    list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count = 0
    for chars in text:
        count += 1
        if chars in alphabet:
            pos = alphabet.index(chars)
            list[pos] += 1


    for chars in alphabet:
        print("{}: {}".format(chars, list[alphabet.index(chars)]))

    print()
    char_most_appearance = max(list)
    alphabet_char = alphabet[list.index(max(list))]
    
    #round parameter 2 = antal decimal.
    percent_of_time_shown = round(char_most_appearance * 100 / count,2)
    print("Total chars: {}".format(count))
    print("{} blev vist {} gange, dette svarer til {}%".format(alphabet_char,
                                                               char_most_appearance,
                                                               percent_of_time_shown))
    print()


def cipher(text, key):
    result = ""
    for chars in text:
        if chars in alphabet:
            pos = alphabet.index(chars)
            pos = pos + key
            pos = (pos + len(alphabet)) % len(alphabet)
            result += alphabet[pos]
        else:
            result = result + chars
    return result


get_mode()