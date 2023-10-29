
import tkinter as tk

#Print Tkinter version
tcl = tk.Tcl()
print(tcl.call("info", "patchlevel"))

window_width = 640
window_height = 480
main_window = tk.Tk()
main_window.geometry( f"{window_width}x{window_height}" )

main_window.configure(background='white')

name_var = tk.StringVar()
password_var = tk.StringVar()


def LogIn():
    name = name_var.get()
    password=password_var.get()
    
    print(name)
    print(password)

#Labels and Buttons
Intro_label = tk.Label(
    main_window,
    text = "Welcome to CashFlow Creator!",
    relief = tk.RAISED
)

Username_label = tk.Label(
    main_window,
    text = "Enter Username",
    relief = tk.RAISED
)

Username_entry = tk.Entry(
    main_window, 
    textvariable = name_var, 
    relief=tk.RAISED
)

Password_label = tk.Label(
    main_window,
    text = "Enter Password",
    relief = tk.RAISED
)

Password_entry = tk.Entry(
    main_window, 
    textvariable = password_var, 
    relief=tk.RAISED
)

Login_button = tk.Button(
    main_window,
    text = 'Login',
    command = LogIn
)

#Positioning Labels and buttons
Intro_label.grid(row=0, column=0)
Username_label.grid(row=0,column=1)
Username_entry.grid(row=0,column=2)
Password_label.grid(row=1,column=1)
Password_entry.grid(row=1,column=2)
Login_button.grid(row=2,column=1)
  
main_window.mainloop()
