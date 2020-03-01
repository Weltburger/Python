import locale
import re
import sys
from os import path
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.uic.properties import QtGui

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
        self.entry = QStandardItemModel()
        self.ui.listView.setModel(QStandardItemModel(self.entry))
        self.data = []
        if not path.exists('script18.log'):
            mes = QMessageBox(QMessageBox.Information, 'Ошибка', 'Файл лога не найден. Файл будет создан автоматически.', buttons=QMessageBox.Ok, parent=self)
            myFile = open("script18.log", "w+")
            myFile.close()
            mes.open()
        locale.setlocale(locale.LC_ALL, 'ru-RU')

    def find_match(self, text):
        model = self.ui.listView.model()
        for i in range(len(text)):
            pattern = re.compile(r'[a-z]{1,}: (?:int|short|byte) \[[0-9]{1,}\]')
            result = pattern.findall(text[i])
            searchForResult = pattern.search(text[i])
            if searchForResult is not None:
                print('Строка ', i, ', Позиция ', searchForResult.span(), " найдено : '{}'".format(result[0]))
                it = QStandardItem('Строка ', i, ', Позиция ', searchForResult.span(), " найдено : '{}'".format(result[0]))
                model.appendRow(it)
                #self.entry.appendRow(it)


    def open_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.')[0]
        f = open(fname, 'r')
        #self.set_filesize(f)
        #self.set_file_open_action(f)
        with f:
            self.data = f.readlines()
        print(self.data)
        self.find_match(self.data)

        # self.fileDialog = QFileDialog()
        # self.fileDialog.open()
        # self.fileDialog.fileSelected.connect(self.run_script)

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

    def set_file_open_action(self, file):
        self.ui.lastActionLabel.setText('Открыт файл {}'.format(shorten(25, 25, file)))

    def set_filesize(self, file):
        self.ui.lastFileSizeLabel.setText('{:n} байт'.format(path.getsize(file)))


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
