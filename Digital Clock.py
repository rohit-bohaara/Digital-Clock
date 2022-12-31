from tkinter import Label, Tk 
import time
app_window = Tk() 
app_window.title("Analog Clock") 
app_window.geometry("1920x1080") 
app_window.resizable(1,1)

text_font= ("Boulder", 300, 'bold', )
background = "#141414"
foreground= "#FCFCFC"
border_width = 30

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def Analog_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, Analog_clock)

Analog_clock()
app_window.mainloop()