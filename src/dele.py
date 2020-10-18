# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import balance
class Ui_MainWindow(object):

    def delete(self):
        try:
            name= self.Edit_2.toPlainText()
            connect = sqlite3.connect('Data.db')
            connect.execute("delete from account where name= ?;",(str(name),))
            connect.commit()
            connect.close()
        except Exception as e:
            print()

    def delete2(self):
        name = self.Edit_2.toPlainText()
        connect = sqlite3.connect('Data.db')
        connect.execute("delete from customer where name=?;",(str(name),))
        connect.commit()
        connect.close()
        print("UPDATED SUCCESSFULLY")
    def move(self):
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = balance.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            self.close()
        except Exception as e:
            print()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 320, 191, 81))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.delete)
        self.pushButton.clicked.connect(self.delete2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 320, 261, 81))
        self.pushButton_2.clicked.connect(self.move)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 160, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Edit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Edit_2.setGeometry(QtCore.QRect(230, 150, 241, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Edit_2.setFont(font)
        self.Edit_2.setObjectName("Edit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 50, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "DELETE "))
        self.pushButton_2.setText(_translate("MainWindow", "GO TO TRANSACTIONS"))
        self.label_5.setText(_translate("MainWindow", "Name:"))
        self.label_3.setText(_translate("MainWindow", "DELETE OR TRANSACT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

