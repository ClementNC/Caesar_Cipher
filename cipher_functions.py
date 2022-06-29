num_alphabet = 26
upper_alphabet = [chr(i + ord('A')) for i in range(num_alphabet)]
lower_alphabet = [chr(i + ord('a')) for i in range(num_alphabet)]
def encrypt(word, shift):
    word_list = list(word)
    encrypted_word = ""
    for letter in word_list:
        if letter.isalpha():
            if letter.isupper():
                index = (ord(letter) - ord('A') + shift) % num_alphabet
                encrypted_word += upper_alphabet[index]
            else:
                index = (ord(letter) - ord('a') + shift) % num_alphabet
                encrypted_word += lower_alphabet[index]
        else:
            encrypted_word += letter
    print(f"The encryption result is: {encrypted_word}")
def decrypt(cipher, shift):
    cipher_list = list(cipher)
    decrypted_word = ""
    for letter in cipher:
        if letter.isalpha():
            if letter.isupper():
                index = (ord(letter) - ord('A') - shift) % num_alphabet
                decrypted_word += upper_alphabet[index]
            else:
                index = (ord(letter) - ord('a') - shift) % num_alphabet
                decrypted_word += lower_alphabet[index]
        else:
            decrypted_word += letter
    print(f"The decrypted word is: {decrypted_word}")
