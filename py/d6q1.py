import tkinter as tk

w=tk.Tk()

w.title("Dictionary")

label=tk.Label(w,text="Enter the word you want to find the meaning of: ")
label.grid()

label1=tk.Label(w,text="The word does not exist in the given database")
label1.grid()

def click():
	if label1["text"]=="The word does not exist in the given database":
		label1["text"]="the word exists"
	else:
		label1["text"]="The word does not exist in the given database"

button=tk.Button(w,text="Check word in dict",command=click)

w.mainloop()



