import tkinter as tk
window = tk.Tk()
window.title("Checkbutton & Radiobutton Demo")
window.geometry("350x300")
tk.Label(window, text="Select your hobbies:").pack()
hobby1 = tk.IntVar()
hobby2 = tk.IntVar()
cb1 = tk.Checkbutton(window, text="Reading", variable=hobby1)
cb1.pack()
cb2 = tk.Checkbutton(window, text="Gaming", variable=hobby2)
cb2.pack()
tk.Label(window, text="Select your gender:").pack()
gender = tk.StringVar()
rb1 = tk.Radiobutton(window, text="Male", variable=gender, value="Male")
rb1.pack()
rb2 = tk.Radiobutton(window, text="Female", variable=gender, value="Female")
rb2.pack()
def show_selection():
    hobbies = ""
    if hobby1.get() == 1:
        hobbies += "Reading "
    if hobby2.get() == 1:
        hobbies += "Gaming "
    
    result_label.config(text="Hobbies: " + hobbies + "\nGender: " + gender.get())
btn = tk.Button(window, text="Submit", command=show_selection)
btn.pack(pady=10)
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()