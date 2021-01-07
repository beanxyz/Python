from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


windows = Tk()
windows.title ("Password Manager")
windows.config(padx = 50, pady = 50)

canvas = Canvas (width=200, height = 200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(102,100,image=lock_img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

website_text=Entry(width=35)
website_text.grid(row=1,column=1,columnspan=2)


email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)

email_text = Entry(width=35)
email_text.grid(row=2,column=1, columnspan =2)

password_label= Label(text = "Password:")
password_label.grid(row=3,column=0)

password_text = Entry(width=16)
password_text.grid(row=3,column=1)

password_btn= Button(text = "Generate Password")
password_btn.grid(row=3,column=2)

add_btn = Button(text = "Add",width=45)
add_btn.grid(row = 4,column=1,columnspan=2)




windows.mainloop()