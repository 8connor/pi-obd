# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
import obd;
import time


# a callback that prints every new value to the console


# print(supports)

# # the callback will now be fired upon receipt of new values


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()
        

    def changeNum (self):
         
        print('HELLO WORLD!!!')

        def new_rpm(r):
            print(r.value)

            new_num = [int(s) for s in str(r).split() if s.isdigit()]
            print(round(new_num[0] * 0.14503774));
            display_num = round(new_num[0] * 0.14503774)

            self.findChild(QtWidgets.QLCDNumber, 'lcdNumber').display(display_num)

        connection = obd.Async('/dev/cu.usbserial-113011152750');
        connection.watch(obd.commands.INTAKE_PRESSURE, callback=new_rpm, force=True)
        connection.start()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.changeNum()
    widget.show()
    sys.exit(app.exec_())
