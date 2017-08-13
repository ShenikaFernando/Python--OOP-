import tkinter as tk
import webbrowser as wb

def doorbell(event):
	print("You rang the door bell!")

def knockknock(event):
	print("Knock knock who is in here?")

def click_cp(event):
	wb.open_new_tab("https://cleverprogrammer.com")

def pluralsight(event):
	wb.open_new_tab("https://www.pluralsight.com")


window = tk.Tk()
window.geometry("300x200")

alabel = tk.Label(text="Banana") #add 1 st label
alabel.grid(column=0, row=0) #position the 1st label

alabel2= tk.Label(text="Mango")
alabel2.grid(column=1, row=0)

alabel3 = tk.Label(text="PluralSight")
alabel3.grid(column=2, row=0)

button = tk.Button(window, text="Doorbell")
button.grid(column=0, row=1)

button2 = tk.Button(window, text="Knock knock")
button2.grid(column=1, row=1)

button3 = tk.Button(window, text="Visit PluralSight")
button3.grid(column=2, row=1)

button.bind("<Button-1>", doorbell)
button2.bind("<Button-1>", click_cp)
button3.bind("<Button-1>", pluralsight)

window.mainloop()