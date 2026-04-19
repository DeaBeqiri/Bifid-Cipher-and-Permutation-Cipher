
def create_polybius_square(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.upper().replace("J", "I")

    square = []
    used = set()

    for char in key:
        if char in alphabet and char not in used:
            square.append(char)
            used.add(char)

    for char in alphabet:
        if char not in used:
            square.append(char)

    return [square[i:i+5] for i in range(0, 25, 5)]


def create_lookup(matrix):
    return {matrix[r][c]: (r, c) for r in range(5) for c in range(5)}


def bifid_decrypt(ciphertext, key, period):
    matrix = create_polybius_square(key)
    lookup = create_lookup(matrix)

    ciphertext = ciphertext.upper().replace("J", "I")
    ciphertext = ''.join(c for c in ciphertext if c.isalpha())

    plaintext = ""

    for i in range(0, len(ciphertext), period):
        block = ciphertext[i:i+period]

        coords = []

        for char in block:
            r, c = lookup[char]
            coords.extend([r, c])

        half = len(coords) // 2
        rows = coords[:half]
        cols = coords[half:]

        for j in range(len(rows)):
            plaintext += matrix[rows[j]][cols[j]]

    return plaintext


# ===== MAIN =====
text = input("Enter ciphertext: ")
key = input("Enter key: ")
period = int(input("Enter period: "))

print("Decrypted:", bifid_decrypt(text, key, period))
