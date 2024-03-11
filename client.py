import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = "localhost"
server_port = 12345
client_socket.connect((server_host, server_port))
welcome_message = client_socket.recv(1024).decode()
print("Received from server:", welcome_message)
while True:
    message_to_server = input("Your message to the server (type 'exit' to quit): ")
    client_socket.send(message_to_server.encode())
    if message_to_server.lower() == "exit":
        break
    response_from_server = client_socket.recv(1024).decode()
    print("Received from server:", response_from_server)
client_socket.close()