import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(5)
    print("Server is listening on port 12345...")

    while True:
        client_socket, client_address = server.accept()
        print(f"Connection from {client_address} has been established.")
        
        client_socket.send("Welcome to the chat!".encode())
        
        while True:
            message = client_socket.recv(1024).decode()
            if message.lower() == 'exit':
                print("Closing connection.")
                client_socket.send("Goodbye!".encode())
                client_socket.close()
                break
            print(f"Client: {message}")
            response = input("Server: ")
            client_socket.send(response.encode())

if __name__ == "__main__":
    start_server()
