import socket
import threading

SERVER_HOST = '127.0.0.1' # localhost
SERVER_PORT = 4567

client_socket = socket.socket()
print(f'Connecting on {SERVER_HOST}:{SERVER_PORT}')
client_socket.connect((SERVER_HOST, SERVER_PORT))
print(f'Connected')

name = input('Enter your name:')

def listen_for_message():
    while True:
        message = client_socket.recv(1024).decode()
        print(message)

task = threading.Thread(target=listen_for_message, daemon=True)
task.start()

commands = """ All available commands
/list : Get all rooms
/create room_name password : Create new room
/join  room_name password : Join to existing room
/rename room_name new_room_name : Rename room by administrator
/exit : Exit from current room
/close : Close program  
"""

print(commands)

while True:
    # # send = input('[*]: ')
    # if send == 'q':
    #     break
    # to_send = f'{name}: {send}'
    # client_socket.send(to_send.encode())
    send = input()
    if send.split()[0] in ['/list', '/create', '/join', '/rename', '/exit']:
        client_socket.send(send.encode())
    elif send.split()[0] == '/close':
        client_socket.close()
        break
    else:
        to_send = f'{name}: {send}'
        client_socket.send(to_send.encode())