import threading

from ui_send import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
import os
import threading
from class_send import send
import class_send

class mainwindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.filear=[]

        # -----------------Buttons ---------------------
        self.ui.send.clicked.connect(self.sendmakesure)
        self.ui.makesurenext.clicked.connect(self.showsendfiles)
        self.ui.readytogonext.clicked.connect(self.fgout)
        # -----------------Buttons ---------------------


    def show(self):
        self.main_win.show()

    def filesentthread(self):
        while 1:
            if self.s.complete:
                self.ui.filessent.setText(self.s.filesent)
            else:
                self.ui.label_3.setPixmap(QtGui.QPixmap("resources/completed.svg"))
                self.ui.filessent.setText(self.s.filesent)
                break

    def stest(self):
        self.s = send()
        self.s.estcon()
        self.s.sendlist(self.filear)
        self.s.filenameextractor(class_send.filesarray)
        threading.Thread(target=self.filesentthread).start()
        self.s.sendfiles(class_send.filesarray)
    def sendmakesure(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.makesure)
        # --------------To display ready to go files & file size --------------
        self.i = os.listdir("Ready to go/")
        for j in self.i:
            a = os.path.getsize("Ready to go/" + j)
            if a > 1024 and a < (1048576):
                a = a / 1024
                a = "%.2f" % a  # to round decimals upto two points
                a = str(a) + " KB"
            elif a > (1048576) and a < (1073741824):
                a = a / (1048576)
                a = "%.2f" % a  # to round decimals upto two points
                a = str(a) + " MB"
            elif a > (1073741824):
                a = a / (1073741824)
                a = "%.2f" % a  # to round decimals upto two points
                a = str(a) + " GB"
            else:
                a = str(a) + " B"
            k=j + "  (" + str(a) + ")"
            self.filear.append(k)
            self.ui.listWidget.addItem(k)
        # ---------------------------------------------------------------------

    def showsendfiles(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.readytogo)

    def fgout(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.fragementsareout)
        t1=threading.Thread(target=self.stest)
        t1.start()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = mainwindow()
    main_win.show()
    sys.exit(app.exec_())
