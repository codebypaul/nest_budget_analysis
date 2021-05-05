from tkinter import *

# Create window object
app = Tk()

# part
part_text = StringVar()
part_label = Label(app, text="Part Name", font=("bold", 14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)
# customer
customer_text = StringVar()
customer_label = Label(app, text="Part Name", font=("bold", 14))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=part_text)
customer_entry.grid(row=0, column=3)
#
part_text = StringVar()
part_label = Label(app, text="Part Name", font=("bold", 14))
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)
# part
part_text = StringVar()
part_label = Label(app, text="Part Name", font=("bold", 14))
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

app.title("Nest Homes")
app.geometry("1000x700")

# Start project
app.mainloop()
