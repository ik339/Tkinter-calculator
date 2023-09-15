from tkinter import * 
import re
calc = Tk()                      
calc.title('Calculator')
calc.geometry("300x500") 
calc.configure(background = "beige") 
frame =LabelFrame(calc, padx=35, pady=35) 
frame.pack(padx=40, pady=40) 
e = Entry(calc,width=20,fg='darkgreen',font=("calibri"),textvariable=StringVar)
e.pack()
#FUNCTIONS:
def pressclear():
    e.delete(0, END)
def buttonclick(string):
    etext = e.get()              
    new_etext= etext + string
    e.delete(0, END)
    e.insert(0,new_etext)
def Performcalculation():
    etext = e.get()     
    list_etext = re.split(r'(\D)',etext) #separate string to list
    print(list_etext)
    newlist = list_etext [:]  
   #control loop:
    for i in range(0,len(list_etext)-1):
        if list_etext[i].isnumeric() == False:
            print (list_etext[i-1])
            print(list_etext[i])
            print(list_etext[i+1])
            print("---")
   #Reverse BODMAS and calculation loops:
    for i in range(0, len(list_etext)-1): 
        if list_etext[i] == "-":
            exp_result = str(float(list_etext[i-1]) - float(list_etext[i+1])) 
            exp_slice_start = i-1 
            exp_slice_end = i+1 
            newlist = list_etext[:exp_slice_start]+[exp_result]+ list_etext[exp_slice_end+1:] #concatenate, remove slice.
    for i in range(0, len(list_etext)-1): 
        if list_etext[i] == "+":
            exp_result = str(float(list_etext[i-1]) + float(list_etext[i+1]))
            exp_slice_start = i-1 
            exp_slice_end = i+1 
            newlist = list_etext[:exp_slice_start]+[exp_result]+ list_etext[exp_slice_end+1:] 

    for i in range(0, len(newlist)-1):
        if newlist[i] == "*":
            exp_result = str(float(newlist[i-1]) * float(newlist[i+1]))
            exp_slice_start = i-1 
            exp_slice_end = i+1 
            newlist = newlist[:exp_slice_start]+[exp_result]+ newlist[exp_slice_end+1:] 

    for i in range(0, len(newlist)-1):
        if newlist[i] == "/":
            exp_result = str(float(newlist[i-1]) / float(newlist[i+1]))
            exp_slice_start = i-1 
            exp_slice_end = i+1  
            newlist = newlist[:exp_slice_start]+[exp_result]+ newlist[exp_slice_end+1:]
    e.delete(0, END)
    e.insert(0, newlist[0]) 
    
#buttons:
clearbutton = Button(frame,text="C",bg='red',fg='black',padx=10,pady=10, command=pressclear)
clearbutton.grid(row=5,column=2)
Equalsbutton = Button(frame,text="=",command=Performcalculation,bg='orange',fg='black',padx=10,pady=10)
Equalsbutton.grid(row=5,column=3)            
Plusbutton = Button(frame,text="+",bg='grey',fg='white',padx=9,pady=10,command=lambda:buttonclick("+"))
Plusbutton.grid(row=1, column=4) 
Minusbutton = Button(frame,text="-",bg='grey',fg='white',padx=10,pady=10,command=lambda:buttonclick("-"))
Minusbutton.grid(row=2,column=4)
Dividebutton = Button(frame,text="/",bg='grey',fg='white',padx=10,pady=10,command=lambda:buttonclick("/"))
Dividebutton.grid(row=3,column=4)
Multiplybutton = Button(frame, text="*",bg='grey',fg='white',padx=10,pady=10,command=lambda:buttonclick("*"))
Multiplybutton.grid(row=4,column=4)
LBracketbutton = Button(frame,text="(",bg='grey',fg='black',padx=10,pady=10,command=lambda:buttonclick("("))
LBracketbutton.grid(row=4,column=2)
RBracketbutton = Button(frame,text=")",bg='grey',fg='black',padx=10,pady=10,command=lambda:buttonclick(")"))
RBracketbutton.grid(row=4,column=3)
OneButton =Button(frame,text="1",bg='grey',fg='white',padx=10,pady=10,command=lambda:buttonclick("1"))
OneButton.grid(row =1,column=1)                                                
TwoButton = Button(frame,text="2",bg='grey',fg='white',padx=10,pady=10,command=lambda:buttonclick("2"))
TwoButton.grid(row=1,column=2)
threebutton=Button(frame,text="3",bg='grey',fg='white',padx=10,pady=10,command=lambda:buttonclick("3"))
threebutton.grid(row=1,column=3)
fourbutton= Button(frame,text="4",bg='grey',fg='white',padx=10,pady=10,command=lambda:buttonclick("4"))
fourbutton.grid(row=2,column=1)
fivebutton= Button(frame,text="5",bg='grey',fg='white',padx=10,pady=10,command=lambda:buttonclick("5"))
fivebutton.grid(row=2,column=2)
sixbutton = Button(frame,text="6",bg='grey',fg='white',padx=10,pady=10,command=lambda:buttonclick("6"))
sixbutton.grid(row=2,column =3)
sevenbutton=Button(frame,text="7",bg='grey',fg='white',padx=10,pady=10,command=lambda:buttonclick("7"))
sevenbutton.grid(row=3,column=1)
eightbutton=Button(frame,text="8",bg='grey',fg='white',padx=10,pady=10,command=lambda:buttonclick("8"))
eightbutton.grid(row=3,column=2)
ninebutton =Button(frame,text="9",bg='grey',fg='white',padx=10,pady=10,command=lambda:buttonclick("9"))
ninebutton.grid(row=3,column=3)
zerobutton =Button(frame,text="0",bg='grey',fg='white',padx=10,pady=10,command=lambda:buttonclick("0"))
zerobutton.grid(row=4,column=1) #add colspan?
calc.mainloop()
