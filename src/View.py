# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_ViewWindow(object):
    def loadData(self):
        connect = sqlite3.connect('Data.db')
        query = 'select * from customer'
        result = connect.execute(query)
        self.tableWidget.setRowCount(0)
        for rnum, rowdata in enumerate(result):
            self.tableWidget.insertRow(rnum)
            for colnum, coldata in enumerate(rowdata):
                self.tableWidget.setItem(rnum, colnum, QtWidgets.QTableWidgetItem(str(coldata)))
        connect.close()
    def setupUi(self, ViewWindow):
        ViewWindow.setObjectName("ViewWindow")
        ViewWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ViewWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(230, 20, 311, 401))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 440, 201, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loadData)
        ViewWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ViewWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        ViewWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ViewWindow)
        self.statusbar.setObjectName("statusbar")
        ViewWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ViewWindow)
        QtCore.QMetaObject.connectSlotsByName(ViewWindow)

    def retranslateUi(self, ViewWindow):
        _translate = QtCore.QCoreApplication.translate
        ViewWindow.setWindowTitle(_translate("ViewWindow", "MainWindow"))
        self.pushButton.setText(_translate("ViewWindow", "LOAD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewWindow = QtWidgets.QMainWindow()
    ui = Ui_ViewWindow()
    ui.setupUi(ViewWindow)
    ViewWindow.show()
    sys.exit(app.exec_())

