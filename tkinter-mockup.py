# Some important notes:
# pack(), grid(), and place() all load widgets into the window.
# Do NOT pack/grid/place in the same statement as creating a widget. (this leads
# to undefined behavior)
# Grid configuration methods are your best friends for creating a layout that
# looks exactly like you envisioned.
# Use the 'master' arg to specify where stuff goes. It also helps make your code
# easier to read.
# Use the 'sticky' arg in grid() to make stuff the same size.

import tkinter

window_width  = 640
window_height = 480

main_window = tkinter.Tk()
main_window.geometry( f"{window_width}x{window_height}" )

main_window.grid_columnconfigure(0, weight = 1)
main_window.grid_columnconfigure(1, weight = 1)
main_window.grid_rowconfigure   (0, weight = 1)

# need a frame for each section of the window
left_frame  = tkinter.Frame( master = main_window )
right_frame = tkinter.Frame( master = main_window )

left_frame.grid_columnconfigure ( 0, weight = 1 )
right_frame.grid_columnconfigure( 1, weight = 1 )

left_frame.grid_rowconfigure ( 0, weight = 1 )
right_frame.grid_rowconfigure( 0, weight = 1 )

left_frame.grid ( row = 0, column = 0 )
right_frame.grid( row = 0, column = 1 )

# create placeholder widget for right side graph
_placeholder_graph = tkinter.Label(
    master = right_frame,
    text = "placeholder"
)

# create buttons on the left side
insert_new_expense_button = tkinter.Button(
    master = left_frame,
    text = "New expense",
    relief = tkinter.RAISED
)

insert_new_income_button = tkinter.Button(
    master = left_frame,
    text = "New income",
    relief = tkinter.RAISED
)

get_financial_advice_button = tkinter.Button(
    master = left_frame,
    text = "Financial advice",
    relief = tkinter.RAISED
)

_placeholder_graph.grid( row = 0, column = 0 )
insert_new_expense_button.grid  ( row = 0, column = 0, sticky = "ew" )
insert_new_income_button.grid   ( row = 1, column = 0, sticky = "ew" )
get_financial_advice_button.grid( row = 2, column = 0, sticky = "ew" )

main_window.mainloop()
