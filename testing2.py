import tkinter as tk
import time

def type_text(label, text, delay=100):
    for char in text:
        label.config(text=label.cget("text") + char)
        root.update_idletasks()
        root.after(delay)

def type_text_decorator(func):
    def wrapper(*args, **kwargs):
        label = args[0]
        text = kwargs['text']
        delay = kwargs.get('delay', 100)
        type_text(label, text, delay)
        return func(*args, **kwargs)
    return wrapper

root = tk.Tk()

label = tk.Label(root, text="", font=("Arial", 24))
label.pack()

def print_hello():
    label.config(text="")

print_hello()
root.update_idletasks()
root.after(1000)

def greet():
    label.config(text=label.cget("text") + "Hello, world!")
    root.update_idletasks()
    root.after(100)

@type_text_decorator
def print_text():
    label.config(text=label.cget("text") + " This is a slowly typed message.")
    root.update_idletasks()
    root.after(100)

root.after(2000, print_text)
root.after(3000, greet)

root.mainloop()