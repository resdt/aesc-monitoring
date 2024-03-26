import sys

import src.main.PATH as path
import src.main.utils as utl
import src.main.WindowAction as wa
import src.windows.LoginPage as lp


TMP_FOLD = path.TMP_FOLD

clean_dir = utl.clean_dir


def main():
    app = lp.QtWidgets.QApplication(sys.argv)
    window = wa.MyWin()

    window.show()
    app.exec_()

    clean_dir(TMP_FOLD)
