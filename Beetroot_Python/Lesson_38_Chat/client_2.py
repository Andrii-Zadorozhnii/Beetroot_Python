import socket
import threading

SERVER_HOST = '127.0.0.1'  # localhost
SERVER_PORT = 4567

client_socket = socket.socket()

# Подключение к серверу
try:
    print(f'Connecting on {SERVER_HOST}:{SERVER_PORT}')
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f'Connected')
except Exception as e:
    print(f"Failed to connect: {e}")
    exit(1)

name = input('Enter your name: ')


def listen_for_message():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                print("Server disconnected")
                break
            print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

    client_socket.close()


task = threading.Thread(target=listen_for_message, daemon=True)
task.start()

while True:
    try:
        send = input('[*]: ')
        if send == 'q':
            break
        to_send = f'{name}: {send}'
        client_socket.send(to_send.encode())
    except Exception as e:
        print(f"Error sending message: {e}")
        break

client_socket.close()
print("Connection closed")
