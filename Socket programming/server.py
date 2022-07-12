import socket
import threading

# ------------------------ General Variables----------------------------------
PORT = 5050  # socket port number

# Automatically getting the host IP address
SERVER = input('Ip address: ')

# Byte size to recieve
HEADER = 1024

# UTF- decoding format(UTF-8)
FORMAT = 'utf-8'

# DISCONNECT Variable to print disconnect message
DISCONNECT = '!Disconnect'
clients = []
clients_lock = threading.Lock()
aliases = []

# -------------------- connecting sockets -------------------
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ADDR = (SERVER, PORT)
server.bind(ADDR)  # Binding the server and port
server.listen()

def broadcast(message):
    for client in clients:
        client.send(message)


def handle_client(client):
    while True:
        try:
            message = client.recv(HEADER)
            broadcast(message)
            print(message)

        except:
            index =  clients.index(client)
            clients.remove(client)
            client.close()
            alias= aliases[index]
            broadcast(f'{alias}has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)
            break
    
def recv():
    while True:
        print('Server is running and waiting for connections.....')
        client, address = server.accept()
        print(f'{str(address)} connected to the server')
        client.send('alias?'.encode(FORMAT))
        alias = client.recv(HEADER)
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of this client is {alias}'.encode(FORMAT))
        broadcast(f'{alias} has joined the party 🎉🎊'.encode(FORMAT))
        client.send('You are now connected 😎'.encode(FORMAT))
        thread = threading.Thread(target= handle_client, args=(client,))
        thread.start()

if __name__ == '__main__':
    recv()