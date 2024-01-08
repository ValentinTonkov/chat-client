import socket


def send_message():
    server_address = ("192.168.1.142", 1080)  # change the ip address
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(server_address)
        msg = input("send: ")
        client_socket.sendall(msg.encode('utf-8'))

        response = client_socket.recv(64)
        print("recv: " + response.decode('utf-8'))

    finally:
        client_socket.close()


if __name__ == '__main__':
    while True:
        send_message()
