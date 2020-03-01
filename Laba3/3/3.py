import sys
import locale
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ex3 import Ui_MainWindow
from script import script
from datetime import datetime
from re import sub
from os import path

log_filename = 'script18.log'


def shorten(from_start, to_end, string):
    return sub(r'^(.{,25}/).*?(/.{,25})$', '\g<1>...\g<2>', string)


def get_time_now():
    return datetime.now().strftime('%x %X')


class MyForm(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.listView.setModel(QStandardItemModel(self))
        if not path.exists(log_filename):
            mes = QMessageBox(QMessageBox.Information, 'Файл лога не найден', 'Файл лога не найден. \nФайл будет создан автоматически.', buttons=QMessageBox.Ok, parent=self)
            myFile = open(log_filename, 'w+')
            myFile.close()
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
            model.appendRow(QStandardItem('Файл {} был обработан {}:'
                                          .format(shorten(25, 25, file),
                                                  get_time_now())))
            model.appendRow(QStandardItem(''))
            for s in script(file):
                model.appendRow(QStandardItem(s))
            model.appendRow(QStandardItem(''))

    def export_log(self):
        self.exportDialog = QFileDialog()
        self.exportDialog.acceptMode = QFileDialog.AcceptSave
        self.exportDialog.setModal(True)
        self.exportDialog.exec()
        with open(self.exportDialog.selectedFiles()[0], 'wb') as log:
            model = self.ui.listView.model()
            log.writelines([(model.item(i).text() + '\n').encode('utf-8')
                           for i in range(model.rowCount())])

    def add_log(self):
        with open(log_filename, 'ab') as log:
            model = self.ui.listView.model()
            log.writelines([(model.item(i).text() + '\n').encode('utf-8')
                           for i in range(model.rowCount())])

    def look_log(self):
        if not path.exists(log_filename):
            return
        self.ask_to_look()

    def ask_to_look(self):
        buttonReply = QMessageBox.question(self, 'Подтверждение действия', 'Вы действительно хотите открыть лог? '
                                                                           'Данные последних поисков будут потеряны!',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            model = self.ui.listView.model()
            model.clear()
            with open(log_filename, 'rb') as log:
                self.set_log_open_action()
                self.set_filesize(log_filename)
                for string in log:
                    model.appendRow(QStandardItem(string.decode('utf-8').strip()))
        else:
            return

    def set_file_open_action(self, file):
        self.ui.lastActionLabel.setText('Открыт файл {}'.format(shorten(25, 25, file)))

    def set_log_open_action(self):
        self.ui.lastActionLabel.setText('Открыт лог')

    def set_filesize(self, file):
        self.ui.lastFileSizeLabel.setText('{:n} байт'.format(path.getsize(file)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    try:
        sys.exit(app.exec_())
    except SystemExit as se:
        print('Program has exited with code {}'.format(se))
