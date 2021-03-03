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

def beginButton():
    lbl_welcome.grid_forget()
    btn_begin.grid_forget()
    lbl_Instructions.grid(row=9, column=9, columnspan=3, sticky="N")
    chk_Sun.grid(row=10, column=8, sticky="E")
    chk_Mon.grid(row=10, column=9, sticky="W")
    chk_Tues.grid(row=10, column=9, sticky="E")
    chk_Wed.grid(row=10, column=10)
    chk_Thur.grid(row=10, column=11, sticky="W")
    chk_Fri.grid(row=10, column=11, sticky="E")
    chk_Sat.grid(row=10, column=12, sticky="W")
    btn_submit.grid(row=11, column=10)
    
def printCheck():
    print("Monday: %d\nTuesday: %d\nWednesday: %d\n" %(Monday.get(), Tuesday.get(), Wednesday.get()))
    
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
    
    if Sunday==1:
        lbl_sun.grid(row=10,column=10)
    
    
#for r in range(20):
#    for c in range(20):
#        lbl_grid = Label(gui, text="R%s/C%s"%(r,c), borderwidth = 1).grid(row=r,column=c)

welcomeFont = font.Font(family='Helvetica', size=60, weight='bold')
instructionsFont = font.Font(family='Helvetica', size=24, weight='bold')
dayFont= font.Font(family='Helvetica', size=16, weight='bold')

lbl_welcome = Label(gui, text="WELCOME", font=welcomeFont, fg = 'white', bg = 'black')
btn_begin = Button(gui, text="Begin",command = beginButton)

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

chk_Mon = Checkbutton(gui, text="Monday", variable=Monday, highlightcolor='blue', width=6)
chk_Tues = Checkbutton(gui, text="Tuesday", variable=Tuesday, highlightcolor='blue', width=7)
chk_Wed = Checkbutton(gui, text="Wednesday", variable=Wednesday, highlightcolor='blue', width=9)
chk_Thur = Checkbutton(gui, text="Thursday", variable=Thursday, highlightcolor='blue', width=8)
chk_Fri = Checkbutton(gui, text="Friday", variable=Friday, highlightcolor='blue', width=6)
chk_Sat = Checkbutton(gui, text="Saturday", variable=Saturday, highlightcolor='blue', width=8)
chk_Sun = Checkbutton(gui, text="Sunday", variable=Sunday, highlightcolor='blue', width=6)
btn_submit = Button(gui, text="Submit", command= confirmPage)

lbl_selection = Label(gui, text="You selected:", font=instructionsFont, fg='white', bg='black')
lbl_sun= Label(gui, text="Sunday", font=dayFont, fg='white', bg='black')
lbl_mon= Label(gui, text="Monday", font=dayFont, fg='white', bg='black')
lbl_tues= Label(gui, text="Tuesday", font=dayFont, fg='white', bg='black')
lbl_wed= Label(gui, text="Wednesday", font=dayFont, fg='white', bg='black')
lbl_thur= Label(gui, text="Thursday", font=dayFont, fg='white', bg='black')
lbl_fri= Label(gui, text="Friday", font=dayFont, fg='white', bg='black')
lbl_sat= Label(gui, text="Saturday", font=dayFont, fg='white', bg='black')

gui.mainloop()