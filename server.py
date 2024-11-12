import socket

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = '127.0.0.1'  # Localhost
server_port = 12345        # Port number

# Start the server
server_socket.bind((server_host, server_port))
server_socket.listen(1)
print("Server is listening...")

# Accept a connection from the client
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

# Message receiving and sending loop
while True:
    # Receive message from client
    client_message = client_socket.recv(1024).decode()
    if client_message.lower() == 'exit':
        print("Connection closed by client.")
        break
    print(f"Client: {client_message}")

    # Send message from server
    server_message = input("Server: ")
    client_socket.send(server_message.encode())
    if server_message.lower() == 'exit':
        break

# Close the connection
client_socket.close()
server_socket.close()
