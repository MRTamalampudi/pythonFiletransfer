import json
import socket
from ui_receive import Ui_MainWindow
filer=[]
class receive:
    def __init__(self):
        self.filecount=0
        self.filename="filename"
        self.filepercent="0%"
        self.complete=1
    def estcon(self,ip):
        self.s = socket.socket()
        self.s.connect(("127.0.0.1",60323))


    def recievelist(self,file):

        jdata=json.loads(self.s.recv(1024).decode())
        filearray=jdata.get('filenames')
        for i in filearray:
            file.append(i)

    def receivefiledetails(self):
        jdata = json.loads(self.s.recv(1024).decode())
        filenames = jdata.get('filenames')
        return filenames

    def receiveFile(self, filename):
        self.filepercent="0%"
        self.filename=filename[0]
        buffc=0
        buff = 2 ** 20
        file = open("Received Files/" + filename[0], 'wb')
        filesize = filename[1]
        # ----------------------------------------------------
        # if file size is less than buff size
        if buff > filesize:
            rbytes = self.s.recv(filesize)
            file.write(rbytes)
            self.filepercent="100%"
            return
        # -----------------------------------------------------
        # if file size is greater than buff
        for i in range(filesize // buff):
            buffc=buffc+buff
            rbytes = self.s.recv(buff)
            file.write(rbytes)
            self.filepercent=str("%.2f"%((buffc/filesize)*100))+"%"
        self.filepercent = "100%"
        rbytes = self.s.recv(filesize % buff)

        file.write(rbytes)

        return
        # ------------------------------------------------------

    def receive1(self,filename):
        for i in filename:
            self.receiveFile(i)
            self.filecount = self.filecount + 1
        self.filename="All Fragments are assembled"
        self.filepercent=""
        self.complete = 0

# if __name__ == "__main__":
#     a = receive()
#     a.estcon("127.0.0.1")
#     filename=a.receivefiledetails()
#     print(filename)
#     a.receive1(filename)
