import socket

HOST = 'localhost'
PORT = 10000


def client():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:

        filename = input('Enter the name of the file to send->')

        if filename == 'exit':
            break

        with open(filename, 'rb') as f:
            s.sendfile(f)

        data = s.recv(1024)
        if not data:
            break
        else:
            print(data.decode('utf-8'))

    s.close()


if __name__ == "__main__":
    client()
