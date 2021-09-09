import socket

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 4444))
    server.listen()

    print('Waiting for client to connect...')

    client, address = server.accept()

    print('Client connection is established')

    while True:
        data = client.recv(1024).decode()
        print(data)
