import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = "localhost", 12345
server_socket.bind((host, port))
server_socket.listen(5)
print(f"Server listening on {host}:{port}")
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Received connection from {client_address}")
    welcome_message = "Welcome ! You are connected."
    client_socket.send(welcome_message.encode())
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode()
        if "Hi?" in message:
            response = "Hi! Type Roll number to check ID."
        elif "Roll number?" in message:
            response = "AP21110010443"
        elif "exit?" in message:
            response = "bye"
        else:
            response = "Wrong Input, Please Try Again."
        client_socket.send(response.encode())
    client_socket.close()
server_socket.close()