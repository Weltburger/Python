import re
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication, QPushButton, QCheckBox, QSpinBox, QRadioButton)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # -----------Creation---------------------------------------------
        # label
        labelStroka = QLabel('Строка: ')
        labelResult = QLabel('Результат: ')
        labelBkv = QLabel('букв')

        # lineEdit

        self.lineEditInput = QLineEdit()
        self.lineEditResult = QLineEdit()
        self.input_ = self.lineEditInput.text()
        self.output_ = self.lineEditResult.text()

        # chekbox
        self.checkbox1 = QCheckBox('Удалить слова размером меньше')
        self.checkbox1.setGeometry(0, 0, 220, 21)
        self.checkbox2 = QCheckBox('Заменить все цифры на *')
        self.checkbox3 = QCheckBox('Вставить по пробелу между символами')
        self.checkbox4 = QCheckBox('Сортировать слова в строке')

        # QSpinBox
        self.spinBox1 = QSpinBox()
        self.spinBox1.setGeometry(0, 0, 42, 22)

        # QPushButton
        buttonFormat = QPushButton('Форматировать!', self)

        # QRadioButton
        self.radio1 = QRadioButton('По размеру')
        self.radio2 = QRadioButton('Лексиграфически')
        self.radio1.setEnabled(False)
        self.radio2.setEnabled(False)
        # ---------------Position-----------------------------
        grid = QGridLayout()
        grid.setSpacing(10)

        # label
        grid.addWidget(labelStroka, 1, 0)
        grid.addWidget(labelResult, 9, 0)
        grid.addWidget(labelBkv, 2, 3)

        # lineEdit
        grid.addWidget(self.lineEditInput, 1, 1)
        grid.addWidget(self.lineEditResult, 9, 1)

        # chekbox
        grid.addWidget(self.checkbox1, 2, 1)
        grid.addWidget(self.checkbox2, 3, 1)
        grid.addWidget(self.checkbox3, 4, 1)
        grid.addWidget(self.checkbox4, 5, 1)

        # QPushButton
        grid.addWidget(buttonFormat, 8, 1)

        # QSpinBox
        grid.addWidget(self.spinBox1, 2, 2)

        # QRadioButton
        grid.addWidget(self.radio1, 6, 1)
        grid.addWidget(self.radio2, 7, 1)

        buttonFormat.clicked.connect(self.buttonClicked)
        self.checkbox4.clicked.connect(self.checkClicked)
        self.radio1.clicked.connect(self.radioClicked)
        self.radio2.clicked.connect(self.radioClicked)
        # ---------------------------------------------------------
        self.setLayout(grid)
        self.setGeometry(350, 350, 400, 350)
        self.setWindowTitle('StringFormatter')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close

    def checkClicked(self):
        if self.checkbox4.isChecked():
            self.radio1.setEnabled(True)
            self.radio2.setEnabled(True)
        else:
            self.radio1.setChecked(False)
            self.radio1.setEnabled(False)
            self.radio2.setChecked(False)
            self.radio2.setEnabled(False)

    def radioClicked(self):
        pass

    def buttonClicked(self):
        # ---on button click starts formatting------
        self.input_ = ''
        self.output_ = ''
        self.input_ = self.lineEditInput.text()
        self.output_ = self.input_

        # --------1st checkbox 'Удалить слова размером меньше n символов'----------------------
        if self.checkbox1.isChecked():
            n = self.spinBox1.value()
            words_list = self.input_.split(' ')
            arr = list(filter(lambda x: len(x) >= n, words_list))
            self.output_ = ' '.join(arr)
            self.lineEditResult.setText(self.output_)

        # --------2nd checkbox 'Заменить все цифры на *'----------------------
        if self.checkbox2.isChecked():
            self.output_ = re.sub('\d', '*', self.output_)
            self.lineEditResult.setText(self.output_)

        # --------3rd checkbox 'Вставить по пробелу между символами'----------------------
        if self.checkbox3.isChecked():
            self.output_ = ' '.join(list(self.output_))
            self.lineEditResult.setText(self.output_)

        # --------4th checkbox 'Сортировать слова в строке'----------------------
        if self.checkbox4.isChecked() and self.radio1.isChecked():  # Size
            arr = sorted(self.output_.split(), key=len)
            self.output_ = ' '.join(arr)
            self.lineEditResult.setText(self.output_)

        if self.checkbox4.isChecked() and self.radio2.isChecked():  # Lex
            arr = sorted(self.output_.split())
            self.output_ = ' '.join(arr)
            self.lineEditResult.setText(self.output_)

        # ----------Output--------------------------
        if not self.checkbox1.isChecked() and not self.checkbox2.isChecked() and not self.checkbox3.isChecked() and not self.checkbox4.isChecked():
            self.output_ = self.input_
            self.lineEditResult.setText(self.output_)
        # ------------------------------------------
        self.lineEditResult.setText(self.output_)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
