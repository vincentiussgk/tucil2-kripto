from extended_vigenere import *

def str_ascii(plaintext):
    return [ord(c) for c in plaintext]

def ascii_str(text):
    return ''.join(chr(i) for i in text)

def ksa(key):
    if type(key) == str:
        key = str_ascii(key)

    S = list(range(256))
    j = 0
    for i in range (256):
        j = (j + S[i] + int(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(text, S):
    encrypt_result = list(range(len(text)))
    i = 0
    j = 0
    for idx in range (0, len(text)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        # Keystream
        keystream = S[t]
        encrypt_result[idx] = keystream ^ text[idx]
    return encrypt_result

def cipher_rc4(plaintext, key):
    # Steps: KSA, PRGA, XOR with Keystream
    text = str_ascii(plaintext)

    S_permutations = ksa(key)
    encrypt_result = prga(text, S_permutations)
    cipher_result = ascii_str(encrypt_result)

    return cipher_result

def encrypt_rc4(text, key):
    vigenere_encrypted = evigenere_encrypt(text, key)
    return cipher_rc4(vigenere_encrypted, key)

def decrypt_rc4(text, key):
    cipher_result = cipher_rc4(text, key)
    return evigenere_decrypt(cipher_result, key)