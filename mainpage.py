from permutation_cipher import (
    encrypt_permutation_cipher,
    decrypt_permutation_cipher,
    is_valid_key
)

from bifid_encrypt import bifid_encrypt
from bifid_decrypt import bifid_decrypt

# visualization (OPTIONAL)
from visualization import (
    animate_permutation_encryption,
    animate_permutation_decryption,
    setup_screen
)

import turtle


def show_menu():
    print("\n====================")
    print(" CIPHER SYSTEM")
    print("====================")
    print("1. Permutation Cipher")
    print("2. Bifid Cipher")
    print("0. Exit")


def show_action():
    print("\n1. Encrypt")
    print("2. Decrypt")


# PERMUTATION
def handle_permutation():
    print("\n--- PERMUTATION CIPHER ---")
    show_action()

    action = input("Zgjedh veprimin: ").strip()
    text = input("Teksti: ").strip()

    key_input = input("Key (p.sh 2 0 3 1 ose 4 1 2 3): ").strip()

    try:
        key = [int(x) for x in key_input.split()]
    except ValueError:
        print("Key duhet me qenë numra!")
        return

    # auto-fix 1-based indexing
    if min(key) == 1:
        key = [k - 1 for k in key]

    if not is_valid_key(key):
        print("Key nuk është valid!")
        return

    vis = input("Me shfaq vizualizim? (y/n): ").strip().lower()

    if action == "1":
        result = encrypt_permutation_cipher(text, key)

        if vis == "y":
            animate_permutation_encryption(
                setup_screen(),
                turtle.Turtle(),
                text,
                key
            )

    elif action == "2":
        result = decrypt_permutation_cipher(text, key)

        if vis == "y":
            animate_permutation_decryption(
                setup_screen(),
                turtle.Turtle(),
                result,
                key
            )
    else:
        print("Zgjedhje e pavlefshme!")
        return

    print("\nRezultati:", result)


# BIFID
def handle_bifid():
    print("\n--- BIFID CIPHER ---")
    show_action()

    action = input("Zgjedh veprimin: ").strip()
    text = input("Teksti: ").strip()
    key = input("Keyword: ").strip()

    try:
        period = int(input("Period: "))
    except ValueError:
        print("Period duhet numër!")
        return

    if action == "1":
        result = bifid_encrypt(text, key, period)
    elif action == "2":
        result = bifid_decrypt(text, key, period)
    else:
        print("Zgjedhje e pavlefshme!")
        return

    print("\nRezultati:", result)


# MAIN LOOP
def main():
    while True:
        show_menu()
        choice = input("Zgjedh opsionin: ").strip()

        if choice == "1":
            handle_permutation()

        elif choice == "2":
            handle_bifid()

        elif choice == "0":
            print("Duke dalë...")
            break

        else:
            print("Zgjedhje e pavlefshme!")


if __name__ == "__main__":
    main()