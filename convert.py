from PyQt5 import uic
# from PyQt5.QtCore import PYQT_VERSION_STR
import PyQt5

fin = open("main.ui", "r")
fout = open("ui.py", "w")
# fout.write("fuck")

uic.compileUi(fin, fout)


# print (PYQT_VERSION_STR)
