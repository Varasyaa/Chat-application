import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

def receive_messages(client_socket, text_widget):
    while True:
        message = client_socket.recv(1024).decode()
        if message.lower() == 'exit':
            client_socket.close()
            break
        text_widget.insert(tk.END, f"Server: {message}\n")
        text_widget.yview(tk.END)

def send_message(client_socket, message_entry):
    message = message_entry.get()
    if message.lower() == 'exit':
        client_socket.send(message.encode())
        client_socket.close()
        root.quit()
    else:
        client_socket.send(message.encode())
    message_entry.delete(0, tk.END)

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))
    
    # Setting up the GUI
    global root
    root = tk.Tk()
    root.title("Chat Application")

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
    text_area.pack(padx=10, pady=10)
    text_area.config(state=tk.DISABLED)

    message_entry = tk.Entry(root, width=40)
    message_entry.pack(padx=10, pady=5)

    send_button = tk.Button(root, text="Send", command=lambda: send_message(client, message_entry))
    send_button.pack(padx=10, pady=5)

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client, text_area))
    receive_thread.start()

    root.mainloop()

if __name__ == "__main__":
    start_client()
