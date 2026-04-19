def clean_text(text):
    return text.upper()


def pad_text(text, block_size):
    while len(text) % block_size != 0:
        text += 'X'
    return text

def get_inverse_key(key):
    inverse = [0] * len(key)
    for i, pos in enumerate(key):
        inverse[pos] = i
    return inverse

def is_valid_key(key):
    return sorted(key)==list(range(len(key)))

def encrypt_permutation_cipher(plaintext, key):
    plaintext = clean_text(plaintext)
    block_size = len(key)
    plaintext = pad_text(plaintext, block_size)

    ciphertext= ""

    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        encrypted_block = [''] * block_size

        for j in range(block_size):
            encrypted_block[j] = block[key[j]]

        ciphertext += ''.join(encrypted_block)

    return ciphertext

def decrypt_permutation_cipher(ciphertext,key):
    ciphertext= clean_text(ciphertext)
    block_size= len(key)
    inverse_key= get_inverse_key(key)

    plaintext=""

    for i in range(0,len(ciphertext),block_size):
        block= ciphertext[i:i+block_size]
        decrypted_block=['']*block_size

        for j in range(block_size):
            decrypted_block[j]= block[inverse_key[j]]


        plaintext += ''.join(decrypted_block)

    return plaintext.rstrip('X')


if __name__ == "__main__":
    
 text = input("Shkruaj fjalen: ")

key_input = input("Shkruaj key: ")
key = list(map(int, key_input.split()))

if not is_valid_key(key):
    print("Key nuk eshte valid")
else:
    encrypted = encrypt_permutation_cipher(text, key)
    decrypted = decrypt_permutation_cipher(encrypted, key)

    print("\n---Permutation Cipher---")
    
    print("Encrypted :", encrypted)
    print("Decrypted :", decrypted)
    
