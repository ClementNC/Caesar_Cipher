from cipher_functions import encrypt, decrypt
from art import logo

# This executes either the encrypt or decrypt function depending on the user's action.
def caesar(action, text, shift):
    if action.lower() == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)

# This is the main function
def main():
    print(logo)
    restart_cipher = 'Y'
    while restart_cipher.upper() == 'Y':
        user_action = " "
        while user_action.lower() != "encode" and user_action.lower() != "decode":
            user_action = input("Type 'encode' to encrypt and 'decode' to decrypt: ")
            if user_action.lower() != "encode" and user_action.lower() != "decode":
                print("Invalid input. Please input 'encode' or 'decode'")
        user_text = input("Type your message: ")
        shift = 0
        while shift <= 0:
            shift = int(input("Type the shift amount: "))
            if shift <= 0:
                print("Invalid input. Shift amount must be greater than 0")
        caesar(user_action, user_text, shift)
        restart_cipher = ' '
        while restart_cipher.upper() != 'Y' and restart_cipher.upper() != 'N':
            restart_cipher = input("Do you want to cipher another message? Input Y/N:\n")
            if restart_cipher.upper() != 'Y' and restart_cipher.upper() != 'N':
                print("Invalid input. Please input Y or N")
        print()
    print("Thank you for using the Caesar Cipher program!", end='\n\n')

if __name__ == "__main__":
    main()
