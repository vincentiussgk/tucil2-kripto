from rc4 import *

plaintext = "The quick brown fox jumps over the lazy dog."

# key = "Alalala"

key = [63,72, 79, 70, 74, 69, 69]

Encrypted_message = encrypt_rc4(plaintext, key)
print(Encrypted_message)

Decrypted_message = decrypt_rc4(Encrypted_message, key)
print(Decrypted_message)

