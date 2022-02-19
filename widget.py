# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys;
import obd;
from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

connection = obd.Async('/dev/cu.usbserial-113011152750');


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()
        

    def changeNum (self):
        def new_psi(r):
            new_num = [int(s) for s in str(r).split() if s.isdigit()]
            display_num = round(new_num[0] * 0.14503774)

            self.findChild(QtWidgets.QLCDNumber, 'lcdNumber').display(display_num)

        def new_oil_temp(r):
            print(r.value)

            new_num = [int(s) for s in str(r.value.to('f')).split() if s.isdigit()]
            print(round(new_num[0]));

            self.findChild(QtWidgets.QLCDNumber, 'lcdNumber_2').display()


        connection.watch(obd.commands.INTAKE_PRESSURE, callback=new_psi, force=True);
        connection.watch(obd.commands.OIL_TEMP, callback=new_oil_temp, force=True);

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
