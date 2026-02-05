import string
lowercase_alphabet =  string.ascii_lowercase

ciphertext = "aiwfeyq ayc adcsvke!" #received encrypted code
key_message = "cat" #key

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

#decryption
def polyalphabetic_decode(ciphertext, key_message):
    decoded_text = ''
    for i in range(len(ciphertext)):
        if ciphertext[i] in lowercase_alphabet:
            idx = (lowercase_alphabet.index(ciphertext[i])+lowercase_alphabet.index(key_message[i]))%26
            decoded_text += lowercase_alphabet[idx]
        else:
            decoded_text += ciphertext[i]
    return decoded_text


print(polyalphabetic_decode(ciphertext,key_message_generator(ciphertext, key_message)))



#encryption code
ciphertext = "yes, i am able to decode it."
key_message = "friends"

def polyalphabetic_decode(ciphertext, key_message):
    decoded_text = ''
    for i in range(len(ciphertext)):
        if ciphertext[i] in lowercase_alphabet:
            idx = (lowercase_alphabet.index(ciphertext[i])-lowercase_alphabet.index(key_message[i]))%26
            decoded_text += lowercase_alphabet[idx]
        else:
            decoded_text += ciphertext[i]
    return decoded_text

print(polyalphabetic_decode(ciphertext,key_message_generator(ciphertext, key_message)))