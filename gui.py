
import tkinter as tk
from tkinter import filedialog
import os
from tkinter import *



def gu(self):


    # application_window = tk.Tk()
    window = Tk()
    window.title("Welcome to  app")
    window.geometry('350x200')
    lbl = Label(window, text=self)
    lbl.grid(column=0, row=0)
    window.mainloop()

#
# # Build a list of tuples for each file type the file dialog should display
#     my_filetypes = [('all files', '.*'), ('text files', '.wav')]

# Ask the user to select a folder.
# answer = filedialog.askdirectory(parent=application_window,
#                                  initialdir=os.getcwd(),
#                                  title="Please select a folder:")

# Ask the user to select a single file name.
#     answer = filedialog.askopenfilename(parent=application_window,
#                                     initialdir=os.getcwd(),
#                                     title="Please select a file:",
#                                     filetypes=my_filetypes)
#     print (answer)
#     return answer

#
#
# # Build a list of tuples for each file type the file dialog should display
# my_filetypes = [('all files', '.*'), ('text files', '.wav')]
#
# # Ask the user to select a folder.
# # answer = filedialog.askdirectory(parent=application_window,
# #                                  initialdir=os.getcwd(),
# #                                  title="Please select a folder:")
#
# # Ask the user to select a single file name.
# answer = filedialog.askopenfilename(parent=application_window,
#                                     initialdir=os.getcwd(),
#                                     title="Please select a file:",
#                                     filetypes=my_filetypes)
# print (answer)

# import tkinter as tk
# from tkinter import simpledialog
#
# application_window = tk.Tk()
#
# answer = simpledialog.askstring("Input", "What is your first name?",
#                                 parent=application_window)
# if answer is not None:
#     print("Your first name is ", answer)
# else:
#     print("You don't have a first name?")
#
# answer = simpledialog.askinteger("Input", "What is your age?",
#                                  parent=application_window,
#                                  minvalue=0, maxvalue=100)
# if answer is not None:
#     print("Your age is ", answer)
# else:
#     print("You don't have an age?")
#
# answer = simpledialog.askfloat("Input", "What is your salary?",
#                                parent=application_window,
#                                minvalue=0.0, maxvalue=100000.0)
# if answer is not None:
#     print("Your salary is ", answer)
# else:
#     print("You don't have a salary?")


if __name__ == '__main__':
    gu()
