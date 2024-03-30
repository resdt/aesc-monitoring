import sys

import src.main.PATH as path
import src.main.utils as utl
import src.main.window_action as wa
import src.windows.login_window as lw


TMP_FOLD = path.TMP_FOLD

clean_dir = utl.clean_dir


def main():
    app = lw.QtWidgets.QApplication(sys.argv)
    window = wa.MyWin()

    window.show()
    app.exec_()

    clean_dir(TMP_FOLD)
