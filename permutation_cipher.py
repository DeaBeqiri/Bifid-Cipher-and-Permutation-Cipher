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
    n = len(key)

    # pa duplicate
    if len(set(key)) != n:
        return False

    # case 1: 0-based
    if sorted(key) == list(range(n)):
        return True

    # case 2: 1-based (USER FRIENDLY)
    if sorted(key) == list(range(1, n + 1)):
        return True

    return False

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