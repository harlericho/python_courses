from tkinter import *
root = Tk()

def send():
    send = "You: " + e.get()
    text.insert(END,"\n" +send)
    if (e.get() == "hola"):
        text.insert(END,"\n" +"Bot: Hola")
    elif (e.get() == "como estas?"):
        text.insert(END,"\n" +"Bot: yo muy bien y tu?")
    elif (e.get() == "estoy muy bien"):
        text.insert(END,"\n" +"Bot: me alegro ver que estas bien")
    elif (e.get() == "de donde eres?"):
        text.insert(END,"\n" +"Bot: soy de cualquier parte del mundo")
    else:
        text.insert(END,"\n" +"Bot: no te entiendo tu idioma")  
text = Text(root, bg="white", fg="black", font="lucida 13")
text.grid(row=0, column=0, columnspan=3)
e = Entry(root, bg="white", fg="black", font="lucida 13", width=50)
e.focus()
send = Button(root, text="send", command=send, width=40,bg="gray").grid(row=1, column=2)
e.grid(row=1, column=0, columnspan=2)
root.title("Chatbot")
root.mainloop()