import tkinter as tk
from tkinter import *

# Create root window
root = Tk()
root.title("Caesar Cipher")
root.geometry("800x500")

# Title Label
title = StringVar()
title.set("Caesar Cipher")

label1 = Label(
    root,
    textvariable=title,
    anchor=CENTER,
    height=2,
    font=("Georgia", 20, "bold"),
    fg="black",
    relief=RAISED
)
label1.grid(row=0, column=0, columnspan=3, pady=20, padx=10, sticky=NSEW)

# Input Text Label and Widget
input_label = Label(root, text="Input Text:", font=("Arial", 12))
input_label.grid(row=1, column=0, padx=10, sticky=W)

text1 = Text(root, height=5, width=50)
text1.grid(row=1, column=1, padx=10, pady=5)

# Output Text Label and Widget
output_label = Label(root, text="Output Text:", font=("Arial", 12))
output_label.grid(row=2, column=0, padx=10, sticky=W)

text2 = Text(root, height=5, width=50, state="disabled")
text2.grid(row=2, column=1, padx=10, pady=5)

# Shift Value Label and Entry
shift_label = Label(root, text="Shift Value:", font=("Arial", 12))
shift_label.grid(row=3, column=0, padx=10, sticky=W)

shift_value = Entry(root, width=10)
shift_value.grid(row=3, column=1, padx=10, pady=5, sticky=W)

# Cipher Functions
def encode_text():
    process_text(encode=True)

def decode_text():
    process_text(encode=False)

def process_text(encode=True):
    input_text = text1.get("1.0", "end").strip()
    shift = shift_value.get().strip()

    # Validate shift value
    if not shift.isdigit():
        text2.config(state="normal")
        text2.delete("1.0", "end")
        text2.insert("1.0", "Invalid shift value! Please enter a number.")
        text2.config(state="disabled")
        return

    shift = int(shift)
    if not encode:
        shift = -shift  # Reverse the shift for decoding

    # Process the text
    processed_text = "".join(
        chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper()
        else chr((ord(char) - 97 + shift) % 26 + 97) if char.islower()
        else char
        for char in input_text
    )

    # Display the result
    text2.config(state="normal")
    text2.delete("1.0", "end")
    text2.insert("1.0", processed_text)
    text2.config(state="disabled")

# Buttons for Encode and Decode
encode_button = Button(root, text="Encode", command=encode_text, font=("Arial", 12))
encode_button.grid(row=4, column=1, pady=10, padx=10, sticky=W)

decode_button = Button(root, text="Decode", command=decode_text, font=("Arial", 12))
decode_button.grid(row=4, column=1, pady=10, padx=100, sticky=W)

# Configure column weights to center title
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Run the app
root.mainloop()
