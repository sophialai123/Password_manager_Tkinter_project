import tkinter
from tkinter import *  # all the tkinter class
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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
    # create a new dict to store json data:
    new_data = {
        website: {"Email": email,
                  "Password": password
        }

    }

    #if any fields are empty, showinfo
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please make sure you have not left any fields empty.")
    else:
        try:
            # create a new file, if the file doest not exist, will create it for you,
            with open("my_password_info.json", "r") as my_password_data:
                # how to read json file:
                data = json.load(my_password_data) # dict type
        #cathch an error:
        except FileNotFoundError:
            #if the file does not exist, will create a new one
            with open ("my_password_info.json", "w") as my_password_data:
                # how to use json to write the data and saving updated the data
                # first input is data and second input is file name, indent will have better format
                json.dump(new_data, my_password_data, indent=4)

        else: # ONLY if  try statement block of codes are True, the file found, this will be executed.
            # how to use json to update the data, first read the data,
            data.update(new_data)
            with open("my_password_info.json",'w') as my_password_data:
            # how to use json to write the data and saving updated the data
                json.dump(data, my_password_data, indent=4)

        finally:
            # delete all the entries once it finished, so will be ready for next
            web_input.delete(0, END)  # delete the from first to the last
            #user_input.delete(0, END)
            password_input.delete(0, END)



# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    # to get email and password values:
    website = web_input.get()

    # to catch errors:
    try:
        with open("my_password_info.json", 'r') as my_password_data:
            # read the file
            data = json.load(my_password_data)  # data is nested dict

    except FileNotFoundError:
        # show an error pop-ups
        messagebox.showinfo(title="Error", message="Sorry, No Data File Found.")

    else:
        # check if user's entry matches an item in Json's file
        if website in data:
            # to email and password value form nested dict
            email = data[website]["Email"]
            password = data [website]["Password"]
            # to updated the title and pop-ups:
            messagebox.showinfo(title=f"{website}", message=f" Email: {email}\n "
                                                    f"Password: {password}\n")
        # if user's details are not exist.
        else:
            messagebox.showinfo(title="Error", message=F"No details for {website} exists")



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
web_input = Entry(width=21)
web_input.grid(column=1, row=1)

#show the first input
web_input.focus()

# add columnspan
user_input = Entry(width=35)
user_input.grid(column=1, row=2,columnspan=2)

# show preinput: Entry.insert() method:
user_input.insert(0, "sophiacodes@yooho.com")  # 0index is the first character, END is the very last charater

password_input = Entry(width=21)

password_input.grid(column=1, row=3)

#create buttons and grid layout:
password_button = Button(text="Generate Password", command=generate_password)  # call the function
password_button.grid(column=2, row=3)

add_button = Button(text="Add",width=36, command=save) # command to call the save() function
add_button.grid(column=1, row=4,columnspan=2)

search_button = Button(text="Search",width=13, command=find_password) #command to call the function
search_button.grid(column=2, row=1)

#keep the window open
window.mainloop()
