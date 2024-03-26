import os
import pandas as pd

import src.main.PATH as path
import src.windows.LoginPage as lp
import src.windows.AdminWindow as aw
import src.windows.UserWindow as uw


TMP_FOLD = path.TMP_FOLD

ADMIN_DATA_FILE_PATH = path.ADMIN_DATA_FILE_PATH
USER_DATA_FILE_PATH = path.USER_DATA_FILE_PATH
CUR_LOGIN_DATA_PATH = path.CUR_LOGIN_DATA_PATH


class MyWin(lp.QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        lp.QtWidgets.QWidget.__init__(self, parent)

        self.ui = lp.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.entry_button.clicked.connect(self.check_login)

    def check_login(self):
        admin_df = pd.read_csv(ADMIN_DATA_FILE_PATH, dtype=str)
        user_df = pd.read_csv(USER_DATA_FILE_PATH, dtype=str)

        cur_login = self.ui.login_line.text()
        cur_passwd = self.ui.passwd_line.text()

        if admin_df.loc[(admin_df["Login"] == cur_login) &
                        (admin_df["Password"] == cur_passwd)].any().any():
            self.open_admin_window()
        elif user_df.loc[(user_df["Login"] == cur_login) &
                         (user_df["Password"] == cur_passwd)].any().any():
            df_row = user_df[user_df["Login"] == cur_login]

            os.makedirs(TMP_FOLD, exist_ok=True)

            with open(CUR_LOGIN_DATA_PATH, "w", newline="") as login_file:
                df_row.to_csv(login_file, index=False)

            self.open_user_window()

    def open_admin_window(self):
        self.adminWindow = lp.QtWidgets.QMainWindow()
        self.ui = aw.Ui_AdminWindow()

        self.ui.setupUi(self.adminWindow)
        self.adminWindow.show()

    def open_user_window(self):
        self.userWindow = lp.QtWidgets.QMainWindow()
        self.ui = uw.Ui_UserWindow()

        self.ui.setupUi(self.userWindow)
        self.userWindow.show()
