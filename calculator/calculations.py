from tkinter import *

class Output:
    #initialize inputfield and history
    def __init__(self, input_Field, history):
        self.input_Field = input_Field
        self.history = history
        self.answer = {}

    #clear field
    def clear(self):
        self.input_Field.set("")
    
    #show the history
    def show_History(self):

        popup = Toplevel()
        popup.title("History")
        popup.geometry("800x600")

        history_text = "\n".join([f"{k}: {v}" for k, v in self.answer.items()])
        history_Label = Label(popup, text= history_text)
        history_Label.pack()

    #add a number/operator
    def add_Number(self, num):
        new_Output = StringVar()
        new_Output.set(f'{self.input_Field.get()}{num}')
        self.input_Field.set(new_Output.get())
    
    #return the answer
    def return_Value(self):
        #try to get the result and store it into answer dict
        try:
            result = eval(self.input_Field.get())
            self.answer[f"{self.input_Field.get()} ({self.history})"] = result
        #if not possible, then give syntax error
        except:
            self.input_Field.set("Syntax Error")
        #set field to answer and increment history
        self.history += 1
        #check if history > 39, if so, clear
        self.input_Field.set(result)
        if (self.history > 39):
            self.answer.clear()
            self.history = 0
        
        