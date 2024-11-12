import socket

# Set up the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = '127.0.0.1'  # Localhost
server_port = 12345        # Server's port number

# Connect to the server
client_socket.connect((server_host, server_port))
print("Connected to the server.")

# Message receiving and sending loop
while True:
    # Send message from client
    client_message = input("Client: ")
    client_socket.send(client_message.encode())
    if client_message.lower() == 'exit':
        break

    # Receive message from server
    server_message = client_socket.recv(1024).decode()
    if server_message.lower() == 'exit':
        print("Connection closed by server.")
        break
    print(f"Server: {server_message}")

# Close the connection
client_socket.close()
