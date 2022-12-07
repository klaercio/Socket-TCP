from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ("O servidor está pronto para receber")

while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	soma = str(eval(sentence.decode())).encode()
	connectionSocket.send(soma)
	connectionSocket.close()