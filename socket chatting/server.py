
import socket

server=socket.socket()

server.bind(('192.168.217.118', 61111))

server.listen()

client_socket,client_address=server.accept()

print('Got a connection ',client_address)
while True:
    result=client_socket.recv(1024).decode()
    if result.upper() == 'BYE':
        client_socket.send('Thank You'.encode())
        client_socket.close()
        server.close()
        break
    print("Client :",result)
    client_socket.send(input('Server : ').encode( ))

 
 
 
