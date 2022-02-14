import json
import socket

s = socket.socket()
s.connect(('127.0.0.1', 9001))


def receiveFileDetails():
    jdata = json.loads(s.recv(1024).decode())
    filenames = jdata.get("filenames")
    return filenames


def receiveFile(filename):
    buff = 2 ** 20
    file = open("C:/Users/Manikanta Reddy/Documents/test/" + filename[0], 'wb')
    filesize = filename[1]
    # ----------------------------------------------------
    # if file size is less than buff size
    if buff > filesize:
        rbytes = s.recv(filesize)
        file.write(rbytes)
        return
    # -----------------------------------------------------
    # if file size is greater than buff
    for i in range(filesize // buff):
        rbytes = s.recv(buff)
        file.write(rbytes)
    rbytes = s.recv(filesize % buff)
    file.write(rbytes)
    return
    # ------------------------------------------------------


def receive1():
    filenames = receiveFileDetails()
    for i in filenames:
        receiveFile(i)


receive1()
