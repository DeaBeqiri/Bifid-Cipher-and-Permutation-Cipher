def clean_text(text):
    return text.replace(" ", "").upper()


def pad_text(text, block_size):
    while len(text) % block_size != 0:
        text += 'X'
    return text

def get_inverse_key(key):
    inverse = [0] * len(key)
    for i, pos in enumerate(key):
        inverse[pos] = i
    return inverse

def encrypt_permutation_cipher(plaintext, key):
    plaintext = clean_text(plaintext)
    block_size = len(key)
    plaintext = pad_text(plaintext, block_size)

    ciphertext= " "

    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        encrypted_block = [''] * block_size

        for j in range(block_size):
            encrypted_block[j] = block[key[j]]

        ciphertext += ''.join(encrypted_block)

    return ciphertext




if __name__ == "__main__":
    key = [2,0,3,1]
    text="COMPUTER"

    encrypted = encrypt_permutation_cipher(text, key)
  

    print("\n---Permutation Cipher---")
    print("Original :", text)
    print("Encrypted :", encrypted)

    
