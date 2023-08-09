import socket
import threading
import datetime

import mysql
import mysql.connector 
conn= mysql.connector.connect(host="localhost", user="root",passwd="password",database="WeTalk")
cur=conn.cursor()

hostname=socket.gethostname()
port=1234
active_clients=[]
ip_address='127.0.0.1'
print(ip_address)

def send_message(choice,message,username):
    if choice=='1':
        split_message=message.split('?')
        username=split_message[0]
        content=split_message[1]
        date=split_message[2]
        q="insert into message(username, messages, sent_time) values ('{0}','{1}','{2}')".format(username,content,date)
        cur.execute(q)
        conn.commit()
        message=choice+message
        print(message)
        for i in active_clients:
            i[1].sendall(message.encode())
    elif choice=='2':
        q1="select * from message"
        cur.execute(q1)
        history=str(cur.fetchall())
        h=choice+history
        for i in active_clients:
            if i[0]==username:
                user=i[1]
        user.sendall(h.encode())
    elif choice=='3':
        split_message=message.split('?')
        search=split_message[1]
        q2="select * from message where messages like '%{}%'".format(search)
        cur.execute(q2)
        search=str(cur.fetchall())
        s=choice+search
        for i in active_clients:
            if i[0]==username:
                user=i[1]
        user.sendall(s.encode())

def listen(client,username):
    while True:
        message1=client.recv(2048).decode('utf-8')
        message2=message1.split(';')
        choice=message2[0]
        final_message= username+'?'+ message2[1]+'?'+str(datetime.datetime.now())
        send_message(choice,final_message,username)
        
 

def handle(client):
    while True:
        username=client.recv(2048).decode('utf-8')
        print(username)
        if username!='':
            active_clients.append([username,client])
            break
        else:
            print("username empty")


    threading.Thread(target=listen,args=(client,username)).start()



def connection():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        server.bind((ip_address,port))
        print("server running")
    except:
        print("not running")

    server.listen(5)

    while True:
        global client
        global address
        client,address=server.accept() 
        print("succesfully connected to client")

        threading.Thread(target=handle,args=(client,)).start()

connection()

