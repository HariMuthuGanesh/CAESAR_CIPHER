from tkinter import *
from tkinter import messagebox

def caesar_encrypt(text, key):
    result = ''
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            result += char
    return result

def caesar_decrypt(text, key):
    result = ''
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        else:
            result += char
    return result


def encrypt_text():
    try:
        text = input_text.get("1.0", END).strip()
        key = int(shift_entry.get())
        result = caesar_encrypt(text, key)
        output_text.delete("1.0", END)
        output_text.insert(END, result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the shift.")

def decrypt_text():
    try:
        text = input_text.get("1.0", END).strip()
        key = int(shift_entry.get())
        result = caesar_decrypt(text, key)
        output_text.delete("1.0", END)
        output_text.insert(END, result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the shift.")


window = Tk()
window.title("Caesar Cipher - Encrypt & Decrypt")
window.geometry("600x600")  
window.config(bg="#726DFF")

main_frame = Frame(window, bg="#4f6fff",highlightbackground="gray" ,relief="groove",borderwidth=2)
main_frame.pack(padx=25, pady=25, fill=BOTH, expand=True)
main_frame.place(relx=0.5, rely=0.5, anchor="center") 


Label(main_frame, text="🔐 Caesar Cipher", font=("Times New Roman", 26, "bold"), bg="#ffffff",fg="#212121").pack(padx=(1,0),pady=(2,0))
Label(main_frame, text="Enter your message:", font=("Times New Roman", 16), bg="#f0f0f0",fg="#212121").pack(pady=(15,5))
input_text = Text(main_frame, height=5, width=55, font=("Times New Roman", 14),bd=2, relief="solid")
input_text.pack(pady=5,padx=10)

Label(main_frame, text="Key value:", font
      =("Times New Roman", 16), bg="#f0f0f0").pack(pady=(15,5))
shift_entry = Entry(main_frame, font=("Times New Roman", 14), width=10, justify="center",bd=2, relief="solid")
shift_entry.pack()

button_frame = Frame(main_frame, bg="#5e7bfc")
button_frame.pack(pady=18,padx=10)

encrypt_btn = Button(button_frame, text="Encrypt", command=encrypt_text, bg="#4CAF50", fg="white", font=("Times New Roman", 16), width=12)
encrypt_btn.grid(row=0, column=0, padx=11)

decrypt_btn = Button(button_frame, text="Decrypt", command=decrypt_text, bg="#2196F3", fg="white", font=("Times New Roman", 16), width=12)
decrypt_btn.grid(row=0, column=1, padx=11)

Label(main_frame, text="Result:", font=("Times New Roman", 14), bg="#f0f0f0",fg="#212121").pack()
output_text = Text(main_frame, height=5, width=55, font=("Times New Roman", 12),bd=2, relief="solid")
output_text.pack(pady=10)

window.mainloop()