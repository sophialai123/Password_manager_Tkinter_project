# Password_manager_Tkinter_project
"""
https://tkdocs.com/tutorial/canvas.html
https://tkdocs.com/tutorial/widgets.html#entry
https://www.w3schools.com/python/python_file_write.asp
https://pypi.org/project/pyperclip/
"""
import tkinter
from tkinter import *  # all the tkinter class
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    # to show the pop up
    password_input.insert(0, password)

    # user pyperclip to copy  and paste the password
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    #to get the entry values:

    website = web_input.get()
    email = user_input.get()
    password = password_input.get()

    #if any fields are empty, showinfo
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please make sure you have not left any fields empty.")
    else:
        # show message pop_ups
        # messagebox.showinfo(title="Title", message="Message")
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details are entered: Email:{email}"
                                               f"\n Password:{password}\n Is that ok to save? ")
        # if is_ok is ture, all the input information will be added into a file, if is_ok is false, it will not be added
        if is_ok:
            # create a new file, if the file doest not exist, will create it for you,
            with open("my_password_info.txt", "a") as my_password_data:
                # write all the data into a file:
                my_password_data.write(f"{website} | {email} | {password}\n")
                # delete all the entries once it finished, so will be ready for next
                web_input.delete(0, END)  # delete the from first to the last
                user_input.delete(0, END)
                password_input.delete(0, END)
                user_input.insert(0, "sophiacodes@yooho.com") # the email stays the same


# ---------------------------- UI SETUP ------------------------------- #
# create a window :
window = Tk()
#create a title:
window.title("Password Manager")

#to add paddings in window
window.config(padx=50, pady=50)


#create a canvas:
canvas = Canvas(width=200, height=200)

# to read through an image file, and provide the image location:
img = PhotoImage(file="logo.png")


# insert the image:
canvas.create_image(100, 100, image=img) # x and y position , half the size of image


#layout of canvas:
canvas.grid(column=1, row=0)

#create labels and grid layout
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)



user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#create input entries and grid layout:
web_input = Entry(width=35)
web_input.grid(column=1, row=1,columnspan=2)

#show the first input
web_input.focus()

user_input = Entry(width=35)
user_input.grid(column=1, row=2,columnspan=2)

# show preinput: Entry.insert() method:
user_input.insert(0, "sophiacodes@yooho.com")  # 0index is the first character, END is the very last charater

password_input = Entry(width=21)
# add columnspan
password_input.grid(column=1, row=3)

#create a button and grid layout:
password_button = Button(text="Generate Password", command=generate_password)  # call the function
password_button.grid(column=2, row=3)

add_button = Button(text="Add",width=36, command=save) # command to call the function
add_button.grid(column=1, row=4,columnspan=2)

#keep the window open
window.mainloop()
