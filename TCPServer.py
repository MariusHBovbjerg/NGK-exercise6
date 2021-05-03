import sys
import socket
from lib import Lib

HOST = ""
PORT = 9000
BUFSIZE = 1000

def main(argv):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Listen")
        while True:
            conn, addr = s.accept()
            print("accepted")
            while conn:
                print('Connected by', addr, ".")
                
                data = Lib.readTextTCP(conn)
                filesize = Lib.check_File_Exists(data)
                if (filesize):
                    filesizeStr = str(filesize) + '\0'
                    conn.send(filesizeStr.encode())
                    sendFile(data,conn)
                else:
                    filesizeStr = str(filesize) + '\0'
                    conn.send(filesizeStr.encode())
                conn.close()
                conn = None
                print("Connection closed")

def sendFile(fileName, conn):
    file = open(fileName,"rb")
    TEXTBUF = file.read(BUFSIZE)
    print("Read:",len(TEXTBUF), ".")
    while(TEXTBUF):
        conn.send(TEXTBUF)
        TEXTBUF = file.read(BUFSIZE)
        print("Read:",len(TEXTBUF),".")
    file.close
    print("File closed.")

if __name__ == "__main__":
   main(sys.argv[1:])
