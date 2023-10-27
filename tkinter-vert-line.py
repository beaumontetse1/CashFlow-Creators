import tkinter as tk

root = tk.Tk()
root.title("Vertical Line Example")

# Set the width and height of the window
window_width = 400
window_height = 300

# Create a Canvas widget
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

# Calculate the x-coordinate for the vertical line (half of the window width)
line_x = window_width // 2

canvas.create_line(line_x, 0, line_x, window_height, fill="black")

# Run the Tkinter main loop
root.mainloop()
