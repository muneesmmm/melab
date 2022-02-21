from tkinter import *

import cx_Oracle


def OraCon(user):
 try:
   connection = cx_Oracle.connect(user)
   return connection
 except cx_Oracle.Error as error:
  print('Error on connection')
  print(error)
  return connection


def Kill(can):
 can.destroy()


# --------------------------------- Rec Comm Functions ----------------------------------------
def Screen_Mstcom():
 return


# --------------------------------- Rec Unt Functions ----------------------------------------
def Screen_Mstunt():
 return


# --------------------------------- Rec Patient Functions ----------------------------------------
def Screen_Mstpat():
 return


# --------------------------------- Rec Master Functions ----------------------------------------
def Screen_Mstrec():
 return


# --------------------------------- Rty Master Functions ----------------------------------------
def Rty_Key(event):
 Tp = '.'
 Prm = '.'
 Unt = '.'
 Pri = '.'
 try:
  if event.keysym == 'Return':
   if event.widget.extra == 'Code':
    cur = con.cursor()
    res = cur.callfunc('GET_ANMSTMCH', cx_Oracle.STRING,(machine.get(), Tp, Prm))
    cur.close()
    machname.delete(0, "end")
    machname.insert(0, res)
    if res == '*not found':
     return
   elif event.widget.extra == 'Type':
    cur = con.cursor()
    res = cur.callfunc('GET_ANMSTRTY', cx_Oracle.STRING, (machine.get(), rstype.get()))
    cur.close()
    rsdesc.delete(0, "end")
    analpar.delete(0, "end")
    pardesc.delete(0, "end")
    unit.delete(0, "end")
    priority.delete(0, "end")
    if res != '*not found':
     rsdesc.insert(0, res)
   elif event.widget.extra == 'Parm':
    cur = con.cursor()
    res = cur.callfunc('GET_ANRSLDEF', cx_Oracle.STRING,(machine.get(), rstype.get(), analparm.get(), Unt, Pri, 0))
    cur.close()
    pardesc.delete(0, "end")
    unit.delete(0, "end")
    priority.delete(0, "end")
    if res != '*not found':
     pardesc.insert(0, res)
    unit.insert(0, Unt)
    priority.insert(0, Pri)
    event.widget.tk_focusNext().focus()
    return ("break")
   else:
    print('In Mch')
 except:
   print('No extra')
   print(v1)
   event.widget.tk_focusNext().focus()
   return ("break")


def insert_RTY(wmach, wctype, wdesc, wparm, wpdesc, wunit, wprior):
 # construct an insert statement to add a new row
 try:
 # create a cursor
  cur = con.cursor()
  res = cur.callfunc('WRITE_RESDEF', cx_Oracle.NUMBER,(wmach, wctype, wdesc, wparm, wpdesc, wunit, wprior))
  cur.close
  analpar.delete(0, "end")
  pardesc.delete(0, "end")
  unit.delete(0, "end")
  priority.delete(0, "end")
  analpar.focus_set()
 except cx_Oracle.Error as error:
  print('insert error:')
  print(error)


def Screen_Mstrty():
 canvas = Canvas(root, width=600, height=600)
 root.unbind("<KeyRelease>")
 root.bind("<KeyRelease>", Rty_Key)
 canvas.pack()
 # this creates 'Label' widget for Form and uses place() method.
 label_0 = Label(canvas, text="Result Type Definition", width=20, font=("bold", 20))
 # place method in tkinter is geometry manager it is used to organize widgets by placing them in specific position
 label_0.place(x=90, y=60)
 # this creates 'Label' widget for name and uses place() method.
 label_1 = Label(canvas, text="Code", width=20, font=("bold", 10))
 label_1.place(x=40, y=130)
 # this will accept the input string text from the user.
 global machine
 machine = Entry(canvas, width=5)
 machine.place(x=180, y=130)
 machine.extra = "Code"
 # show the desc of machine
 global machname
 machname = Entry(canvas, width=40, state=DISABLED)
 machname.place(x=250, y=130)
 # this creates 'Label' widget for Type and uses place() method.
 label_2 = Label(canvas, text="Type", width=20, font=("bold", 10))
 label_2.place(x=40, y=160)
 global rstype
 rstype = Entry(canvas, width=6)
 rstype.place(x=180, y=160)
 rstype.extra = "Type"
 # this creates 'Label' widget for Type and uses place() method.
 label_3 = Label(canvas, text="Type Desc.", width=20, font=("bold", 10))
 label_3.place(x=40, y=190)
 global rsdes
 rsdes = Entry(canvas, width=58)
 rsdes.place(x=180, y=190)
 rsdes.extra = "Desc"
 label_4 = Label(canvas, text="Parameter.", width=20, font=("bold", 10))
 label_4.place(x=40, y=220)
 global analpar
 analpar = Entry(canvas, width=10)
 analpar.place(x=180, y=220)
 analpar.extra = "Parm"
 label_5 = Label(canvas, text="Par. Desc.", width=20, font=("bold", 10))
 label_5.place(x=40, y=250)
 global pardesc
 pardesc = Entry(canvas, width=58)
 pardesc.place(x=180, y=250)
 pardesc.extra = "Pdes"
 label_6 = Label(canvas, text="Unit.", width=20, font=("bold", 10))
 label_6.place(x=40, y=280)
 global unit
 unit = Entry(canvas, width=4)
 unit.place(x=180, y=280)
 unit.extra = "Unit"
 label_7 = Label(canvas, text="Priority.", width=20, font=("bold", 10))
 label_7.place(x=40, y=310)
 global priority
 priority = Entry(canvas, width=3)
 priority.place(x=180, y=310)
 priority.extra = "Prio"
 # this creates button for submitting the details provides by the user
 Button(canvas, text='Save', width=20, bg="black", fg='white', command=lambda: \
 \
  insert_RTY(machine.get(), rstype.get(), rsdes.get(), analpar.get(), pardesc.get(), unit.get(
  ), priority.get())).place(x=180, y=380)
 Button(canvas, text='Exit', width=20, bg="black", fg='white', command=lambda:
 Kill(canvas)).place(x=300, y=380)
 machine.focus_set()


# ---------------------------Mahine master functions--------------------------------------
def Mch_Key(event):
 try:
  global comm
  if event.keysym == 'Return':
   if event.widget.extra == 'Code':
    cur = con.cursor()
    Tp = cur.var(str)
    Prm = cur.var(str)
    Tp.setvalue(0, '')
    Prm.setvalue(0, '')
    res = cur.callfunc('GET_ANMSTMCH', cx_Oracle.STRING,(entry_1.get(), Tp, Prm));
    cur.close()
    entry_2.delete(0, "end")
    entry_4.delete(0, "end")
    if res != '*not found':
     entry_2.insert(0, res)
  entry_4.insert(0, Prm.getvalue(0))
  if Tp.getvalue() == ('TCP'):
   print(Tp.getvalue() + 'TCP')
   comm.set(1)
  else:
   print(Tp.getvalue() + 'RS')
   comm.set(2)
   event.widget.tk_focusNext().focus()
   return ("break")
 except Exception as e:
   print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
   print('No extra')

def insert_Machine(wmach, wdesc, wctype, wparm):
  if wctype == 1:
   Cmt = 'TCP'
  else:
   Cmt = '232'

  # construct an insert statement to add a new row
  try:
  # create a cursor
   cur = con.cursor()
   res = cur.callfunc('WRITE_MSTMCH', cx_Oracle.STRING,(wmach, wdesc, Cmt, wparm))
   cur.close
   entry_1.delete(0, "end")
   entry_2.delete(0, "end")
   entry_4.delete(0, "end")
   comm.set(0)
   entry_1.focus_set()
  except cx_Oracle.Error as error:
   print('insert error:')
   print(error)

def Screen_Mstmch():
 canvas = Canvas(root, width=600, height=600)
 root.unbind("<KeyRelease>")
 root.bind("<KeyRelease>", Mch_Key)
 canvas.pack()
 # this creates 'Label' widget for Machine Form and uses place() method.
 label_0 = Label(canvas, text="Machine form", width=20, font=("bold", 20))
 # place method in tkinter is geometry manager it is used to organize widgets byplacingthem in specific position
 label_0.place(x=90, y=60)
 # this creates 'Label' widget for Fullname and uses place() method.
 label_1 = Label(canvas, text="Code", width=20, font=("bold", 10))
 label_1.place(x=80, y=130)
 # this will accept the input string text from the user.
 global entry_1
 entry_1 = Entry(canvas, width=8)
 entry_1.place(x=230, y=130)
 entry_1.extra = "Code"
 # this creates 'Label' widget for Email and uses place() method.
 label_2 = Label(canvas, text="Name", width=20, font=("bold", 10))
 label_2.place(x=80, y=180)
 global entry_2
 entry_2 = Entry(canvas, width=55)
 entry_2.place(x=230, y=180)
 entry_2.extra = "Name"
 # this creates 'Label' widget for Gender and uses place() method.
 label_3 = Label(canvas, text="Comm.Type", width=20, font=("bold", 10))
 label_3.place(x=70, y=230)
 # the variable 'var' mentioned here holds Integer Value, by deault 0
 global comm
 comm = IntVar(root)
 # this creates 'Radio button' widget and uses place() method
 Radiobutton(canvas, text="TCP/IP", padx=40, variable=comm,
             value=1).place(x=200, y=230)
 Radiobutton(canvas, text="RS232", padx=20, variable=comm,
             value=2).place(x=310, y=230)
 label_4 = Label(canvas, text="Comm.Param", width=20, font=("bold", 10))
 label_4.place(x=68, y=280)
 global entry_4
 entry_4 = Entry(canvas, width=58)
 entry_4.place(x=230, y=280)
 entry_4.extra = "Parm"
 # this creates button for submitting the details provided by the user
 Button(canvas, text='Submit', width=20, bg="black", fg='white', command=lambda:
 insert_Machine(entry_1.get(), entry_2.get(), comm.get(),
                entry_4.get())).place(x=180, y=380)
 Button(canvas, text='Exit', width=20, bg="black", fg='white', command=lambda:
 Kill(canvas)).place(x=300, y=380)
 entry_1.focus_set()


# -----------------End of machine master--------------------------------------------------------

# Creating object 'root' of Tk()
root = Tk()
con = OraCon('medlar/123458@localhost');
canvas = Canvas(root, width=500, height=600)
canvas.pack()
canvas.destroy()
#Providing Geometry to the form
root.geometry("1000x500")
#Providing title to the form
root.title('Medical Lab Analysis Capture')
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Machine master',command=Screen_Mstmch)
filemenu.add_command(label='Result Type and Parameters',command=Screen_Mstrty);
filemenu.add_command(label='Packet Slcing Details',command=Screen_Mstrec);
filemenu.add_command(label='Unit Master maintenance',command=Screen_Mstunt);
filemenu.add_command(label='Com. Type Mastermaintenance',command=Screen_Mstcom);
filemenu.add_command(label='Patient ID Master maintenance',command=Screen_Mstpat);
#filemenu.add_separator()
Exitmenu = Menu(menu)
menu.add_cascade(label='Exit', menu=Exitmenu);
Exitmenu.add_command(label='Exit', command=root.quit);
con = OraCon('medlar/123458@localhost');
root.mainloop()