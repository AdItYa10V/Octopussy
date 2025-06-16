from tkinter import * 

root=Tk()

op=StringVar(root)
name=StringVar()
# l=Label(root, text="Select One")
# l.grid(row=1,column=1)
root.minsize(400,400)
# opp=OptionMenu(root, op, 'Insurance', 'Cash', 'Fixed Deposit', 'Credit Card', 'Debit Card')
# opp.grid(row=1,column=2)
n=Entry(textvariable=name)
n.pack()
root.mainloop()
# with open('data.txt', 'w') as d11:
