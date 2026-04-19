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


def bifid_encrypt(plaintext, key, period):
    matrix = create_polybius_square(key)
    lookup = create_lookup(matrix)

    plaintext = plaintext.upper().replace("J", "I")
    plaintext = ''.join(c for c in plaintext if c.isalpha())

    ciphertext = ""

    for i in range(0, len(plaintext), period):
        block = plaintext[i:i+period]

        rows, cols = [], []

        for char in block:
            r, c = lookup[char]
            rows.append(r)
            cols.append(c)

        combined = rows + cols

        for j in range(0, len(combined), 2):
            ciphertext += matrix[combined[j]][combined[j+1]]

    return ciphertext


# ===== MAIN =====
text = input("Enter plaintext: ")
key = input("Enter key: ")
period = int(input("Enter period: "))

print("Encrypted:", bifid_encrypt(text, key, period))
