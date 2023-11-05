import tkinter as tk

#Print Tkinter version
tcl = tk.Tcl()
print(tcl.call("info", "patchlevel"))

window_width = 640
window_height = 480
main_window = tk.Tk()
main_window.geometry( f"{window_width}x{window_height}" )

main_window.grid_columnconfigure(0, weight = 1)
main_window.grid_columnconfigure(1, weight = 1)
main_window.grid_rowconfigure(0, weight = 1)

# create a frame for each section of the window
left_frame  = tk.Frame( master = main_window )
right_frame = tk.Frame( master = main_window )

left_frame.grid_columnconfigure ( 0, weight = 1 )
right_frame.grid_columnconfigure( 1, weight = 1 )

left_frame.grid_rowconfigure ( 0, weight = 1 )
right_frame.grid_rowconfigure( 0, weight = 1 )

left_frame.grid ( row = 0, column = 0 )
right_frame.grid( row = 0, column = 1 )

#declare variables for income and categories
income_var = tk.IntVar()
new_category = tk.StringVar() # maybe appending it to a list would be better, but I just set it as string for now
total_income = tk.DoubleVar()
total_income = 1000.00

#buttons and labels
income_label = tk.Label(
    master=left_frame,
    text = "Input Income",
    relief = tk.GROOVE
)

income_entry = tk.Entry(
    master=left_frame,
    textvariable=income_var, # should be an integer to store income
    relief = tk.GROOVE
)

edit_categories_label = tk.Label(
    master=left_frame,
    text="Edit Categories",
    relief = tk.GROOVE
)
edit_categories_entry = tk.Entry(
    master=left_frame,
    textvariable=new_category,
    relief = tk.GROOVE
)

total_income = tk.Label(
    master=right_frame,
    text="Total Income: $" + str(total_income)
)

income_categories_list = tk.Listbox(
    master=right_frame
)

# for line in range(10):
#     income_categories_list.insert(line)

#left side of window
income_label.grid(row=1, column=0)
income_entry.grid(row=1, column=1)
edit_categories_label.grid(row=2,column=0)
edit_categories_entry.grid(row=2,column=1)

#right side of window
total_income.grid(row=1, column=0)
income_categories_list.grid(row=2, column=0)

main_window.mainloop()