import locale
import sys
from os import path
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from ex3 import Ui_MainWindow  # импорт нашего сгенерированного файла

log_filename = 'script18.log'


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        if not path.exists(log_filename):
            mes = QMessageBox(QMessageBox.Information,
                              'Ошибка', 'Файл лога не найден. '
                                        'Файл будет создан автоматически.',
                              buttons=QMessageBox.Ok, parent=self)
            mes.open()
        locale.setlocale(locale.LC_ALL, 'ru-RU')


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
