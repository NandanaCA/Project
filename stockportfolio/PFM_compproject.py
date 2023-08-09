import mysql
import mysql.connector as mys

mycon=mys.connect(host="localhost",user="root",password="22dec2003",database="pfm_compproject")
mycursor=mycon.cursor()


from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime
from PIL import ImageTk,Image
import matplotlib.pyplot as plt

sdata=list()
userdict={ "Jane":"000","Nandana":"123","Shashank":"345","Jayprakash":"567","Subhashini":"789"}

root_window=Tk()
root_window.withdraw()
menu_window=Toplevel()
menu_window.title("PERSONAL FINANCE MANAGEMENT")
menu_window.geometry("1925x1085")

bg=PhotoImage(file="./icons2/comp_bg1920_1080.png")
bg_label=Label(menu_window,image=bg)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)
logo=ImageTk.PhotoImage(Image.open("./icons2/PFMlogo80_68.png"))

menu_frame1=Frame(menu_window,background='#083447')
menu_frame1.pack(fill=X)
    
Label(menu_frame1,text="",background='#083447').pack()
Label(menu_frame1,text="PERSONAL FINANCE MANAGEMENT",background='#083447',foreground="white",font=("Verdana", 16,"bold")).pack()
Label(menu_frame1,text="",background='#083447').pack()
logo_label=Label(menu_frame1,image=logo,borderwidth=0)
logo_label.place(x=0,y=0)

maintenance_t=PhotoImage(file='./icons2/transactionmaintenance_186.95.png')
maintenance_md=PhotoImage(file='./icons2/marketdatamaintenance_186.95.png')
analysis_t=PhotoImage(file='./icons2/transactionanalysis_186.95.png')
analysis_md=PhotoImage(file='./icons2/marketdataanalysis_186.95.png')
exit_button=PhotoImage(file='./icons2/exitbutton_186.95.png')

update_button=PhotoImage(file='./icons2/update_button100_32.png')
delete_button=PhotoImage(file='./icons2/delete100_32.png')
append_button=PhotoImage(file='./icons2/append100_32.png')
enter_button=PhotoImage(file='./icons2/enter100_32.png')
login_button=PhotoImage(file='./icons2/login150_48.png')
revenuepat_button=PhotoImage(file='./icons2/Revenue_PAT150_38.png')
realisedprofit_button=PhotoImage(file='./icons2/realisedprofit150_38.png')
    

##############################################################################################################################################################################

def maintenance_transactions():
    maintenance_window=Toplevel()
    maintenance_window.title("TRANSACTIONS MAINTENANCE")
    maintenance_window.geometry("1500x650")

    dropmenu_var1=StringVar()

    share_info0=list()
    query0="select * from share_info"
    mycursor.execute(query0)
    share_info0=mycursor.fetchall()

    share_name=['   ']
    for eachrow in share_info0:
        var=eachrow[1]
        if var not in share_name:
            share_name.append(var)
    
    maintenance_nb=ttk.Notebook(maintenance_window)
    maintenance_nb.pack(fill=BOTH,expand=1)

    transactions_frame=Frame(maintenance_nb)

    maintenance_nb.add(transactions_frame,text="TRANSACTIONS")
    
    transactions_frame1=Frame(transactions_frame,background='#083447')
    transactions_frame1.pack(fill=X)
    
    Label(transactions_frame1,text="",background='#083447').pack()
    Label(transactions_frame1,text="PERSONAL FINANCE MANAGEMENT",background='#083447',foreground="white",font=("Verdana", 16,"bold")).pack()
    Label(transactions_frame1,text="",background='#083447').pack()
    logo_label=Label(transactions_frame1,image=logo,borderwidth=0)
    logo_label.place(x=0,y=0)


    shares_portfolio=list()
    query1="select * from Shares_Portfolio"
    mycursor.execute(query1)
    shares_portfolio=mycursor.fetchall()

    style=ttk.Style()

    style.configure("Treeview.Heading",foreground='#083447',font=("Consolas", 10,"bold"))
    style.configure("Treeview",rowheight=25,background="#D3D3D3",foreground="black",fieldbackground="#D3D3D3",font=("Times", 8))

    style.map('Treeview',background=[('selected','#083447')])

    transactions_frame2=LabelFrame(transactions_frame)
    transactions_frame2.pack(fill=X)
    transactions_frame3=Frame(transactions_frame2)
    transactions_frame3.pack()

    transactions_scrollbar=Scrollbar(transactions_frame3)
    transactions_scrollbar.pack(side=RIGHT,fill=Y)

    transactions_tree=ttk.Treeview(transactions_frame3,yscrollcommand=transactions_scrollbar.set)
    transactions_tree.pack()

    transactions_scrollbar.config(command=transactions_tree.yview)

    transactions_tree['columns']=("ID","SHARE NAME","DATE","PRICE","QUANTITY","BUY/SELL")
    transactions_tree.column("#0",width=0)
    transactions_tree.column("ID",anchor=W,width=150,minwidth=150)
    transactions_tree.column("SHARE NAME",anchor=W,width=150,minwidth=150)
    transactions_tree.column("DATE",anchor=W,width=150,minwidth=150)
    transactions_tree.column("PRICE",anchor=W,width=150,minwidth=150)
    transactions_tree.column("QUANTITY",anchor=W,width=150,minwidth=150)

    transactions_tree.column("BUY/SELL",anchor=W,width=150)

    transactions_tree.heading("#0",text="",anchor=W)
    transactions_tree.heading("ID",text="ID",anchor=W)
    transactions_tree.heading("SHARE NAME",text="SHARE NAME",anchor=W)
    transactions_tree.heading("DATE",text="DATE",anchor=W)
    transactions_tree.heading("PRICE",text="PRICE",anchor=W)
    transactions_tree.heading("QUANTITY",text="QUANTITY",anchor=W)
    transactions_tree.heading("BUY/SELL",text="BUY/SELL",anchor=W)

    transactions_tree.tag_configure('oddrow',background="white")
    transactions_tree.tag_configure('evenrow',background="#99bccf")

    transactions_tree.insert(parent='',index='end',iid=0,text="",values=(""),tags=('evenrow',))
    
    count=1
    for eachrow in shares_portfolio:
        if count%2==0:
            transactions_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3],eachrow[4],eachrow[5]),tags=('evenrow',))
        else:
            transactions_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3],eachrow[4],eachrow[5]),tags=('oddrow',))
        count=count+1

    def select():

        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        
        selected=transactions_tree.focus()
        values=transactions_tree.item(selected,'values')

        dropmenu_var1.set(values[1])
        e2.insert(0,values[2])
        e3.insert(0,values[3])
        e4.insert(0,values[4])
        e5.insert(0,values[5])
    

    def clicker(e):
        select()

    def on_click1():

        m0a=messagebox.askyesno("Update","Are you sure you want to update this data?")
        if m0a==1:

            selected=transactions_tree.focus()
            values=transactions_tree.item(selected,'values')
           
            transactions_tree.item(selected,text="",values=(values[0],dropmenu_var1.get(),values[2],values[3],values[4],values[5]))
            query1="update Shares_Portfolio set Share_name='{}'where Id={}".format(dropmenu_var1.get(),values[0])
            mycursor.execute(query1)
            values=transactions_tree.item(selected,'values')
            dropmenu_var1.set("  ")
            date=e2.get()
            y=date[0:4]
            m=date[5:7]
            d=date[8:]
            isValidDate = True
            try :
                datetime.datetime(int(y),int(m),int(d))
            except ValueError :
                isValidDate = False
            
            if(isValidDate):
                transactions_tree.item(selected,text="",values=(values[0],values[1],e2.get(),values[3],values[4],values[5]))
                query2="update Shares_Portfolio set Date_of_Transaction='{}' where Id={}".format(e2.get(),values[0])
                mycursor.execute(query2)
                e2.delete(0,END)
                values=transactions_tree.item(selected,'values')
            
                if e3.get().isdigit()==True:
                    query3="update Shares_Portfolio set Price={} where Id={}".format(int(e3.get()),values[0])
                    mycursor.execute(query3)
                    transactions_tree.item(selected,text="",values=(values[0],values[1],values[2],e3.get(),values[4],values[5]))
                    e3.delete(0,END)
                    values=transactions_tree.item(selected,'values')
                    
                    if e4.get().isdigit()==True:
                        query4="update Shares_Portfolio set Quantity={} where Id={}".format(int(e4.get()),values[0])
                        mycursor.execute(query4)
                        transactions_tree.item(selected,text="",values=(values[0],values[1],values[2],values[3],e4.get(),values[5]))
                        e4.delete(0,END)
                        values=transactions_tree.item(selected,'values')
                        
                        if e5.get()!="":
                            query5="update Shares_Portfolio set Transaction_Type='{}'where Id={}".format(e5.get().upper(),values[0])
                            mycursor.execute(query5)
                            transactions_tree.item(selected,text="",values=(values[0],values[1],values[2],values[3],values[4],e5.get().upper()))
                            e5.delete(0,END)
                            values=transactions_tree.item(selected,'values')
                    
                            mycon.commit()
                            m0b=messagebox.showinfo("transactions","Data has been updated")

                        else:
                            e5.delete(0,END)
                            m5=messagebox.showerror("Update","Incorrect Transaction Type format")
                    else:
                        e4.delete(0,END)
                        m4=messagebox.showerror("Update","Incorrect quantity format")
                        
                else:
                    e3.delete(0,END)
                    m3=messagebox.showerror("Update","Incorrect price format")
            else:
                e2.delete(0,END)
                m2=messagebox.showerror("Update","Incorrect date format,should be YYYY-MM-DD")

                    

    def on_click2():
        share_symbol=dropmenu_var1.get()
        date=e2.get()
        transaction=e5.get().upper()
        
        y=date[0:4]
        m=date[5:7]
        d=date[8:]
        isValidDate = True
        try :
            datetime.datetime(int(y),int(m),int(d))
        except ValueError :
            isValidDate = False
    
        if(isValidDate):
            if e3.get().isdigit()==True:
                price=int(e3.get())
                if e4.get().isdigit()==True:
                    quantity=int(e4.get())
                    if e5.get()!="":
                        query1= "insert into Shares_Portfolio (Share_name,Date_of_Transaction,Price,Quantity,Transaction_Type) values('{0}','{1}',{2},{3},'{4}')".format(share_symbol,date,price,quantity,transaction)
                        mycursor.execute(query1)
                        mycon.commit()

                        dropmenu_var1.set("  ")
                        e2.delete(0,END)
                        e3.delete(0,END)
                        e4.delete(0,END)
                        e5.delete(0,END)

                        query1="select * from Shares_Portfolio"
                        mycursor.execute(query1)
                        shares_portfolio=mycursor.fetchall()
                        count=1
                        for record in transactions_tree.get_children():
                            transactions_tree.delete(record)
                        transactions_tree.insert(parent='',index='end',iid=0,text="",values=(""),tags=('evenrow',))
                        for eachrow in shares_portfolio:
                            if count%2==0:
                                transactions_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3],eachrow[4],eachrow[5]),tags=('evenrow',))
                            else:
                                transactions_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3],eachrow[4],eachrow[5]),tags=('oddrow',))
                            count=count+1
                    else:
                        e5.delete(0,END)
                        m5=messagebox.showerror("Append","Incorrect Transaction type format")
                        
                else:
                    e4.delete(0,END)
                    m4=messagebox.showerror("Append","Incorrect quantity format")
                    
            else:
                e3.delete(0,END)
                m3=messagebox.showerror("Append","Incorrect price format")
        else:
            e2.delete(0,END)
            m2=messagebox.showerror("Append","Incorrect date format,should be YYYY-MM-DD")

    def on_click3():
        selected=transactions_tree.focus()
        values=transactions_tree.item(selected,'values')
        x=transactions_tree.selection()
        for record in x:
            m2=messagebox.askyesno("Delete","Are you sure you want to delete this data?")
            if m2==1:
                query2="delete from Shares_Portfolio where id={}".format(values[0])
                mycursor.execute(query2)
                mycon.commit()
                m3=messagebox.showinfo("Delete","Data has been deleted")
                transactions_tree.delete(record)

    transactions_tree.bind("<Double-1>",clicker)

    transactions_frame4=LabelFrame(transactions_frame,text="Edit Share Details:",foreground='#083447',font=("Verdana", 10,"bold"))
    transactions_frame4.pack(fill="both",expand='yes')

    Label(transactions_frame4,text="Share Name:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=52,y=20)
    d1=OptionMenu(transactions_frame4,dropmenu_var1,*share_name)
    d1.place(x=210,y=14)
    dropmenu_var1.set("      ")

    Label(transactions_frame4,text="Date:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=52,y=60)
    e2=Entry(transactions_frame4,width=20,font="none 8")
    e2.place(x=200,y=60)

    Label(transactions_frame4,text="Price:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=52,y=100)
    e3=Entry(transactions_frame4,width=20,font="none 8")
    e3.place(x=200,y=100)


    Label(transactions_frame4,text="Quantity:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=52,y=140)
    e4=Entry(transactions_frame4,width=20,font="none 8")
    e4.place(x=200,y=140)


    Label(transactions_frame4,text="Transaction Type:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=52,y=180)
    e5=Entry(transactions_frame4,width=20,font="none 8")
    e5.place(x=200,y=180)

    Label(transactions_frame4,text="").pack()

    b1=Button(transactions_frame4,image=update_button,borderwidth=0,command=on_click1).place(x=350,y=85)
    b2=Button(transactions_frame4,image=append_button,borderwidth=0,command=on_click2).place(x=350,y=125)
    b3=Button(transactions_frame4,image=delete_button,borderwidth=0,command=on_click3).place(x=350,y=165)


    footer_frame=Frame(maintenance_window,background='#083447')
    footer_frame.pack(fill=X)
    Label(footer_frame,text="",background='#083447').pack()



##############################################################################################################################################################################

def maintenance_marketdata():
    maintenance_window=Toplevel()
    maintenance_window.title("MARKET DATA MAINTENANCE")
    maintenance_window.geometry("1500x650")
    
    maintenance_nb=ttk.Notebook(maintenance_window)
    maintenance_nb.pack(fill=BOTH,expand=1)

    shareinfo_frame=Frame(maintenance_nb)

    annualdata_frame=Frame(maintenance_nb)

    maintenance_nb.add(shareinfo_frame,text="SHARE INFO")
    maintenance_nb.add(annualdata_frame,text="ANNUAL MARKET DATA")

    #shareinfo

    shareinfo_frame1=Frame(shareinfo_frame,background='#083447')
    shareinfo_frame1.pack(fill=X)

    Label(shareinfo_frame1,text="",background='#083447').pack()
    Label(shareinfo_frame1,text="PERSONAL FINANCE MANAGEMENT",background='#083447',foreground="white",font=("Verdana", 16,"bold")).pack()
    Label(shareinfo_frame1,text="",background='#083447').pack()
    logo_label=Label(shareinfo_frame1,image=logo,borderwidth=0)
    logo_label.place(x=0,y=0)

    share_info=list()
    query1="select Share_Id,Share_Symbol,Company_Name,Market_Cap from share_info"
    mycursor.execute(query1)
    share_info=mycursor.fetchall()

    style=ttk.Style()

    style.configure("Treeview.Heading",foreground='#083447',font=("Consolas", 10,"bold"))
    style.configure("Treeview",rowheight=25,background="#D3D3D3",foreground="black",fieldbackground="#D3D3D3",font=("Times", 8))

    style.map('Treeview',background=[('selected','#083447')])

    shareinfo_frame2=LabelFrame(shareinfo_frame)
    shareinfo_frame2.pack(fill=X)
    shareinfo_frame3=Frame(shareinfo_frame2)
    shareinfo_frame3.pack()

    shareinfo_scrollbar=Scrollbar(shareinfo_frame3)
    shareinfo_scrollbar.pack(side=RIGHT,fill=Y)

    shareinfo_tree=ttk.Treeview(shareinfo_frame3,yscrollcommand=shareinfo_scrollbar.set)
    shareinfo_tree.pack()

    shareinfo_scrollbar.config(command=shareinfo_tree.yview)

    shareinfo_tree['columns']=("ID","SHARE SYMBOL","COMPANY NAME","MARKET CAP")
    shareinfo_tree.column("#0",width=0)
    shareinfo_tree.column("ID",anchor=W,width=100,minwidth=100)
    shareinfo_tree.column("SHARE SYMBOL",anchor=W,width=150,minwidth=150)
    shareinfo_tree.column("COMPANY NAME",anchor=W,width=200,minwidth=200)
    shareinfo_tree.column("MARKET CAP",anchor=W,width=100,minwidth=100)


    shareinfo_tree.heading("#0",text="",anchor=W)
    shareinfo_tree.heading("ID",text="ID",anchor=W)
    shareinfo_tree.heading("SHARE SYMBOL",text="SHARE SYMBOL",anchor=W)
    shareinfo_tree.heading("COMPANY NAME",text="COMPANY NAME",anchor=W)
    shareinfo_tree.heading("MARKET CAP",text="MARKET CAP",anchor=W)

    shareinfo_tree.tag_configure('oddrow',background="white")
    shareinfo_tree.tag_configure('evenrow',background="#99bccf")

    shareinfo_tree.insert(parent='',index='end',iid=0,text="",values=(""),tags=('evenrow',))
    global count
    count=1
    for eachrow in share_info:
        if count%2==0:
            shareinfo_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3]),tags=('evenrow',))
        else:
            shareinfo_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3]),tags=('oddrow',))
        count=count+1


    def selects():
        e1s.delete(0,END)
        e2s.delete(0,END)
        e3s.delete(0,END)

        selected=shareinfo_tree.focus()
        values=shareinfo_tree.item(selected,'values')

        e1s.insert(0,values[1])
        e2s.insert(0,values[2])
        e3s.insert(0,values[3])


    def clickers(e):
        selects()

    def on_click1():

        m0a=messagebox.askyesno("Share Info","Are you sure you want to update this data?")
        if m0a==1:

            selected=shareinfo_tree.focus()
            values=shareinfo_tree.item(selected,'values')
           
            if e1s.get()!="" and e2s.get()!="" and e3s.get()!="":
                query1="update share_info set Share_Symbol='{}'where Share_Id={}".format(e1s.get(),values[0])
                mycursor.execute(query1)

                shareinfo_tree.item(selected,text="",values=(values[0],values[1],e2s.get(),values[3]))
                query2="update share_info set Company_Name='{}' where Share_Id={}".format(e2s.get(),values[0])
                
                query4="update share_info set Market_Cap='{}' where Share_Id={}".format(e3s.get(),values[0])
                mycursor.execute(query4)

                shareinfo_tree.item(selected,text="",values=(values[0],e1s.get(),e2s.get(),e3s.get()))
                values=shareinfo_tree.item(selected,'values')
                e1s.delete(0,END)
                e2s.delete(0,END)
                e3s.delete(0,END)

                mycon.commit()
                m0b=messagebox.showinfo("Share info","Data has been updated")
            else:
                m1=messagebox.showerror("Share info","Incorrect format")


    def on_click2():
        if e1s.get()!="" and e2s.get()!="" and e3s.get()!="":
            share_symbol=e1s.get()
            company_name=e2s.get()
            market_cap=e3s.get()

            query1= "insert into share_info(Share_Symbol,Company_Name,Market_Cap) values('{0}','{1}','{2}')".format(share_symbol,company_name,market_cap)
            mycursor.execute(query1)
            mycon.commit()
            
            e1s.delete(0,END)
            e2s.delete(0,END)
            e3s.delete(0,END)
         
            query1="select Share_Id,Share_Symbol,Company_Name,Market_Cap from share_info"
            mycursor.execute(query1)
            share_info=mycursor.fetchall()
            count=1
            for record in shareinfo_tree.get_children():
                shareinfo_tree.delete(record)
            for eachrow in share_info:
                if count%2==0:
                    shareinfo_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3]),tags=('evenrow',))
                else:
                    shareinfo_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3]),tags=('oddrow',))
                count=count+1
        else:
            m1=messagebox.showerror("Share info","Incorrect format")


    def on_click3():
        selected=shareinfo_tree.focus()
        values=shareinfo_tree.item(selected,'values')
        x=shareinfo_tree.selection()
        for record in x:
            m2=messagebox.askyesno("Delete","Are you sure you want to delete this data?")
            if m2==1:
                query2="delete from share_info where Share_Id={}".format(values[0])
                mycursor.execute(query2)
                mycon.commit()
                m3=messagebox.showinfo("Delete","Data has been deleted")
                shareinfo_tree.delete(record)

    shareinfo_tree.bind("<Double-1>",clickers)

    shareinfo_frame4=LabelFrame(shareinfo_frame,text="Edit Share Details:",foreground='#083447',font=("Verdana", 10,"bold"))
    shareinfo_frame4.pack(fill="both",expand='yes')

    Label(shareinfo_frame4,text="Share Symbol:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=52,y=100)
    e1s=Entry(shareinfo_frame4,width=20,font="none 8")
    e1s.place(x=200,y=100)

    Label(shareinfo_frame4,text="Company Name:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=52,y=140)
    e2s=Entry(shareinfo_frame4,width=20,font="none 8")
    e2s.place(x=200,y=140)

    Label(shareinfo_frame4,text="Market Cap:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=52,y=180)
    e3s=Entry(shareinfo_frame4,width=20,font="none 8")
    e3s.place(x=200,y=180)

    Label(shareinfo_frame4,text="").pack()

    b1=Button(shareinfo_frame4,image=update_button,borderwidth=0,command=on_click1).place(x=350,y=85)
    b2=Button(shareinfo_frame4,image=append_button,borderwidth=0,command=on_click2).place(x=350,y=125)
    b3=Button(shareinfo_frame4,image=delete_button,borderwidth=0,command=on_click3).place(x=350,y=165)

    #annualdata   

    annualdata_frame1=Frame(annualdata_frame,background='#083447')
    annualdata_frame1.pack(fill=X)

    Label(annualdata_frame1,text="",background='#083447').pack()
    Label(annualdata_frame1,text="PERSONAL FINANCE MANAGEMENT",background='#083447',foreground="white",font=("Verdana", 16,"bold")).pack()
    Label(annualdata_frame1,text="",background='#083447').pack()
    logo_label=Label(annualdata_frame1,image=logo,borderwidth=0)
    logo_label.place(x=0,y=0)

    share_info=list()
    query1="select annualinfo_id,Share_Symbol,annual_infoyear,totalrevenue,otherincome,totalexpense,financecost,depr_amortexpense,pat,net_profit,equity_currentyear,equity_previousyear,totalassets_currentyear,totalassets_previousyear,PBT,Tax,Debt from share_info,company_annualinfo where share_info.share_id=company_annualinfo.share_id"
    mycursor.execute(query1)
    share_info=mycursor.fetchall()
    query2="select * from company_annualinfo"
    mycursor.execute(query2)
    s=mycursor.fetchall()

    dropmenu_var3=StringVar()

    share_info0=list()
    query0="select * from share_info"
    mycursor.execute(query0)
    share_info0=mycursor.fetchall()

    share_name=['   ']
    for eachrow in share_info0:
        var=eachrow[1]
        if var not in share_name:
            share_name.append(var)

    style=ttk.Style()

    style.configure("Treeview.Heading",foreground='#083447',font=("Consolas", 10,"bold"))
    style.configure("Treeview",rowheight=25,background="#D3D3D3",foreground="black",fieldbackground="#D3D3D3",font=("Times", 8))

    style.map('Treeview',background=[('selected','#083447')])

    annualdata_frame2=LabelFrame(annualdata_frame)
    annualdata_frame2.pack(fill=X)
    annualdata_frame3=Frame(annualdata_frame2)
    annualdata_frame3.pack()

    annualdata_scrollbar1=Scrollbar(annualdata_frame3)
    annualdata_scrollbar1.pack(side=RIGHT,fill=Y)

    annualdata_scrollbar2=Scrollbar(annualdata_frame3,orient='horizontal')
    annualdata_scrollbar2.pack(side=BOTTOM,fill=X)

    annualdata_tree=ttk.Treeview(annualdata_frame3,yscrollcommand=annualdata_scrollbar1.set,xscrollcommand=annualdata_scrollbar2.set)
    annualdata_tree.pack()

    annualdata_scrollbar1.config(command=annualdata_tree.yview)
    annualdata_scrollbar2.config(command=annualdata_tree.xview)


    annualdata_tree['columns']=("ID","SHARE SYMBOL","YEAR","TOTAL REVENUE","OTHER INCOME","TOTAL EXPENCE","FINANCE COST","DEPR AND AMORT EXPENSE","PAT","NET PROFIT","EQUITY CURRENTYEAR","EQUITY PREVIOUSYEAR","TOTALASSETS CURRENTYEAR","TOTALASSETS PREVIOUSYEAR","PBT","TAX","DEBT")
    annualdata_tree.column("#0",width=0)
    annualdata_tree.column("ID",anchor=W,width=100,minwidth=100)
    annualdata_tree.column("SHARE SYMBOL",anchor=W,width=100,minwidth=100)
    annualdata_tree.column("YEAR",anchor=W,width=100,minwidth=100)
    annualdata_tree.column("TOTAL REVENUE",anchor=W,width=150,minwidth=150)
    annualdata_tree.column("OTHER INCOME",anchor=W,width=150,minwidth=150)
    annualdata_tree.column("TOTAL EXPENCE",anchor=W,width=150,minwidth=150)
    annualdata_tree.column("FINANCE COST",anchor=W,width=150,minwidth=150)
    annualdata_tree.column("DEPR AND AMORT EXPENSE",anchor=W,width=180,minwidth=180)
    annualdata_tree.column("PAT",anchor=W,width=180,minwidth=180)
    annualdata_tree.column("NET PROFIT",anchor=W,width=180,minwidth=180)
    annualdata_tree.column("EQUITY CURRENTYEAR",anchor=W,width=180,minwidth=180)
    annualdata_tree.column("EQUITY PREVIOUSYEAR",anchor=W,width=180,minwidth=180)
    annualdata_tree.column("TOTALASSETS CURRENTYEAR",anchor=W,width=180,minwidth=180)
    annualdata_tree.column("TOTALASSETS PREVIOUSYEAR",anchor=W,width=180,minwidth=180)
    annualdata_tree.column("PBT",anchor=W,width=180,minwidth=180)
    annualdata_tree.column("TAX",anchor=W,width=180,minwidth=180)
    annualdata_tree.column("DEBT",anchor=W,width=180,minwidth=180)



    annualdata_tree.heading("#0",text="",anchor=W)
    annualdata_tree.heading("ID",text="ID",anchor=W)
    annualdata_tree.heading("SHARE SYMBOL",text="SHARE SYMBOL",anchor=W)
    annualdata_tree.heading("YEAR",text="YEAR",anchor=W)
    annualdata_tree.heading("TOTAL REVENUE",text="TOTAL REVENUE",anchor=W)
    annualdata_tree.heading("OTHER INCOME",text="OTHER INCOME",anchor=W)
    annualdata_tree.heading("TOTAL EXPENCE",text="TOTAL EXPENCE",anchor=W)
    annualdata_tree.heading("FINANCE COST",text="FINANCE COST",anchor=W)
    annualdata_tree.heading("DEPR AND AMORT EXPENSE",text="DEPR AND AMORT EXPENSE",anchor=W)
    annualdata_tree.heading("PAT",text="PAT",anchor=W)
    annualdata_tree.heading("NET PROFIT",text="NET PROFIT",anchor=W)
    annualdata_tree.heading("EQUITY CURRENTYEAR",text="EQUITY CURRENTYEAR",anchor=W)
    annualdata_tree.heading("EQUITY PREVIOUSYEAR",text="EQUITY PREVIOUSYEAR",anchor=W)
    annualdata_tree.heading("TOTALASSETS CURRENTYEAR",text="TOTALASSETS CURRENTYEAR",anchor=W)
    annualdata_tree.heading("TOTALASSETS PREVIOUSYEAR",text="TOTALASSETS PREVIOUSYEAR",anchor=W)
    annualdata_tree.heading("PBT",text="PBT",anchor=W)
    annualdata_tree.heading("TAX",text="TAX",anchor=W)
    annualdata_tree.heading("DEBT",text="DEBT",anchor=W)


    annualdata_tree.tag_configure('oddrow',background="white")
    annualdata_tree.tag_configure('evenrow',background="#99bccf")

    annualdata_tree.insert(parent='',index='end',iid=0,text="",values=(""),tags=('evenrow',))
    count=1
    for eachrow in share_info:
        if count%2==0:
            annualdata_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3],eachrow[4],eachrow[5],eachrow[6],eachrow[7],eachrow[8],eachrow[9],eachrow[10],eachrow[11],eachrow[12],eachrow[13],eachrow[14],eachrow[15],eachrow[16]),tags=('evenrow',))
        else:
            annualdata_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3],eachrow[4],eachrow[5],eachrow[6],eachrow[7],eachrow[8],eachrow[9],eachrow[10],eachrow[11],eachrow[12],eachrow[13],eachrow[14],eachrow[15],eachrow[16]),tags=('oddrow',))
        count=count+1


    def selecta():
        e2a.delete(0,END)
        e3a.delete(0,END)
        e4a.delete(0,END)
        e5a.delete(0,END)
        e6a.delete(0,END)
        e7a.delete(0,END)
        e8a.delete(0,END)
        e9a.delete(0,END)
        e10a.delete(0,END)
        e11a.delete(0,END)
        e12a.delete(0,END)
        e13a.delete(0,END)
        e14a.delete(0,END)
        e15a.delete(0,END)
        e16a.delete(0,END)
        
        selected=annualdata_tree.focus()
        values=annualdata_tree.item(selected,'values')

        dropmenu_var3.set(values[1])
        e2a.insert(0,values[2])
        e3a.insert(0,values[3])
        e4a.insert(0,values[4])
        e5a.insert(0,values[5])
        e6a.insert(0,values[6])
        e7a.insert(0,values[7])
        e8a.insert(0,values[8])
        e9a.insert(0,values[9])
        e10a.insert(0,values[10])
        e11a.insert(0,values[11])
        e12a.insert(0,values[12])
        e13a.insert(0,values[13])
        e14a.insert(0,values[14])
        e15a.insert(0,values[15])
        e16a.insert(0,values[16])


    def clickera(e):
        selecta()

    def on_click4():

        m0a=messagebox.askyesno("Share Info","Are you sure you want to update this data?")
        if m0a==1:
            if e2a.get()!="":
                if e3a.get().isdigit()==True:
                    if e4a.get().isdigit()==True:
                        if e5a.get().isdigit()==True:
                            if e6a.get().isdigit()==True:
                                if e7a.get().isdigit()==True:
                                    if e8a.get().isdigit()==True:
                                        if e9a.get().isdigit()==True:
                                            if e10a.get().isdigit()==True:
                                                if e11a.get().isdigit()==True:
                                                    if e12a.get().isdigit()==True:
                                                        if e13a.get().isdigit()==True:
                                                            if e14a.get().isdigit()==True:
                                                                if e15a.get().isdigit()==True:
                                                                    if e16a.get().isdigit()==True:

                                                                        selected=annualdata_tree.focus()
                                                                        values=annualdata_tree.item(selected,'values')

                                                                        query0="select share_id from share_info where share_symbol='{}'".format(dropmenu_var3.get())
                                                                        mycursor.execute(query0)
                                                                        Id=mycursor.fetchall()
                                                                       
                                                                        query1="update company_annualinfo set share_id='{}'where annualinfo_id={}".format(Id[0][0],values[0])
                                                                        mycursor.execute(query1)
                                                                        
                                                                        
                                                                        query2="update company_annualinfo set annual_infoyear='{}'where annualinfo_id={}".format(e2a.get(),values[0])
                                                                        mycursor.execute(query2)
                                                                        

                                                                        query3="update company_annualinfo set totalrevenue={} where annualinfo_id={}".format(int(e3a.get()),values[0])
                                                                        mycursor.execute(query3)
                                                                        

                                                                        query4="update company_annualinfo set otherincome={} where annualinfo_id={}".format(int(e4a.get()),values[0])
                                                                        mycursor.execute(query4)
                                                                       

                                                                        query5="update company_annualinfo set totalexpense={} where annualinfo_id={}".format(int(e5a.get()),values[0])
                                                                        mycursor.execute(query5)
                                                                        

                                                                        query6="update company_annualinfo set financecost={} where annualinfo_id={}".format(int(e6a.get()),values[0])
                                                                        mycursor.execute(query6)
                                                                        

                                                                        query7="update company_annualinfo set depr_amortexpense={} where annualinfo_id={}".format(int(e7a.get()),values[0])
                                                                        mycursor.execute(query7)
                                                                        

                                                                        query8="update company_annualinfo set pat={} where annualinfo_id={}".format(int(e8a.get()),values[0])
                                                                        mycursor.execute(query8)
                                                                        

                                                                        query9="update company_annualinfo set net_profit={} where annualinfo_id={}".format(int(e9a.get()),values[0])
                                                                        mycursor.execute(query9)
                                                                        

                                                                        query10="update company_annualinfo set equity_currentyear={} where annualinfo_id={}".format(int(e10a.get()),values[0])
                                                                        mycursor.execute(query10)
                                                                        

                                                                        query11="update company_annualinfo set equity_previousyear={} where annualinfo_id={}".format(int(e11a.get()),values[0])
                                                                        mycursor.execute(query11)
                                                                        

                                                                        query12="update company_annualinfo set totalassets_currentyear={} where annualinfo_id={}".format(int(e12a.get()),values[0])
                                                                        mycursor.execute(query12)
                                                                        

                                                                        query13="update company_annualinfo set totalassets_previousyear={} where annualinfo_id={}".format(int(e13a.get()),values[0])
                                                                        mycursor.execute(query13)
                                                                        

                                                                        query14="update company_annualinfo set PBT={} where annualinfo_id={}".format(int(e14a.get()),values[0])
                                                                        mycursor.execute(query14)
                                                                        

                                                                        query15="update company_annualinfo set Tax={} where annualinfo_id={}".format(int(e15a.get()),values[0])
                                                                        mycursor.execute(query15)
                                                                       

                                                                        query16="update company_annualinfo set Debt={} where annualinfo_id={}".format(int(e16a.get()),values[0])
                                                                        mycursor.execute(query16)
                                                                        
                                                                        annualdata_tree.item(selected,text="",values=(values[0],dropmenu_var3.get(),e2a.get(),e3a.get(),e4a.get(),e5a.get(),e6a.get(),e7a.get(),e8a.get(),e9a.get(),e10a.get(),e11a.get(),e12a.get(),e13a.get(),e14a.get(),e15a.get(),e16a.get()))

                                                                        dropmenu_var3.set("   ")
                                                                        e2a.delete(0,END)
                                                                        e3a.delete(0,END)
                                                                        e4a.delete(0,END)
                                                                        e5a.delete(0,END)
                                                                        e6a.delete(0,END)
                                                                        e7a.delete(0,END)
                                                                        e8a.delete(0,END)
                                                                        e9a.delete(0,END)
                                                                        e10a.delete(0,END)
                                                                        e11a.delete(0,END)
                                                                        e12a.delete(0,END)
                                                                        e13a.delete(0,END)
                                                                        e14a.delete(0,END)
                                                                        e15a.delete(0,END)
                                                                        e16a.delete(0,END)
                                                                        
                                                                        values=annualdata_tree.item(selected,'values')

                                                                        mycon.commit()
                                                                        m0b=messagebox.showinfo("Share info","Data has been updated")
                                                                    else:
                                                                        e16a.delete(0,END)
                                                                        m16=messagebox.showerror("Company Annual Info","Incorrect Debt format")
                                                                else:
                                                                    e15a.delete(0,END)
                                                                    m15=messagebox.showerror("Company Annual Info","Incorrect Tax format")
                                                            else:
                                                                e14a.delete(0,END)
                                                                m14=messagebox.showerror("Company Annual Info","Incorrect PBT format")
                                                        else:
                                                            e13a.delete(0,END)
                                                            m13=messagebox.showerror("Company Annual Info","Incorrect Total assets Previous year format")
                                                    else:
                                                        e12a.delete(0,END)
                                                        m12=messagebox.showerror("Company Annual Info","Incorrect Total assets Current year format")
                                                else:
                                                    e11a.delete(0,END)
                                                    m11=messagebox.showerror("Company Annual Info","Incorrect Equity Previous year format")
                                            else:
                                                e10a.delete(0,END)
                                                m10=messagebox.showerror("Company Annual Info","Incorrect Equity Current year format")
                                        else:
                                            e9a.delete(0,END)
                                            m9=messagebox.showerror("Company Annual Info","Incorrect Net Profit format")
                                    else:
                                        e8a.delete(0,END)
                                        m8=messagebox.showerror("Company Annual Info","Incorrect PAT format")
                                    
                                else:
                                    e7a.delete(0,END)
                                    m7=messagebox.showerror("Company Annual Info","Incorrect depr_amort format")
                            else:
                                e6a.delete(0,END)
                                m6=messagebox.showerror("Company Annual Info","Incorrect finance cost format")
                                
                        else:
                            e5a.delete(0,END)
                            m5=messagebox.showerror("Company Annual Info","Incorrect total expense format")
                            
                    else:
                        e4a.delete(0,END)
                        m4=messagebox.showerror("Company Annual Info","Incorrect other income format")
                        
                else:
                    e3a.delete(0,END)
                    m3=messagebox.showerror("Company Annual Info","Incorrect total revenue format")
            else:
                m1=messagebox.showerror("Company Annual Info","Incorrect format")
                
        else:
            m1=messagebox.showerror("Share info","Incorrect format")    

    def on_click5():
        if e2a.get()!="":
            share_symbol=dropmenu_var3.get()
            year=e2a.get()
            if e3a.get().isdigit()==True:
                totalrevenue=e3a.get()
                if e4a.get().isdigit()==True:
                    otherincome=e4a.get()
                    if e5a.get().isdigit()==True:
                        totalexpense=e5a.get()
                        if e6a.get().isdigit()==True:
                            financecost=e6a.get()
                            if e7a.get().isdigit()==True:
                                depandamortexp=e7a.get()
                                if e8a.get().isdigit()==True:
                                    pat=e8a.get()
                                    if e9a.get().isdigit()==True:
                                        net_profit=e9a.get()
                                        if e10a.get().isdigit()==True:
                                            equity_current=e10a.get()
                                            if e11a.get().isdigit()==True:
                                                equity_previous=e11a.get()
                                                if e12a.get().isdigit()==True:
                                                    totalassets_current=e12a.get()
                                                    if e13a.get().isdigit()==True:
                                                        totalassets_previous=e13a.get()
                                                        if e14a.get().isdigit()==True:
                                                            pbt=e14a.get()
                                                            if e15a.get().isdigit()==True:
                                                                tax=e15a.get()
                                                                if e16a.get().isdigit()==True:
                                                                    debt=e16a.get()

                                                                    query1="select share_id from share_info where share_symbol='{}'".format(dropmenu_var3.get())
                                                                    mycursor.execute(query1)
                                                                    Id=mycursor.fetchall()
                                                 
                                                                    query2= "insert into company_annualinfo (share_id,annual_infoyear,totalrevenue,otherincome,totalexpense,financecost,depr_amortexpense,pat,net_profit,equity_currentyear,equity_previousyear,totalassets_currentyear,totalassets_previousyear,PBT,Tax,Debt) values({0},'{1}',{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15})".format(Id[0][0],year,totalrevenue,otherincome,totalexpense,financecost,depandamortexp,pat,net_profit,equity_current,equity_previous,totalassets_current,totalassets_previous,pbt,tax,debt)
                                                                    mycursor.execute(query2)
                                                                    mycon.commit()
                                                                    
                                                                    dropmenu_var3.set("  ")
                                                                    e2a.delete(0,END)
                                                                    e3a.delete(0,END)
                                                                    e4a.delete(0,END)
                                                                    e5a.delete(0,END)
                                                                    e6a.delete(0,END)
                                                                    e7a.delete(0,END)
                                                                    e8a.delete(0,END)
                                                                    e9a.delete(0,END)
                                                                    e10a.delete(0,END)
                                                                    e11a.delete(0,END)
                                                                    e12a.delete(0,END)
                                                                    e13a.delete(0,END)
                                                                    e14a.delete(0,END)
                                                                    e15a.delete(0,END)
                                                                    e16a.delete(0,END)

                                                                    query1="select annualinfo_id,Share_Symbol,annual_infoyear,totalrevenue,otherincome,totalexpense,financecost,depr_amortexpense,pat,net_profit,equity_currentyear,equity_previousyear,totalassets_currentyear,totalassets_previousyear,PBT,Tax,Debt from share_info,company_annualinfo where share_info. share_id=company_annualinfo.share_id"
                                                                    mycursor.execute(query1)
                                                                    share_info=mycursor.fetchall()
                                                                    count=1
                                                                    for record in annualdata_tree.get_children():
                                                                        annualdata_tree.delete(record)
                                                                    annualdata_tree.insert(parent='',index='end',iid=0,text="",values=(""),tags=('evenrow',))
                                                                    for eachrow in share_info:
                                                                        if count%2==0:
                                                                            annualdata_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3],eachrow[4],eachrow[5],eachrow[6],eachrow[7],eachrow[8],eachrow[9],eachrow[10],eachrow[11],eachrow[12],eachrow[13],eachrow[14],eachrow[15],eachrow[16]),tags=('evenrow',))
                                                                        else:
                                                                            annualdata_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3],eachrow[4],eachrow[5],eachrow[6],eachrow[7],eachrow[8],eachrow[9],eachrow[10],eachrow[11],eachrow[12],eachrow[13],eachrow[14],eachrow[15],eachrow[16]),tags=('oddrow',))
                                                                        count=count+1
                                                                else:
                                                                    e16a.delete(0,END)
                                                                    m16=messagebox.showerror("Company Annual Info","Incorrect Debt format")
                                                            else:
                                                                e15a.delete(0,END)
                                                                m15=messagebox.showerror("Company Annual Info","Incorrect Tax format")
                                                        else:
                                                            e14a.delete(0,END)
                                                            m14=messagebox.showerror("Company Annual Info","Incorrect PBT format")
                                                    else:
                                                        e13a.delete(0,END)
                                                        m13=messagebox.showerror("Company Annual Info","Incorrect Total assets Previous year format")
                                                else:
                                                    e12a.delete(0,END)
                                                    m12=messagebox.showerror("Company Annual Info","Incorrect Total assets Current year format")
                                            else:
                                                e11a.delete(0,END)
                                                m11=messagebox.showerror("Company Annual Info","Incorrect Equity Previous year format")
                                        else:
                                            e10a.delete(0,END)
                                            m10=messagebox.showerror("Company Annual Info","Incorrect Equity Current year format")
                                    else:
                                        e9a.delete(0,END)
                                        m9=messagebox.showerror("Company Annual Info","Incorrect Net Profit format")
                                else:
                                    e8a.delete(0,END)
                                    m8=messagebox.showerror("Company Annual Info","Incorrect PAT format")                                                                    
                            else:
                                e7a.delete(0,END)
                                m7=messagebox.showerror("Company Annual Info","Incorrect other income format")
                                
                        else:
                            e6a.delete(0,END)
                            m6=messagebox.showerror("Company Annual Info","Incorrect finance cost format")
                            
                    else:
                        e5a.delete(0,END)
                        m5=messagebox.showerror("Company Annual Info","Incorrect total expense format")
                        
                else:
                    e4a.delete(0,END)
                    m4=messagebox.showerror("Company Annual Info","Incorrect other income format")
                    
            else:
                e3a.delete(0,END)
                m3=messagebox.showerror("Company Annual Info","Incorrect total revenue format")
        else:
            m1=messagebox.showerror("Company Annual Info","Incorrect format")


    def on_click6():
        selected=annualdata_tree.focus()
        values=annualdata_tree.item(selected,'values')
        x=annualdata_tree.selection()
        for record in x:
            m2=messagebox.askyesno("Delete","Are you sure you want to delete this data?")
            if m2==1:
                query2="delete from company_annualinfo where annualinfo_id={}".format(values[0])
                mycursor.execute(query2)
                mycon.commit()
                m3=messagebox.showinfo("Delete","Data has been deleted")
                annualdata_tree.delete(record)
                
    annualdata_tree.bind("<Double-1>",clickera)

    annualdata_frame4=LabelFrame(annualdata_frame,text="Edit Share Details:",foreground='#083447',font=("Verdana", 10,"bold"))
    annualdata_frame4.pack(fill="both",expand='yes')

    Label(annualdata_frame4,text="Share Symbol:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=60,y=20)
    d3=OptionMenu(annualdata_frame4,dropmenu_var3,*share_name)
    d3.place(x=190,y=14)
    dropmenu_var3.set("      ")

    Label(annualdata_frame4,text="Year:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=60,y=60)
    e2a=Entry(annualdata_frame4,width=12,font="none 8")
    e2a.place(x=190,y=60)

    Label(annualdata_frame4,text="Total revenue:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=60,y=100)
    e3a=Entry(annualdata_frame4,width=12,font="none 8")
    e3a.place(x=190,y=100)

    Label(annualdata_frame4,text="Other income:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=60,y=140)
    e4a=Entry(annualdata_frame4,width=12,font="none 8")
    e4a.place(x=190,y=140)

    Label(annualdata_frame4,text="Total expense:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=60,y=180)
    e5a=Entry(annualdata_frame4,width=12,font="none 8")
    e5a.place(x=190,y=180)

    Label(annualdata_frame4,text="Finance cost:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=320,y=20)
    e6a=Entry(annualdata_frame4,width=12,font="none 8")
    e6a.place(x=470,y=20)

    Label(annualdata_frame4,text="Depreciation and",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=320,y=60)
    Label(annualdata_frame4,text="Amortization expense:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=320,y=80)
    e7a=Entry(annualdata_frame4,width=12,font="none 8")
    e7a.place(x=470,y=80)

    Label(annualdata_frame4,text="PAT:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=320,y=120)
    e8a=Entry(annualdata_frame4,width=12,font="none 8")
    e8a.place(x=470,y=120)

    Label(annualdata_frame4,text="Net Profit:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=320,y=160)
    e9a=Entry(annualdata_frame4,width=12,font="none 8")
    e9a.place(x=470,y=160)

    Label(annualdata_frame4,text="Equity current:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=580,y=20)
    e10a=Entry(annualdata_frame4,width=12,font="none 8")
    e10a.place(x=730,y=20)

    Label(annualdata_frame4,text="Equity previous:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=580,y=60)
    e11a=Entry(annualdata_frame4,width=12,font="none 8")
    e11a.place(x=730,y=60)

    Label(annualdata_frame4,text="Total assets current:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=580,y=100)
    e12a=Entry(annualdata_frame4,width=12,font="none 8")
    e12a.place(x=730,y=100)

    Label(annualdata_frame4,text="Total assets previous:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=580,y=140)
    e13a=Entry(annualdata_frame4,width=12,font="none 8")
    e13a.place(x=730,y=140)

    Label(annualdata_frame4,text="PBT:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=580,y=180)
    e14a=Entry(annualdata_frame4,width=12,font="none 8")
    e14a.place(x=730,y=180)

    Label(annualdata_frame4,text="Tax:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=840,y=20)
    e15a=Entry(annualdata_frame4,width=12,font="none 8")
    e15a.place(x=990,y=20)

    Label(annualdata_frame4,text="Debt:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=840,y=60)
    e16a=Entry(annualdata_frame4,width=12,font="none 8")
    e16a.place(x=990,y=60)

    Label(annualdata_frame4,text="").pack()

    b1=Button(annualdata_frame4,image=update_button,borderwidth=0,command=on_click4).place(x=900,y=100)
    b2=Button(annualdata_frame4,image=append_button,borderwidth=0,command=on_click5).place(x=900,y=140)
    b3=Button(annualdata_frame4,image=delete_button,borderwidth=0,command=on_click6).place(x=900,y=180)

    footer_frame=Frame(maintenance_window,background='#083447')
    footer_frame.pack(fill=X)
    Label(footer_frame,text="",background='#083447').pack()

##########################################################################################################################################################################################################
def transaction_analysis():
    analysis_window=Toplevel()
    analysis_window.title("TRANSACTION ANALYSIS")
    analysis_window.geometry("1500x650")
    
    analysis_nb=ttk.Notebook(analysis_window)
    analysis_nb.pack(fill=BOTH,expand=1)

    holdings_frame=Frame(analysis_nb)

    transactionsummary_frame=Frame(analysis_nb)

    transactions_frame=Frame(analysis_nb)

    tradereport_frame=Frame(analysis_nb)

    yearlygrowth_frame=Frame(analysis_nb)

    analysis_nb.add(transactions_frame,text="TRANSACTIONS")
    analysis_nb.add(tradereport_frame,text="TRADE REPORT")
    analysis_nb.add(holdings_frame,text="HOLDINGS")
    analysis_nb.add(transactionsummary_frame,text="TRANSACTION SUMMARY")
    analysis_nb.add(yearlygrowth_frame,text="YEARLY GROWTH")

    shares_portfolio0=list()
    query0="select * from Shares_Portfolio"
    mycursor.execute(query0)
    shares_portfolio0=mycursor.fetchall()

    share_name2=['   ']
    share_name3=list()
    for eachrow in shares_portfolio0:
        var=eachrow[1]
        if var not in share_name2:
            share_name2.append(var)
            share_name3.append(var)



    #transactions

    transactions_frame1=Frame(transactions_frame,background='#083447')
    transactions_frame1.pack(fill=X)
    
    Label(transactions_frame1,text="",background='#083447').pack()
    Label(transactions_frame1,text="PERSONAL FINANCE MANAGEMENT",background='#083447',foreground="white",font=("Verdana", 16,"bold")).pack()
    Label(transactions_frame1,text="",background='#083447').pack()
    logo_label=Label(transactions_frame1,image=logo,borderwidth=0)
    logo_label.place(x=0,y=0)


    shares_portfolio=list()
    query1="select * from Shares_Portfolio"
    mycursor.execute(query1)
    shares_portfolio=mycursor.fetchall()
    

    Label(transactions_frame,text="").pack()


    style=ttk.Style()

    style.configure("Treeview.Heading",foreground='#083447',font=("Consolas", 10,"bold"))
    style.configure("Treeview",rowheight=25,background="#D3D3D3",foreground="black",fieldbackground="#D3D3D3",font=("Times", 8))

    style.map('Treeview',background=[('selected','#083447')])

    transactions_frame2=LabelFrame(transactions_frame)
    transactions_frame2.pack(fill=BOTH,expand=1)
    transactions_frame3=Frame(transactions_frame2)
    transactions_frame3.pack(fill=BOTH,expand=1)

    transactions_scrollbar=Scrollbar(transactions_frame3)
    transactions_scrollbar.pack(side=RIGHT,fill=Y)

    transactions_tree=ttk.Treeview(transactions_frame3,yscrollcommand=transactions_scrollbar.set)
    transactions_tree.pack(fill=BOTH,expand=1)

    transactions_scrollbar.config(command=transactions_tree.yview)

    transactions_tree['columns']=("ID","SHARE NAME","DATE","PRICE","QUANTITY","BUY/SELL")
    transactions_tree.column("#0",width=0)
    transactions_tree.column("ID",anchor=W,width=150,minwidth=150)
    transactions_tree.column("SHARE NAME",anchor=W,width=150,minwidth=150)
    transactions_tree.column("DATE",anchor=W,width=150,minwidth=150)
    transactions_tree.column("PRICE",anchor=W,width=150,minwidth=150)
    transactions_tree.column("QUANTITY",anchor=W,width=150,minwidth=150)

    transactions_tree.column("BUY/SELL",anchor=W,width=150)

    transactions_tree.heading("#0",text="",anchor=W)
    transactions_tree.heading("ID",text="ID",anchor=W)
    transactions_tree.heading("SHARE NAME",text="SHARE NAME",anchor=W)
    transactions_tree.heading("DATE",text="DATE",anchor=W)
    transactions_tree.heading("PRICE",text="PRICE",anchor=W)
    transactions_tree.heading("QUANTITY",text="QUANTITY",anchor=W)
    transactions_tree.heading("BUY/SELL",text="BUY/SELL",anchor=W)

    transactions_tree.tag_configure('oddrow',background="white")
    transactions_tree.tag_configure('evenrow',background="#99bccf")

    transactions_tree.insert(parent='',index='end',iid=0,text="",values=(""),tags=('evenrow',))
    global count
    count=1
    for eachrow in shares_portfolio:
        if count%2==0:
            transactions_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3],eachrow[4],eachrow[5]),tags=('evenrow',))
        else:
            transactions_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3],eachrow[4],eachrow[5]),tags=('oddrow',))
        count=count+1

    #tradereport

    tradereport_frame1=Frame(tradereport_frame,background='#083447')
    tradereport_frame1.pack(fill=X)
    
    Label(tradereport_frame1,text="",background='#083447').pack()
    Label(tradereport_frame1,text="PERSONAL FINANCE MANAGEMENT",background='#083447',foreground="white",font=("Verdana", 16,"bold")).pack()
    Label(tradereport_frame1,text="",background='#083447').pack()
    logo_label=Label(tradereport_frame1,image=logo,borderwidth=0)
    logo_label.place(x=0,y=0)

    tradereport_frame2=LabelFrame(tradereport_frame,text="Edit Share Details:",foreground='#083447',font=("Verdana", 10,"bold"))
    tradereport_frame2.pack(fill="both",expand='yes')

    Label(tradereport_frame2,text="From:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=52,y=80)
    e1tr=Entry(tradereport_frame2,width=20,font="none 8")
    e1tr.place(x=200,y=80)

    Label(tradereport_frame2,text="To:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=52,y=120)
    e2tr=Entry(tradereport_frame2,width=20,font="none 8")
    e2tr.place(x=200,y=120)

    dropmenu_var4=StringVar()
    dropmenu_var4.set("All")
    share_name3.append("All")
        
    Label(tradereport_frame2,text="SHARE SYMBOL:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=52,y=40)
    d4=OptionMenu(tradereport_frame2,dropmenu_var4,*share_name3)
    d4.place(x=230,y=36)


    style=ttk.Style()

    style.configure("Treeview.Heading",foreground='#083447',font=("Consolas", 10,"bold"))
    style.configure("Treeview",rowheight=25,background="#D3D3D3",foreground="black",fieldbackground="#D3D3D3",font=("Times", 8))

    style.map('Treeview',background=[('selected','#083447')])

    tradereport_frame3=LabelFrame(tradereport_frame)
    tradereport_frame3.pack(fill=X)
    tradereport_frame4=Frame(tradereport_frame3)
    tradereport_frame4.pack()

    tradereport_scrollbar=Scrollbar(tradereport_frame4)
    tradereport_scrollbar.pack(side=RIGHT,fill=Y)

    tradereport_tree=ttk.Treeview(tradereport_frame4,yscrollcommand=tradereport_scrollbar.set)
    tradereport_tree.pack()

    tradereport_scrollbar.config(command=tradereport_tree.yview)

    tradereport_tree['columns']=("ID","SHARE NAME","DATE","PRICE","QUANTITY","BUY/SELL")
    tradereport_tree.column("#0",width=0)
    tradereport_tree.column("ID",anchor=W,width=150,minwidth=150)
    tradereport_tree.column("SHARE NAME",anchor=W,width=150,minwidth=150)
    tradereport_tree.column("DATE",anchor=W,width=150,minwidth=150)
    tradereport_tree.column("PRICE",anchor=W,width=150,minwidth=150)
    tradereport_tree.column("QUANTITY",anchor=W,width=150,minwidth=150)

    tradereport_tree.column("BUY/SELL",anchor=W,width=150)

    tradereport_tree.heading("#0",text="",anchor=W)
    tradereport_tree.heading("ID",text="ID",anchor=W)
    tradereport_tree.heading("SHARE NAME",text="SHARE NAME",anchor=W)
    tradereport_tree.heading("DATE",text="DATE",anchor=W)
    tradereport_tree.heading("PRICE",text="PRICE",anchor=W)
    tradereport_tree.heading("QUANTITY",text="QUANTITY",anchor=W)
    tradereport_tree.heading("BUY/SELL",text="BUY/SELL",anchor=W)

    tradereport_tree.tag_configure('oddrow',background="white")
    tradereport_tree.tag_configure('evenrow',background="#99bccf")

    def on_click1():
        shares_portfolio=list()
        query1="select * from Shares_Portfolio"
        mycursor.execute(query1)
        shares_portfolio=mycursor.fetchall()
        for record in tradereport_tree.get_children():
            tradereport_tree.delete(record)
        count=1
        share_symbol=dropmenu_var4.get()
        fromdate=e1tr.get()
        todate=e2tr.get()
        fy=fromdate[0:4]
        fm=fromdate[5:7]
        fd=fromdate[8:]
        
        ty=todate[0:4]
        tm=todate[5:7]
        td=todate[8:]
        isValidDate1 = True
        try :
            datetime.datetime(int(fy),int(fm),int(fd))
        except ValueError :
            isValidDate1 = False
        
        if(isValidDate1):
            isValidDate2 = True
            try :
                datetime.datetime(int(ty),int(tm),int(td))
            except ValueError :
               isValidDate2 = False
        
            if(isValidDate2):
                start_date=datetime.date(int(fy),int(fm),int(fd))
                end_date=datetime.date(int(ty),int(tm),int(td))
                delta=datetime.timedelta(days=1)
                 
                while start_date<=end_date:
                    for eachrow in shares_portfolio:
                        if share_symbol=="All":
                            if eachrow[2]==start_date:                          
                                count=count+1
                                if count%2==0:
                                    tradereport_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3],eachrow[4],eachrow[5]),tags=('evenrow',))
                                else:
                                    tradereport_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3],eachrow[4],eachrow[5]),tags=('oddrow',))
                        else:
                            if eachrow[1]==share_symbol:
                                if eachrow[2]==start_date:
                                    count=count+1
                                    if count%2==0:
                                        tradereport_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3],eachrow[4],eachrow[5]),tags=('evenrow',))
                                    else:
                                        tradereport_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3],eachrow[4],eachrow[5]),tags=('oddrow',))

                                
                    start_date+=delta
            else:
                e2tr.delete(0,END)
                m2=messagebox.showerror("Tradereport","Incorrect date format,should be YYYY/MM/DD")
        else:
            e1tr.delete(0,END)
            m1=messagebox.showerror("Tradereport","Incorrect date format,should be YYYY-MM-DD")                

    b1=Button(tradereport_frame2,image=enter_button,borderwidth=0,command=on_click1).place(x=130,y=160)

    #holdings

    holdings_frame1=Frame(holdings_frame,background='#083447')
    holdings_frame1.pack(fill=X)
    
    Label(holdings_frame1,text="",background='#083447').pack()
    Label(holdings_frame1,text="PERSONAL FINANCE MANAGEMENT",background='#083447',foreground="white",font=("Verdana", 16,"bold")).pack()
    Label(holdings_frame1,text="",background='#083447').pack()
    logo_label=Label(holdings_frame1,image=logo,borderwidth=0)
    logo_label.place(x=0,y=0)

    holdings_frame2=LabelFrame(holdings_frame,text="Enter Share Details:",foreground='#083447',font=("Verdana", 10,"bold"))
    holdings_frame2.pack(fill="both",expand='yes')
    Label(holdings_frame2,text="").pack()
    Label(holdings_frame2,text="").pack()

    dropmenu_var5=StringVar()

    Label(holdings_frame2,text="Enter Share Name:",width=16,background='white',foreground='#083447',font=("Verdana", 8,"bold")).pack()
    Label(holdings_frame2,text="").pack()
    d5=OptionMenu(holdings_frame2,dropmenu_var5,*share_name2)
    d5.pack()
    dropmenu_var5.set("      ")
    Label(holdings_frame2,text="").pack()
    Label(holdings_frame2,text="Enter Current Price:",width=16,background='white',foreground='#083447',font=("Verdana", 8,"bold")).pack()
    e2h=Entry(holdings_frame2,width=22,font="none 8")
    e2h.pack()
    Label(holdings_frame2,text="").pack()

    def on_click2():
        shares_portfolio=list()
        query1="select * from Shares_Portfolio"
        mycursor.execute(query1)
        shares_portfolio=mycursor.fetchall()
        sname=dropmenu_var5.get()
        if e2h.get().isdigit()==True:
            currentprice=int(e2h.get())
            l=len(shares_portfolio)
            c=0
            qty1=0
            qty2=0
            costprice=0
            for i in range(0,l):
                if (shares_portfolio[i][1]==sname) and (shares_portfolio[i][5]=='BUY'):
                    qty1=qty1+(shares_portfolio[i][4])
                
                if (shares_portfolio[i][1]==sname) and (shares_portfolio[i][5]=='SELL'):
                    qty2=qty2+(shares_portfolio[i][4])
                
                qty3=qty1-qty2
                n=qty3

            for i in range(0,l):
                if (shares_portfolio[i][1]==sname) and (shares_portfolio[i][5]=='BUY'):
                            c=1
                            while qty3>0:
                                    quantity=shares_portfolio[i][4]
                                    price=shares_portfolio[i][3]
                                    if qty3<quantity:
                                            costprice=costprice+qty3*price
                                    if qty3>=quantity:
                                            costprice=costprice+quantity*price
                                            i=i+1
                                    qty3=qty3-quantity

            if c==1:
                currentvalue=n*currentprice
                profit_loss=currentvalue-costprice
                if profit_loss!=0:
                    amtgrowthpercent=(profit_loss/costprice)*100
                else:
                    amtgrowthpercent=0
                for widget in holdings_frame3.winfo_children():
                    widget.config(text="")
                Label(holdings_frame3,text="SHARE SYMBOL:",background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=480,y=20)
                Label(holdings_frame3,text="QUANTITY:",background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=480,y=50)
                Label(holdings_frame3,text="TOTAL COST PRICE:",background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=480,y=80)
                Label(holdings_frame3,text="CURRENT PRICE:",background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=480,y=110)
                Label(holdings_frame3,text="CURRENT VALUE:",background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=480,y=140)
                Label(holdings_frame3,text="PROFIT/LOSS:",background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=480,y=170)
                Label(holdings_frame3,text="AMOUNT GROWTH%:",background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=480,y=200)
                Label(holdings_frame3,text=sname,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=730,y=20)
                Label(holdings_frame3,text=str(n),background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=730,y=50)
                Label(holdings_frame3,text=str(costprice),background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=730,y=80)
                Label(holdings_frame3,text=str(currentprice),background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=730,y=110)
                Label(holdings_frame3,text=str(currentvalue),background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=730,y=140)
                Label(holdings_frame3,text=str(profit_loss),background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=730,y=170)
                Label(holdings_frame3,text=str(amtgrowthpercent),background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=730,y=200)


            else:
                for widget in holdings_frame3.winfo_children():
                    widget.config(text="")
                Label(holdings_frame3,text="SHARE NOT FOUND",background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=280,y=20)
        else:
            e2h.delete(0,END)
            m1=messagebox.showerror("Holdings","Please provide valid Current price")
            

    b2=Button(holdings_frame2,image=enter_button,borderwidth=0,command=on_click2).pack()
    Label(holdings_frame2,text="").pack()

    holdings_frame3=LabelFrame(holdings_frame2,background='white',foreground='#083447',font=("Verdana", 10,"bold"))
    holdings_frame3.pack(fill=BOTH,expand=1)

    #transactionsummary

    transactionsummary_frame1=Frame(transactionsummary_frame,background='#083447')
    transactionsummary_frame1.pack(fill=X)
    
    Label(transactionsummary_frame1,text="",background='#083447').pack()
    Label(transactionsummary_frame1,text="PERSONAL FINANCE MANAGEMENT",background='#083447',foreground="white",font=("Verdana", 16,"bold")).pack()
    Label(transactionsummary_frame1,text="",background='#083447').pack()
    logo_label=Label(transactionsummary_frame1,image=logo,borderwidth=0)
    logo_label.place(x=0,y=0)

    dropmenu_var6=StringVar()

    transactionsummary_frame2=LabelFrame(transactionsummary_frame,text="Enter Share Details:",foreground='#083447',font=("Verdana", 10,"bold"))
    transactionsummary_frame2.pack(fill="both",expand='yes')
    Label(transactionsummary_frame2,text="").pack()
    Label(transactionsummary_frame2,text="").pack()


    def on_click3():
        shares_portfolio=list()
        query1="select * from Shares_Portfolio"
        mycursor.execute(query1)
        shares_portfolio=mycursor.fetchall()
        l=len(shares_portfolio)
        global share_name
        share_name=list()
        for eachrow in shares_portfolio:
            var=eachrow[1]
            if var not in share_name:
                share_name.append(var)
        li=len(share_name)
        
        global amtgrowthlist
        amtgrowthlist=list()
        c=0
        qty=0
        cost=0
        costprice=0
        for i in range(0,li):
            sname=share_name[i]
            for i in range(0,l):
                    if (shares_portfolio[i][1]==sname) and (shares_portfolio[i][5]=='SELL'):
                            qty=qty+(shares_portfolio[i][4])
                            cost=cost+(shares_portfolio[i][3]*shares_portfolio[i][4])
                            c=1


            n=qty
            for i in range(0,l):
                    if (shares_portfolio[i][1]==sname and shares_portfolio[i][5]=='BUY'):
                            while qty>0:
                                    quantity=shares_portfolio[i][4]
                                    price=shares_portfolio[i][3]
                                    if qty<quantity:
                                            costprice=costprice+qty*price
                                    if qty>=quantity:
                                            costprice=costprice+quantity*price
                                            i=i+1
                                    qty=qty-quantity


            if n!=0:
                avgsellprice=cost/n
                totalprice=n*avgsellprice
                profit_loss=totalprice-costprice
                amtgrowthpercent=(profit_loss/costprice)*100
                amtgrowthlist.append(amtgrowthpercent)
                qty=0
            else:
                amtgrowthpercent=0
                amtgrowthlist.append(amtgrowthpercent)


        plt.bar(share_name,amtgrowthlist, label="profit",color='#083447',width=0.8)

        plt.legend()
        plt.xlabel('Share Symbol')
        plt.ylabel('Realised Profit')

        plt.title('Realised Profit')

        plt.show()
    


    b3=Button(transactionsummary_frame2,image=realisedprofit_button,borderwidth=0,command=on_click3).pack()
    Label(transactionsummary_frame2,text="").pack()

    Label(transactionsummary_frame2,text="Enter Share Name:",width=16,background='white',foreground='#083447',font=("Verdana", 8,"bold")).pack()
    Label(transactionsummary_frame2,text="").pack()
    d6=OptionMenu(transactionsummary_frame2,dropmenu_var6,*share_name2)
    d6.pack()
    dropmenu_var6.set("      ")
    Label(transactionsummary_frame2,text="").pack()

    def on_click4():
        shares_portfolio=list()
        query1="select * from Shares_Portfolio"
        mycursor.execute(query1)
        shares_portfolio=mycursor.fetchall()        
        sname=dropmenu_var6.get()        
        l=len(shares_portfolio)
        c=0
        qty=0
        cost=0
        costprice=0
        for i in range(0,l):
                if (shares_portfolio[i][1]==sname) and (shares_portfolio[i][5]=='SELL'):
                        qty=qty+(shares_portfolio[i][4])
                        cost=cost+(shares_portfolio[i][3]*shares_portfolio[i][4])
                        c=1


        n=qty
        for i in range(0,l):
                if (shares_portfolio[i][1]==sname and shares_portfolio[i][5]=='BUY'):
                        while qty>0:
                                quantity=shares_portfolio[i][4]
                                price=shares_portfolio[i][3]
                                if qty<quantity:
                                        costprice=costprice+qty*price
                                if qty>=quantity:
                                        costprice=costprice+quantity*price
                                        i=i+1
                                qty=qty-quantity


        if c==1:
                avgsellprice=cost/n
                totalprice=n*avgsellprice
                profit_loss=totalprice-costprice
                amtgrowthpercent=(profit_loss/costprice)*100
                for widget in transactionsummary_frame3.winfo_children():
                    widget.config(text="")

                Label(transactionsummary_frame3,text="SHARE SYMBOL:",background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=480,y=20)
                Label(transactionsummary_frame3,text="QUANTITY:",background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=480,y=50)
                Label(transactionsummary_frame3,text="TOTAL COST PRICE:",background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=480,y=80)
                Label(transactionsummary_frame3,text="AVERAGE SELLING PRICE :",background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=480,y=110)
                Label(transactionsummary_frame3,text="TOTAL SELLING PRICE:",background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=480,y=140)
                Label(transactionsummary_frame3,text="PROFIT/LOSS:",background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=480,y=170)
                Label(transactionsummary_frame3,text="AMOUNT GROWTH%:",background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=480,y=200)
                Label(transactionsummary_frame3,text=sname,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=730,y=20)
                Label(transactionsummary_frame3,text=str(n),background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=730,y=50)
                Label(transactionsummary_frame3,text=str(costprice),background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=730,y=80)
                Label(transactionsummary_frame3,text=str(avgsellprice),background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=730,y=110)
                Label(transactionsummary_frame3,text=str(totalprice),background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=730,y=140)
                Label(transactionsummary_frame3,text=str(profit_loss),background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=730,y=170)
                Label(transactionsummary_frame3,text=str(amtgrowthpercent),background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=730,y=200)

        else:
            for widget in transactionsummary_frame3.winfo_children():
                    widget.config(text="")
            Label(transactionsummary_frame3,text="SHARE NOT FOUND",background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=230,y=20)



    b4=Button(transactionsummary_frame2,image=enter_button,borderwidth=0,command=on_click4).pack()
    Label(transactionsummary_frame2,text="").pack()

    transactionsummary_frame3=LabelFrame(transactionsummary_frame2,background='white',foreground='#083447',font=("Verdana", 10,"bold"))
    transactionsummary_frame3.pack(fill=BOTH,expand=1)

    #yearlygrowth

    yearlygrowth_frame1=Frame(yearlygrowth_frame,background='#083447')
    yearlygrowth_frame1.pack(fill=X)

    Label(yearlygrowth_frame1,text="",background='#083447').pack()
    Label(yearlygrowth_frame1,text="PERSONAL FINANCE MANAGEMENT",background='#083447',foreground="white",font=("Verdana", 16,"bold")).pack()
    Label(yearlygrowth_frame1,text="",background='#083447').pack()
    logo_label=Label(yearlygrowth_frame1,image=logo,borderwidth=0)
    logo_label.place(x=0,y=0)


    yearlygrowth_frame2=LabelFrame(yearlygrowth_frame,text="Edit Share Details:",foreground='#083447',font=("Verdana", 10,"bold"))
    yearlygrowth_frame2.pack(fill="both",expand='yes')

    Label(yearlygrowth_frame2,text="").pack()
    Label(yearlygrowth_frame2,text="").pack()

    dropmenu_var7=StringVar()

    Label(yearlygrowth_frame2,text="Enter Share Name:",width=16,background='white',foreground='#083447',font=("Verdana", 8,"bold")).pack()
    Label(yearlygrowth_frame2,text="").pack()
    d7=OptionMenu(yearlygrowth_frame2,dropmenu_var7,*share_name2)
    d7.pack()
    dropmenu_var7.set("      ")
    Label(yearlygrowth_frame2,text="").pack()


    style=ttk.Style()

    style.configure("Treeview.Heading",foreground='#083447',font=("Consolas", 10,"bold"))
    style.configure("Treeview",rowheight=25,background="#D3D3D3",foreground="black",fieldbackground="#D3D3D3",font=("Times", 8))

    style.map('Treeview',background=[('selected','#083447')])

    yearlygrowth_frame3=LabelFrame(yearlygrowth_frame)
    yearlygrowth_frame3.pack(fill=X)
    yearlygrowth_frame4=Frame(yearlygrowth_frame3)
    yearlygrowth_frame4.pack()

    yearlygrowth_scrollbar=Scrollbar(yearlygrowth_frame4)
    yearlygrowth_scrollbar.pack(side=RIGHT,fill=Y)

    yearlygrowth_tree=ttk.Treeview(yearlygrowth_frame4,yscrollcommand=yearlygrowth_scrollbar.set)
    yearlygrowth_tree.pack()

    yearlygrowth_scrollbar.config(command=yearlygrowth_tree.yview)

    yearlygrowth_tree['columns']=("ID","SHARE NAME","DATE","PRICE","QUANTITY","BUY/SELL","YEARLY GROWTH")
    yearlygrowth_tree.column("#0",width=0)
    yearlygrowth_tree.column("ID",anchor=W,width=150,minwidth=150)
    yearlygrowth_tree.column("SHARE NAME",anchor=W,width=150,minwidth=150)
    yearlygrowth_tree.column("DATE",anchor=W,width=150,minwidth=150)
    yearlygrowth_tree.column("PRICE",anchor=W,width=150,minwidth=150)
    yearlygrowth_tree.column("QUANTITY",anchor=W,width=150,minwidth=150)
    yearlygrowth_tree.column("BUY/SELL",anchor=W,width=150)
    yearlygrowth_tree.column("YEARLY GROWTH",anchor=W,width=150)

    yearlygrowth_tree.heading("#0",text="",anchor=W)
    yearlygrowth_tree.heading("ID",text="ID",anchor=W)
    yearlygrowth_tree.heading("SHARE NAME",text="SHARE NAME",anchor=W)
    yearlygrowth_tree.heading("DATE",text="DATE",anchor=W)
    yearlygrowth_tree.heading("PRICE",text="PRICE",anchor=W)
    yearlygrowth_tree.heading("QUANTITY",text="QUANTITY",anchor=W)
    yearlygrowth_tree.heading("BUY/SELL",text="BUY/SELL",anchor=W)
    yearlygrowth_tree.heading("YEARLY GROWTH",text="YEARLY GROWTH",anchor=W)

    yearlygrowth_tree.tag_configure('oddrow',background="white")
    yearlygrowth_tree.tag_configure('evenrow',background="#99bccf")

    shares_portfolio=list()
    query1="select * from Shares_Portfolio"
    mycursor.execute(query1)
    shares_portfolio=mycursor.fetchall()
    l=len(shares_portfolio)

    
    def on_click5():
        sname=dropmenu_var7.get()
        costprice=0
        n=0
        qty2=0
        global count
        count=1
        for record in yearlygrowth_tree.get_children():
            yearlygrowth_tree.delete(record)
        for eachrow in shares_portfolio:
            if eachrow[1]==sname and eachrow[5]=='BUY':
                fromdate=eachrow[2]
                break
        for eachrow in shares_portfolio:
            if eachrow[1]==sname and eachrow[5]=='SELL':
                
                count=count+1
                todate=eachrow[2]
                costprice=0
                qty1=eachrow[4]
                price1=eachrow[3]
                sellprice=qty1*price1
                for i in range(0,l):
                    if shares_portfolio[i][1]==sname:
                        while qty1>0:
                            if shares_portfolio[i][5]=='BUY' and qty2<=0:
                                qty2=shares_portfolio[i][4]
                                price2=shares_portfolio[i][3]
                            if qty1<qty2:
                                costprice=costprice+qty1*price2
                                qty3=qty1
                            if qty1>=qty2:
                                costprice=costprice+qty2*price2
                                qty3=qty2
                                i=i+1
                            qty2=qty2-qty1
                            qty1=qty1-qty3
                if todate==fromdate:
                    no_days=1
                    profit_loss=sellprice-costprice
                    yg=(profit_loss*(365/no_days)*(100/costprice))                    
                else:
                    days_string=str(todate-fromdate)
                    d=days_string.split(" ")
                    no_days=int(d[0])
                    profit_loss=sellprice-costprice
                    yg=(profit_loss*(365/no_days)*(100/costprice))
                if count%2==0:
                    yearlygrowth_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3],eachrow[4],eachrow[5],yg),tags=('evenrow',))
                else:
                    yearlygrowth_tree.insert(parent='',index='end',iid=count,text="",values=(eachrow[0],eachrow[1],eachrow[2],eachrow[3],eachrow[4],eachrow[5],yg),tags=('oddrow',))

                
    b5=Button(yearlygrowth_frame2,image=enter_button,borderwidth=0,command=on_click5).pack()    

    footer_frame=Frame(analysis_window,background='#083447')
    footer_frame.pack(fill=X)
    Label(footer_frame,text="",background='#083447').pack()

    

##########################################################################################################################################################################################################

def marketdata_analysis():
    analysis_window=Toplevel()
    analysis_window.title("MARKET DATA ANALYSIS")
    analysis_window.geometry("1500x650")
    
    analysis_nb=ttk.Notebook(analysis_window)
    analysis_nb.pack(fill=BOTH,expand=1)

    annualdata_frame=Frame(analysis_nb)

    analysis_nb.add(annualdata_frame,text="ANNUAL DATA CALCULATIONS")

    #annualdatacalculation

    annualdata_frame1=Frame(annualdata_frame,background='#083447')
    annualdata_frame1.pack(fill=X)

    Label(annualdata_frame1,text="",background='#083447').pack()
    Label(annualdata_frame1,text="PERSONAL FINANCE MANAGEMENT",background='#083447',foreground="white",font=("Verdana", 16,"bold")).pack()
    Label(annualdata_frame1,text="",background='#083447').pack()
    logo_label=Label(annualdata_frame1,image=logo,borderwidth=0)
    logo_label.place(x=0,y=0)


    share_info=list()
    query1="select annualinfo_id,Share_Symbol,annual_infoyear,totalrevenue,otherincome,totalexpense,financecost,depr_amortexpense,pat,net_profit,equity_currentyear,equity_previousyear,totalassets_currentyear,totalassets_previousyear,PBT,Tax,Debt from share_info,company_annualinfo where share_info.share_id=company_annualinfo.share_id order by annual_infoyear asc"
    mycursor.execute(query1)
    share_info=mycursor.fetchall()
    l=len(share_info)

    dropmenu_var8=StringVar()

    share_info0=list()
    query0="select * from share_info"
    mycursor.execute(query0)
    share_info0=mycursor.fetchall()

    share_name=['   ']
    for eachrow in share_info0:
        var=eachrow[1]
        if var not in share_name:
            share_name.append(var)


    Label(annualdata_frame,text="").pack()


    style=ttk.Style()

    style.configure("Treeview.Heading",foreground='#083447',font=("Consolas", 10,"bold"))
    style.configure("Treeview",rowheight=25,background="#D3D3D3",foreground="black",fieldbackground="#D3D3D3",font=("Times", 8))

    style.map('Treeview',background=[('selected','#083447')])

    annualdata_frame2=LabelFrame(annualdata_frame)
    annualdata_frame2.pack(fill=X)
    annualdata_frame3=Frame(annualdata_frame2)
    annualdata_frame3.pack()

    annualdata_scrollbar1=Scrollbar(annualdata_frame3)
    annualdata_scrollbar1.pack(side=RIGHT,fill=Y)

    annualdata_scrollbar2=Scrollbar(annualdata_frame3,orient='horizontal')
    annualdata_scrollbar2.pack(side=BOTTOM,fill=X)

    annualdata_tree=ttk.Treeview(annualdata_frame3,yscrollcommand=annualdata_scrollbar1.set,xscrollcommand=annualdata_scrollbar2.set)
    annualdata_tree.pack()

    annualdata_scrollbar1.config(command=annualdata_tree.yview)
    annualdata_scrollbar2.config(command=annualdata_tree.xview)


    annualdata_tree['columns']=("Share Symbol","Year","EBITDA","EBITDA margin","PAT margin","Return on equity","Asset Turnover","Financial Leverage","RoE_DuPont","Return on Asset","Overall Capital Employed","Return on Capital Employed")
    annualdata_tree.column("#0",width=0)
    annualdata_tree.column("Share Symbol",anchor=W,width=100,minwidth=100)
    annualdata_tree.column("Year",anchor=W,width=100,minwidth=100)
    annualdata_tree.column("EBITDA",anchor=W,width=150,minwidth=150)
    annualdata_tree.column("EBITDA margin",anchor=W,width=150,minwidth=150)
    annualdata_tree.column("PAT margin",anchor=W,width=150,minwidth=150)
    annualdata_tree.column("Return on equity",anchor=W,width=150,minwidth=150)
    annualdata_tree.column("Asset Turnover",anchor=W,width=180,minwidth=180)
    annualdata_tree.column("Financial Leverage",anchor=W,width=180,minwidth=180)
    annualdata_tree.column("RoE_DuPont",anchor=W,width=180,minwidth=180)
    annualdata_tree.column("Return on Asset",anchor=W,width=180,minwidth=180)
    annualdata_tree.column("Overall Capital Employed",anchor=W,width=180,minwidth=180)
    annualdata_tree.column("Return on Capital Employed",anchor=W,width=180,minwidth=180)


    annualdata_tree.heading("#0",text="",anchor=W)
    annualdata_tree.heading("Share Symbol",text="Share Symbol",anchor=W)
    annualdata_tree.heading("Year",text="Year",anchor=W)
    annualdata_tree.heading("EBITDA",text="EBITDA",anchor=W)
    annualdata_tree.heading("EBITDA margin",text="EBITDA margin",anchor=W)
    annualdata_tree.heading("PAT margin",text="PAT margin",anchor=W)
    annualdata_tree.heading("Return on equity",text="Return on equity",anchor=W)
    annualdata_tree.heading("Asset Turnover",text="Asset Turnover",anchor=W)
    annualdata_tree.heading("Financial Leverage",text="Financial Leverage",anchor=W)
    annualdata_tree.heading("RoE_DuPont",text="RoE_DuPont",anchor=W)
    annualdata_tree.heading("Return on Asset",text="Return on Asset",anchor=W)
    annualdata_tree.heading("Overall Capital Employed",text="Overall Capital Employed",anchor=W)
    annualdata_tree.heading("Return on Capital Employed",text="Return on Capital Employed",anchor=W)



    annualdata_tree.tag_configure('oddrow',background="white")
    annualdata_tree.tag_configure('evenrow',background="#99bccf")

    annualdata_tree.insert(parent='',index='end',iid=0,text="",values=(""),tags=('evenrow',))

    annualdata_frame4=LabelFrame(annualdata_frame,text="Edit Share Details:",foreground='#083447',font=("Verdana", 10,"bold"))
    annualdata_frame4.pack(fill="both",expand='yes')

    def on_click1():
        global info
        info=list()
        for i in range(0,l):
            if share_info[i][1]==dropmenu_var8.get():
                calculations=list()
                EBITDA=(share_info[i][3]-share_info[i][4])-(share_info[i][5]-share_info[i][6]-share_info[i][7])
                EBITDAmargin=(EBITDA/(share_info[i][3]- share_info[i][4]))*100
                PATmargin=(share_info[i][8]/share_info[i][3])*100
                avgEQUITY=(share_info[i][10]+share_info[i][11])/2
                ROE_simple=(share_info[i][9]/avgEQUITY)*100
                NetProfitmargin=PATmargin
                NetSALES=share_info[i][3]
                avgTOTALASSETS=(share_info[i][12]+share_info[i][13])/2
                AssetTurnover=NetSALES/avgTOTALASSETS
                FinancialLeverage=avgTOTALASSETS/avgEQUITY
                ROE_DuPont=NetProfitmargin*AssetTurnover*FinancialLeverage
                NetIncome=share_info[i][8]
                Interest=share_info[i][6]
                TaxRate=share_info[i][15]/share_info[i][14]
                ROA=((NetIncome+Interest*(1-TaxRate))/avgTOTALASSETS)*100
                PBIT=share_info[i][14]-Interest
                OverallCapitalEmployed=share_info[i][16]+share_info[i][10]
                ROCE=(PBIT/OverallCapitalEmployed)*100
                calculations=[share_info[i][1],share_info[i][2],EBITDA,EBITDAmargin,PATmargin,ROE_simple,AssetTurnover,FinancialLeverage,ROE_DuPont,ROA,OverallCapitalEmployed,ROCE]
                info.append(calculations)
        
        le=len(info)
        for record in annualdata_tree.get_children():
            annualdata_tree.delete(record)
        annualdata_tree.insert(parent='',index='end',iid=0,text="",values=(""),tags=('evenrow',))
        global count
        count=1
        for i in range(0,le):
            if count%2==0:
                annualdata_tree.insert(parent='',index='end',iid=count,text="",values=(info[i][0],info[i][1],info[i][2],info[i][3],info[i][4],info[i][5],info[i][6],info[i][7],info[i][8],info[i][9],info[i][10],info[i][11]),tags=('evenrow',))
            else:
                annualdata_tree.insert(parent='',index='end',iid=count,text="",values=(info[i][0],info[i][1],info[i][2],info[i][3],info[i][4],info[i][5],info[i][6],info[i][7],info[i][8],info[i][9],info[i][10],info[i][11]),tags=('oddrow',))
            count=count+1

    def graph_revenuepat():
        year=list()
        revenue=list()
        pat=list()
        try:
            for i in range(0,l):
                if share_info[i][1]==dropmenu_var8.get():
                    year.append(share_info[i][2])
                    revenue.append(share_info[i][3])
                    pat.append(share_info[i][8])

            plt.bar(year,revenue,label="revenue",color='#083447',width=0.8)

            plt.bar(year,pat,label="profit after tax",color='#99bccf',width=0.5)

            plt.legend()
            plt.xlabel('Year')
            plt.ylabel('Revenue and Profit after Tax')

            plt.title('Revenue and Profit after Tax(₹ crore)')

            plt.show()
            
        except:
            m1=messagebox.showerror("Company Annual Info","No sufficient data")
            
        
    Label(annualdata_frame4,text="").pack()
    Label(annualdata_frame4,text="Enter Share Name:",width=16,background='white',foreground='#083447',font=("Verdana", 8,"bold")).pack()
    Label(annualdata_frame4,text="").pack()
    d8=OptionMenu(annualdata_frame4,dropmenu_var8,*share_name)
    d8.pack()
    dropmenu_var8.set("      ")
    Label(annualdata_frame4,text="").pack()

    b1=Button(annualdata_frame4,image=enter_button,borderwidth=0,command=on_click1).pack()
    Label(annualdata_frame4,text="").pack()
    b2=Button(annualdata_frame4,image=revenuepat_button,borderwidth=0,command=graph_revenuepat).pack()

    Label(annualdata_frame4,text="",background='#083447',width=1000).place(x=0,y=240)

    footer_frame=Frame(analysis_window,background='#083447')
    footer_frame.pack(fill=X)
    Label(footer_frame,text="",background='#083447').pack()

##########################################################################################################################################################################################################

def login():
    login_window=Toplevel()
    login_window.title("LOGIN")
    login_window.geometry("400x325")

    login_frame1=Frame(login_window,background='#083447')
    login_frame1.pack(fill=BOTH,expand=1)

    login_frame2=LabelFrame(login_frame1)
    login_frame2.pack(fill=BOTH,padx=40,pady=40,expand=1)

    Label(login_frame2,text="LOGIN",width=25,background='white',foreground="#083447",font=("Verdana", 14,"bold")).pack()

    Label(login_frame2,text="Username:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=22,y=80)
    e1=Entry(login_frame2,width=20,font="none 8")
    e1.place(x=170,y=80)

    Label(login_frame2,text="Password:",width=18,background='white',foreground='#083447',font=("Verdana", 8,"bold")).place(x=22,y=120)
    e2=Entry(login_frame2,width=20,show='*',font="none 8")
    e2.place(x=170,y=120)

    def on_click1():
        username=e1.get()
        password=e2.get()

        if username in userdict:

            password=e2.get()               
            if password==userdict[username]:
                e1.delete(0,END)
                e2.delete(0,END)
                b0.destroy()
                login_window.destroy()              
                
                b1=Button(menu_window,image=maintenance_t,command=maintenance_transactions).place(x=435,y=160)
                b2=Button(menu_window,image=maintenance_md,command=maintenance_marketdata).place(x=635,y=160)
                b3=Button(menu_window,image=analysis_t,command=transaction_analysis).place(x=435,y=265)
                b4=Button(menu_window,image=analysis_md,command=marketdata_analysis).place(x=635,y=265)
                b5=Button(menu_window,image=exit_button,command=quit).place(x=530,y=370)
    
                                
            else:
                e2.delete(0,END)
                m1=messagebox.showerror("Login","Invalid Password")
        else:
            e1.delete(0,END)
            m1=messagebox.showerror("Login","User is not a valid user of the system")

    b1=Button(login_frame2,image=enter_button,borderwidth=0,command=on_click1).place(x=100,y=160)

    




###############################################################################################################################################################    

b0=Button(menu_window,image=login_button,borderwidth=0,command=login)
b0.place(x=550,y=200)

################################################################################################################################################################


root_window.mainloop













































