import time
import _csv
import csv

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from design_before import Ui_MainWindow
from text_generator import generator
from mistakesper import dice_coefficient
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from results import Ui_Form
import sys


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.num_of_secs = 10
        self.startBut.clicked.connect(self.start)
        self.count = 100
        self.txtinput.setReadOnly(True)
        self.lcdNumber.display('10.0')
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.start)
        self.start = True
        self.statBut.clicked.connect(self.show_stat)

    def start(self):
        try:
            # update the timer every tenth second
            self.timer.start(100)
            if self.start:
                # incrementing the counter
                self.count -= 1
                # print(self.count)

                # timer is completed
                if self.count == 0:
                    # making flag false
                    self.start = False

                    # setting text to the label
                    self.lcdNumber.display("0:0")
                    self.thetext = generator()
                    self.textBrowser.setPlainText(self.thetext)
                    self.txtinput.setText('')
                    self.txtinput.setReadOnly(False)
                    self.txtinput.setFocus()
                    self.label_2.setVisible(False)
                    self.lcdNumber.setVisible(False)
                    self.startBut.setText('Завершить')
                    self.stime = time.time()
                    self.startBut.clicked.connect(self.Stop)
                    # self.textBrowser.setStyleSheet("font-family: MS Shell Dlg 2"
                    #                                "font-size:10pt;"
                    #                                "font-weight:400;"
                    #                                "font-style:normal;")
                    self.startBut.setStyleSheet("background-color: rgb(220,20,60);\n"
                                                "font-family: Courier New;\n"
                                                "font-size: 10pt;")

            if self.start:
                # getting text from count
                text = str(self.count / 10)

                # showing text
                self.lcdNumber.display(text)
        except KeyboardInterrupt:
            print('Программа завершена.')

    def Stop(self):
        self.txtinput.setReadOnly(True)
        self.usertext = self.txtinput.toPlainText()
        self.startBut.setVisible(False)
        self.sttime = time.time()
        self.tottime = QLabel('', self)
        self.horizontalLayout_2.addWidget(self.tottime)
        self.restime = self.time_convert(self.sttime - self.stime)
        self.mistakes = str(100 - dice_coefficient(self.thetext, self.usertext)) + '%'
        self.speed = 0
        if len(self.usertext) - 25 <= len(self.thetext) <= len(self.usertext) + 25:
            self.speed = len(self.usertext) // (self.sec / 60)
        if self.speed >= 1080:
            self.speed = 0
        # print(self.speed, self.restime, self.mistakes)
        self.res_form = SecondForm()
        self.res_form.update_vars(self.restime, self.mistakes, self.speed)
        self.res_form.show()

    def time_convert(self, sec):
        self.sec = sec
        mins = sec // 60
        sec = int(sec % 60)
        hours = mins // 60
        mins = mins % 60
        return ("{0}:{1}".format(int(mins), sec))

    def show_stat(self):
        self.stat_form = StatWidget()
        self.stat_form.show()


class SecondForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.setupUi(self)
        self.statBut.clicked.connect(self.save_stat)

    def update_vars(self, time, mis, speed):
        self.time = time
        self.mis = mis
        self.speed = speed
        self.lcdNumber.display(time)
        self.lcdNumber_2.display(mis)
        self.lcdNumber_3.display(speed)
        if speed == 0:
            self.label.setVisible(True)

    def save_stat(self):
        if self.label.isVisible() is False:
            sniffer = csv.Sniffer()
            sample_bytes = 64
            head = ['time', 'mistakes', 'speed']
            t = self.time
            m = self.mis
            s = self.speed
            data = [t, m, s]
            with open('statistic.csv', 'a', encoding='UTF8', newline='') as csvfile:
                # csvfile.seek(-1, 2)
                try:
                    if sniffer.has_header(open("statistic.csv").read(sample_bytes)):
                        header = True
                except _csv.Error:
                    header = False
                except FileNotFoundError:
                    header = False
                writer = csv.writer(csvfile)
                if header is False:
                    writer.writerow(head)
                writer.writerow(data)
                self.statBut.setVisible(False)

        else:
            self.statBut.setVisible(False)


class StatWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('statistic_ui.ui', self)
        self.loadTable('statistic.csv')

    def loadTable(self, table_name):
        try:
            with open(table_name, encoding="utf8") as csvfile:
                reader = csv.reader(csvfile,
                                    delimiter=',', quotechar='"')
                title = next(reader)
                self.tableWidget.setColumnCount(len(title))
                self.tableWidget.setHorizontalHeaderLabels(title)
                self.tableWidget.setRowCount(0)
                for i, row in enumerate(reader):
                    self.tableWidget.setRowCount(
                        self.tableWidget.rowCount() + 1)
                    for j, elem in enumerate(row):
                        self.tableWidget.setItem(
                            i, j, QTableWidgetItem(elem))
            self.tableWidget.resizeColumnsToContents()
        except FileNotFoundError:
            pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
