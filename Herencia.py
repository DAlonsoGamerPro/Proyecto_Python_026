from tkinter import *
root = Tk()
root.geometry("600x600")
root.title("Herencia")

label_name = Label(root,text="Nombre del Usuario: ")
label_name.place(relx=0.3,rely=0.2,anchor=CENTER)

entry_name = Entry(root)
entry_name.place(relx=0.6,rely=0.2,anchor=CENTER)

label_email = Label(root,text="Correo Electrónico: ")
label_email.place(relx=0.3,rely=0.3,anchor=CENTER)

entry_email = Entry(root)
entry_email.place(relx=0.6,rely=0.3,anchor=CENTER)

btn = Button(root,text="Agregar detalles del Usuario")
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

root.mainloop()