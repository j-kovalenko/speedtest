# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_before.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 606)
        MainWindow.setStyleSheet("QWidget#centralwidget {\n"
                                 "    background-color:  rgb(41, 41, 41);\n"
                                 "}\n"
                                 "QPushButton#statBut {\n"
                                 "    background-color: rgb(216, 243, 220);\n"
                                 "    border-style: outset;\n"
                                 "    border-width: 2px;\n"
                                 "    border-radius: 10px;\n"
                                 "    border-color: rgb(20, 33, 61);\n"
                                 "    font: bold 14px;\n"
                                 "    min-width: 10em;\n"
                                 "    padding: 6px;\n"
                                 "}\n"
                                 "QTextEdit#txtinput {\n"
                                 "    background-color: rgb(216, 243, 220);\n"
                                 "    border-radius: 10px\n"
                                 "}\n"
                                 "QTextBrowser#textBrowser {\n"
                                 "    border-radius: 10px;\n"
                                 "    background-color: rgb(237, 224, 212);\n"
                                 "}\n"
                                 "QPushButton#startBut {\n"
                                 "    background-color: rgb(144, 190, 109);\n"
                                 "    border-style: outset;\n"
                                 "    border-width: 2px;\n"
                                 "    border-radius: 10px;\n"
                                 "    border-color: rgb(20, 33, 61);\n"
                                 "    font: bold 14px;\n"
                                 "    min-width: 5em;\n"
                                 "    padding: 6px;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 50, 641, 71))
        self.label.setObjectName("label")
        self.statBut = QtWidgets.QPushButton(self.centralwidget)
        self.statBut.setGeometry(QtCore.QRect(630, 530, 186, 28))
        self.statBut.setStyleSheet("color: rgb(8, 28, 21);\n"
                                   "font-family: \"Lucida Console\" monospace;")
        self.statBut.setObjectName("statBut")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(90, 150, 651, 121))
        self.textBrowser.setStyleSheet("border-radius: 10px;\n"
                                       "font-family: MS Shell Dlg 2;\n"
                                       "font-size: 7.8pt;\n"
                                       "font-weight: 400;\n"
                                       "font-style:normal;\n"
                                       "font-size:10pt;\n"
                                       "color:#414833;")
        self.textBrowser.setObjectName("textBrowser")
        self.txtinput = QtWidgets.QTextEdit(self.centralwidget)
        self.txtinput.setGeometry(QtCore.QRect(90, 300, 651, 121))
        self.txtinput.setStyleSheet("border-radius: 10px;\n"
                                    "font-family: MS Shell Dlg 2;\n"
                                    "font-size: 7.8pt;\n"
                                    "font-weight: 400;\n"
                                    "font-style:normal;\n"
                                    "font-size:10pt;\n"
                                    "color:#414833;")
        self.txtinput.setObjectName("txtinput")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(270, 450, 271, 38))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startBut = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.startBut.setStyleSheet("color: rgb(2, 48, 71);\n"
                                    "font-family: Courier New;\n"
                                    "font-size: 10pt;")
        self.startBut.setObjectName("startBut")
        self.horizontalLayout_2.addWidget(self.startBut)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_2.addWidget(self.lcdNumber)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тест скорости печати"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-family:\'Courier\'; font-size:36pt; color:#c5c6d0;\">Tест скорости печати</span></p></body></html>"))
        self.statBut.setText(_translate("MainWindow", "Посмотреть статистику"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#414833;\">Здесь появится текст после истечения таймера.</span></p></body></html>"))
        self.txtinput.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#414833;\">Здесь надо будет набирать текст после истечения таймера.</span></p></body></html>"))
        self.startBut.setText(_translate("MainWindow", "Старт"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt; color:#ffaa7f;\">через:</span></p></body></html>"))
