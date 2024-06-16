import tkinter

# Define root window
root = tkinter.Tk()
root.title('Metric Helper')
root.iconbitmap('./images/ruler.ico')
# By not setting geo, the window will expand to fit widgets
# root. geometry('???x???')
root.resizable(0,0)

# Define fonts and colors
field_font = ('Cambria', 10)
bg_color = '#c84755'
button_color = '#f5cf87'
root.config(bg=bg_color)

# Define funcitons




# Run app
root.mainloop()
