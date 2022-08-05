import socket
import pickle

# Handles connections to server
#
class Network:
    
    # Initializes network information
    #   self.server, self. port specifically match server.py values
    #
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.113"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.player = self.connect()

    # Generates a new connection for this player.
    #
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            return 'There was an error connecting to the server.'

    # Returns player this connection handles.
    #
    def get_player(self):
        return self.player
    
    # Sends updated game data to the server.
    #   data = object containing various game data
    #
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)