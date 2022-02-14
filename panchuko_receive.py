from ui_receive import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from class_receive import receive
import threading

class mainwindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.recieve.clicked.connect(self.enterip)
        self.ui.ipnext.clicked.connect(self.waiting)
        self.filelist=[]
    def show(self):
        self.main_win.show()
    def enterip(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.enterip)
        self.r=receive()

    def filenamethread(self):
        while (1):
            # self.filename=self.r.filename
            if self.r.complete:
                self.ui.filename.setText(self.r.filename)
                self.ui.filecount.setText(str(self.r.filecount))
                self.ui.filepercent.setText(self.r.filepercent)
            else:
                self.ui.filename.setText(self.r.filename)
                self.ui.filecount.setText(str(self.r.filecount))
                self.ui.filepercent.setText(self.r.filepercent)
                break


    def ests(self):
        self.ip = self.ui.ip1.text() + "." + self.ui.ip2.text() + "." + self.ui.ip3.text() + "." + self.ui.ip4.text()
        self.r = receive()
        self.r.estcon(self.ip)
        self.r.recievelist(self.filelist)
        self.percent()
        # self.ui.filerecievenext.clicked.connect(self.percent)
        filename = self.r.receivefiledetails()
        filenameThread=threading.Thread(target=self.filenamethread)
        filenameThread.start()
        self.r.receive1(filename)
        return
    def waiting(self):
        threading.Thread(target=self.ests).start()
        self.ui.stackedWidget.setCurrentWidget(self.ui.waiting)
    def filereceive(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.filereceive)
        for i in self.filelist:
            self.ui.listWidget_2.addItem(i)
    def percent(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.percent)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = mainwindow()
    main_win.show()
    sys.exit(app.exec_())