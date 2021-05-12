from tkinter import *
from PIL import ImageTk, Image
# Create window object
from db import Database, ActDatabase

budg_db=Database('budget.db')
act_db=Database('act.db')

def populate_list():
    report.delete(0,END)
    for row in db.fetch():
        report.insert(END,row)

def generate_report():
    print(prop_no_text.get())


app = Tk()

img = Image.open('./images/nest-logo.png')
img = img.resize((200,110),Image.ANTIALIAS)
test = ImageTk.PhotoImage(img)

img_label = Label(app,image=test,pady=40,anchor=CENTER)
img_label.image = test
img_label.pack()

# part
prop_no_text = StringVar()
prop_no_label = Label(app, text="Property Code", font=("bold", 14),anchor=CENTER)
prop_no_label.pack()
prop_no_entry = Entry(app, textvariable=prop_no_text)
prop_no_entry.pack()
# search button
search_btn=Button(app,text='Generate Report',width=20,command=generate_report)
search_btn.pack()
report = Listbox(app,height=50,width=75,border=0)
report.pack()

scrollbar = Scrollbar(app)
# scrollbar.grid(row=3,column=5)

# Set scrollbar
report.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=report.yview)

app.title("Nest Homes")
app.geometry("1000x700")


# Start project
app.mainloop()
