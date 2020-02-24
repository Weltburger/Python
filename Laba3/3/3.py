import locale
import sys
from os import path
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from script import script
from datetime import datetime
from re import sub

from ex3 import Ui_MainWindow  # импорт нашего сгенерированного файла


def shorten(from_start, to_end, string):
    return sub(r'^(.{,25}/).*?(/.{,25})$', '\g<1>...\g<2>', string)


def get_time_now():
    return datetime.now().strftime('%x %X')


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.listView.setModel(QStandardItemModel(self))
        if not path.exists('script18.log'):
            mes = QMessageBox(QMessageBox.Information, 'Ошибка', 'Файл лога не найден. Файл будет создан автоматически.', buttons=QMessageBox.Ok, parent=self)
            mes.open()
        locale.setlocale(locale.LC_ALL, 'ru-RU')

    def open_file(self):
        self.fileDialog = QFileDialog()
        self.fileDialog.open()
        self.fileDialog.fileSelected.connect(self.run_script)

    def run_script(self):
        model = self.ui.listView.model()
        for file in self.fileDialog.selectedFiles():
            self.set_filesize(file)
            self.set_file_open_action(file)
            item = QStandardItem('Файл {} был обработан {}:'.format(shorten(25, 25, file), get_time_now()))
            model.appendRow(item)
            model.appendRow(QStandardItem(''))
            for s in script(file):
                model.appendRow(QStandardItem(s))
            model.appendRow(QStandardItem(''))


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
