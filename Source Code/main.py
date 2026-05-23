# =====================================================
#   Caesar Cipher Encryption-Decryption Tool (UPGRADED)
# =====================================================

from datetime import datetime
import os

# =====================================================
# PATH SETUP AND HISTORY FILES
# =====================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HISTORY_DIR = os.path.join(BASE_DIR, "History")

# Ensure History folder exists
os.makedirs(HISTORY_DIR, exist_ok=True)

encrypt_file = os.path.join(HISTORY_DIR, "encrypt_history.txt")
decrypt_file = os.path.join(HISTORY_DIR, "decrypt_history.txt")


# =====================================================
# HEADER
# =====================================================
print("===========================================================================")
print("      Welcome to the Caesar Cipher Encryption-Decryption Tool!             ")
print("===========================================================================")


# =====================================================
# TEXT VALIDATION FUNCTION
# =====================================================
def get_text():
    while True:
        text = input("Enter the text you want to encrypt or decrypt: ")

        if any(char.isdigit() for char in text):
            print("Numbers are not allowed. Please enter only text.")

        elif text.strip() == "":
            print("Text cannot be empty.")

        else:
            return text


# =====================================================
# SHIFT VALIDATION FUNCTION
# =====================================================
def get_shift():
    while True:
        try:
            shift = int(input("Enter shift key (1-26): "))

            if shift < 1 or shift > 26:
                print("Invalid shift key! Please enter a number between 1 and 26.")
            else:
                shift = shift % 26
                if shift == 0:
                    shift = 26
                return shift

        except ValueError:
            print("Please enter a valid number.")


# =====================================================
# MAIN MENU LOOP
# =====================================================
while True:

    print("================ MENU ================")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. View History")
    print("4. Clear History")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    # =====================================================
    # ENCRYPTION
    # =====================================================
    if choice == 1:

        text = get_text()
        shift = get_shift()

        encrypted_text = ""

        for char in text:
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            elif char.islower():
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted_text += char

        print("\nEncrypted message is:", encrypted_text)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(encrypt_file, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] Encrypt: {text} -> {encrypted_text}\n")


    # =====================================================
    # DECRYPTION
    # =====================================================
    elif choice == 2:

        text = get_text()
        shift = get_shift()

        decrypted_text = ""

        for char in text:
            if char.isupper():
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
            elif char.islower():
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                decrypted_text += char

        print("\nDecrypted message is:", decrypted_text)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(decrypt_file, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] Decrypt: {text} -> {decrypted_text}\n")


    # =====================================================
    # VIEW HISTORY
    # =====================================================
    elif choice == 3:

        print("\n================ HISTORY ================\n")

        print("----- Encrypt History -----")
        try:
            with open(encrypt_file, "r", encoding="utf-8") as file:
                data = file.read()
                print(data if data.strip() else "No encrypt history available.")
        except FileNotFoundError:
            print("Encrypt history file not found.")

        print("\n----- Decrypt History -----")
        try:
            with open(decrypt_file, "r", encoding="utf-8") as file:
                data = file.read()
                print(data if data.strip() else "No decrypt history available.")
        except FileNotFoundError:
            print("Decrypt history file not found.")


    # =====================================================
    # CLEAR HISTORY
    # =====================================================
    elif choice == 4:

        confirm = input("Are you sure you want to clear history? (yes/no): ")

        if confirm.lower() == "yes":
            open(encrypt_file, "w", encoding="utf-8").close()
            open(decrypt_file, "w", encoding="utf-8").close()
            print("History cleared successfully.")
        else:
            print("History was not cleared.")


    # =====================================================
    # EXIT
    # =====================================================
    elif choice == 5:
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice! Please select any number from 1 to 5.")
        