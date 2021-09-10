from tkinter import *
from random import randint

root = Tk()
root.title('Strong PassWord Generator')
root.geometry("500x300")



def new_rand():
	# Clear entry box
	pw_entry.delete(0, END)
	
	# Get PW length and convert to integer
	pw_length = int(my_entry.get())


# create a variable to hold our password
	my_password = ''

# Loop through password length

	for x in range(pw_length):
		my_password += chr(randint(33,126))

# Output password to the screen
	pw_entry.insert(0, my_password)

def clipper():
	pass 

# Copy to clipboard
def clipper():
	# clear the clipboard
	root.clipboard_clear()
	# copy to clipboard
	root.clipboard_append(pw_entry.get())

# Label Frame
lf = LabelFrame(root, text="How Many Charecters ?")
lf.pack(pady=20)

# Create entry box to designate number of charecters
my_entry = Entry(lf, font=("Helvetic", 24))
my_entry.pack(pady=20, padx=20)

# Create Entry box for our returned password

pw_entry = Entry(root,font=("Helvetica", 24), bd=0)
pw_entry.pack(pady=20)
pw_var = StringVar()
pw_entry.configure(textvariable=pw_var)

# Create a frame for our buttons
my_frame = Frame(root)
my_frame.pack(pady=20)


# Create our buttons
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)


clip_button = Button(my_frame, text="Copy To Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()
