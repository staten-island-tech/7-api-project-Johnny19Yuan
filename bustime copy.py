import tkinter as tk

window = tk.Tk()
window.title("Bustime")
window.geometry("1024x728")
btn = tk.Button(
    window,
    text="see more",
    width=120,
    height=2,
    font=("Impact", 32),
    bg="black",
    fg="white",
    activebackground="gray",
    padx=10,
    pady=5
)
btn.pack(pady=20)
label = tk.Label(
    window,
    text="Welcome to mta bus time enhanced™ super editon®",
    font=("Comic Sans MS", 14),
    fg="blue"
)
label.pack(pady=10)

window.mainloop()
