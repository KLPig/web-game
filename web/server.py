import socket
import os
import sys
from _thread import *
from database import config as db_config

class Server:
    ip = socket.gethostbyname(socket.gethostname())
    port = 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def on_handle(self, bytes_data, address) -> str:
        pass

    def on_close(self, address):
        pass

    def __init__(self):
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(5)
        print("Server started on port", self.port)

    def start(self):
        while True:
            client_socket, address = self.server_socket.accept()
            print("Connected with", address)
            start_new_thread(self.client_thread, (client_socket, address))

    def client_thread(self, client_socket, address):
        client_socket.send("Welcome to the server!".encode())
        while True:
            bytes_data = client_socket.recv(1024)
            print("Received:", bytes_data.decode(), f"({address})")
            if not bytes_data:
                break
            if bytes_data.decode() in ['exit', 'quit', 'close']:
                response = "Error: Exit command inputted."
            elif bytes_data.decode() == "getAddr":
                response = f"Address: {address[0]}:{address[1]}"
            else:
                try:
                    response = self.on_handle(bytes_data, address)
                except Exception as e:
                    print(f"Error: {e}")
                    response = "Error: " + str(e)
                except ConnectionResetError:
                    break
            print( "Returned:", response, f"({address})")
            client_socket.send(response.encode())
            if response.startswith("Error:"):
                break
        self.on_close(address)
        client_socket.close()
        print(f"Connection closed on {address}")
