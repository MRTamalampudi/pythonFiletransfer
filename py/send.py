import socket
import json
import os

s = socket.socket()
port = 9000
s.bind(('', port))
s.listen(5)
connection, addr = s.accept()
filesarray = ["C:/Users/Manikanta Reddy/Pictures/dhoni.jpg", "C:/Users/Manikanta Reddy/Desktop/links.txt"]


def sendpasscode(text):
    connection.send(text.eccode())
def fileSize():
    filesizearray = []
    for i in filesarray:
        filesizearray.append(os.path.getsize(i))
    return filesizearray


def filenameextractor(filesarray):
    filenamesarray = []
    for i in range(len(filesarray)):
        filenamesarray.append([os.path.split(filesarray[i])[1], os.path.getsize(filesarray[i])])
    connection.send(json.dumps({"filenames": filenamesarray}).encode())


def sendFile(filePath):
    buff = 2 ** 20
    file = open(filePath, 'rb')
    re = file.read(buff)
    while len(re):
        connection.send(re)
        re = file.read(buff)
    return


def sendfiles():
    for i in filesarray:
        sendFile(i)


filenameextractor(filesarray)
sendfiles()
