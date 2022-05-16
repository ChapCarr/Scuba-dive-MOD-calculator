
import tkinter as tk

def oxygenToMod():
    feetEntry.delete(1.0, "end")
    oxygen = float(oxygenEntry.get())
    mod = (1.4 / (oxygen/ 100) - 1) * 33
    feetEntry.insert(1.0 , f"Your Max Operating Depth with {oxygen}% O2 is {int(mod)} feet at a PpO2 of 1.4ata")

bgColor = "#040405"
fgColor = "#2596be"
entryWidith = 32
entryHeight = 5

root = tk.Tk()
root.geometry("450x250")
root.title("Max Operating Depth Calculator")
root.configure(bg=bgColor)

titleScreen = tk.Label(root, text="Calculate Your Max Operating Depth:", font=("arial", 16), fg=fgColor, bg=bgColor)
titleDirection = tk.Label(root,font=("arial", 10),text="Enter your oxygen percentage as a whole number in the box below Ex: 32% will be entered as 32", fg=fgColor, bg=bgColor)
oxygenEntry = tk.Entry(root, width=entryWidith, font=("arial", 16), highlightbackground=fgColor)
feetEntry = tk.Text(root,width=42, height=entryHeight,wrap="word",font=("arial", 16),highlightbackground=bgColor)
calcButton = tk.Button(root,text="Calculate MOD", command=oxygenToMod, font=('arial', 24),highlightbackground=bgColor)

titleScreen.pack()
titleDirection.pack()
oxygenEntry.pack()
feetEntry.pack()
calcButton.pack()


root.mainloop()