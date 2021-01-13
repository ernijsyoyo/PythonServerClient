# Implemented after this https://pythontic.com/modules/socket/udp-client-server-example
import socket

class Server():
  def __init__(self, ipAddress = "127.0.0.1", port=6969):
    # Variable setup
    self.localIP     = ipAddress
    self.localPort   = port
    self.bufferSize  = 1024

    # Create a datagram socket
    self.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to address and ip
    self.UDPServerSocket.bind((self.localIP, self.localPort))
    print("UDP server up and listening on endpoint {0}:{1}".format(self.localIP, self.localPort))


  def MainEntry(self):
    # Listen for incoming datagrams
    while(True):
      bytesAddressPair = self.UDPServerSocket.recvfrom(self.bufferSize)
      message = bytesAddressPair[0]
      address = bytesAddressPair[1]
      msgDecoded = message.decode('utf-8')
      
      if (msgDecoded == "/initialize"):
        print("Initializing . . .")
      
      elif (msgDecoded == "/sendPos"):
        print("Sending Position . . .")

      else:
        print("Unknown message: ", msgDecoded)


if __name__ == "__main__":
  serv = Server()
  serv.MainEntry()