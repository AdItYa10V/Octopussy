# I'm Lactose Enjoyer, creater of this program. I've included notes for convenience.
# NOTICE - There is a minor issue with the program - the window opening command opens 2 windows if 2 is clicked, not just the 2, 1 AND 2. For more context go to line 27.

import tkinter as tkkll # this module id the GUI tool - creates the application window
from tkcalendar import DateEntry # to make the manual date entry easier
from tktimepicker import AnalogPicker, constants # to make time picking easier, though automatic would be killer. Both date and time.
import mysql.connector as oo # connects the program to the MySQL database

con=oo.connect(host='localhost', user='root', password='Aditya12sadwert12345%', database="hospital_management") # created the connection
cu=con.cursor() # cursor object lets us execute SQL queries from python
def saveData1(): # function to take entered data in the app, put it in its designated table and commit(save).
    cu.execute("insert into patients(P_ID,FN,LN,admnDate,familyContact) values(%s,%s,%s,%s,%s)",(iDd.get(),fn.get(),ln.get(),c.get(),contt.get()))
    cu.execute("commit") # this saves the data in the MySQL database. The "%s" in the command above is to provide a placeholder for data that doens't exist yet, so that when it is entered, we can use the get() method to fetch it and feed it here :)

def saveData2(): # 4 windows, 4 functions, so that distinction can be maintained. All this could've been done in 1 function, but for ease of understanding, I did it in 4. Maybe I'll do that in the future.
    cu.execute("insert into payment(P_ID,paymentType,Amount) values(%s,%s,%s)",(iDd.get(),pTt.get(),Am.get())) 
    cu.execute("commit") 

def saveData3(): 
    cu.execute("insert into medicalHistory(P_ID,Name,medications,treatment) values(%s,%s,%s,%s)",(iDd.get(),n.get(),med.get(), Tr.get())) 
    cu.execute("commit") 

def saveData4(): 
    cu.execute("insert into appointments(P_ID,dateA,timeA,doctor,status) values(%s,%s,%s,%s,%s)",(iDd.get(),c.get(),tttt.get(),docc.get(),stt.get())) 
    cu.execute("commit") 

print("In which table do you want to add data? \n 1 for 'Patient data'\n 2 for 'Payment'\n 3 for 'Medical History'\n 4 for 'Appointments'")
a = int(input("Enter Choice: ")) # this lets you select which table you wanna enter data into. BUT, there's an issue, if you enter 1, "Patient Data" gets opened. If you enter 2, "Payment" AND "Patient Data" get opened, not just "Payment". Similarly, entering 4 will open ALL 4 windows, not just 4.

w1=tkkll.Tk() # this creates the 1st window
w1.minsize(500,500) # sets the minimum size of the window

iDd=tkkll.IntVar() # IntVar() method stores a value until the get() method is used to fetch it. Look at the savedata functions above for context 
iddd=tkkll.Label(w1,text="P_ID") # this creates the Label for above the Entry space(heading of sorts)
iDd=tkkll.Entry(w1) # this is the place where the value is entered
iddd.pack() # pack function takes the object and places it in the window. CAUTION: THE PACK ORDER MATTERS.
iDd.pack() 

w1.title("Patients' Data Entry") 
fn=tkkll.StringVar() # similar to IntVar, StringVar holds a string instead of an integer.
fnn=tkkll.Label(w1,text="First Name") 
fn=tkkll.Entry(w1) 
fnn.pack() 
fn.pack() 

ln=tkkll.StringVar() 
lnn=tkkll.Label(w1,text="Last Name") 
ln=tkkll.Entry(w1) 
lnn.pack() 
ln.pack() 

d=tkkll.StringVar() 
ddd=tkkll.Label(w1,text="Date") 
ddd.pack() 

c=DateEntry(w1, date_pattern="yyyy/mm/dd") # this is the DateEntry widget that gives the simple window a little bit of pizazz, although I'd prefer this selection to be automatic based on the system date and time.
c.pack() 

contt=tkkll.StringVar() 
conttt=tkkll.Label(w1,text="Last Name") 
contt=tkkll.Entry(w1) 
conttt.pack() 
contt.pack()  

buton = tkkll.Button(w1, text="Confirm", command=saveData1) # this programs the onscreen button to call the already defined saveData function for the first window.There will be 3 more.
buton.pack() 

def dateSS(): 
    l1=tkkll.Label 
    dddd=c.get_date() # the get method for date looks different because it's its own datatype.
    ddddlabel=tkkll.Label(w1,text="Date: {dddd}") 

if a==1: 
    w1.mainloop() # this is the thing that should've done the tric for calling the individual windows. Dunno why it didn't work though.
else: 
    pass 

w2=tkkll.Tk() 
w2.minsize(500,500) 
w2.title("Payment Data Entry") # similarly, all the rest of the app windows are made.

iDd=tkkll.IntVar() 
iddd=tkkll.Label(w2,text="P_ID") 
iDd=tkkll.Entry(w2) 
iddd.pack() 
iDd.pack() 

pTt=tkkll.StringVar() 
options=['Insurance', 'Fixed deposit', 'Cash','Credit Card','Debit Card', 'Net banking'] 
pT=tkkll.OptionMenu(w2,pTt,*options) 
pT.pack() 

Am=tkkll.IntVar() 
Amm=tkkll.Label(w2,text="Amount:") 
Am=tkkll.Entry(w2) 
Amm.pack() 
Am.pack() 

buton = tkkll.Button(w2, text="Confirm", command=saveData2) 
buton.pack() 

if a==2: 
    w2.mainloop() 
else: 
    pass 

w3=tkkll.Tk() 
w3.minsize(500,500) 
w3.title("Medical History Data Entry") 
iDd=tkkll.IntVar() 
iddd=tkkll.Label(w3,text="P_ID") 
iDd=tkkll.Entry(w3) 
iddd.pack() 
iDd.pack() 
n=tkkll.StringVar() 
nn=tkkll.Label(w3,text="Name") 
n=tkkll.Entry(w3) 
nn.pack() 
n.pack()

med=tkkll.StringVar() 
medd=tkkll.Label(w3,text="Medications") 
med=tkkll.Entry(w3) 
medd.pack() 
med.pack() 

Tr=tkkll.StringVar() 
trr=tkkll.Label(w3,text="Treatments") 
Tr=tkkll.Entry(w3) 
trr.pack() 
Tr.pack() 

buton = tkkll.Button(w3, text="Confirm", command=saveData3) 
buton.pack() 

if a==3: 
    w3.mainloop() 
else: 
    pass 

w4=tkkll.Tk()  
w4.minsize(500,500)
iDd=tkkll.IntVar() 
iddd=tkkll.Label(w4,text="P_ID") 
iDd=tkkll.Entry(w4) 
iddd.pack() 
iDd.pack() 
c=DateEntry(w4, date_pattern="yyyy/mm/dd") 
c.pack() 

tttt=tkkll.StringVar() 
ttt=AnalogPicker(w4, type=constants.HOURS24) 
ttt.pack() 

 
docc=tkkll.StringVar() 
dc=tkkll.Label(w4,text="Doctor's name") 
docc=tkkll.Entry(w4) 
dc.pack() 
docc.pack() 

stt=tkkll.StringVar() 
st=tkkll.Label(w4,text="Status") 
stt=tkkll.Entry(w4) 
st.pack() 
stt.pack() 
buton = tkkll.Button(w4, text="Confirm", command=saveData4) 
buton.pack() 

if a==4: 
    w4.mainloop() 
else: 
    pass 