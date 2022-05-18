import socket




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("212.76.128.141", 2000))
server.listen(4)
print('Starting...')
while(True):
    client_socket, address = server.accept()
    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    #HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=uft-8\r\n\r\n'
    content = "I ebal tvou mamku".encode('utf-8')
    client_socket.send(content)
print('Server close !')