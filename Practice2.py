import string
lowercase_alphabet = list(string.ascii_lowercase)
# print(lowercase_alphabet)
received_text ="xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
def decipher(text):
    decoded_text= ''
    for i in range(len(text)):
        if text[i] in lowercase_alphabet:
            txt = text[i]
            # print(txt)
            idx = lowercase_alphabet.index(txt)
            # print(idx)
            decoded_text += lowercase_alphabet[(idx + 10) % 26]
        else:
            decoded_text += text[i]
    return decoded_text

# print(received_text)
# print(decipher(received_text))




lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)
# print(lowercase_alphabet)
transmitting_text ="hey! cool. Yes, i decoded you cipher. send me more of we will have fun"
def decipher(text):
    encoded_text= ''
    for i in range(len(text)):
        if text[i] in lowercase_alphabet:
            txt = text[i]
            # print(txt)
            idx = lowercase_alphabet.index(txt)
            # print(idx)
            encoded_text += lowercase_alphabet[(idx - 10) % 26]
        elif text[i] in uppercase_alphabet:
            txt = text[i]
            # print(txt)
            idx = uppercase_alphabet.index(txt)
            # print(idx)
            encoded_text += uppercase_alphabet[(idx - 10) % 26]
        else:
            encoded_text += text[i]
    return encoded_text

# print(transmitting_text)
# print(decipher(transmitting_text))
lowercase_alphabet =  string.ascii_lowercase
print(lowercase_alphabet)


ciphertext = "ymlok cp fbb ejv"
key_message = "dog"

def key_message_generator(ciphertext, key_message):
    expanded_key = ""
    k = 0  # key index
    for i in range(len(ciphertext)):
        if ciphertext[i] in lowercase_alphabet:
            expanded_key += key_message[k % len(key_message)]
            k += 1
        else:
            expanded_key += ciphertext[i]
    return expanded_key


def polyalphabetic_decode(ciphertext, key_message):
    decoded_text = ''
    for i in range(len(ciphertext)):
        if ciphertext[i] in lowercase_alphabet:
            value = lowercase_alphabet.index(ciphertext[i]) - lowercase_alphabet.index(key_message[i])
            if value < 0:
                value += 26
            decoded_text += lowercase_alphabet[value]
        else:
            decoded_text += ciphertext[i]
    return decoded_text

print(key_message_generator("barry is the spy","dog"))
# print(polyalphabetic_decode(ciphertext,key_message_generator(ciphertext, key_message)))