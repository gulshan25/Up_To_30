from tkinter import *
from tkinter import font
import datetime


#def quit(*args):
	#window.destroy()
#	window.quit()

def toggle_fullscreen(self, event=None):
        window.state = not self.state  # Just toggling the boolean
        window.attributes("-fullscreen", self.state)
        return "break"
		
def end_fullscreen(self, event=None):
        window.state = False
        window.attributes("-fullscreen", False)
        return "break"
		
def finish(*args):
	global window
	window.destroy()
	
def clock_time():
	time = datetime.datetime.now()
	time= time.strftime("%H:%M:%S")
	txt.set(time)
	
	window.after(1000,clock_time)
	 
window = Tk()
window.title("Welcome")
window.geometry('850x200')
#window.attributes("-fullscreen", False)
#window.attributes('-fullscreen',True)
window.resizable(False, False)
window.configure(background='black')
window.bind("x",finish)
window.bind("<Escape>", finish)


window.after(1000,clock_time)

window.state = False
window.bind("<F10>", toggle_fullscreen)
window.bind("<F11>", end_fullscreen)

fnt = font.Font(family='Helvetica',size=120,weight='bold')
txt= StringVar()

lbl = Label(window, textvariable=txt,font=fnt,foreground='white',background='black')
lbl.place(relx=0.5,rely=0.5,anchor=CENTER)
 
window.mainloop()
