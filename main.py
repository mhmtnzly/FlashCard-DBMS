from login import Login_window
from PyQt5 import QtWidgets,uic
import sys
app = QtWidgets.QApplication(sys.argv)
window = Login_window()
app.exec_()