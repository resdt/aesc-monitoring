import os
import shutil as sht
import PIL
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dat
from PyQt5 import QtCore, QtWidgets

import src.main.PATH as path
import src.main.utils as utl


DATA_FOLD = path.DATA_FOLD
TMP_FOLD = path.TMP_FOLD
OUT_FOLD = path.OUT_FOLD

CUR_LOGIN_DATA_PATH = path.CUR_LOGIN_DATA_PATH

DATA_BACKGROUND_PATH = f"{DATA_FOLD}/img/work-background.jpeg"
RESIZED_BACKGROUND_PATH = f"{TMP_FOLD}/user-background.jpeg"
STATION_DATA_FOLD = f"{DATA_FOLD}/example"
OUT_TABLE_PATH = f"{OUT_FOLD}/table.csv"
PLOT_TABLE_PATH = f"{TMP_FOLD}/plot-table.csv"
PLOT_PICT1_PATH = f"{TMP_FOLD}/1.png"
PLOT_PICT2_PATH = f"{TMP_FOLD}/2.png"
RESIZED_PLOT_PICT1_PATH = f"{TMP_FOLD}/resized-1.png"
RESIZED_PLOT_PICT2_PATH = f"{TMP_FOLD}/resized-2.png"
OUT_PICT1_PATH = f"{OUT_FOLD}/1.png"
OUT_PICT2_PATH = f"{OUT_FOLD}/2.png"

STATION_DATA_FILE_COLUMNS = ["Measurement start time",
                             "Measurement end time",
                             "Reactive power phase A on",
                             "Reactive power phase B on",
                             "Reactive power phase C on",
                             "Active power phase A on",
                             "Active power phase B on",
                             "Active power phase C on",
                             "Voltage phase A on",
                             "Voltage phase B on",
                             "Voltage phase C on",
                             "Cosine phase A on",
                             "Cosine phase B on",
                             "Cosine phase C on",
                             "Reactive power phase A off",
                             "Reactive power phase B off",
                             "Reactive power phase C off",
                             "Active power phase A off",
                             "Active power phase B off",
                             "Active power phase C off",
                             "Voltage phase A off",
                             "Voltage phase B off",
                             "Voltage phase C off",
                             "Cosine phase A off",
                             "Cosine phase B off",
                             "Cosine phase C off",
                             "Number of powered blocks"]


class UiUserWindow(object):

    def setup_ui(self, user_window):
        user_window.setObjectName("user_window")
        user_window.resize(1180, 800)
        user_window.setMinimumSize(QtCore.QSize(1180, 800))
        user_window.setMaximumSize(QtCore.QSize(1180, 800))

        self.main_widget = QtWidgets.QWidget(user_window)
        self.main_widget.setGeometry(QtCore.QRect(0, 0, 1180, 800))
        self.main_widget.setObjectName("main_widget")

        self.background_widget = QtWidgets.QLabel(self.main_widget)
        self.background_widget.setGeometry(QtCore.QRect(0, 0, 1180, 800))
        image = PIL.Image.open(DATA_BACKGROUND_PATH)
        resized_image = image.resize((1180, 800))
        os.makedirs(TMP_FOLD, exist_ok=True)
        resized_image.save(RESIZED_BACKGROUND_PATH)
        self.background_widget.setStyleSheet(f"background-image: url({RESIZED_BACKGROUND_PATH});\n"
                                             "background-repeat: no-repeat;\n"
                                             "background-position: center;")
        self.background_widget.setObjectName("background_widget")

        self.left_frame = QtWidgets.QLabel(self.main_widget)
        self.left_frame.setGeometry(QtCore.QRect(0, 0, 260, 800))
        self.left_frame.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.left_frame.setObjectName("left_frame")

        self.list_frame = QtWidgets.QLabel(self.main_widget)
        self.list_frame.setGeometry(QtCore.QRect(40, 40, 180, 390))
        self.list_frame.setStyleSheet("border-radius: 15px;\n"
                                      "background-color: rgb(250, 250, 250);")
        self.list_frame.setObjectName("list_frame")

        self.complex_list_widget = QtWidgets.QListWidget(self.main_widget)
        self.complex_list_widget.setGeometry(QtCore.QRect(55, 55, 150, 120))
        self.complex_list_widget.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";\n"
                                               "background-color: rgb(250, 250, 250);")
        self.complex_list_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.complex_list_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.complex_list_widget.setObjectName("complex_list_widget")
        df_row = pd.read_csv(CUR_LOGIN_DATA_PATH)
        available_stations = df_row.iloc[:, 2:].dropna(axis=1)
        station_list = available_stations.values.flatten().tolist()
        self.complex_list_widget.addItems(station_list)
        self.complex_list_widget.itemClicked.connect(self.show_available_stations)

        self.station_file_list_widget = QtWidgets.QListWidget(self.main_widget)
        self.station_file_list_widget.setGeometry(QtCore.QRect(55, 175, 150, 120))
        self.station_file_list_widget.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";\n"
                                                    "background-color: rgb(250, 250, 250);")
        self.station_file_list_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.station_file_list_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.station_file_list_widget.setObjectName("station_file_list_widget")
        self.station_file_list_widget.itemClicked.connect(self.load_recording_list)

        self.station_rec_list_widget = QtWidgets.QListWidget(self.main_widget)
        self.station_rec_list_widget.setGeometry(QtCore.QRect(55, 295, 150, 120))
        self.station_rec_list_widget.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";\n"
                                                   "background-color: rgb(250, 250, 250);")
        self.station_rec_list_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.station_rec_list_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.station_rec_list_widget.setObjectName("station_rec_list_widget")
        self.station_rec_list_widget.itemClicked.connect(self.view_station_data)
        self.complex_list_widget.itemClicked.connect(self.station_rec_list_widget.clear)

        self.view_frame = QtWidgets.QLabel(self.main_widget)
        self.view_frame.setGeometry(QtCore.QRect(260, 0, 740, 800))
        self.view_frame.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.view_frame.setObjectName("view_frame")

        self.view_top_subframe = QtWidgets.QLabel(self.main_widget)
        self.view_top_subframe.setGeometry(QtCore.QRect(275, 15, 710, 335))
        self.view_top_subframe.setStyleSheet("border-top-left-radius: 15px;\n"
                                             "border-top-right-radius: 15px;\n"
                                             "background-color: rgb(255, 255, 255);")
        self.view_top_subframe.setObjectName("view_top_subframe")

        self.rct_pow_a_label = QtWidgets.QLabel(self.main_widget)
        self.rct_pow_a_label.setGeometry(QtCore.QRect(370, 55, 250, 20))
        self.rct_pow_a_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.rct_pow_a_label.setObjectName("rct_pow_a_label")

        self.rct_pow_b_label = QtWidgets.QLabel(self.main_widget)
        self.rct_pow_b_label.setGeometry(QtCore.QRect(370, 78, 250, 20))
        self.rct_pow_b_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.rct_pow_b_label.setObjectName("rct_pow_b_label")

        self.rct_pow_c_label = QtWidgets.QLabel(self.main_widget)
        self.rct_pow_c_label.setGeometry(QtCore.QRect(370, 101, 250, 20))
        self.rct_pow_c_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.rct_pow_c_label.setObjectName("rct_pow_c_label")

        self.act_pow_a_label = QtWidgets.QLabel(self.main_widget)
        self.act_pow_a_label.setGeometry(QtCore.QRect(370, 124, 250, 20))
        self.act_pow_a_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.act_pow_a_label.setObjectName("act_pow_a_label")

        self.act_pow_b_label = QtWidgets.QLabel(self.main_widget)
        self.act_pow_b_label.setGeometry(QtCore.QRect(370, 147, 250, 20))
        self.act_pow_b_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.act_pow_b_label.setObjectName("act_pow_b_label")

        self.act_pow_c_label = QtWidgets.QLabel(self.main_widget)
        self.act_pow_c_label.setGeometry(QtCore.QRect(370, 170, 250, 20))
        self.act_pow_c_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.act_pow_c_label.setObjectName("act_pow_c_label")

        self.vlt_a_label = QtWidgets.QLabel(self.main_widget)
        self.vlt_a_label.setGeometry(QtCore.QRect(370, 193, 250, 20))
        self.vlt_a_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.vlt_a_label.setObjectName("vlt_a_label")

        self.vlt_b_label = QtWidgets.QLabel(self.main_widget)
        self.vlt_b_label.setGeometry(QtCore.QRect(370, 216, 250, 20))
        self.vlt_b_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.vlt_b_label.setObjectName("vlt_b_label")

        self.vlt_c_label = QtWidgets.QLabel(self.main_widget)
        self.vlt_c_label.setGeometry(QtCore.QRect(370, 239, 250, 20))
        self.vlt_c_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.vlt_c_label.setObjectName("vlt_c_label")

        self.cos_a_label = QtWidgets.QLabel(self.main_widget)
        self.cos_a_label.setGeometry(QtCore.QRect(370, 262, 250, 20))
        self.cos_a_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.cos_a_label.setObjectName("cos_a_label")

        self.cos_b_label = QtWidgets.QLabel(self.main_widget)
        self.cos_b_label.setGeometry(QtCore.QRect(370, 285, 250, 20))
        self.cos_b_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.cos_b_label.setObjectName("cos_b_label")

        self.cos_c_label = QtWidgets.QLabel(self.main_widget)
        self.cos_c_label.setGeometry(QtCore.QRect(370, 308, 250, 20))
        self.cos_c_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.cos_c_label.setObjectName("cos_c_label")

        self.sys_on_label = QtWidgets.QLabel(self.main_widget)
        self.sys_on_label.setGeometry(QtCore.QRect(630, 30, 100, 20))
        self.sys_on_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.sys_on_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sys_on_label.setObjectName("sys_on_label")

        self.sys_off_label = QtWidgets.QLabel(self.main_widget)
        self.sys_off_label.setGeometry(QtCore.QRect(730, 30, 100, 20))
        self.sys_off_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.sys_off_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sys_off_label.setObjectName("sys_off_label")

        self.data_table = QtWidgets.QTableWidget(self.main_widget)
        self.data_table.setGeometry(QtCore.QRect(630, 55, 202, 278))
        self.data_table.setStyleSheet("font: 9pt \"Yu Gothic UI Semibold\";")
        self.data_table.horizontalHeader().setVisible(False)
        self.data_table.verticalHeader().setVisible(False)
        self.data_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.data_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.data_table.setObjectName("data_table")
        self.data_table.setColumnCount(2)
        self.data_table.setRowCount(12)
        self.data_table.resizeRowsToContents()

        self.var1_label = QtWidgets.QLabel(self.main_widget)
        self.var1_label.setGeometry(QtCore.QRect(840, 55, 50, 20))
        self.var1_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.var1_label.setObjectName("var1_label")

        self.var2_label = QtWidgets.QLabel(self.main_widget)
        self.var2_label.setGeometry(QtCore.QRect(840, 78, 50, 20))
        self.var2_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.var2_label.setObjectName("var2_label")

        self.var3_label = QtWidgets.QLabel(self.main_widget)
        self.var3_label.setGeometry(QtCore.QRect(840, 101, 50, 20))
        self.var3_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.var3_label.setObjectName("var3_label")

        self.vt1_label = QtWidgets.QLabel(self.main_widget)
        self.vt1_label.setGeometry(QtCore.QRect(840, 124, 50, 20))
        self.vt1_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.vt1_label.setObjectName("vt1_label")

        self.vt2_label = QtWidgets.QLabel(self.main_widget)
        self.vt2_label.setGeometry(QtCore.QRect(840, 147, 50, 20))
        self.vt2_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.vt2_label.setObjectName("vt2_label")

        self.vt3_label = QtWidgets.QLabel(self.main_widget)
        self.vt3_label.setGeometry(QtCore.QRect(840, 170, 50, 20))
        self.vt3_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.vt3_label.setObjectName("vt3_label")

        self.volt1_label = QtWidgets.QLabel(self.main_widget)
        self.volt1_label.setGeometry(QtCore.QRect(840, 193, 50, 20))
        self.volt1_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.volt1_label.setObjectName("volt1_label")

        self.volt2_label = QtWidgets.QLabel(self.main_widget)
        self.volt2_label.setGeometry(QtCore.QRect(840, 216, 50, 20))
        self.volt2_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.volt2_label.setObjectName("volt2_label")

        self.volt3_label = QtWidgets.QLabel(self.main_widget)
        self.volt3_label.setGeometry(QtCore.QRect(840, 239, 50, 20))
        self.volt3_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.volt3_label.setObjectName("volt3_label")

        self.view_bottom_subframe = QtWidgets.QLabel(self.main_widget)
        self.view_bottom_subframe.setGeometry(QtCore.QRect(275, 355, 710, 105))
        self.view_bottom_subframe.setStyleSheet("border-bottom-left-radius: 15px;\n"
                                                "border-bottom-right-radius: 15px;\n"
                                                "background-color: rgb(255, 255, 255);")
        self.view_bottom_subframe.setObjectName("view_bottom_subframe")

        self.meas_start_label = QtWidgets.QLabel(self.main_widget)
        self.meas_start_label.setGeometry(QtCore.QRect(290, 370, 255, 20))
        self.meas_start_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.meas_start_label.setObjectName("meas_start_label")

        self.meas_start_line = QtWidgets.QLabel(self.main_widget)
        self.meas_start_line.setGeometry(QtCore.QRect(555, 370, 135, 23))
        self.meas_start_line.setStyleSheet("border: 1px solid rgb(230, 230, 230);\n"
                                           "border-radius: 10px;\n"
                                           "background-color: rgb(240, 240, 240);"
                                           "padding: 0px 3px 0px 3px;\n"
                                           "font: 9pt \"Yu Gothic UI Semibold\";")
        self.meas_start_line.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.meas_start_line.setObjectName("meas_start_line")

        self.meas_end_label = QtWidgets.QLabel(self.main_widget)
        self.meas_end_label.setGeometry(QtCore.QRect(290, 396, 255, 20))
        self.meas_end_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.meas_end_label.setObjectName("meas_end_label")

        self.meas_end_line = QtWidgets.QLabel(self.main_widget)
        self.meas_end_line.setGeometry(QtCore.QRect(555, 396, 135, 23))
        self.meas_end_line.setStyleSheet("border: 1px solid rgb(230, 230, 230);\n"
                                         "border-radius: 10px;\n"
                                         "background-color: rgb(240, 240, 240);"
                                         "padding: 0px 3px 0px 3px;\n"
                                         "font: 9pt \"Yu Gothic UI Semibold\";")
        self.meas_end_line.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.meas_end_line.setObjectName("meas_end_line")

        self.on_block_amnt_label = QtWidgets.QLabel(self.main_widget)
        self.on_block_amnt_label.setGeometry(QtCore.QRect(290, 422, 255, 20))
        self.on_block_amnt_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.on_block_amnt_label.setObjectName("on_block_amnt_label")

        self.on_block_amnt_line = QtWidgets.QLabel(self.main_widget)
        self.on_block_amnt_line.setGeometry(QtCore.QRect(555, 422, 135, 23))
        self.on_block_amnt_line.setStyleSheet("border: 1px solid rgb(230, 230, 230);\n"
                                              "border-radius: 10px;\n"
                                              "background-color: rgb(240, 240, 240);"
                                              "padding: 0px 3px 0px 3px;\n"
                                              "font: 9pt \"Yu Gothic UI Semibold\";")
        self.on_block_amnt_line.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.on_block_amnt_line.setObjectName("on_block_amnt_line")

        self.p_on_label = QtWidgets.QLabel(self.main_widget)
        self.p_on_label.setGeometry(QtCore.QRect(785, 370, 40, 20))
        self.p_on_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.p_on_label.setObjectName("p_on_label")

        self.p_on_line = QtWidgets.QLabel(self.main_widget)
        self.p_on_line.setGeometry(QtCore.QRect(835, 370, 135, 23))
        self.p_on_line.setStyleSheet("border: 1px solid rgb(230, 230, 230);\n"
                                     "border-radius: 10px;\n"
                                     "background-color: rgb(240, 240, 240);"
                                     "padding: 0px 3px 0px 3px;\n"
                                     "font: 9pt \"Yu Gothic UI Semibold\";")
        self.p_on_line.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.p_on_line.setObjectName("p_on_line")

        self.p_off_label = QtWidgets.QLabel(self.main_widget)
        self.p_off_label.setGeometry(QtCore.QRect(785, 396, 40, 20))
        self.p_off_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.p_off_label.setObjectName("p_off_label")

        self.p_off_line = QtWidgets.QLabel(self.main_widget)
        self.p_off_line.setGeometry(QtCore.QRect(835, 396, 135, 23))
        self.p_off_line.setStyleSheet("border: 1px solid rgb(230, 230, 230);\n"
                                      "border-radius: 10px;\n"
                                      "background-color: rgb(240, 240, 240);"
                                      "padding: 0px 3px 0px 3px;\n"
                                      "font: 9pt \"Yu Gothic UI Semibold\";")
        self.p_off_line.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.p_off_line.setObjectName("p_off_line")

        self.n_label = QtWidgets.QLabel(self.main_widget)
        self.n_label.setGeometry(QtCore.QRect(785, 422, 40, 20))
        self.n_label.setStyleSheet("font: 12pt \"Yu Gothic UI Semibold\";")
        self.n_label.setObjectName("n_label")

        self.n_line = QtWidgets.QLabel(self.main_widget)
        self.n_line.setGeometry(QtCore.QRect(835, 422, 135, 23))
        self.n_line.setStyleSheet("border: 1px solid rgb(230, 230, 230);\n"
                                  "border-radius: 10px;\n"
                                  "background-color: rgb(240, 240, 240);"
                                  "padding: 0px 3px 0px 3px;\n"
                                  "font: 9pt \"Yu Gothic UI Semibold\";")
        self.n_line.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.n_line.setObjectName("n_line")

        self.action_frame = QtWidgets.QLabel(self.main_widget)
        self.action_frame.setGeometry(QtCore.QRect(40, 475, 180, 285))
        self.action_frame.setStyleSheet("border-radius: 15px;\n"
                                        "background-color: rgb(250, 250, 250);")
        self.action_frame.setObjectName("action_frame")

        self.view_rng_main_label = QtWidgets.QLabel(self.main_widget)
        self.view_rng_main_label.setGeometry(QtCore.QRect(55, 490, 150, 20))
        self.view_rng_main_label.setStyleSheet("font: 10pt \"Yu Gothic UI Semibold\";")
        self.view_rng_main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.view_rng_main_label.setObjectName("view_rng_main_label")

        self.view_rng_start_label = QtWidgets.QLabel(self.main_widget)
        self.view_rng_start_label.setGeometry(QtCore.QRect(55, 530, 25, 20))
        self.view_rng_start_label.setStyleSheet("font: 10pt \"Yu Gothic UI Semibold\";")
        self.view_rng_start_label.setAlignment(QtCore.Qt.AlignCenter)
        self.view_rng_start_label.setObjectName("view_rng_start_label")

        self.view_rng_start_line = QtWidgets.QDateTimeEdit(self.main_widget)
        self.view_rng_start_line.setGeometry(QtCore.QRect(80, 520, 125, 40))
        self.view_rng_start_line.setStyleSheet("font: 10pt \"Yu Gothic UI Semibold\";\n"
                                               "background-color: rgb(250, 250, 250);")
        self.view_rng_start_line.setButtonSymbols(2)
        self.view_rng_start_line.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 2, 19), QtCore.QTime(0, 0, 0)))
        self.view_rng_start_line.setAlignment(QtCore.Qt.AlignCenter)
        self.view_rng_start_line.setObjectName("view_rng_start_line")

        self.view_rng_end_label = QtWidgets.QLabel(self.main_widget)
        self.view_rng_end_label.setGeometry(QtCore.QRect(55, 575, 25, 20))
        self.view_rng_end_label.setStyleSheet("font: 10pt \"Yu Gothic UI Semibold\";")
        self.view_rng_end_label.setAlignment(QtCore.Qt.AlignCenter)
        self.view_rng_end_label.setObjectName("view_rng_end_label")

        self.view_rng_end_line = QtWidgets.QDateTimeEdit(self.main_widget)
        self.view_rng_end_line.setGeometry(QtCore.QRect(80, 565, 125, 40))
        self.view_rng_end_line.setStyleSheet("font: 10pt \"Yu Gothic UI Semibold\";\n"
                                             "background-color: rgb(250, 250, 250);")
        self.view_rng_end_line.setButtonSymbols(2)
        self.view_rng_end_line.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 2, 19), QtCore.QTime(0, 0, 0)))
        self.view_rng_end_line.setAlignment(QtCore.Qt.AlignCenter)
        self.view_rng_end_line.setObjectName("view_rng_end_line")

        self.confirm_button = QtWidgets.QPushButton(self.main_widget)
        self.confirm_button.setGeometry(QtCore.QRect(55, 620, 150, 35))
        self.confirm_button.setStyleSheet("border-radius: 15px;\n"
                                          "background-color: rgb(112, 112, 112);\n"
                                          "font: 12pt \"Yu Gothic UI Semibold\";\n"
                                          "color: rgb(255, 255, 255);")
        self.confirm_button.setObjectName("confirm_button")
        self.confirm_button.clicked.connect(self.make_table)
        self.confirm_button.clicked.connect(self.make_plots)

        self.downld_data_button = QtWidgets.QPushButton(self.main_widget)
        self.downld_data_button.setGeometry(QtCore.QRect(55, 695, 150, 50))
        self.downld_data_button.setStyleSheet("border-radius: 15px;\n"
                                              "background-color: rgb(47, 142, 192);\n"
                                              "font: 12pt \"Yu Gothic UI Semibold\";\n"
                                              "color: rgb(255, 255, 255);")
        self.downld_data_button.setObjectName("downld_data_button")
        self.downld_data_button.clicked.connect(self.download_data)

        self.plot_frame = QtWidgets.QLabel(self.main_widget)
        self.plot_frame.setGeometry(QtCore.QRect(260, 475, 740, 325))
        self.plot_frame.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.plot_frame.setObjectName("plot_frame")

        self.left_plot = QtWidgets.QLabel(self.main_widget)
        self.left_plot.setGeometry(QtCore.QRect(260, 475, 370, 325))
        self.left_plot.setObjectName("left_plot")

        self.right_plot = QtWidgets.QLabel(self.main_widget)
        self.right_plot.setGeometry(QtCore.QRect(630, 475, 370, 325))
        self.right_plot.setObjectName("right_plot")

        self.make_plots()

        self.retranslate_ui(user_window)
        QtCore.QMetaObject.connectSlotsByName(user_window)

    def retranslate_ui(self, user_window):
        win_translate = QtCore.QCoreApplication.translate

        user_window.setWindowTitle(win_translate("user_window", "user_window"))

        self.downld_data_button.setText(win_translate("user_window",
                                                      "Скачать данные"))
        self.confirm_button.setText(win_translate("user_window",
                                                  "Подтвердить"))
        self.view_rng_start_line.setDisplayFormat(win_translate("user_window",
                                                                "dd.MM.yyyy H:mm:ss"))
        self.view_rng_end_line.setDisplayFormat(win_translate("user_window", "dd.MM.yyyy H:mm:ss"))
        self.view_rng_main_label.setText(win_translate("user_window", "Диапазон измерений:"))
        self.view_rng_start_label.setText(win_translate("user_window", "с"))
        self.view_rng_end_label.setText(win_translate("user_window", "до"))
        self.sys_on_label.setText(win_translate("user_window", "Включена"))
        self.sys_off_label.setText(win_translate("user_window", "Выключена"))
        self.meas_start_label.setText(win_translate("user_window",
                                                    "Время начала измерений:"))
        self.meas_end_label.setText(win_translate("user_window",
                                                  "Время окончания измерений:"))
        self.rct_pow_a_label.setText(win_translate("user_window", "Реактивная мощность по фазе A:"))
        self.rct_pow_b_label.setText(win_translate("user_window", "Реактивная мощность по фазе B:"))
        self.rct_pow_c_label.setText(win_translate("user_window", "Реактивная мощность по фазе C:"))
        self.act_pow_a_label.setText(win_translate("user_window", "Активная мощность по фазе A:"))
        self.act_pow_b_label.setText(win_translate("user_window","Активная мощность по фазе B:"))
        self.act_pow_c_label.setText(win_translate("user_window", "Активная мощность по фазе C:"))
        self.vlt_a_label.setText(win_translate("user_window",
                                               "Напряжение по фазе A:"))
        self.vlt_b_label.setText(win_translate("user_window",
                                               "Напряжение по фазе B:"))
        self.vlt_c_label.setText(win_translate("user_window",
                                               "Напряжение по фазе C:"))
        self.cos_a_label.setText(win_translate("user_window",
                                               "Косинус по фазе A:"))
        self.cos_b_label.setText(win_translate("user_window",
                                               "Косинус по фазе B:"))
        self.cos_c_label.setText(win_translate("user_window",
                                               "Косинус по фазе C:"))
        self.var1_label.setText(win_translate("user_window", "ВАр"))
        self.var2_label.setText(win_translate("user_window", "ВАр"))
        self.var3_label.setText(win_translate("user_window", "ВАр"))
        self.vt1_label.setText(win_translate("user_window", "Вт"))
        self.vt2_label.setText(win_translate("user_window", "Вт"))
        self.vt3_label.setText(win_translate("user_window", "Вт"))
        self.volt1_label.setText(win_translate("user_window", "Вольт"))
        self.volt2_label.setText(win_translate("user_window", "Вольт"))
        self.volt3_label.setText(win_translate("user_window", "Вольт"))
        self.p_on_label.setText(win_translate("user_window", "P_on"))
        self.p_off_label.setText(win_translate("user_window", "P_off"))
        self.n_label.setText(win_translate("user_window", "n"))
        self.on_block_amnt_label.setText(win_translate("user_window", "Количество включенных блоков:"))

    def show_available_stations(self):
        self.station_file_list_widget.clear()

        current = self.complex_list_widget.currentItem().text()
        data_filenames = os.listdir(path=STATION_DATA_FOLD)

        for filename in data_filenames:
            if current in filename:
                station = filename.split(".")[0]
                self.station_file_list_widget.addItem(station)

        self.station_file_list_widget.sortItems()

    def load_recording_list(self):
        filename = self.station_file_list_widget.currentItem().text() + ".csv"

        self.station_rec_list_widget.clear()

        with open(f"{STATION_DATA_FOLD}/{filename}") as station_content:
            length = len(station_content.readlines())

        self.station_rec_list_widget.addItems(map(str, list(range(1, length + 1))))

    def view_station_data(self):
        win_translate = QtCore.QCoreApplication.translate

        filename = self.station_file_list_widget.currentItem().text() + ".csv"
        row_number = int(self.station_rec_list_widget.currentItem().text()) - 1

        station_content = open(f"{STATION_DATA_FOLD}/{filename}").readlines()
        content_list = station_content[row_number].split(";")
        content_list += [""] * (len(STATION_DATA_FILE_COLUMNS) -
                                len(content_list))

        self.meas_start_line.setText(content_list[0])
        self.meas_end_line.setText(content_list[1])

        for column in range(2):
            for row in range(12):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.data_table.setItem(row, column, item)

                item = self.data_table.item(row, column)
                item.setText(win_translate("admin_window", content_list[row + column*12 + 2]))

        self.on_block_amnt_line.setText(str(int(content_list[26])) if content_list[26] != ""
                                        else "")

        f_on = sum(list(map(float, content_list[5:8])))
        f_off = 0

        if content_list[17] != "":
            f_off = sum(list(map(float, content_list[17:20])))

        self.p_on_line.setText(str(f_on))

        if f_off != 0:
            self.p_off_line.setText(str(f_off))
            self.n_line.setText(str((f_off-f_on) / f_off * 100))

    def make_table(self):
        available_stations_df = pd.DataFrame(columns=STATION_DATA_FILE_COLUMNS)

        date_start = dat.datetime.strptime(self.view_rng_start_line.text(),
                                           "%d.%m.%Y %H:%M:%S")
        date_end = dat.datetime.strptime(self.view_rng_end_line.text(),
                                         "%d.%m.%Y %H:%M:%S")

        cur_station = self.complex_list_widget.currentItem().text()
        data_filenames = os.listdir(path=STATION_DATA_FOLD)

        for filename in data_filenames:
            if cur_station in filename:
                station_content = open(f"{STATION_DATA_FOLD}/{filename}").readlines()

                for line in station_content:
                    content_list = line.split(";")
                    content_list += [None] * (len(STATION_DATA_FILE_COLUMNS) -
                                              len(content_list))
                    date_start_file = dat.datetime.strptime(content_list[0],
                                                            "%d.%m.%Y %H:%M:%S")
                    date_end_file = dat.datetime.strptime(content_list[1],
                                                          "%d.%m.%Y %H:%M:%S")

                    if (date_start <= date_start_file and
                        date_end >= date_end_file):
                        station_df = pd.DataFrame([content_list],
                                                  columns=STATION_DATA_FILE_COLUMNS)
                        available_stations_df = pd.concat([available_stations_df,
                                                           station_df])

        utl.df_date_sort(available_stations_df,
                         "Measurement start time",
                         "%d.%m.%Y %H:%M:%S")

        os.makedirs(TMP_FOLD, exist_ok=True)
        available_stations_df.to_csv(PLOT_TABLE_PATH, index=False)

    def make_plots(self):
        plt.close()

        try:
            df = pd.read_csv(PLOT_TABLE_PATH)
        except FileNotFoundError:
            df = pd.DataFrame(columns=STATION_DATA_FILE_COLUMNS)

        plt.style.use("ggplot")
        plot_legend = ["по фазе A",
                       "по фазе B",
                       "по фазе C"]

        try:
            ax = df.plot(figsize=(7, 6),
                         xlabel="Время",
                         ylabel="Активная мощность при включенной системе",
                         y=["Active power phase A on",
                            "Active power phase B on",
                            "Active power phase C on"])
        except TypeError:
            ax = plt.subplot()
            ax.plot()
            ax.set_xlabel("Время")
            ax.set_ylabel("Активная мощность при включенной системе")

        ax.legend(plot_legend)

        os.makedirs(TMP_FOLD, exist_ok=True)

        ax.figure.savefig(PLOT_PICT1_PATH)
        image = PIL.Image.open(PLOT_PICT1_PATH)
        resized_image = image.resize((370, 325))
        resized_image.save(RESIZED_PLOT_PICT1_PATH)
        self.left_plot.setStyleSheet(f"background-image: url({RESIZED_PLOT_PICT1_PATH});\n"
                                     "background-repeat: no-repeat;\n"
                                     "background-position: center;")

        try:
            ax2 = df.plot(figsize=(7, 6),
                          xlabel="Время",
                          ylabel="Реактивная мощность при включенной системе",
                          y=["Reactive power phase A on",
                             "Reactive power phase B on",
                             "Reactive power phase C on"])
        except TypeError:
            ax2 = plt.subplot()
            ax2.plot()
            ax2.set_xlabel("Время")
            ax2.set_ylabel("Реактивная мощность при включенной системе")

        ax2.legend(plot_legend)

        ax2.figure.savefig(PLOT_PICT2_PATH)
        image = PIL.Image.open(PLOT_PICT2_PATH)
        resized_image = image.resize((370, 325))
        resized_image.save(RESIZED_PLOT_PICT2_PATH)
        self.right_plot.setStyleSheet(f"background-image: url({RESIZED_PLOT_PICT2_PATH});\n"
                                      "background-repeat: no-repeat;\n"
                                      "background-position: center;")

        plt.close()

    def download_data(self):
        os.makedirs(OUT_FOLD, exist_ok=True)

        sht.copyfile(PLOT_TABLE_PATH, OUT_TABLE_PATH)

        sht.copyfile(PLOT_PICT1_PATH, OUT_PICT1_PATH)
        sht.copyfile(PLOT_PICT2_PATH, OUT_PICT2_PATH)
