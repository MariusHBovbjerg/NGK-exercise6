import sys
import socket
from lib import Lib

HOST = ""
PORT = 9001
BUFSIZE = 1000

def main(argv):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by ', addr)
            while True:
                data = Lib.readTextTCP(conn)
                print("yo ", data, " ", Lib.check_File_Exists(data))
                if (Lib.check_File_Exists(data)):
                    print(":)")
                    sendFile(data,conn)

def sendFile(fileName, conn):
    file = open(fileName,"r")
    TEXTBUF = file.read(BUFSIZE)
    print("Read: ",len(TEXTBUF))
    while(TEXTBUF):
        #Lib.writeTextTCP(TEXTBUF,conn)
        conn.send(TEXTBUF.encode())
        TEXTBUF = file.read(BUFSIZE)
        print(len(TEXTBUF))
    conn.send(b'\0')
    file.close
    print("File closed")

if __name__ == "__main__":
   main(sys.argv[1:])
