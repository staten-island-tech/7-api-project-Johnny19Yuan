import tkinter as tk

window = tk.Tk()
window.title("Bustime")
window.geometry("1166x768")
btn = tk.Button(
    window,
    text="Enter",
    width=10,
    height=2,
    font=("Helvetica", 32, "bold"),
    bg="black",
    fg="white",
    activebackground="gray",
    padx=10,
    pady=5
) 
btn.grid(row=10, column=0, padx=10, pady=20)
label = tk.Label(
    window,
    text="Welcome to mta bus time enhanced™ super editon®",
    font=("Comic Sans MS", 14),
    fg="red"
)
label.grid(row=1, column=0, pady=10)

def search():
    print(entry.get)


entry = tk.Entry(window, width=30)
button = tk.Button(window, text="Search", command=search)

entry.grid(row=0, column=0, padx=10, pady=20)
button.grid(row=0, column=1, padx=2, pady=20)


label.grid(pady=10)
print(entry.get)
window.mainloop()