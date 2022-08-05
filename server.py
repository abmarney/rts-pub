import socket
from _thread import *
from player import Player
import pickle

# Creates a client connection instance on a separate thread and handles information transfer between clients.
#   connection_socket = socket given from connection to server socket
#   player = the specific player for the thread
def threaded_client(connection_socket, player):
    connection_socket.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(connection_socket.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

            connection_socket.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    connection_socket.close()
    exit()

#Values are for internal network, cannot be accessed outside of network
server = "192.168.1.113"
port = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((server, port))
except socket.error as error:
    str(error)

server_socket.listen(2)
print("Waiting for a connection, Server Started")

# Hard coded values for 2 Players.
players = [Player(10, 10, (255,0,0), (255,102,102)), Player(100, 100, (0,0,255), (102,102,255))]

# Initializes the current player to position 0 for hard coded values
current_player = 0

while True:
    connection_socket, address = server_socket.accept()
    print("Connected to:", address)

    start_new_thread(threaded_client, (connection_socket, current_player))
    current_player += 1