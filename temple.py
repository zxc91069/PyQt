# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui, QtCore
from UI_main import Ui_MainWindow
import sys
from Csv_person import Person, Family
import csv


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.nl_pushButton.clicked.connect(self.NLbuttonClicked)
        self.ui.sl_pushButton.clicked.connect(self.SLbuttonClicked)
        self.ui.qa_pushButton.clicked.connect(self.SameAddrClicked)
        self.ui.pushButton_3.clicked.connect(self.query_record)

    def query_record(self):
        name = self.ui.ql_name.text()
        with open('./csv/所有點燈紀錄.csv', newline='') as csvfile:
            allcsvrows = csv.reader(csvfile)
            lit = []
            for i in allcsvrows:
                if i[0] == name:
                    lit.append(f"{i[0]}  {i[1]}  {i[3]}")
        # QlistView設定
        if lit:
            slm = QtCore.QStringListModel()
            self.ui.listView.qList = lit
            slm.setStringList(self.ui.listView.qList)
            self.ui.listView.setModel(slm)
        else:
            QtWidgets.QMessageBox.information(self, '錯誤', '查無相關紀錄')


    def SameAddrClicked(self):
        query_name = str(self.ui.qa_name_2.text())
        self.family = Family()
        self.family.same_address(query_name)
        # QlistView設定
        if self.family.p:
            slm = QtCore.QStringListModel()
            self.ui.listView_2.qList = self.family.p
            slm.setStringList(self.ui.listView_2.qList)
            self.ui.listView_2.setModel(slm)
            self.ui.qa_label.setText(self.family.adr)
        else:
            QtWidgets.QMessageBox.information(self, '錯誤', '查無相關同住人')

    def NLbuttonClicked(self):
        name = self.ui.nl_name.text()
        date = self.ui.nl_date.text()
        addr = self.ui.ni_address.text()
        self.person = Person(name, date, addr)
        self.person.new_person()
        if self.person.err:
            QtWidgets.QMessageBox.information(self, '錯誤', self.person.err)
        else:
            pass
        # self.ui.test_label.setText(name)
        # self.ui.lineEdit.clear()
        self.stateCheck()
        self.ui.nl_name.clear()
        self.ui.ni_address.clear()


    def SLbuttonClicked(self):
        name = self.ui.sl_name.text()
        addr = self.ui.sl_address.text()
        light_name = self.ui.sl_lightname.text()
        person = Person(name, None, addr)
        person.read_csv("所有點燈紀錄.csv", [person.name, light_name, person.address, person.time])
        person.read_csv("其他燈.csv", [person.name, light_name, person.address])
        if person.err:
            QtWidgets.QMessageBox.information(self, '錯誤', person.err)
        else:
            pass
        self.ui.sl_lightname.clear()
        self.ui.sl_address.clear()
        self.ui.sl_name.clear()

    def stateCheck(self):
        if self.ui.checkBox.isChecked() and self.ui.checkBox_2.isChecked() and self.ui.checkBox_3.isChecked() and self.ui.checkBox_4.isChecked():
            self.person.read_csv("光明燈.csv", [self.person.name])
            self.person.read_csv("太歲燈.csv", [self.person.name])
            self.person.read_csv("健康燈.csv", [self.person.name])
            self.person.read_csv("文昌燈.csv", [self.person.name])
            self.person.read_csv("所有點燈紀錄.csv", [self.person.name, '光明燈 太歲燈 健康燈 文昌燈', self.person.address, self.person.time])
        elif self.ui.checkBox.isChecked() and self.ui.checkBox_2.isChecked() and self.ui.checkBox_3.isChecked():
            self.person.read_csv("光明燈.csv", [self.person.name])
            self.person.read_csv("太歲燈.csv", [self.person.name])
            self.person.read_csv("健康燈.csv", [self.person.name])
            self.person.read_csv("所有點燈紀錄.csv", [self.person.name, '光明燈 太歲燈 健康燈', self.person.address, self.person.time])
        elif self.ui.checkBox.isChecked() and self.ui.checkBox_2.isChecked() and self.ui.checkBox_4.isChecked():
            self.person.read_csv("光明燈.csv", [self.person.name])
            self.person.read_csv("太歲燈.csv", [self.person.name])
            self.person.read_csv("文昌燈.csv", [self.person.name])
            self.person.read_csv("所有點燈紀錄.csv", [self.person.name, '光明燈 太歲燈 文昌燈', self.person.address, self.person.time])
        elif self.ui.checkBox.isChecked() and self.ui.checkBox_3.isChecked() and self.ui.checkBox_4.isChecked():
            self.person.read_csv("光明燈.csv", [self.person.name])
            self.person.read_csv("健康燈.csv", [self.person.name])
            self.person.read_csv("文昌燈.csv", [self.person.name])
            self.person.read_csv("所有點燈紀錄.csv", [self.person.name, '光明燈 健康燈 文昌燈', self.person.address, self.person.time])
        elif self.ui.checkBox_2.isChecked() and self.ui.checkBox_3.isChecked() and self.ui.checkBox_4.isChecked():
            self.person.read_csv("太歲燈.csv", [self.person.name])
            self.person.read_csv("健康燈.csv", [self.person.name])
            self.person.read_csv("文昌燈.csv", [self.person.name])
            self.person.read_csv("所有點燈紀錄.csv", [self.person.name, '太歲燈 健康燈 文昌燈', self.person.address, self.person.time])
        elif self.ui.checkBox.isChecked() and self.ui.checkBox_2.isChecked():
            self.person.read_csv("光明燈.csv", [self.person.name])
            self.person.read_csv("太歲燈.csv", [self.person.name])
            self.person.read_csv("所有點燈紀錄.csv", [self.person.name, '光明燈 太歲燈', self.person.address, self.person.time])
        elif self.ui.checkBox.isChecked() and self.ui.checkBox_3.isChecked():
            self.person.read_csv("光明燈.csv", [self.person.name])
            self.person.read_csv("健康燈.csv", [self.person.name])
            self.person.read_csv("所有點燈紀錄.csv", [self.person.name, '光明燈 健康燈', self.person.address, self.person.time])
        elif self.ui.checkBox.isChecked() and self.ui.checkBox_4.isChecked():
            self.person.read_csv("光明燈.csv", [self.person.name])
            self.person.read_csv("文昌燈.csv", [self.person.name])
            self.person.read_csv("所有點燈紀錄.csv", [self.person.name, '光明燈 文昌燈', self.person.address, self.person.time])
        elif self.ui.checkBox_2.isChecked() and self.ui.checkBox_3.isChecked():
            self.person.read_csv("太歲燈.csv", [self.person.name])
            self.person.read_csv("健康燈.csv", [self.person.name])
            self.person.read_csv("所有點燈紀錄.csv", [self.person.name, '太歲燈 健康燈', self.person.address, self.person.time])
        elif self.ui.checkBox_2.isChecked() and self.ui.checkBox_4.isChecked():
            self.person.read_csv("太歲燈.csv", [self.person.name])
            self.person.read_csv("文昌燈.csv", [self.person.name])
            self.person.read_csv("所有點燈紀錄.csv", [self.person.name, '太歲燈 文昌燈', self.person.address, self.person.time])
        elif self.ui.checkBox_3.isChecked() and self.ui.checkBox_4.isChecked():
            self.person.read_csv("健康燈.csv", [self.person.name])
            self.person.read_csv("文昌燈.csv", [self.person.name])
            self.person.read_csv("所有點燈紀錄.csv", [self.person.name, '健康燈 文昌燈', self.person.address, self.person.time])
        elif self.ui.checkBox.isChecked():
            self.person.read_csv("光明燈.csv", [self.person.name])
            self.person.read_csv("所有點燈紀錄.csv", [self.person.name, '光明燈', self.person.address, self.person.time])
        elif self.ui.checkBox_2.isChecked():
            self.person.read_csv("太歲燈.csv", [self.person.name])
            self.person.read_csv("所有點燈紀錄.csv", [self.person.name, '太歲燈', self.person.address, self.person.time])
        elif self.ui.checkBox_3.isChecked():
            self.person.read_csv("健康燈.csv", [self.person.name])
            self.person.read_csv("所有點燈紀錄.csv", [self.person.name, '健康燈', self.person.address, self.person.time])
        elif self.ui.checkBox_4.isChecked():
            self.person.read_csv("文昌燈.csv", [self.person.name])
            self.person.read_csv("所有點燈紀錄.csv", [self.person.name, '文昌燈', self.person.address, self.person.time])
        else:
            QtWidgets.QMessageBox.information(self, '點燈資訊', '請勾選')




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())