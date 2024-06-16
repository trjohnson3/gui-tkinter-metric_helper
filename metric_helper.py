import tkinter

#Define root window
root = tkinter.Tk()
root.title('Metric Helper')
root.iconbitmap('./images/ruler.ico')
root.resizable(0,0)

#Define fonts and colors
field_font = ('Cambria', 10)
bg_color = '#c84755'
button_color = '#f5cf87'
root.config(bg=bg_color)

#Define funcitons


#Define layout
#Create input and output entry fields
input_field = tkinter.Entry(root, width=20, font=field_font)
output_field = tkinter.Entry(root, width=20, font=field_font)
equal_label = tkinter.Label(root, text='=', font=field_font, bg=bg_color)

input_field.grid(row=0, column=0, padx=10, pady=10)
equal_label.grid(row=0, column=1, padx=10, pady=10)
output_field.grid(row=0, column=2, padx=10, pady=10)

input_field.insert(0, 'Enter your quantity')
output_field.insert(0, 'Result')
output_field.config(state='readonly')



# Run app
root.mainloop()
