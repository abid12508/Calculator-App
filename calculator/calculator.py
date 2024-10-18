import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk
import calculations

class Calculate:
    #create and customize window
    def window(self):
        global win
        win = tk.Tk()
        win.title("Calculator")
        win.geometry("380x468")
        win.resizable(False, False)
    #just the input and output labels
    def screen(self):
        #setting screen variables
        input_Field = tk.StringVar()
        input_Field.set("")

        self.output = calculations.Output(input_Field, 0)

        #screen
        screen_Frame = ttk.Frame()

        #set font
        label_font = font.Font(family='Helvetica', size=30)

        #initialize input_Label and customize
        input_Label = tk.Label(screen_Frame, textvariable=input_Field, font=label_font, width=17, borderwidth=2, relief="solid")
        input_Label.grid(row=0, column=0)
        input_Label.config(anchor='center')

        screen_Frame.place(y=30)

    #Buttons
    def button_Make(self):
        button_Frame = ttk.Frame()

        clear_Button = tk.Button(button_Frame, text="CLEAR", height=5, width=10, borderwidth=0, background="red",
                            command=lambda: self.output.clear())
        show_History = tk.Button(button_Frame, text="HISTORY", height=5, width=10, borderwidth=0, background="lightgrey",
                            command=lambda: self.output.show_History())
        #number buttons
        number_1 = tk.Button(button_Frame, text="1", height=5, width=10, borderwidth=0, background="grey",
                            command=lambda: self.output.add_Number("1"))
        number_2 = tk.Button(button_Frame, text="2", height=5, width=10, borderwidth=0, background="grey",
                            command=lambda: self.output.add_Number("2")) 
        number_3 = tk.Button(button_Frame, text="3", height=5, width=10, borderwidth=0, background="grey",
                            command=lambda: self.output.add_Number("3")) 
        number_4 = tk.Button(button_Frame, text="4", height=5, width=10, borderwidth=0, background="grey",
                            command=lambda: self.output.add_Number("4")) 
        number_5 = tk.Button(button_Frame, text="5", height=5, width=10, borderwidth=0, background="grey",
                            command=lambda: self.output.add_Number("5")) 
        number_6 = tk.Button(button_Frame, text="6", height=5, width=10, borderwidth=0, background="grey",
                            command=lambda: self.output.add_Number("6"))
        number_7 = tk.Button(button_Frame, text="7", height=5, width=10, borderwidth=0, background="grey",
                            command=lambda: self.output.add_Number("7"))
        number_8 = tk.Button(button_Frame, text="8", height=5, width=10, borderwidth=0, background="grey",
                            command=lambda: self.output.add_Number("8"))   
        number_9 = tk.Button(button_Frame, text="9", height=5, width=10, borderwidth=0, background="grey", 
                            command=lambda: self.output.add_Number("9"))
        number_0 = tk.Button(button_Frame, text="0", height=5, width=10, borderwidth=0, background="grey", 
                            command=lambda: self.output.add_Number("0"))
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

        clear_Button.grid(row=1, column=0)
        show_History.grid(row=2, column=0)
        number_1.grid(row=1, column=1)
        number_2.grid(row=1, column=2)
        number_3.grid(row=1, column=3)
        number_4.grid(row=2, column=1)
        number_5.grid(row=2, column=2)
        number_6.grid(row=2, column=3)
        number_7.grid(row=3, column=1)
        number_8.grid(row=3, column=2)
        number_9.grid(row=3, column=3)
        number_0.grid(row=4, column=2)
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
    win.mainloop()




        