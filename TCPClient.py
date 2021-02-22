import sys
import socket
from lib import Lib


HOST = "10.0.0.1"
PORT = 9000
BUFSIZE = 1000

def main(argv):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Connection established.")
        s.sendall(b'/home/ase/Desktop/NGK-exercise6/hello.txt\0')
        receiveFile("/home/ase/Desktop/NGK-exercise6/hello.txt",s)
        s.close()
        print("Connection closed")
    
def receiveFile(fileName,  conn):
    file = open(fileName,"w")
    print("Writing file.")
    file.write(Lib.readTextTCP(conn))
    file.close()
    print("File closed.")

if __name__ == "__main__":
   main(sys.argv[1:])
