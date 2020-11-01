# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import generator
from functools import partial
import gen_pdf as gen
import time


def Gen_pdf_file(ui):
    add_flag = ui.ck_add_minus.isChecked()
    multi_flag = ui.ck_multi_plus.isChecked()
    add_range_value = ui.spinBox_add.value()
    multi_range_value = ui.spinBox_multi.value()
    pdf_name = time.strftime('%Y-%m-%d') + "练习题"
    print(add_flag, add_range_value, multi_flag, multi_range_value)
    gen.Gen_pdf(pdf_name, add_flag, add_range_value, multi_flag, multi_range_value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = generator.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.spinBox_add.setMaximum(100)
    ui.spinBox_add.setMinimum(10)
    ui.spinBox_multi.setMaximum(100)
    ui.spinBox_multi.setMinimum(10)
    MainWindow.show()
    ui.button_gen.clicked.connect(partial(Gen_pdf_file, ui))
    sys.exit(app.exec_())
