import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, shift):
    # Helper function to shift a single character
    def shift_char(c, shift):
        if c.isalpha():
            start = ord('A') if c.isupper() else ord('a')
            return chr((ord(c) - start + shift) % 26 + start)
        return c

    return ''.join(shift_char(c, shift) for c in text)

# Function to encode a message
def encode_caesar_cipher(text, shift):
    return caesar_cipher(text, shift)

# Function to decode a message
def decode_caesar_cipher(text, shift):
    return caesar_cipher(text, -shift)

# Function to handle encoding
def handle_encode():
    plaintext = text_entry.get()
    try:
        shift = int(shift_entry.get())
        ciphertext = encode_caesar_cipher(plaintext, shift)
        result_text.set(f"Ciphertext: {ciphertext}")
    except ValueError:
        result_text.set("Invalid shift value! Please enter an integer.")

# Function to handle decoding
def handle_decode():
    ciphertext = result_text.get().split(": ")[-1]  # Extract ciphertext from result_text
    try:
        shift = int(shift_entry.get())
        decoded_text = decode_caesar_cipher(ciphertext, shift)
        result_text.set(f"Decoded text: {decoded_text}")  # Update result_text with decoded text
    except ValueError:
        result_text.set("Invalid shift value! Please enter an integer.")

# Set up the main application window
root = tk.Tk()
root.title("Caesar Cipher")

# Define and place the GUI elements
ttk.Label(root, text="Enter text:",foreground="blue").grid(row=0, column=0, padx=10, pady=5, sticky="w")
text_entry = ttk.Entry(root, width=40)
text_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Enter shift value:",foreground="blue").grid(row=1, column=0, padx=10, pady=5, sticky="w")
shift_entry = ttk.Entry(root, width=10)
shift_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

encode_button = ttk.Button(root, text="Encrypt", command=handle_encode)
encode_button.grid(row=2, column=0, padx=10, pady=10, sticky="e")

decode_button = ttk.Button(root, text="Decrypt", command=handle_decode)
decode_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, font=("Helvetica", 12))
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the main application loop
root.mainloop()
