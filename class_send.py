import socket
import json
import os
import threading

filesarray =os.listdir("Ready to go/")
class send:
    def __init__(self):
        self.filesent="Files Sent: 00"
        self.complete=1

    def estcon(self):
        self.s = socket.socket()
        port = 60323
        self.s.bind(('', port))
        self.s.listen(5)
        self.connection, address = self.s.accept()

    def sendlist(self,file):
        self.connection.send(json.dumps({"filenames":file}).encode())


    def filenameextractor(self, filesarray):
        filenamesarray = []
        for i in range(len(filesarray)):
            filenamesarray.append([os.path.split(filesarray[i])[1], os.path.getsize("Ready to go/"+filesarray[i])])
        self.connection.send(json.dumps({"filenames": filenamesarray}).encode())

    def sendfile(self, filepath):
        buff = 2 ** 20
        file = open("Ready to go/"+filepath, 'rb')
        re = file.read(buff)
        while len(re):
            self.connection.send(re)
            re = file.read(buff)
        # print(filepath)
        return
    def sendfiles(self,filesarray):
        count=0
        for i in filesarray:
            self.sendfile(i)
            count=count+1
            self.filesent="Files Sent: "+str(count)
        self.filesent="All Fragments are Sent\nYou can close now"
        self.complete=0
        self.connection.close()

# if __name__ == "__main__":
#     a=send()
#     a.estcon()
#     a.filenameextractor(filesarray)
#     a.sendfiles(filesarray)