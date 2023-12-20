import socket
import pickle


class Network:
    """The class of network connection

    :param client: client that connected to the server
    :type client: socket.socket
    :param server: the IP adress of the server
    :type server: str
    :param port: the port of the server
    :type port: int
    :param addr: the whole address of server
    :type addr: tuple
    :param p: the connection to the server
    :type p: Network.client.recv() - str

    """

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        """Taking the connection status

        """
        return self.p

    def connect(self):
        """Connection to the server

        """
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except BaseException:
            pass

    def send(self, data):
        """The function of sending message to the server

        :param data: message to the server
        :type data: str
        :returns: the deserialized response from the server
        :rtype: any
        :raises socket.error: If it was an error trying to send data

        """
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048 * 2))
        except socket.error as e:
            print(e)
