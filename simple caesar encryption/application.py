from tkinter import Tk, Label, Text, Button, END


def encrypt():
    text = input_text_Text.get("1.0", END)
    enc_shift = int(input_shifter_Text.get("1.0", END))
    encrypted_text = ""
    for i in text:
        encrypted_text += str(chr(ord(i) + enc_shift))
    print(encrypted_text)
    output_text_Text.delete("1.0", END)
    output_text_Text.insert("1.0", encrypted_text)


def decrypt():
    text = input_text_Text.get("1.0", END)
    dcr_shift = int(input_shifter_Text.get("1.0", END))
    decrypted_text = ""
    for i in text:
        decrypted_text += str(chr(ord(i) - int(dcr_shift)))
    print(decrypted_text)
    output_text_Text.delete("1.0", END)
    output_text_Text.insert("1.0", decrypted_text)


def clear():
    input_text_Text.delete("1.0", END)
    encrypted_text.delete("1.0", END)
    output_text_Text.delete("1.0", END)


root = Tk()
root.geometry("500x700")
root.title = "Encryption-inator"

input_text_Label = Label(root, text="Enter text to be encrypted/decrypted:")
input_text_Label.grid(row=0, column=0, columnspan=3, pady=9)

input_text_Text = Text(root, width=60, height=15)
input_text_Text.grid(row=1, column=0, columnspan=3, rowspan=5, padx=6)


input_shifter_Label = Label(root, text="Shift value:")
input_shifter_Label.grid(row=6, column=0, pady=9)

input_shifter_Text = Text(root, width=30, height=1)
input_shifter_Text.grid(row=6, column=1, rowspan=1, columnspan=2)


encrypt_Button = Button(root, text="ENCRYPT", command=encrypt)
encrypt_Button.grid(row=7, column=0, pady=9)


decrypt_Button = Button(root, text="DECRYPT", command=decrypt)
decrypt_Button.grid(row=7, column=1, pady=9)


clear_Button = Button(root, text="CLEAR", command=clear)
clear_Button.grid(row=7, column=2, pady=9)


output_text_Label = Label(root, text="Encrypted / decrypted text:")
output_text_Label.grid(row=8, column=0, columnspan=3, pady=9)

output_text_Text = Text(root, width=60, height=15)
output_text_Text.grid(row=9, column=0, columnspan=3, rowspan=5, padx=6)

root.mainloop()
