import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))
    
    welcome_message = client.recv(1024).decode()
    print(welcome_message)

    while True:
        message = input("Client: ")
        client.send(message.encode())

        if message.lower() == 'exit':
            print("Closing connection.")
            client.close()
            break
        
        response = client.recv(1024).decode()
        print(f"Server: {response}")

if __name__ == "__main__":
    start_client()
