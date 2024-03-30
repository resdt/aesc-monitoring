import os
import pandas as pd

import src.main.PATH as path
import src.windows.login_window as lw
import src.windows.admin_window as aw
import src.windows.user_window as uw


TMP_FOLD = path.TMP_FOLD

ADMIN_DATA_FILE_PATH = path.ADMIN_DATA_FILE_PATH
USER_DATA_FILE_PATH = path.USER_DATA_FILE_PATH
CUR_LOGIN_DATA_PATH = path.CUR_LOGIN_DATA_PATH


class MyWin(lw.QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        lw.QtWidgets.QWidget.__init__(self, parent)

        self.login_ui = lw.UiLoginWindow()
        self.login_ui.setup_ui(self)
        self.login_ui.entry_button.clicked.connect(self.check_login)

    def check_login(self):
        admin_df = pd.read_csv(ADMIN_DATA_FILE_PATH, dtype=str)
        user_df = pd.read_csv(USER_DATA_FILE_PATH, dtype=str)

        cur_login = self.login_ui.login_line.text()
        cur_passwd = self.login_ui.passwd_line.text()

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
        self.admin_window = lw.QtWidgets.QMainWindow()
        self.admin_ui = aw.UiAdminWindow()

        self.admin_ui.setup_ui(self.admin_window)
        self.admin_window.show()

    def open_user_window(self):
        self.user_window = lw.QtWidgets.QMainWindow()
        self.user_ui = uw.UiUserWindow()

        self.user_ui.setup_ui(self.user_window)
        self.user_window.show()
