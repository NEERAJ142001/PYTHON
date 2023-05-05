from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# shift = shift % 26

encrypt_answer = ""


# this function encrypt the code
def encrypt(test1, shift1):
    global encrypt_answer
    encrypt_answer = ""

    for i in test1:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift1

            if new_position > 25:
                new_position = new_position % 26

            new_letter = alphabet[new_position]
            encrypt_answer = encrypt_answer + new_letter
        #     else indicates characters other than letters
        else:
            encrypt_answer = encrypt_answer + i
    print(f"The decode text is '{encrypt_answer}'")


decrypt_answer = ""


# this function decrypt the code
def decrypt(text2, shift2):
    global decrypt_answer
    decrypt_answer = ""
    for i in text2:

        if i in alphabet:
            position = alphabet.index(i)
            new_position = position - shift2
            if new_position < 0:
                new_position = new_position % 26

            new_letter = alphabet[new_position]
            decrypt_answer = decrypt_answer + new_letter
        else:
            decrypt_answer = decrypt_answer + i
    print(f"The decode text is '{decrypt_answer}'")


flag = True

while flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    if direction == "encode" or direction == 'e':
        encrypt(text, shift)
        choice = input(f"u wanna do also decode the same code '{encrypt_answer}': yes/no \n")

        if choice == "yes" or choice == 'y':
            new_shift = int(input("Type the shift number:\n"))
            decrypt(encrypt_answer, shift)
            continue

        elif choice == "no" or choice == 'n':
            continue

    elif direction == "decode" or direction == 'd':
        decrypt(text, shift)
        choice = input(f"u wanna do also encode the same code '{decrypt_answer}: yes/no \n")

        if choice == "yes":
            new_shift = int(input("Type the shift number also to encode it:\n"))
            encrypt(decrypt_answer, shift)
            continue

        elif choice == "no" or choice == "n":
            continue

    else:
        flag = False
