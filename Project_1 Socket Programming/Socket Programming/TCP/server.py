def replace_vowels(text):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        text = text.replace(vowel, '#')
    return text

from socket import *
serverPort = 1020
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    
    sentence = connectionSocket.recv(1024).decode()
    newSentence = replace_vowels(sentence)
    connectionSocket.send(newSentence.encode())
    connectionSocket.close()


