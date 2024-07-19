import socket
client = socket.socket()
client.connect(('192.168.217.118', 61111))
while True:
    client.send(input('You : ').encode())
    result = client.recv(1024).decode()
    if result == 'Thank You':
        print('Server :',result)
        client.close()
        break
    print('Server :',result)
