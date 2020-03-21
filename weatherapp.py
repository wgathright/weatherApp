import tkinter as tk

HEIGHT = 400
WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT,width=WIDTH)
canvas.pack()

frame = tk.Frame(root,bg='#80c1ff')
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

button = tk.Button(frame, text="Test Button")
button.place(relx=0,rely=0,relwidth=0.25,relheight=0.15)

label = tk.Label(frame, text="This is a label", bg='yellow')
label.place(relx=0.3,rely=0,relwidth=0.45,relheight=0.15)

entry = tk.Entry(frame, bg='green')
entry.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.15)





root.mainloop()