import socket
import threading

def receive_messages(client_socket):
    name = True
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{message}")
        except:
            print("Connection closed.")
            client_socket.close()
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("balls")
    try:
        client.connect(('0.0.0.0', 447))
        print("Connected to server.")
    except socket.timeout:
        print("Connection timed out. Please check the server IP and port.")
        return
    except Exception as e:
        print(f"Connection error: {e}")
        return
    
    
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()
    
    send_name = True
    send_room = True
    while True:
        try:
            if send_name:
                message = input("What is Your Name? ")
                name = message
                send_name = False
            elif send_room:
                message = input("Which room would you like to join? ")
                send_room = False
            else:
                l = input("")
                if l.lower() == "exit":
                    print("Closing connection...")
                    client.send(l.encode('utf-8'))
                    client.close()
                    break
                if l:
                    print("\033[F", end='')
                    print(f'Me: {l}')
                message = f"{name}: {l}"
            client.send(message.encode('utf-8'))
        except BrokenPipeError:
            print("Connection was closed by the server.")
            break
        except Exception as e:
            print(f"Error sending message: {e}")
            break

        

if __name__ == "__main__":
    start_client()
