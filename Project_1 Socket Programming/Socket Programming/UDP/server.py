from socket import *

serverPort = 476
serverName = "localhost"

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind((serverName, serverPort))

print(f"Server listening on port {serverPort}")

lastMessages = {}
while True:
    message, client_address = server_socket.recvfrom(2048)
    message = message.decode()

    lastMessages[client_address] = message

    print(f"Received message from {client_address}: {message}")

    response = f"Server received your message: {message}"
    server_socket.sendto(response.encode(), client_address)

    print("Last received messages from all peers:")
    for clientAdd, msg in lastMessages.items():
        print(f"From {clientAdd}: {msg}")