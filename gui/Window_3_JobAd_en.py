# Form implementation generated from reading ui file 'Window_3_JobAd_en.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Window_1_Start(object):
    def setupUi(self, Window_1_Start):
        Window_1_Start.setObjectName("Window_1_Start")
        Window_1_Start.resize(1000, 800)
        Window_1_Start.setStyleSheet("background-color: rgb(220, 138, 221);")
        self.centralwidget = QtWidgets.QWidget(parent=Window_1_Start)
        self.centralwidget.setObjectName("centralwidget")
        self.welcoming_text_1 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.welcoming_text_1.setGeometry(QtCore.QRect(0, 50, 1000, 60))
        self.welcoming_text_1.setAutoFillBackground(True)
        self.welcoming_text_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.welcoming_text_1.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.welcoming_text_1.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.welcoming_text_1.setLineWidth(0)
        self.welcoming_text_1.setObjectName("welcoming_text_1")
        self.next_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(650, 705, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.next_button.setFont(font)
        self.next_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.next_button.setObjectName("next_button")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 139, 900, 549))
        self.plainTextEdit.setStyleSheet("background-color: rgb(252, 240, 251);")
        self.plainTextEdit.setOverwriteMode(True)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.back_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(150, 705, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.back_button.setObjectName("back_button")
        Window_1_Start.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Window_1_Start)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        Window_1_Start.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Window_1_Start)
        self.statusbar.setObjectName("statusbar")
        Window_1_Start.setStatusBar(self.statusbar)

        self.retranslateUi(Window_1_Start)
        QtCore.QMetaObject.connectSlotsByName(Window_1_Start)

    def retranslateUi(self, Window_1_Start):
        _translate = QtCore.QCoreApplication.translate
        Window_1_Start.setWindowTitle(_translate("Window_1_Start", "LazyApp"))
        self.welcoming_text_1.setHtml(_translate("Window_1_Start", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">Which job do you want to apply for?</span></p></body></html>"))
        self.next_button.setText(_translate("Window_1_Start", "NEXT ->"))
        self.plainTextEdit.setPlainText(_translate("Window_1_Start", "Please copy and paste the advertising for your dream job here."))
        self.back_button.setText(_translate("Window_1_Start", "<- BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window_1_Start = QtWidgets.QMainWindow()
    ui = Ui_Window_1_Start()
    ui.setupUi(Window_1_Start)
    Window_1_Start.show()
    sys.exit(app.exec())