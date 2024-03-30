import os
import PIL
from PyQt5 import QtCore, QtGui, QtWidgets

import src.main.PATH as path


DATA_FOLD = path.DATA_FOLD
TMP_FOLD = path.TMP_FOLD

DATA_BACKGROUND_PATH = f"{DATA_FOLD}/img/login-background.jpg"
RESIZED_BACKGROUND_PATH = f"{TMP_FOLD}/login-background.jpg"


class UiLoginWindow(object):

    def setup_ui(self, login_window):
        login_window.setObjectName("login_window")
        login_window.resize(1280, 800)
        login_window.setMinimumSize(QtCore.QSize(1280, 800))
        login_window.setMaximumSize(QtCore.QSize(1280, 800))
        login_window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        self.main_widget = QtWidgets.QWidget(login_window)
        self.main_widget.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.main_widget.setObjectName("main_widget")

        self.background_widget = QtWidgets.QLabel(self.main_widget)
        self.background_widget.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        image = PIL.Image.open(DATA_BACKGROUND_PATH)
        resized_image = image.resize((1280, 800))
        os.makedirs(TMP_FOLD, exist_ok=True)
        resized_image.save(RESIZED_BACKGROUND_PATH)
        self.background_widget.setStyleSheet(f"background-image: url({RESIZED_BACKGROUND_PATH});\n"
                                             "background-repeat: no-repeat;\n"
                                             "background-position: center;")
        self.background_widget.setObjectName("background_widget")

        self.header_label = QtWidgets.QLabel(self.main_widget)
        self.header_label.setGeometry(QtCore.QRect(165, 120, 950, 50))
        self.header_label.setAcceptDrops(True)
        self.header_label.setStyleSheet("font: 35pt \"OCR A Extended\";\n"
                                        "color: rgb(255, 255, 255);")
        self.header_label.setScaledContents(False)
        self.header_label.setObjectName("header_label")

        self.login_frame = QtWidgets.QLabel(self.main_widget)
        self.login_frame.setGeometry(QtCore.QRect(1280//2 - 380//2, 295, 380, 365))
        self.login_frame.setStyleSheet("border-radius: 30px;\n"
                                       "background-color: rgb(112, 112, 112);")
        self.login_frame.setObjectName("login_frame")

        self.auth_label = QtWidgets.QLabel(self.main_widget)
        self.auth_label.setGeometry(QtCore.QRect(535, 335, 210, 35))
        self.auth_label.setStyleSheet("font: 25pt\"Yu Gothic UI Semibold\";\n"
                                      "color: rgb(255, 255, 255);")
        self.auth_label.setObjectName("auth_label")

        self.login_label = QtWidgets.QLabel(self.main_widget)
        self.login_label.setGeometry(QtCore.QRect(490, 425, 130, 30))
        self.login_label.setStyleSheet("font: 15pt \"Yu Gothic UI Semibold\";\n"
                                       "color: rgb(255, 255, 255);")
        self.login_label.setObjectName("login_label")

        self.login_line = QtWidgets.QLineEdit(self.main_widget)
        self.login_line.setGeometry(QtCore.QRect(580, 420, 210, 40))
        self.login_line.setStyleSheet("border-radius: 15px;\n"
                                      "padding: 0px 10px 0px 10px;\n"
                                      "font: 15pt \"Yu Gothic UI Semibold\";")
        self.login_line.setObjectName("login_line")

        self.passwd_label = QtWidgets.QLabel(self.main_widget)
        self.passwd_label.setGeometry(QtCore.QRect(490, 485, 160, 30))
        self.passwd_label.setStyleSheet("font: 15pt \"Yu Gothic UI Semibold\";\n"
                                        "color: rgb(255, 255, 255);")
        self.passwd_label.setObjectName("passwd_label")

        self.passwd_line = QtWidgets.QLineEdit(self.main_widget)
        self.passwd_line.setGeometry(QtCore.QRect(580, 480, 210, 40))
        self.passwd_line.setStyleSheet("border-radius: 15px;\n"
                                       "padding: 0px 10px 0px 10px;\n"
                                       "font: 15pt \"Yu Gothic UI Semibold\";")
        self.passwd_line.setObjectName("passwd_line")

        self.entry_button = QtWidgets.QPushButton(self.main_widget)
        self.entry_button.setGeometry(QtCore.QRect(510, 570, 250, 50))
        self.entry_button.setStyleSheet("border-radius: 15px;\n"
                                        "background-color: rgb(47, 142, 192);\n"
                                        "font: 16pt \"Yu Gothic UI Semibold\";\n"
                                        "color: rgb(255, 255, 255);")
        self.entry_button.setObjectName("entry_button")

        login_window.setCentralWidget(self.main_widget)
        self.retranslate_ui(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def retranslate_ui(self, login_window):
        win_translate = QtCore.QCoreApplication.translate

        login_window.setWindowTitle(win_translate("login_window", "login_window"))

        self.header_label.setText(win_translate("login_window", "Мониторинг комплекса энергосбережения"))
        self.auth_label.setText(win_translate("login_window", "Авторизация"))
        self.login_label.setText(win_translate("login_window", "Логин:"))
        self.passwd_label.setText(win_translate("login_window", "Пароль:"))
        self.entry_button.setText(win_translate("login_window", "Вход"))
