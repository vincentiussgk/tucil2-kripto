from rc4 import *

from tkinter import *
import time
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog

root = Tk()
root.title("Kriptografi, Tucil 2")
root.geometry("600x600")

rc4Title = Label(
    text="RC4 Cypher, Extended Vigenere Cypher Modified"
)
rc4Title.pack()

def loadResultFromFile():
    textfile = filedialog.askopenfilename(initialdir = ".",
            title = "Select a File",
            filetypes = (("Text files",
                        "*.txt*"),
                        ("all files",
                        "*.*")))
    textfile = open(textfile, encoding='utf-8')
    cypherText = textfile.readline()
    key = textfile.readline()

    plainTextTextbox.delete(0, END)
    plainTextTextbox.insert(END, cypherText)

    cypherKeyTextbox.delete(0, END)
    cypherKeyTextbox.insert(END, key)

rc4LoadButton = Button(
    text="Load",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = loadResultFromFile
)
rc4LoadButton.pack()


plainTextLabel = Label(
    text="Enter Text"
)
plainTextLabel.pack()

plainTextTextbox = Entry()
plainTextTextbox.pack()

cypherKeyLabel = Label(
    text="Enter Key"
)
cypherKeyLabel.pack()

cypherKeyTextbox = Entry()
cypherKeyTextbox.pack()

def rc4Encyrpt():
    rc4Input = plainTextTextbox.get()
    rc4Key = cypherKeyTextbox.get()
    encryptResult, encryptResultB64 = encrypt_rc4(rc4Input, rc4Key)

    cypherResultTextbox.delete(0, END)
    cypherResultTextbox.insert(END, encryptResult)

    cypherResultB64Textbox.delete(0, END)
    cypherResultB64Textbox.insert(END, encryptResultB64)

rc4EncryptButton = Button(
    text="Encrypt",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = rc4Encyrpt
)
rc4EncryptButton.pack()

# Decryption
def rc4Decyrpt():
    rc4Encrypted = plainTextTextbox.get()
    rc4Key = cypherKeyTextbox.get()
    decryptResult, decryptResultB64 = decrypt_rc4(rc4Encrypted, rc4Key)
    
    cypherResultTextbox.delete(0, END)
    cypherResultTextbox.insert(END, decryptResult)

    cypherResultB64Textbox.delete(0, END)
    cypherResultB64Textbox.insert(END, decryptResultB64)

rc4DecyrptButton = Button(
    text="Decrypt",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = rc4Decyrpt
)
rc4DecyrptButton.pack()

# Start the app

cypherResult = Label(
    text="Result"
)
cypherResult.pack()

cypherResultTextbox = Entry()
cypherResultTextbox.pack()

virgenereResultB64 = Label(
    text="Result Base-64"
)
virgenereResultB64.pack()

cypherResultB64Textbox = Entry()
cypherResultB64Textbox.pack()

# Write to file
def saveResultToFile():
    f = open("cypher_result.txt", "w", encoding="utf-8")
    f.write(cypherResultTextbox.get())
    f.write('\n')
    f.write(cypherKeyTextbox.get())
    f.close()

cypherSaveButton = Button(
    text="Save",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = saveResultToFile
)
cypherSaveButton.pack()


root.mainloop()


f = open("input.txt", "r")

plaintext = f.readline()
key = f.readline()


plaintext = "The quick brown fox jumps over the lazy dog."

# key = "Alalala"

key = [63,72, 79, 70, 74, 69, 69]

Encrypted_message = encrypt_rc4(plaintext, key)
print(Encrypted_message)

Decrypted_message = decrypt_rc4(Encrypted_message, key)
print(Decrypted_message)

print(type(Encrypted_message))

f = open("output.txt", "w", encoding="utf-8")
f.write(Encrypted_message)
f.close()
