import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk
import calculations

class Calculate:
    def __init__(self):
        self.win = tk.Tk()
    #customize window
    def window(self):
        self.win.title("Calculator")
        self.win.geometry("380x468")
        self.win.resizable(False, False)
    #just the input and output labels
    def screen(self):
        #setting screen variables
        input_Field = tk.StringVar()
        input_Field.set(" ")

        self.output = calculations.Output(input_Field, 0, self.buttondic)

        #screen
        screen_Frame = ttk.Frame()

        #set font
        label_font = font.Font(family='Helvetica', size=28)

        #initialize input_Label and customize
        input_Label = tk.Label(screen_Frame, textvariable=input_Field, font=label_font, width=17, height=2)
        input_Label.grid(row=0, column=0)
        input_Label.config(anchor='center')

        screen_Frame.place(y=30)

    #Buttons
    def button_Make(self):

        self.buttondic = {}
        button_Frame = ttk.Frame(self.win)

        clear_Button = tk.Button(button_Frame, text="CLEAR", height=5, width=10, borderwidth=0, background="red",
                            command=lambda: self.output.clear())
        show_History = tk.Button(button_Frame, text="HISTORY", height=5, width=10, borderwidth=0, background="lightgrey",
                            command=lambda: self.output.show_History())
        #number buttons
        for i in range(1, 10):
            butt = tk.Button(button_Frame, text=f"{i}", height=5, width=10, borderwidth=0, background="grey",
                            command=lambda idx = i: self.output.add_Number(idx))
            self.buttondic[i] = butt  

        #0 is a special exception for positional reasons
        number_0 = tk.Button(button_Frame, text="0", height=5, width=10, borderwidth=0, background="grey", 
                    command=lambda: self.output.add_Number(10))
        self.buttondic[10] = number_0
    
        #place the buttons on the grid according to their index in the button dictionary value arrays
        for i, buttons in enumerate(self.buttondic.values()):
            buttons.grid(row=(i//3)+1, column = (i%3)+1)
            
        #operations
        plus_Button = tk.Button(button_Frame, text="+", height=5, width=10, borderwidth=0, background="lightgrey", 
                    command=lambda: self.output.add_Number("+"))
        minus_Button = tk.Button(button_Frame, text="-", height=5, width=10, borderwidth=0, background="lightgrey", 
                    command=lambda: self.output.add_Number("-"))
        mult_Button = tk.Button(button_Frame, text="*", height=5, width=10, borderwidth=0, background="lightgrey", 
                    command=lambda: self.output.add_Number("*"))
        div_Button = tk.Button(button_Frame, text="/", height=5, width=10, borderwidth=0, background="lightgrey", 
                    command=lambda: self.output.add_Number("/"))
        
        #enter
        enter = tk.Button(button_Frame, text="ENTER", height=5, width=10, borderwidth=0, background="lightcoral", 
                        command=lambda: self.output.return_Value())

        #place everything on the window
        button_Frame.place(x=0, y=140)

        #make every button appear on the frame
        number_0.grid(row=4, column=2)
        clear_Button.grid(row=1, column=0)
        show_History.grid(row=2, column=0)
        plus_Button.grid(row=1, column=4)
        minus_Button.grid(row=2, column=4)
        mult_Button.grid(row=3, column=4)
        div_Button.grid(row=4, column=4)
        enter.grid(row=4, column=3)

#combine all the pieces into everything
def everything():
    calc = Calculate()
    calc.window()
    calc.button_Make()
    calc.screen()
    calc.win.mainloop()




        