import getpass
import random
import string
alphabet = letters_1 = string.ascii_lowercase + string.ascii_uppercase + "!@#$%^&*()_+-=" + "0123456789"
def encryption(p_txt, shift_n):
    cipher_txt = ""
    for char in p_txt:
        if char in alphabet:
           position = alphabet.index(char)
           new_pos = (position+shift_n)%len(alphabet)
           cipher_txt += alphabet[new_pos]
        else:
           cipher_txt += char  # Preserve characters not in the alphabet
    print(f"Here's is the text after encryption : {cipher_txt}")
    return cipher_txt
def decryption(cipher_txt, shift_n):
    plain_txt = ""
    for char in cipher_txt:
        if char in alphabet:
            position = alphabet.index(char)
            new_pos = (position - shift_n) % len(alphabet)
            plain_txt += alphabet[new_pos]
        else:
            plain_txt += char  # Preserve characters not in the alphabet
    print(f"Here's is the text after decryption : {plain_txt}")
    return plain_txt
print('____________________Messages are end to end    encrypted____________________')
end = False
end_game = False
while not end:
    shift = random.randint(1, len(alphabet))
    while not end_game:
        ende = input("Type 'encrypt' for encryption, type 'decrypt' for decryption : ")
        text = input("Type your message here : ")
        if ende == 'encrypt':
            encryption(p_txt=text, shift_n=shift)
        elif ende == 'decrypt':
            decryption(cipher_txt=text, shift_n=shift)
            con = input("Do you want to continue this chat or want to create new chat :")
            if con == 'no':
                end_game = True
    play_againg = input("Are you sure you want to create new chat : ")
    if play_againg == 'no':
        end = True
        print('Program ends ...')