import socket
import threading
import sys

clients = []
client_rooms = {}
thread = True

def handle_client(client_socket):
    global thread
    while thread:
        try:
            client_socket.settimeout(1.0)  # Set a timeout to avoid blocking indefinitely
            message = client_socket.recv(1024).decode('utf-8')

            if not thread:
                break

            if message.lower() == "exit":
                print("Closing client connection...")
                clients.remove(client_socket)
                client_socket.close()
                break

            if not message:
                break

            print(f"Received message from {message} to room {client_rooms.get(client_socket)}")
            file = open(client_rooms.get(client_socket), 'a')
            file.write(message + "\n")
            file.close()
            
            for client in clients:
                if client != client_socket and client_rooms.get(client) == client_rooms.get(client_socket):
                    client.send(message.encode('utf-8'))
                    
        except socket.timeout:
            continue
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def close_server(server):
    global thread
    shut_down = input("Type 'y' to close the server:\n")
    if shut_down.lower() == "y":
        print("Shutting down the server...")
        thread = False
        server.close()
        for client in clients:
            client.close()
        sys.exit()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.settimeout(1.0)  # Set a timeout for the server's accept call
    server.bind(('0.0.0.0', 447))
    server.listen(5)
    print("Server started, waiting for connections...")

    shutdown_thread = threading.Thread(target=close_server, args=(server,))
    shutdown_thread.start()

    while thread:
        try:
            client_socket, addr = server.accept()
            name = client_socket.recv(1024).decode('utf-8')
            room = client_socket.recv(1024).decode('utf-8')
            print(f"Accepted connection from {name}, joined {room}...")
            
            clients.append(client_socket)
            client_rooms[client_socket] = room.lower() + ".txt"
            print(client_rooms.get(client_socket))
            
            try:
                chatHist = open(client_rooms.get(client_socket), 'r')
            except FileNotFoundError:
                print("File not found. Creating a new one.")
                chatHist = open(client_rooms.get(client_socket), 'w')
                chatHist.close()
                chatHist = open(client_rooms.get(client_socket), 'r')
                
            text = chatHist.read()
            chatHist.close()
            
            client_socket.send(text.encode('utf-8'))
            


            
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
        except socket.timeout:
            continue
        except OSError:
            break

    shutdown_thread.join()

if __name__ == "__main__":
    start_server()
