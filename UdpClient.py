from email import message
from socket import *

serverName = '127.0.0.1'
serverPort = 12000


clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowcase sentence:')

clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, severAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
