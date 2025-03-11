
import socket
import threading
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
messages = []
name = None
client = None
room = None

def receive_messages(client_socket):
    name = True
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            messages.append(message)
            
        except:
            print("Connection closed.")
            client_socket.close()
            break
      
@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    global name, room, client

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('0.0.0.0', 447))
        print("Connected to server.")
    except socket.timeout:
        print("Connection timed out. Please check the server IP and port.")
        return
    except Exception as e:
        print(f"Connection error: {e}")
        return

    # Start thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()
    
    if 'name' in request.form:
        name = request.form['name']
        room = request.form['room']
        client.send(name.encode('utf-8'))
        client.send(room.encode('utf-8'))

    return redirect(url_for('chat'))


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    global name, client

    if request.method == 'POST':
        # Send message
        message = request.form['message']
        if message.lower() == "exit":
            print("Closing connection...")
            client.send(message.encode('utf-8'))
            client.close()
    
        if message:
            client.send(f"{name}: {message}".encode('utf-8'))

    return render_template('chat.html', messages=messages)


if __name__ == "__main__":
    app.run(debug=True)