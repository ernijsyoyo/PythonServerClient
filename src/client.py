# Implemented after this https://pythontic.com/modules/socket/udp-client-server-example
import socket

class Client():
  def __init__(self, ipAddress = "127.0.0.1", port = 6969):
    self.serverAddressPort   = (ipAddress, port)
    self.bufferSize      = 1024
    # Create a UDP socket at client side
    self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

  def SendMessage(self, msg: str):
    msg = str.encode(msg)
    self.UDPClientSocket.sendto(msg, self.serverAddressPort)

  def SendInput(self):
    while(True):
      sec = input('Enter message to transmit: ')
      if(sec == "q"):
        break
      msg = str.encode(sec)
      self.UDPClientSocket.sendto(msg, self.serverAddressPort)

if __name__ == "__main__":
    client = Client()
    client.SendInput()

    
