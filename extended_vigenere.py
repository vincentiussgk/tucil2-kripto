def evigenere_encrypt(plaintext, key):
    
    keyrdy = ''
    key_int = []

    for i in range (len(plaintext)):
        if type(key) == str:
            keyrdy += key[i % len(key)]
        else:
            key_int.append(key[i % len(key)])
    if type(key) == str:
        key_int = [ord(i) for i in keyrdy]

    plain_int = [ord(i) for i in plaintext]

    cyphertext = ''
    for i in range (len(plaintext)):
        charvalue = (plain_int[i] + key_int[i]) % 256
        cyphertext = cyphertext + chr(charvalue)

    return cyphertext

def evigenere_decrypt(cyphertext, key):

    keyrdy = ''
    key_int = []

    for i in range (len(cyphertext)):
        if type(key) == str:
            keyrdy += key[i % len(key)]
        else:
            key_int.append(key[i % len(key)])
    if type(key) == str:
        key_int = [ord(i) for i in keyrdy]

    cyp_int = [ord(i) for i in cyphertext]

    plaintext = ''
    for i in range (len(cyphertext)):
        charvalue = (cyp_int[i] - key_int[i]) % 256
        plaintext = plaintext + chr(charvalue)

    return plaintext

    