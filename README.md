# ec10_caesar_cipher_plus_diffie_hellman
EC10: Diffie-Hellman + Caesar Cipher

Matheus Vinicius Miranda Brito          081200024

Gabriel Mendes Barbosa                  081200037

Gabriel Nunes Alves Santos              081200038

Matheus Vital dos Santos de Oliveira    081210042


TCP Client-Server with Diffie-Hellman Key Exchange and Caesar Cipher
This project implements a simple TCP client-server communication system with basic encryption using the Diffie-Hellman key exchange protocol combined with a Caesar cipher for message encryption and decryption.

Project Structure
Simple_tcpServer.py: The server-side script that handles incoming connections, performs the Diffie-Hellman key exchange, and decrypts messages from the client.
Simple_tcpClient.py: The client-side script that connects to the server, performs the Diffie-Hellman key exchange, and encrypts the message before sending it.
Features
Diffie-Hellman Key Exchange:

The client and server generate a shared secret key (K) using the Diffie-Hellman key exchange. The base (G) and the prime number (N) used are hardcoded as 7 and 23, respectively.
The server prompts the user for Y (private key), and the client prompts for X (private key). The exchanged public values are used to compute the shared secret key.
Message Encryption:

After generating the shared key, the client encrypts the message using a Caesar cipher. The shift value for the cipher is the shared key K.
Message Decryption:

The server receives the encrypted message and decrypts it using the same key K.
How to Run
Start the Server:

Run Simple_tcpServer.py.
The server will wait for a connection from the client.
When a client connects, you will be prompted to enter your private key Y (must be a prime number).
Start the Client:

Run Simple_tcpClient.py.
The client will connect to the server using the specified IP address and port.
You will be prompted to enter your private key X (must be a prime number) and the message to send.
Exchange and Communication:

The client sends its public value R1 to the server.
The server responds with its public value R2.
The client encrypts the message using the shared key K and sends it to the server.
The server decrypts the message and displays both the encrypted and decrypted versions.
Example Execution
Server Side:

Run Simple_tcpServer.py.
Enter the prime number Y when prompted (e.g., 5).
Wait for and process the incoming encrypted message.
Client Side:

Run Simple_tcpClient.py.
Enter the prime number X when prompted (e.g., 6).
Enter the message you wish to send to the server (e.g., Hello).
Output:

The server displays the received message both in its encrypted and decrypted form.
Requirements
Python 3.x
Note
Ensure that the client and server use prime numbers for their private keys X and Y.
The IP address and port used in the scripts should match the environment where the server is hosted.
