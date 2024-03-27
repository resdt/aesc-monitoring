import os
import csv
import PIL
from PyQt5 import QtCore, QtWidgets

import src.main.PATH as path


DATA_FOLD = path.DATA_FOLD
TMP_FOLD = path.TMP_FOLD

ADMIN_DATA_FILE_PATH = path.ADMIN_DATA_FILE_PATH
USER_DATA_FILE_PATH = path.USER_DATA_FILE_PATH

DATA_BACKGROUND_PATH = f"{DATA_FOLD}/img/work-background.jpeg"
RESIZED_BACKGROUND_PATH = f"{TMP_FOLD}/work-background.jpeg"

STATION_AMOUNT = 3
ADMIN_TABLE_ROWS = 20
ADMIN_TABLE_COLUMNS = 3


class Ui_AdminWindow(object):

    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(922, 540)
        AdminWindow.setMinimumSize(QtCore.QSize(922, 540))
        AdminWindow.setMaximumSize(QtCore.QSize(922, 540))

        self.main_widget = QtWidgets.QWidget(AdminWindow)
        self.main_widget.setGeometry(QtCore.QRect(0, 0, 922, 540))
        self.main_widget.setObjectName("main_widget")

        self.background_widget = QtWidgets.QLabel(self.main_widget)
        self.background_widget.setGeometry(QtCore.QRect(0, 0, 922, 540))
        image = PIL.Image.open(DATA_BACKGROUND_PATH)
        resized_image = image.resize((922, 540))
        os.makedirs(TMP_FOLD, exist_ok=True)
        resized_image.save(RESIZED_BACKGROUND_PATH)
        self.background_widget.setStyleSheet(f"background-image: url({RESIZED_BACKGROUND_PATH});\n"
                                             "background-repeat: no-repeat;\n"
                                             "background-position: center;")
        self.background_widget.setObjectName("background_widget")

        self.left_frame = QtWidgets.QLabel(self.main_widget)
        self.left_frame.setGeometry(QtCore.QRect(0, 0, 260, 540))
        self.left_frame.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.left_frame.setObjectName("left_frame")

        self.login_line = QtWidgets.QLineEdit(self.main_widget)
        self.login_line.setGeometry(QtCore.QRect(40, 75, 180, 40))
        self.login_line.setStyleSheet("border-radius: 15px;\n"
                                      "padding: 0px 10px 0px 10px;\n"
                                      "font: 63 10pt \"Yu Gothic UI Semibold\";")
        self.login_line.setPlaceholderText("логин")
        self.login_line.textChanged.connect(self.change_font_size)
        self.login_line.setObjectName("login_line")

        self.passwd_line = QtWidgets.QLineEdit(self.main_widget)
        self.passwd_line.setGeometry(QtCore.QRect(40, 125, 180, 40))
        self.passwd_line.setStyleSheet("border-radius: 15px;\n"
                                       "padding: 0px 10px 0px 10px;\n"
                                       "font: 63 10pt \"Yu Gothic UI Semibold\";")
        self.passwd_line.setPlaceholderText("пароль")
        self.passwd_line.textChanged.connect(self.change_font_size)
        self.passwd_line.setObjectName("passwd_line")

        self.station_line = QtWidgets.QLineEdit(self.main_widget)
        self.station_line.setEnabled(True)
        self.station_line.setGeometry(QtCore.QRect(40, 175, 180, 40))
        self.station_line.setStyleSheet("border-radius: 15px;\n"
                                        "padding: 0px 10px 0px 10px;\n"
                                        "font: 63 7pt \"Yu Gothic UI Semibold\";")
        self.station_line.setPlaceholderText("станции (пусто для администратора)")
        self.station_line.textChanged.connect(self.change_font_size)
        self.station_line.setObjectName("station_line")

        self.add_button = QtWidgets.QPushButton(self.main_widget)
        self.add_button.setGeometry(QtCore.QRect(40, 255, 180, 60))
        self.add_button.setStyleSheet("border-radius: 15px;\n"
                                      "background-color: rgb(112, 112, 112);\n"
                                      "font: 63 16pt \"Yu Gothic UI Semibold\";\n"
                                      "color: rgb(255, 255, 255);")
        self.add_button.clicked.connect(self.fill_table)
        self.add_button.setObjectName("add_button")

        self.s_n_exit_button = QtWidgets.QPushButton(self.main_widget)
        self.s_n_exit_button.setGeometry(QtCore.QRect(40, 405, 180, 60))
        self.s_n_exit_button.setStyleSheet("border-radius: 15px;\n"
                                           "background-color: rgb(47, 142, 192);\n"
                                           "font: 63 16pt \"Yu Gothic UI Semibold\";\n"
                                           "color: rgb(255, 255, 255);")
        self.s_n_exit_button.clicked.connect(self.save_login_data)
        self.s_n_exit_button.setObjectName("s_n_exit_button")

        self.table_widget = QtWidgets.QTableWidget(self.main_widget)
        self.table_widget.setGeometry(QtCore.QRect(260, 0, 482, 540))
        self.table_widget.setStyleSheet("border-radius: 15px;\n"
                                        "font: 63 16pt \"Yu Gothic UI Semibold\";")
        self.table_widget.setMaximumSize(QtCore.QSize(482, 540))
        self.table_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setColumnCount(ADMIN_TABLE_COLUMNS)
        self.table_widget.setRowCount(ADMIN_TABLE_ROWS)

        for row in range(ADMIN_TABLE_ROWS):
            item = QtWidgets.QTableWidgetItem()
            self.table_widget.setVerticalHeaderItem(row, item)

        for column in range(ADMIN_TABLE_COLUMNS):
            item = QtWidgets.QTableWidgetItem()
            self.table_widget.setHorizontalHeaderItem(column, item)
            self.table_widget.setColumnWidth(column, 150)

        for row in range(ADMIN_TABLE_ROWS):
            for column in range(ADMIN_TABLE_COLUMNS):
                item = QtWidgets.QTableWidgetItem()
                self.table_widget.setItem(row, column, item)

        self.table_widget.horizontalHeader().setCascadingSectionResizes(False)

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def change_font_size(self, AdminWindow):
        if self.login_line.text() == "":
            self.login_line.setStyleSheet("border-radius: 15px;\n"
                                          "padding: 0px 10px 0px 10px;\n"
                                          "font: 63 10pt \"Yu Gothic UI Semibold\";")
        else:
            self.login_line.setStyleSheet("border-radius: 15px;\n"
                                          "padding: 0px 10px 0px 10px;\n"
                                          "font: 63 15pt \"Yu Gothic UI Semibold\";")

        if self.passwd_line.text() == "":
            self.passwd_line.setStyleSheet("border-radius: 15px;\n"
                                           "padding: 0px 10px 0px 10px;\n"
                                           "font: 63 10pt \"Yu Gothic UI Semibold\";")
        else:
            self.passwd_line.setStyleSheet("border-radius: 15px;\n"
                                           "padding: 0px 10px 0px 10px;\n"
                                           "font: 63 15pt \"Yu Gothic UI Semibold\";")

        if self.station_line.text() == "":
            self.station_line.setStyleSheet("border-radius: 15px;\n"
                                            "padding: 0px 10px 0px 10px;\n"
                                            "font: 63 7pt \"Yu Gothic UI Semibold\";")
        else:
            self.station_line.setStyleSheet("border-radius: 15px;\n"
                                            "padding: 0px 10px 0px 10px;\n"
                                            "font: 63 15pt \"Yu Gothic UI Semibold\";")

    def fill_table(self, AdminWindow):
        win_translate = QtCore.QCoreApplication.translate

        new_login = self.login_line.text()
        new_password = self.passwd_line.text()
        new_stations = self.station_line.text()
        new_content = [new_login, new_password, new_stations]

        for row in range(ADMIN_TABLE_ROWS):
            login = self.table_widget.item(row, 0).text()

            if login == "":
                for column in range(ADMIN_TABLE_COLUMNS):
                    item = self.table_widget.item(row, column)
                    item.setText(win_translate("AdminWindow", new_content[column]))

                break

    def retranslateUi(self, AdminWindow):
        win_translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(win_translate("AdminWindow", "Form"))
        self.add_button.setText(win_translate("AdminWindow", "Добавить"))

        for row in range(ADMIN_TABLE_ROWS):
            item = self.table_widget.verticalHeaderItem(row)
            item.setText(win_translate("AdminWindow", str(row + 1)))

        table_headers = ["Логин", "Пароль", "Станции"]

        for column in range(ADMIN_TABLE_COLUMNS):
            item = self.table_widget.horizontalHeaderItem(column)
            item.setText(win_translate("AdminWindow", table_headers[column]))

        self.s_n_exit_button.setText(win_translate("AdminWindow", "Сохранить"))

        admin_login_file = open(ADMIN_DATA_FILE_PATH)
        admin_data = list(csv.reader(admin_login_file))
        admin_amount = len(admin_data) - 1

        for row in range(1, admin_amount + 1):
            login = admin_data[row][0]
            password = admin_data[row][1]
            row_content = [login, password, None]

            for column in range(ADMIN_TABLE_COLUMNS):
                item = self.table_widget.item(row - 1, column)
                item.setText(win_translate("AdminWindow", row_content[column]))

        admin_login_file.close()

        user_login_file = open(USER_DATA_FILE_PATH)
        user_data = list(csv.reader(user_login_file))
        user_amount = len(user_data) - 1

        for row in range(1, user_amount + 1):
            login = user_data[row][0]
            password = user_data[row][1]
            available_stations = list(filter(lambda x: x != "",
                                             user_data[row][2:]))
            row_content = [login, password, ", ".join(available_stations)]

            for column in range(ADMIN_TABLE_COLUMNS):
                item = self.table_widget.item(row + admin_amount - 1, column)
                item.setText(win_translate("AdminWindow", row_content[column]))

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
            login = self.table_widget.item(row, 0).text()
            password = self.table_widget.item(row, 1).text()
            station_list = self.table_widget.item(row, 2).text().split(", ")

            if login != "":
                if station_list[0] == "":
                    admin_writer.writerow([login, password])
                else:
                    data_list = [login, password] + station_list
                    user_writer.writerow(data_list)

        admin_login_file.close()
        user_login_file.close()
