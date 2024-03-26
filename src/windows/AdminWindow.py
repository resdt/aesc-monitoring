# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file "AdminWindow.ui"
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import csv
from PyQt5 import QtCore, QtWidgets

import src.main.PATH as path
import src.main.constants as cst


ADMIN_DATA_FILE_PATH = path.ADMIN_DATA_FILE_PATH
USER_DATA_FILE_PATH = path.USER_DATA_FILE_PATH

STATION_AMOUNT = cst.STATION_AMOUNT
ADMIN_TABLE_ROWS = cst.ADMIN_TABLE_ROWS
ADMIN_TABLE_COLUMNS = cst.ADMIN_TABLE_COLUMNS


class Ui_AdminWindow(object):

    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(510, 580)

        self.pushButton = QtWidgets.QPushButton(AdminWindow)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 181, 61))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(AdminWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 100, 181, 61))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label = QtWidgets.QLabel(AdminWindow)
        self.label.setGeometry(QtCore.QRect(270, 30, 101, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(AdminWindow)
        self.label_2.setGeometry(QtCore.QRect(270, 80, 111, 21))
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(AdminWindow)
        self.lineEdit.setGeometry(QtCore.QRect(270, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(AdminWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 110, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(AdminWindow)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 180, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_3 = QtWidgets.QLabel(AdminWindow)
        self.label_3.setGeometry(QtCore.QRect(270, 150, 171, 16))
        self.label_3.setObjectName("label_3")

        self.tableWidget = QtWidgets.QTableWidget(AdminWindow)
        self.tableWidget.setGeometry(QtCore.QRect(10, 231, 481, 331))
        self.tableWidget.setMaximumSize(QtCore.QSize(481, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(ADMIN_TABLE_COLUMNS)
        self.tableWidget.setRowCount(ADMIN_TABLE_ROWS)

        for row in range(ADMIN_TABLE_ROWS):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(row, item)

        for column in range(ADMIN_TABLE_COLUMNS):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(column, item)

        for row in range(ADMIN_TABLE_ROWS):
            for column in range(ADMIN_TABLE_COLUMNS):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(row, column, item)

        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.pushButton_3 = QtWidgets.QPushButton(AdminWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 170, 181, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)
        self.pushButton_3.clicked.connect(self.save_login_data)

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "Form"))
        self.pushButton.setText(_translate("AdminWindow",
                                           "Добавить администратора"))
        self.pushButton_2.setText(_translate("AdminWindow",
                                             "Добавить пользователя"))
        self.label.setText(_translate("AdminWindow", "Логин:"))
        self.label_2.setText(_translate("AdminWindow", "Пароль:"))
        self.label_3.setText(_translate("AdminWindow",
                                        "Серийные номера пользователя"))
        self.tableWidget.setSortingEnabled(True)

        for row in range(ADMIN_TABLE_ROWS):
            item = self.tableWidget.verticalHeaderItem(row)
            item.setText(_translate("AdminWindow", str(row + 1)))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AdminWindow", "Логин"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AdminWindow", "Пароль"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AdminWindow", "Номера"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_3.setText(_translate("AdminWindow",
                                             "Сохранить изменения и выйти"))

        admin_login_file = open(ADMIN_DATA_FILE_PATH)
        admin_data = list(csv.reader(admin_login_file))
        admin_amount = len(admin_data) - 1

        for row in range(1, admin_amount + 1):
            login = admin_data[row][0]
            password = admin_data[row][1]

            item = self.tableWidget.item(row - 1, 0)
            item.setText(_translate("AdminWindow", login))
            item = self.tableWidget.item(row - 1, 1)
            item.setText(_translate("AdminWindow", password))

        admin_login_file.close()

        user_login_file = open(USER_DATA_FILE_PATH)
        user_data = list(csv.reader(user_login_file))
        user_amount = len(user_data) - 1

        for row in range(1, user_amount + 1):
            login = user_data[row][0]
            password = user_data[row][1]
            available_stations = list(filter(lambda x: x != "",
                                             user_data[row][2:]))

            item = self.tableWidget.item(row + admin_amount - 1, 0)
            item.setText(_translate("AdminWindow", login))
            item = self.tableWidget.item(row + admin_amount - 1, 1)
            item.setText(_translate("AdminWindow", password))
            item = self.tableWidget.item(row + admin_amount - 1, 2)
            item.setText(_translate("AdminWindow",
                                    ", ".join(available_stations)))

        user_login_file.close()

    def save_login_data(self):
        admin_login_file = open(ADMIN_DATA_FILE_PATH, "w", newline="")
        admin_writer = csv.writer(admin_login_file)
        admin_writer.writerow(["Login", "Password"])

        user_login_file = open(USER_DATA_FILE_PATH, "w", newline="")
        user_writer = csv.writer(user_login_file)
        user_writer.writerow(["Login", "Password",
                              *list(range(1, STATION_AMOUNT + 1))])

        for row in range(ADMIN_TABLE_ROWS):
            login = self.tableWidget.item(row, 0).text()
            password = self.tableWidget.item(row, 1).text()
            station_list = self.tableWidget.item(row, 2).text().split(", ")

            if login != "":
                if station_list[0] == "":
                    admin_writer.writerow([login, password])
                else:
                    data_list = [login, password] + station_list
                    user_writer.writerow(data_list)

        admin_login_file.close()
        user_login_file.close()
