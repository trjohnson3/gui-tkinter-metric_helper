import tkinter
from tkinter import ttk

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
input_field = tkinter.Entry(root, width=20, font=field_font, borderwidth=3)
output_field = tkinter.Entry(root, width=20, font=field_font, borderwidth=3)
equal_label = tkinter.Label(root, text='=', font=field_font, bg=bg_color)

input_field.grid(row=0, column=0, padx=10, pady=10)
equal_label.grid(row=0, column=1, padx=10, pady=10)
output_field.grid(row=0, column=2, padx=10, pady=10)

input_field.insert(0, 'Enter your quantity')
output_field.config(state='readonly')

#Create combo boxes for metric values
metric_list = ['femto', 'pico', 'nano', 'micro', 'milli', 'centi', 'deci',
               'base', 'deca', 'hecto', 'kilo', 'mega', 'giga', 'tetra', 'peta']

input_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify='center')
output_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify='center')
to_label = tkinter.Label(root, text='to', font=field_font, bg=bg_color)

input_combobox.grid(row=1, column=0, padx=10, pady=10)
output_combobox.grid(row=1, column=2, padx=10, pady=10)
to_label.grid(row=1, column=1, padx=10, pady=10)

input_combobox.set('base')
output_combobox.set('base')

#Create a conversion button
convert_button = tkinter.Button(root, text='convert', font=field_font, bg=button_color)
convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)


# Run app
root.mainloop()
