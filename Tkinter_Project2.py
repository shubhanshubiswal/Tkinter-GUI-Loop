#for loop
import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title('GUI-Loop')

labels=['What is your Name:','What is your Age:','What is your Gender:','Country:','State:','City','Address']



for i in range(len(labels)):
    cur_label='label'+str(i)  #label0,label1
    cur_label=ttk.Label(win,text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W)

#entry box
user_info={
    'name':tk.StringVar(),
    'age':tk.StringVar(),
    'gender':tk.StringVar(),
    'country':tk.StringVar(),
    'state':tk.StringVar(),
    'city':tk.StringVar(),
    'Address':tk.StringVar()
}
counter=0
for i in user_info:
    cur_entrybox='entry'+i   #entryname # entryage
    cur_entry=ttk.Entry(win,width=16,textvariable=user_info[i])
    cur_entry.grid(row=counter,column=1)
    counter +=1

#submit button
def submit():
    l=[]
    for i in user_info:
        l.append(user_info[i].get())

    print(l)

submit_button=tk.Button(win,text='Submit',command=submit)
submit_button.grid(row=7,columnspan=2)

win.mainloop()