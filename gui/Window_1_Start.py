# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import Window_2_Input


class Ui_Window_1_Start(object):
  
  
    def setupUi(self, Window_1_Start):
        Window_1_Start.setObjectName("Window_1_Start")
        Window_1_Start.resize(1000, 800)
        Window_1_Start.setStyleSheet("background-color: rgb(220, 138, 221);")
        self.centralwidget = QtWidgets.QWidget(parent=Window_1_Start)
        self.centralwidget.setObjectName("centralwidget")
        self.welcoming_text_1 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.welcoming_text_1.setGeometry(QtCore.QRect(0, 270, 1001, 51))
        self.welcoming_text_1.setAutoFillBackground(True)
        self.welcoming_text_1.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.welcoming_text_1.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.welcoming_text_1.setLineWidth(0)
        self.welcoming_text_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.welcoming_text_1.setObjectName("welcoming_text_1")
        self.start_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(410, 440, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")

        # give function to Start button
        self.start_button.clicked.connect(self.start_button_clicked)


        self.welcoming_text_2 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.welcoming_text_2.setGeometry(QtCore.QRect(0, 140, 1001, 121))
        self.welcoming_text_2.setAutoFillBackground(True)
        self.welcoming_text_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.welcoming_text_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.welcoming_text_2.setLineWidth(0)
        self.welcoming_text_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.welcoming_text_2.setObjectName("welcoming_text_2")
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
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">to the laziest way of applying for a new job!</span></p></body></html>"))
        self.start_button.setText(_translate("Window_1_Start", "START"))
        self.start_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.welcoming_text_2.setHtml(_translate("Window_1_Start", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt; font-weight:700;\">WELCOME</span></p></body></html>"))

    def start_button_clicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Window_2_Input.Ui_Window_2_Input()
        self.ui.setupUi(self.window)
        Window_1_Start.hide()
        self.window.show()

    def start_button_clicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Window_2_Input.Ui_Window_2_Input()
        self.ui.setupUi(self.window)
        Window_1_Start.Ui_Window_1_Start.hide()
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window_1_Start = QtWidgets.QMainWindow()
    ui = Ui_Window_1_Start()
    ui.setupUi(Window_1_Start)
    Window_1_Start.show()
    sys.exit(app.exec())
