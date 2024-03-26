from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

window = Tk()

titleFont = ("Arial", "12", "bold")

window.config(padx=20, pady=20)
window.title("Secret Notes")
window.geometry('450x700')

photo = PhotoImage(file="img/image.png")
photoLabel = Label(image=photo)
photoLabel.pack()




titleLabel = Label(text="Enter your title", font=titleFont, padx=10, pady=10)
titleLabel.pack()

titleEntry = Entry(width=50)
titleEntry.pack()

textLabel = Label(text="Enter your secret message", font=titleFont, padx=10, pady=10)
textLabel.pack()

textEntry = Text(width=60, height=20)
textEntry.pack()

keyLabel = Label(text="Enter master key", font=titleFont, padx=10, pady=10)
keyLabel.pack()

keyEntry = Entry(width=50)
keyEntry.pack()


def SaveEncrypt():
    title = titleEntry.get()
    secretMessage = textEntry.get("1.0", END)
    userKey = keyEntry.get()

    if len(title) == 0 or len(secretMessage) == 0 or len(userKey) == 0:
        messagebox.showinfo(title="Error!", message="Please fill all blanks")
    else:
        encodedMessage = encode(userKey, secretMessage)
        try:
            with open("secret.txt", "a") as data_file:
                data_file.write(f"\n{title}\n{encodedMessage}")
        except FileNotFoundError:
            with open("secret.txt", "w") as data_file:
                data_file.write(f"\n{title}\n{encodedMessage}")
        finally:
            titleEntry.delete("0", END)
            keyEntry.delete("0", END)
            textEntry.delete("1.0", END)


def Decrypt():
    encodedMessage = textEntry.get("1.0", END)
    userKey = keyEntry.get()

    if len(userKey) == 0 or len(encodedMessage) == 0:
        messagebox.showinfo(title="Error!", message="Please fill all blanks")
    else:
        decodedMessage = decode(userKey, encodedMessage)
        textEntry.delete("1.0", END)
        keyEntry.delete(0, END)
        textEntry.insert("1.0", decodedMessage)












saveButton = Button(text="Save & Encrypt", command=SaveEncrypt)
saveButton.pack()

decryptButton = Button(text="Decrypt", command=Decrypt)
decryptButton.pack(side="bottom")

"""
message = "hello world"
key = Fernet.generate_key()
fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())
print("original string: ", message)
print("encrypted string: ", encMessage)
decMessage = fernet.decrypt(encMessage).decode()
print("decrypted string: ", decMessage)
"""


window.mainloop()