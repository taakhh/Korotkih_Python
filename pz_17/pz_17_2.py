import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("pz17")
root.geometry("700x500")
root.configure(bg="#336699")

# Группа рамки
frame = tk.LabelFrame(root, text="Registration Details", fg="white", bg="#336699", font=("Arial", 12))
frame.place(x=50, y=40, width=600, height=370)

# Шрифты и параметры
label_font = ("Arial", 10)
entry_width = 30

# Поля
tk.Label(frame, text="University :", bg="#336699", fg="white", font=label_font).grid(row=0, column=0, sticky="e", padx=10, pady=5)
tk.Entry(frame, width=entry_width).grid(row=0, column=1, pady=5)

tk.Label(frame, text="Institute :", bg="#336699", fg="white", font=label_font).grid(row=1, column=0, sticky="e", padx=10, pady=5)
tk.Entry(frame, width=entry_width).grid(row=1, column=1, pady=5)

tk.Label(frame, text="Branch :", bg="#336699", fg="white", font=label_font).grid(row=2, column=0, sticky="e", padx=10, pady=5)
ttk.Combobox(frame, values=["--select--"], width=entry_width-2).grid(row=2, column=1, pady=5)

tk.Label(frame, text="Degree :", bg="#336699", fg="white", font=label_font).grid(row=3, column=0, sticky="e", padx=10, pady=5)
deg_f = tk.Frame(frame, bg="#336699")
deg_f.grid(row=3, column=1, sticky="w")

# Переменная для радиокнопок
degree_var = tk.IntVar(value=0)  # начальное значение

ttk.Combobox(deg_f, values=["--select--"], width=entry_width-12).grid(row=0, column=0)

tk.Radiobutton(
    deg_f, text="Pursuing", variable=degree_var, value=1,
    bg="#336699", fg="white", selectcolor="#336699"
).grid(row=0, column=1, padx=10)

tk.Radiobutton(
    deg_f, text="Completed", variable=degree_var, value=2,
    bg="#336699", fg="white", selectcolor="#336699"
).grid(row=0, column=2)

# Average CPI
tk.Label(frame, text="Average CPI :", bg="#336699", fg="white", font=label_font).grid(row=4, column=0, sticky="e", padx=10, pady=5)
cpi_f = tk.Frame(frame, bg="#336699")
cpi_f.grid(row=4, column=1, sticky="w")
tk.Spinbox(cpi_f, from_=0.0, to=10.0, increment=0.1, width=6).grid(row=0, column=0)
tk.Label(cpi_f, text="Upto", bg="#336699", fg="white").grid(row=0, column=1, padx=5)
tk.Spinbox(cpi_f, from_=1, to=12, width=4).grid(row=0, column=2)
tk.Label(cpi_f, text="Th Semester", bg="#336699", fg="white").grid(row=0, column=3, padx=5)

# Experience
tk.Label(frame, text="Experience :", bg="#336699", fg="white", font=label_font).grid(row=5, column=0, sticky="e", padx=10, pady=5)
exp_f = tk.Frame(frame, bg="#336699")
exp_f.grid(row=5, column=1, sticky="w")
tk.Spinbox(exp_f, from_=0, to=30, width=5).grid(row=0, column=0)
tk.Label(exp_f, text="Years", bg="#336699", fg="white").grid(row=0, column=1, padx=5)

# Website / Blog
tk.Label(frame, text="Your Website Or Blog :", bg="#336699", fg="white", font=label_font).grid(row=6, column=0, sticky="e", padx=10, pady=5)
site_entry = tk.Entry(frame, width=entry_width)
site_entry.insert(0, "http://")
site_entry.grid(row=6, column=1, pady=5)

# Step 2 кнопки
button_f = tk.Frame(root, bg="#336699")
button_f.place(x=280, y=430)

tk.Button(button_f, text="◀", font=("Arial", 16)).grid(row=0, column=0, padx=5)
tk.Label(button_f, text="Step 2", bg="#336699", fg="white", font=("Arial", 12)).grid(row=0, column=1, padx=5)
tk.Button(button_f, text="▶", font=("Arial", 16)).grid(row=0, column=2, padx=5)

root.mainloop()
