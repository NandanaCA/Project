import socket
import threading


hostname=socket.gethostname()
local_ip=socket.gethostbyname(hostname)
print(hostname,local_ip)
port=1234

ip_address='127.0.0.1'


from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk,Image
from tkinter import ttk

root_window=Tk()
root_window.withdraw()

enter_button=PhotoImage(file='C:/Users/nanda/OneDrive/Desktop/COMPUTER_PROJECT/ICONS/enter100_32.png')
login_button=PhotoImage(file='C:/Users/nanda/OneDrive/Desktop/COMPUTER_PROJECT/ICONS/login150_48.png')
search_button=PhotoImage(file='C:/Users/nanda/OneDrive/Desktop/COMPUTER_PROJECT/ICONS/search100_32.png')
history_button=PhotoImage(file='C:/Users/nanda/OneDrive/Desktop/COMPUTER_PROJECT/ICONS/history100_32.png')
    


def send_message(choice,text=''):
    text=choice+';'+text
    print(text)
    client.sendall(text.encode())
                    
def listen1():
    while True:
        message=client.recv(2048).decode('utf-8')
        choice=message[0]
        print(choice,'choice')
        
        if choice=='1':
            split_message=message.split('?')
            username=split_message[0][1:]
            content=split_message[1]
            date=split_message[2]
##            label=Label(mwframe2,text=content,font=('Britannic Bold','26','bold'))
##            label.pack()
            screen.insert('','end',text=1,values=(username,content,date))
            print(date,' ',username,':',content)
            
        elif choice=='2':
            main_window=Toplevel()
            main_window.title("chat")
            main_window.geometry("400x600")

            main_nb=ttk.Notebook(main_window)
            main_nb.pack(fill=BOTH,expand=1)

            chat_frame=Frame(main_nb)

            main_nb.add(chat_frame,text="chat room")

            chat_frame1=Frame(chat_frame,background='#083447')
            chat_frame1.pack(fill=X)

            Label(chat_frame1,text="",background='#083447').pack()
            Label(chat_frame1,text="",background='#083447').pack()

            style=ttk.Style()

            style.configure("Treeview.Heading",foreground='#083447',font=("Consolas", 10,"bold"))
            style.configure("Treeview",rowheight=25,background="#D3D3D3",foreground="black",fieldbackground="#D3D3D3",font=("Times", 8))

            style.map('Treeview',background=[('selected','#083447')])


            chat_frame2=LabelFrame(chat_frame)
            chat_frame2.pack(fill='both',expand='yes')
            chat_frame3=Frame(chat_frame2)
            chat_frame3.pack(fill=BOTH,expand='yes')

            chat_scrollbar=Scrollbar(chat_frame3)
            chat_scrollbar.pack(side=RIGHT,fill=Y)


            screen2=ttk.Treeview(chat_frame3,yscrollcommand=chat_scrollbar.set)
            screen2.pack(fill=BOTH,expand=YES)

            chat_scrollbar.config(command=screen2.yview)

            screen2['columns']=("Participants","message","time")
            screen2.column("#0",width=0)
            screen2.column("Participants",anchor=W,width=150,minwidth=150)
            screen2.column("message",anchor=W,width=150,minwidth=150)
            screen2.column("time",anchor=W,width=150,minwidth=150)



            screen2.heading("#0",text="",anchor=W)
            screen2.heading("Participants",text="PARTICIPANTS",anchor=W)
            screen2.heading("message",text="MESSAGE",anchor=W)
            screen2.heading("time",text="TIME",anchor=W)



            screen2.tag_configure('oddrow',background="white")
            screen2.tag_configure('evenrow',background="#99bccf")

            screen2.insert(parent='',index='end',iid=0,text="",values=(""),tags=('evenrow',))

            chat_frame4=LabelFrame(chat_frame,foreground='#083447')
            chat_frame4.pack(fill="x")


            footer_frame=Frame(main_window,background='#083447')
            footer_frame.pack(fill=X)
            Label(footer_frame,text="",background='#083447').pack()



            message=message[1:]
            history=eval(message)
            for i in history:
                print(i)
                screen2.insert('','end',text=1,values=(i[1],i[2],i[3]))
                
        elif choice=='3':
            main_window=Toplevel()
            main_window.title("chat")
            main_window.geometry("400x600")

            main_nb=ttk.Notebook(main_window)
            main_nb.pack(fill=BOTH,expand=1)

            chat_frame=Frame(main_nb)

            main_nb.add(chat_frame,text="chat room")

            chat_frame1=Frame(chat_frame,background='#083447')
            chat_frame1.pack(fill=X)

            Label(chat_frame1,text="",background='#083447').pack()
            Label(chat_frame1,text="",background='#083447').pack()

            style=ttk.Style()

            style.configure("Treeview.Heading",foreground='#083447',font=("Consolas", 10,"bold"))
            style.configure("Treeview",rowheight=25,background="#D3D3D3",foreground="black",fieldbackground="#D3D3D3",font=("Times", 8))

            style.map('Treeview',background=[('selected','#083447')])


            chat_frame2=LabelFrame(chat_frame)
            chat_frame2.pack(fill='both',expand='yes')
            chat_frame3=Frame(chat_frame2)
            chat_frame3.pack(fill=BOTH,expand='yes')

            chat_scrollbar=Scrollbar(chat_frame3)
            chat_scrollbar.pack(side=RIGHT,fill=Y)


            screen3=ttk.Treeview(chat_frame3,yscrollcommand=chat_scrollbar.set)
            screen3.pack(fill=BOTH,expand=YES)

            chat_scrollbar.config(command=screen3.yview)

            screen3['columns']=("Participants","message","time")
            screen3.column("#0",width=0)
            screen3.column("Participants",anchor=W,width=150,minwidth=150)
            screen3.column("message",anchor=W,width=150,minwidth=150)
            screen3.column("time",anchor=W,width=150,minwidth=150)



            screen3.heading("#0",text="",anchor=W)
            screen3.heading("Participants",text="PARTICIPANTS",anchor=W)
            screen3.heading("message",text="MESSAGE",anchor=W)
            screen3.heading("time",text="TIME",anchor=W)



            screen3.tag_configure('oddrow',background="white")
            screen3.tag_configure('evenrow',background="#99bccf")

            screen3.insert(parent='',index='end',iid=0,text="",values=(""),tags=('evenrow',))

            chat_frame4=LabelFrame(chat_frame,foreground='#083447')
            chat_frame4.pack(fill="x")


            footer_frame=Frame(main_window,background='#083447')
            footer_frame.pack(fill=X)
            Label(footer_frame,text="",background='#083447').pack()


            message=message[1:]
            history=eval(message)
            for i in history:
                print(i)
                screen3.insert('','end',text=1,values=(i[1],i[2],i[3]))

    

           
def main():

    def history():
        choice='2'
        send_message(choice)
        

    def send():
        choice='1'
        text=textbox1.get()
        textbox1.delete(0,END)
        send_message(choice,text)

    def search():
        choice='3'
        text=textbox1.get()
        textbox1.delete(0,END)
        send_message(choice,text)
        
    main_window=Toplevel()
    main_window.title("chat")
    main_window.geometry("400x600")

    main_nb=ttk.Notebook(main_window)
    main_nb.pack(fill=BOTH,expand=1)

    chat_framemw=Frame(main_nb)

    main_nb.add(chat_framemw,text="chat room")

    chat_framemw1=Frame(chat_framemw,background='#083447')
    chat_framemw1.pack(fill=X)

    Label(chat_framemw1,text="",background='#083447').pack()
    Label(chat_framemw1,text="",background='#083447').pack()
    b1=Button(chat_framemw1,image=history_button,borderwidth=0,command=history)
    b1.place(x=10,y=6)
    b2=Button(chat_framemw1,image=search_button,borderwidth=0,command=search)
    b2.place(x=280,y=6)


    style=ttk.Style()

    style.configure("Treeview.Heading",foreground='#083447',font=("Consolas", 10,"bold"))
    style.configure("Treeview",rowheight=25,background="#D3D3D3",foreground="black",fieldbackground="#D3D3D3",font=("Times", 8))

    style.map('Treeview',background=[('selected','#083447')])

    global chat_framemw2
    chat_framemw2=LabelFrame(chat_framemw)
    chat_framemw2.pack(fill='both',expand='yes')
    chat_framemw3=Frame(chat_framemw2)
    chat_framemw3.pack(fill=BOTH,expand='yes')

    chat_scrollbar=Scrollbar(chat_framemw3)
    chat_scrollbar.pack(side=RIGHT,fill=Y)

    global screen
    screen=ttk.Treeview(chat_framemw3,yscrollcommand=chat_scrollbar.set)
    screen.pack(fill=BOTH,expand=YES)

    chat_scrollbar.config(command=screen.yview)

    screen['columns']=("Participants","message","time")
    screen.column("#0",width=0)
    screen.column("Participants",anchor=W,width=150,minwidth=150)
    screen.column("message",anchor=W,width=150,minwidth=150)
    screen.column("time",anchor=W,width=150,minwidth=150)



    screen.heading("#0",text="",anchor=W)
    screen.heading("Participants",text="PARTICIPANTS",anchor=W)
    screen.heading("message",text="MESSAGE",anchor=W)
    screen.heading("time",text="TIME",anchor=W)



    screen.tag_configure('oddrow',background="white")
    screen.tag_configure('evenrow',background="#99bccf")

    screen.insert(parent='',index='end',iid=0,text="",values=(""),tags=('evenrow',))

    chat_framemw4=LabelFrame(chat_framemw,foreground='#083447')
    chat_framemw4.pack(fill="x")

    textbox1=Entry(chat_framemw4,width=80,font="none 8")
    textbox1.pack()

    threading.Thread(target=listen1).start()

    Label(chat_framemw4,text="").pack()
    b1=Button(chat_framemw4,image=enter_button,borderwidth=0,command=send)
    b1.pack()


    footer_frame=Frame(main_window,background='#083447')
    footer_frame.pack(fill=X)
    Label(footer_frame,text="",background='#083447').pack()

    
def username1():
    name=e1.get()
    print(name)
    
    if name=='':
        m2=mb.showerror('Error','Invalid Username')
        e1.delete(0,END)       
    else:
        client.sendall(name.encode())
        main()

        
def connection():
    global client
    client =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        client.connect((ip_address,port))
        print("connected to server")
    except:
        print("not connected")
        
    

login_window=Toplevel()
login_window.title("chat")
login_window.geometry("400x600")

login_nb=ttk.Notebook(login_window)
login_nb.pack(fill=BOTH,expand=1)

login_frame=Frame(login_nb)

login_nb.add(login_frame,text="chat room")

login_frame1=Frame(login_frame,background='#083447')
login_frame1.pack(fill=BOTH,expand=YES)

e1=Entry(login_frame1,width=50,font="none 8")
e1.place(x=50,y=110)
b1=Button(login_frame1,image=login_button,borderwidth=0,command=username1)
b1.place(x=120,y=150)




footer_frame=Frame(login_window,background='#083447')
footer_frame.pack(fill=X)
Label(footer_frame,text="",background='#083447').pack()

connection()

root_window.mainloop()


