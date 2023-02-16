def evigenere_encrypt(plaintext, key):
    # plaintext = plaintext.upper()

    # plaintextrdy = ''

    # for i in range (len(plaintext)):
    #     if(plaintext[i].isalpha()):
    #         plaintextrdy += plaintext[i]

    # key = key.upper()
    # keyprep = ''

    # for i in range (len(key)):
    #     if(key[i].isalpha()):
    #         keyprep += key[i]
    
    keyrdy = ''
    for i in range (len(plaintext)):
        keyrdy += key[i % len(key)]
    
    print(keyrdy)

    plain_int = [ord(i) for i in plaintext]
    key_int = [ord(i) for i in keyrdy]

    cyphertext = ''
    for i in range (len(plaintext)):
        charvalue = (plain_int[i] + key_int[i]) % 256
        cyphertext = cyphertext + chr(charvalue)

    print(cyphertext)
    return cyphertext

def evigenere_decrypt(cyphertext, key):
    # cyphertext = cyphertext.upper()

    # cyphertextrdy = ''

    # for i in range (len(cyphertext)):
    #     if(cyphertext[i].isalpha()):
    #         cyphertextrdy += cyphertext[i]

    # key = key.upper()
    # keyprep = ''

    # for i in range (len(key)):
    #     if(key[i].isalpha()):
    #         keyprep += key[i]
    
    keyrdy = ''
    for i in range (len(cyphertext)):
        keyrdy += key[i % len(key)]

    print(keyrdy)

    cyp_int = [ord(i) for i in cyphertext]
    key_int = [ord(i) for i in keyrdy]

    plaintext = ''
    for i in range (len(cyphertext)):
        charvalue = (cyp_int[i] - key_int[i]) % 256
        plaintext = plaintext + chr(charvalue)

    print(plaintext)
    return plaintext

evigenere_encrypt("ABC #2", "!0.")
evigenere_decrypt("brqAS`", "!0.")

    