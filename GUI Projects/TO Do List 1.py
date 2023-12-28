# Let's import the tkinter module to create GUI
import tkinter 

# lets use dir() function To see whats inside the tkinter 
# print(dir(tkinter))
# lets create an empty gui / root gui
root = tkinter.Tk()

# lets define the width and height of gui
root.geometry("400x400")
root.resizable(width = False, height= False)

# lets change the title
root.title('To-Do-List')

# lets ad entry widget
entry = tkinter.Entry(root)
entry.pack()
# lets call the mainloop function
root.mainloop()