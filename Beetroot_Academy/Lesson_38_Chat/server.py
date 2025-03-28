import socket
import threading

SERVER_HOST = '127.0.0.1' # localhost
SERVER_PORT = 4567

# client_sockets = set()
client_database = {} # замість client_sockets; {conn:['admin', 'new_room'], conn1:['sys', 'default']}
rooms = {} # {room_name:password}

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # уточнити
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)

print(f'Listening on {SERVER_HOST}:{SERVER_PORT}')

def listen_for_message(connection):
    while True:
        try:
            message = connection.recv(1024).decode()
            if len(message.split()) == 3:
                command_or_message, room_name, password_or_new_room_name = tuple(message.split()) # for create, join, rename
            else:
                command_or_message, room_name, password = message, client_database[connection][1], None # for others commands or messages
        except Exception as exp:
            print(f'Fail to recieve with {exp}')
            continue

        if command_or_message =='/list':
            connection.send(str(list(rooms.keys())).encode())
        elif command_or_message =='/create':
            rooms[room_name] = password_or_new_room_name
            client_database[connection] = ['admin', room_name]
            connection.send(f'Reconect to {room_name}'.encode())
        elif command_or_message =='/join':
            if rooms.get(room_name) == password_or_new_room_name:
                client_database[connection] = ['user', room_name]
                connection.send(f'You are conect to {room_name}'.encode())
            else:
                connection.send('Wrong name or password'.encode())
        elif command_or_message =='/rename':
            if client_database[connection] == ['admin', room_name]:
                client_database[connection][1]=password_or_new_room_name
                connection.send(f'{room_name} rename to {password_or_new_room_name}'.encode())
            else:
                connection.send("You are not admin".encode())
        elif command_or_message == '/exit':
            client_database[connection] = ['sys', 'default']
            connection.send(f'Logout from {room_name}'.encode())
        else:
            room_client = dict(filter(lambda x: room_name == x[1][1], client_database.items()))
            # for client in client_database:
            for client in room_client:
                client.send(message.encode())

while True:
    client_connection, client_address = server_socket.accept()
    print(f'{client_address} connected')
    # client_sockets.add(client_connection)
    client_database[client_connection] = ['sys', 'default']
    task = threading.Thread(target=listen_for_message, args=(client_connection,), daemon=True)
    task.start()