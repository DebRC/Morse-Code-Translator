# import all functions from the tkinter
from tkinter import *

# import messagebox class from tkinter
from tkinter import messagebox

# Create a GUI window
root = Tk()
root.resizable(width=False, height=False)
# create a global variables
option1 = StringVar(root)
option2 = StringVar(root)

# initialise the variables
option1.set("From")
option2.set("To")

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-',
					'a':'.-', 'b':'-...',
					'c':'-.-.', 'd':'-..', 'e':'.',
					'f':'..-.', 'g':'--.', 'h':'....',
					'i':'..', 'j':'.---', 'k':'-.-',
					'l':'.-..', 'm':'--', 'n':'-.',
					'o':'---', 'p':'.--.', 'q':'--.-',
					'r':'.-.', 's':'...', 't':'-',
					'u':'..-', 'v':'...-', 'w':'.--',
					'x':'-..-', 'y':'-.--', 'z':'--..',}

# Function to clear both the text areas
def clearAll():
	language1_field.delete(1.0, END)
	language2_field.delete(1.0, END)

# Function to perform conversion form one language to another
def convert():
	message = language1_field.get("1.0", "end")[:-1]
	if option1.get() == option2.get():
		messagebox.showerror("Error! Same Language Selected.")
		return
	elif option1.get() == "English" and option2.get() == "Morse":
		rslt = encrypt(message)
	elif option1.get() == "Morse" and option2.get() == "English":
		rslt = decrypt(message)
	else:
		messagebox.showerror("Please select the languages.")
		return
	language2_field.insert('end -1 chars', rslt)

# Function to encrypt the string according to the morse code chart
def encrypt(message):
	cipher = ''
	for letter in message:
		if letter != ' ':
			cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			cipher += ' '
	return cipher

# Function to decrypt the string from morse to english
def decrypt(message):
	message += ' '
	decipher = ''
	citext = ''
	i = 0
	for letter in message:
		if (letter != ' '):
			i = 0
			citext += letter
		else:
			i += 1
			if i == 2:
				decipher += ' '
			else:
				decipher += list(MORSE_CODE_DICT.keys())[
							list(MORSE_CODE_DICT .values()).index(citext)]
				citext = ''
	return decipher


# Driver code
if __name__ == "__main__" :

	# Set the background colour of GUI window
	root.configure(background = 'light blue')

	# Set the configuration of GUI window (WidthxHeight)
	root.geometry("860x250")

	# set the name of tkinter GUI window
	root.title("Morse Code Translator")

	# Create Welcome to Morse Code Translator label
	headlabel = Label(root, text = 'Morse Code Translator', fg = 'dark green', bg = "light blue", height = 2, font = "algerian")
	headlabel.grid(row = 0, column = 1)

	# Create a text area box
	# for filling or typing the information.
	language1_field = Text(root, height = 5, width = 25, bg = "pink", fg="blue", font = "arial")
	language2_field = Text(root, height = 5, width = 25, bg = "pink", fg="blue", font = "arial")

	# padx keyword argument used to set paading along x-axis .
	language1_field.grid(row = 2, column = 0, padx = 10)
	language2_field.grid(row = 2, column = 2, padx = 10)

	# list of language codes
	languageCode_list = ["English", "Morse"]

	# create a drop down menu using OptionMenu function
	# which takes window name, variable and choices as
	# an argument. use * befor the name of the list,
	# to unpack the values
	FromLanguage_option = OptionMenu(root, option1, *languageCode_list)
	ToLanguage_option = OptionMenu(root, option2, *languageCode_list)
	FromLanguage_option.config(font="calibri", bg="light green", activebackground= "orange")
	ToLanguage_option.config(font="calibri", bg="light green", activebackground= "orange")

	FromLanguage_option.grid(row = 1, column = 0, ipadx = 1)
	ToLanguage_option.grid(row = 1, column = 2, ipadx = 1)

	# Create a Convert Button and attached
	# with convert function
	button1 = Button(root, text = "Convert ->", bg = "light green", fg = "dark blue", activebackground = "red", cursor = "exchange", command = convert)
	button1.grid(row = 2, column = 1)

	# Create a Clear Button and attached
	# with clearAll function
	button2 = Button(root, text = "Clear", bg = "yellow", fg = "black", cursor="dotbox",command = clearAll)
	button2.grid(row = 3, column = 1)
	# Start the GUI
	root.mainloop()
