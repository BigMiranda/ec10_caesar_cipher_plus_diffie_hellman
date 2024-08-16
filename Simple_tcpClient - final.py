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
serverName = "10.1.70.5"
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#Salva a sentença
sentence = input("Bob message: ")

#Salva x
x = int(input("Bob, inform your X: "))
if not verifica_primo(x):
    print("Invalid number (not prime)")
    raise error

#1 - Envia R1
G = 7
N = 23
R1 = pow(G,x) % N
#Nesse caso R1 = 21
clientSocket.send(bytes(str(R1), "utf-8"))

#4 - Recebe R2
receivedR2 = clientSocket.recv(65000)
R2 = int(str(receivedR2, "utf-8"))

#Calula K
K = pow(R2,x) % N
#K = 18

#Criptografar com a chave K
#Add Cifra de Cesar
encrypted = ""
for char in sentence:
    encrypted += chr((ord(char) + K))
sentence = encrypted

#5- Envia a mensagem criptografada
clientSocket.send(bytes(sentence, "utf-8"))
modifiedSentence = clientSocket.recv(65000)
text = str(modifiedSentence,"utf-8")
print ("Received from Server: ", text)

input()

clientSocket.close()