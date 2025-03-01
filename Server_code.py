import socket
import threading

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if message.lower() == 'exit':
            client_socket.send("Goodbye!".encode())
            client_socket.close()
            break
        print(f"Client: {message}")
        response = input("Server: ")
        client_socket.send(response.encode())

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(5)
    print("Server is listening on port 12345...")

    while True:
        client_socket, client_address = server.accept()
        print(f"Connection from {client_address} has been established.")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
