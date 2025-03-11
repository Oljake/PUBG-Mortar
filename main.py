import customtkinter as ctk
import math

def is_numeric(value_if_allowed):
    return value_if_allowed.isdigit() or (value_if_allowed == "" and len(value_if_allowed) == 0)

def calculate_hypotenuse(event=None):
    try:
        a = float(entry_a.get()) if entry_a.get() else 0.0
        b = float(entry_b.get()) if entry_b.get() else 0.0
        c = math.sqrt(a ** 2 + b ** 2)

        if c < 121:
            result_text = f"c = {c:.2f} m (Too Close)"
        elif c > 700:
            result_text = f"c = {c:.2f} m (Too Far)"
        else:
            result_text = f"c = {c:.2f} m"

        label_result.configure(text=result_text)

        entry_a.delete(0, ctk.END)
        entry_b.delete(0, ctk.END)

        entry_a.focus()

    except ValueError:
        label_result.config(text="Please enter valid numbers.")

root = ctk.CTk()
root.title("PUBG Mortar")
root.geometry("245x190")  # Set a wider window size
root.resizable(False, False)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

vcmd = (root.register(is_numeric), '%P')

label_a = ctk.CTkLabel(root, text="a:")
label_a.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

entry_a = ctk.CTkEntry(root, validate='key', validatecommand=vcmd)
entry_a.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
entry_a.focus()
entry_a.bind("<Return>", calculate_hypotenuse)

label_b = ctk.CTkLabel(root, text="b:")
label_b.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

entry_b = ctk.CTkEntry(root, validate='key', validatecommand=vcmd)
entry_b.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
entry_b.bind("<Return>", calculate_hypotenuse)

button_calculate = ctk.CTkButton(root, text="Calculate", command=calculate_hypotenuse)
button_calculate.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

label_result = ctk.CTkLabel(root, text="c = ")
label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

root.mainloop()
