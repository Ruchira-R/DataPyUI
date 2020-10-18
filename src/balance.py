# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'balance.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_MainWindow(object):
    def withdraw(self):
        try:
            name=self.Edit_2.toPlainText()
            amount=self.Edit.toPlainText()
            connect = sqlite3.connect('Data.db')
            connect.execute("update account set current_balance = current_balance - ? where name= ?",(float(amount), str(name)))
            connect.commit()
            connect.close()
            a=open(name+".txt",'a')
            a.write("Name: " + name +"\t" + "Transaction-withdraw: " + str(amount) + "\t" + "\n")
            a.close()
            print("UPDATED SUCCESSFULLY")
        except Exception as e:
            print()



    def withdraw2(self):
        name = self.Edit_2.toPlainText()
        amount = self.Edit.toPlainText()
        connect = sqlite3.connect('Data.db')
        connect.execute("update customer set current_balance = current_balance - ? where  name= ?",
                        (float(amount), str(name)))
        connect.commit()
        connect.close()
    def deposit(self):
        try:
            name = self.Edit_2.toPlainText()
            amount = self.Edit.toPlainText()
            conn = sqlite3.connect('Data.db')
            conn.execute("update account set current_balance = current_balance + ?  where name = ?",(float(amount), str(name)))
            conn.commit()
            conn.close()
            a = open(name + ".txt", 'a')
            a.write("Name: " + name + "\t" + "Transaction-deposit: " + str(amount) + "\t" + "\n")
            a.close()
        except Exception as e:
            print()

        print("UPDATED SUCCESSFULLY")
    def deposit2(self):
        name = self.Edit_2.toPlainText()
        amount = self.Edit.toPlainText()
        conn = sqlite3.connect('Data.db')
        conn.execute("update customer set current_balance = current_balance + ?  where name = ?",(float(amount), str(name)))
        conn.commit()
        conn.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 70, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 230, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 370, 191, 81))
        self.pushButton.clicked.connect(self.withdraw)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.withdraw2)
        self.Edit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Edit.setGeometry(QtCore.QRect(150, 220, 241, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Edit.setFont(font)
        self.Edit.setObjectName("Edit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 370, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.deposit)
        self.pushButton_2.clicked.connect(self.deposit2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 170, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Edit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Edit_2.setGeometry(QtCore.QRect(150, 160, 241, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Edit_2.setFont(font)
        self.Edit_2.setObjectName("Edit_2")
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
        self.label_3.setText(_translate("MainWindow", "BALANCE"))
        self.label_4.setText(_translate("MainWindow", "AMOUNT :"))
        self.pushButton.setText(_translate("MainWindow", "WITHDRAW"))
        self.pushButton_2.setText(_translate("MainWindow", "DEPOSIT"))
        self.label_5.setText(_translate("MainWindow", "NAME:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

