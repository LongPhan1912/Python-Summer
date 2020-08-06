# Exploring the HyperText Transport Protocol
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) #open file call
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512) #reads the data
    if len(data) < 1:
        break
    print(data.decode(),end='') #decodes the data from UTF-8

mysock.close()
