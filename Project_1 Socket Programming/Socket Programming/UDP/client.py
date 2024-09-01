from socket import *

serverName = "localhost"
serverPort = 476

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Input a sentence:")
clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print("Server response:", modifiedMessage.decode())

print(modifiedMessage.decode())

clientSocket.close()