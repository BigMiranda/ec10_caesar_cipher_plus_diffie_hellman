def verifica_primo(N):
    #primo fast

    i = 2
    while i < N:
        R = N % i
        if R == 0:
            return False
        i += 1
    else:
        return True


from socket import *
serverPort = 12500
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(5) # o argumento “listen” diz à biblioteca de soquetes que queremos enfileirar no máximo 5 requisições de conexão (normalmente o máximo) antes de recusar começar a recusar conexões externas. Caso o resto do código esteja escrito corretamente, isso deverá ser o suficiente.
print ("TCP Server\n")
connectionSocket, addr = serverSocket.accept()
sentence = connectionSocket.recv(65000)

#Salva y
y = int(input("Alice, inform your Y: "))
if not verifica_primo(y):
    print("Invalid number (not prime)")
    raise error

#2 - Recebe R1
receivedR1 = str(sentence,"utf-8")
R1 = int(receivedR1)

#3 - Envia R2
G = 7
N = 23
R2 = pow(G,y) % N
#Nesse caso R2 = 4
connectionSocket.send(bytes(str(R2), "utf-8"))

#Calcula K
K = pow(R1,y) % N
#K = 18

#6 - Recebe do client a mensagem criptografada
sentence = connectionSocket.recv(65000)
receivedMsg = str(sentence,"utf-8")

#Descriptografar com a chave K
#Subtract Cifra de Cesar
decrypted = ""
for char in receivedMsg:
    decrypted += chr((ord(char) - K))

#Mostra a mensagem descriptografada
print ("Received From Bob (encriptado): ", receivedMsg)
print ("Received From Bob (decriptado): ", decrypted)

input()

capitalizedSentence = "Sucesso!"
connectionSocket.send(bytes(capitalizedSentence, "utf-8"))
print("Sent back to Client: ", capitalizedSentence)
connectionSocket.close()