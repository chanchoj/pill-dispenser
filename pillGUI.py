from tkinter import *
from tkinter import ttk
import tkinter.font as font

gui = Tk()
gui.title("Pill Dispenser")
gui.configure(bg='black')
gui.attributes("-zoomed", True)
gui.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20),
                    weight = 1)
gui.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20),
                    weight = 1)

#Page 1
def beginButton():
    lbl_welcome.grid_forget()
    btn_begin.grid_forget()
    lbl_Instructions.grid(row=9, column=9, columnspan=3, sticky="N")
    chk_Sun.grid(row=10, column=7, sticky="E")
    chk_Mon.grid(row=10, column=8, sticky='E')
    chk_Tues.grid(row=10, column=9, sticky="E")
    chk_Wed.grid(row=10, column=10)
    chk_Thur.grid(row=10, column=11, sticky="W")
    chk_Fri.grid(row=10, column=12, sticky="W")
    chk_Sat.grid(row=10, column=13, sticky="W")
    btn_submit.grid(row=11, column=10)
   
 #variable checker  
def printCheck():
    print("Monday: %d\nTuesday: %d\nWednesday: %d\n" %(Monday.get(), Tuesday.get(), Wednesday.get()))
 
#Page 2 
def confirmPage():
    lbl_Instructions.grid_forget()
    chk_Sun.grid_forget()
    chk_Mon.grid_forget()
    chk_Tues.grid_forget()
    chk_Wed.grid_forget()
    chk_Thur.grid_forget()
    chk_Fri.grid_forget()
    chk_Sat.grid_forget()
    btn_submit.grid_forget()
    lbl_selection.grid(row=9, column=10)
    btn_confirm.grid(row=18, column=18)
    btn_reject.grid(row=18, column=17)
    if(Sunday.get() == 1):
        lbl_sun.grid(row=10, column=7, sticky='E')
    if(Monday.get() == 1):
        lbl_mon.grid(row=10, column=8, sticky='E')
    if(Tuesday.get() == 1):
        lbl_tues.grid(row=10, column=9, sticky='E')
    if(Wednesday.get() == 1):
        lbl_wed.grid(row=10, column=10)
    if(Thursday.get() == 1):
        lbl_thur.grid(row=10, column=11, sticky='W')
    if(Friday.get() == 1):
        lbl_fri.grid(row=10, column=12, sticky='W')
    if(Saturday.get() == 1):
        lbl_sat.grid(row=10, column=13, sticky='W')
    

def sendData():
    lbl_text= Label(gui, text="DATA SENT", fg='white', bg='black').grid(row=18, column=10)
    #NEED TO INTEGRATE GPIO PINS WITH TONY

#Returns to page 2
def goBack():
    lbl_sun.grid_forget()
    lbl_mon.grid_forget()
    lbl_tues.grid_forget()
    lbl_wed.grid_forget()
    lbl_thur.grid_forget()
    lbl_fri.grid_forget()
    lbl_sat.grid_forget()
    lbl_selection.grid_forget()
    btn_confirm.grid_forget()
    btn_reject.grid_forget()
    lbl_Instructions.grid(row=9, column=9, columnspan=3, sticky="N")
    chk_Sun.grid(row=10, column=7, sticky="E")
    chk_Mon.grid(row=10, column=8, sticky='E')
    chk_Tues.grid(row=10, column=9, sticky="E")
    chk_Wed.grid(row=10, column=10)
    chk_Thur.grid(row=10, column=11, sticky="W")
    chk_Fri.grid(row=10, column=12, sticky="W")
    chk_Sat.grid(row=10, column=13, sticky="W")
    btn_submit.grid(row=11, column=10)
    
    
#for r in range(20):
#    for c in range(20):
#        lbl_grid = Label(gui, text="R%s/C%s"%(r,c), borderwidth = 1).grid(row=r,column=c)

welcomeFont = font.Font(family='Helvetica', size=60, weight='bold')
instructionsFont = font.Font(family='Helvetica', size=24, weight='bold')
dayFont= font.Font(family='Helvetica', size=16, weight='bold')

lbl_welcome = Label(gui, text="WELCOME", font=welcomeFont, fg = 'white', bg = 'black')
btn_begin = Button(gui, text="Begin",command = beginButton, highlightcolor='blue')

lbl_welcome.grid(row=10, column = 10, sticky ="N")
btn_begin.grid(row=10, column = 10, sticky="S")

#FREQUENCY INSTRUCTIONS
lbl_Instructions = Label(gui, text="Please specify frequency of pills:", font=instructionsFont,
                         fg='white', bg='black')
Monday = IntVar()
Tuesday = IntVar()
Wednesday = IntVar()
Thursday = IntVar()
Friday = IntVar()
Saturday = IntVar()
Sunday = IntVar()

#User selects days of week
chk_Sun = Checkbutton(gui, text="Sunday", variable=Sunday, highlightcolor='blue', width=6)
chk_Mon = Checkbutton(gui, text="Monday", variable=Monday, highlightcolor='blue', width=6)
chk_Tues = Checkbutton(gui, text="Tuesday", variable=Tuesday, highlightcolor='blue', width=7)
chk_Wed = Checkbutton(gui, text="Wednesday", variable=Wednesday, highlightcolor='blue', width=9)
chk_Thur = Checkbutton(gui, text="Thursday", variable=Thursday, highlightcolor='blue', width=8)
chk_Fri = Checkbutton(gui, text="Friday", variable=Friday, highlightcolor='blue', width=6)
chk_Sat = Checkbutton(gui, text="Saturday", variable=Saturday, highlightcolor='blue', width=8)
btn_submit = Button(gui, text="Submit", highlightcolor='blue', command= confirmPage)

lbl_selection = Label(gui, text="You selected:", font=instructionsFont, fg='white', bg='black')
lbl_sun= Label(gui, text="Sunday", font=dayFont, fg='white', bg='black')
lbl_mon= Label(gui, text="Monday", font=dayFont, fg='white', bg='black')
lbl_tues= Label(gui, text="Tuesday", font=dayFont, fg='white', bg='black')
lbl_wed= Label(gui, text="Wednesday", font=dayFont, fg='white', bg='black')
lbl_thur= Label(gui, text="Thursday", font=dayFont, fg='white', bg='black')
lbl_fri= Label(gui, text="Friday", font=dayFont, fg='white', bg='black')
lbl_sat= Label(gui, text="Saturday", font=dayFont, fg='white', bg='black')

btn_confirm = Button(gui, text="Confirm", highlightcolor='blue', fg='white', bg='green', command= sendData)
btn_reject = Button(gui, text="Go Back", highlightcolor='blue', fg='white', bg='red', command= goBack)

gui.mainloop()