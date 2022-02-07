import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter

class Conv(QtWidgets.QMainWindow):
    def __init__(self):
        super(Conv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Конвертер валют')
        self.setWindowIcon(QIcon("./ico.png"))
    
        self.ui.input_currency.setPlaceholderText("Из валюты:")
        self.ui.input_amount.setPlaceholderText("У меня есть:")
        self.ui.output_currency.setPlaceholderText("В валюту:")
        self.ui.output_amount.setPlaceholderText("Я получу:")
        self.ui.convert_btn.clicked.connect(self.converter)

    def converter(self):
        c = CurrencyConverter()
        input_currency = self.ui.input_currency.text()
        input_amount = int(self.ui.input_amount.text())
        output_currency = self.ui.output_currency.text()

        output_amount = round(c.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency)), 2)
        
        self.ui.output_amount.setText(str(output_amount))


app = QtWidgets.QApplication([])
application = Conv()
application.show()

sys.exit(app.exec())