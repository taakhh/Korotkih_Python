import tkinter as tk

def calculate():
    output_text.delete("1.0", tk.END)
    try:
        A = float(entry_a.get())
        N = int(entry_n.get())
        if N <= 0:
            output_text.insert(tk.END, "Ошибка: N должно быть больше 0.\n")
            return

        for i in range(1, N + 1):
            result = A ** i
            output_text.insert(tk.END, f"{A}^{i} = {result}\n")

    except ValueError:
        output_text.insert(tk.END, "Ошибка: Введите корректные числовые значения.\n")

root = tk.Tk()
root.title("Степени числа A")

tk.Label(root, text="Вещественное число A:").grid(row=0, column=0, sticky="w")
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

tk.Label(root, text="Целое число N (>0):").grid(row=1, column=0, sticky="w")
entry_n = tk.Entry(root)
entry_n.grid(row=1, column=1)

calc_button = tk.Button(root, text="Вычислить", command=calculate)
calc_button.grid(row=2, column=0, columnspan=2, pady=5)

output_text = tk.Text(root, height=10, width=40)
output_text.grid(row=3, column=0, columnspan=2)

root.mainloop()
