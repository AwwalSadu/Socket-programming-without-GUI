import socket 
import threading
import sys 

#------------------------ General Variables----------------------------------
PORT = 5050 # socket port number 

# Input Alias

alias = input('Enter name here: ')

# Input the getting the host IP address
SERVER = input('Ip address: ')

# Byte size to recieve
HEADER = 1024

# UTF- decoding format(UTF-8)
FORMAT = 'utf-8'

# DISCONNECT Variable to print disconnect message
DISCONNECT  = '! Disconnect'

# ADDR variable 
ADDR = (SERVER,PORT)

#------------ Connecting server and placing server type-------

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send():
    while True:
        try:
           message = f'{alias}: {input("")}'
           client.send(message.encode(FORMAT))
        except:
            break


def receive():
    while True:
        try:
            recv = client.recv(HEADER).decode(FORMAT)
            if recv == 'alias?':
                client.send(alias.encode(FORMAT))
            else:
                print(recv)
        except:
            print('Sorry, An error occured!')
            client.close()
            break   


send_thread = threading.Thread(target=send)
send_thread.start()

receive_thread = threading.Thread(target=receive())
receive_thread.start()



    #192.168.43.27