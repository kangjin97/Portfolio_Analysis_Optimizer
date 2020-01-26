# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'portfolio_analysis_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 700)
        MainWindow.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(80, 600, 211, 41))
        self.Button1.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 63 12pt \"Open Sans Semibold\";")
        self.Button1.setObjectName("Button1")
        self.Button1.clicked.connect(self.pushButton1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 191, 41))
        self.label.setStyleSheet("font: 57 14pt \"Dubai Medium\";")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 100, 51, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_2.raise_()
        self.label_1.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.label_6.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_8.raise_()
        self.label_annualReturn = QtWidgets.QLabel(self.centralwidget)
        self.label_annualReturn.setGeometry(QtCore.QRect(430, 530, 151, 31))
        self.label_annualReturn.setObjectName("label_annualReturn")
        self.label_standardDeviation = QtWidgets.QLabel(self.centralwidget)
        self.label_standardDeviation.setGeometry(QtCore.QRect(430, 580, 141, 31))
        self.label_standardDeviation.setObjectName("label_standardDeviation")
        self.textEdit_annualReturn = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_annualReturn.setGeometry(QtCore.QRect(590, 530, 121, 31))
        self.textEdit_annualReturn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_annualReturn.setObjectName("textEdit_annualReturn")
        self.textEdit_standardDeviation = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_standardDeviation.setGeometry(QtCore.QRect(590, 580, 121, 31))
        self.textEdit_standardDeviation.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_standardDeviation.setObjectName("textEdit_standardDeviation")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(110, 100, 231, 381))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_t1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_t1.setObjectName("lineEdit_t1")
        self.verticalLayout_2.addWidget(self.lineEdit_t1)
        self.lineEdit_t2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_t2.setObjectName("lineEdit_t2")
        self.verticalLayout_2.addWidget(self.lineEdit_t2)
        self.lineEdit_t3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_t3.setObjectName("lineEdit_t3")
        self.verticalLayout_2.addWidget(self.lineEdit_t3)
        self.lineEdit_t4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_t4.setObjectName("lineEdit_t4")
        self.verticalLayout_2.addWidget(self.lineEdit_t4)
        self.lineEdit_t5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_t5.setObjectName("lineEdit_t5")
        self.verticalLayout_2.addWidget(self.lineEdit_t5)
        self.lineEdit_t6 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_t6.setObjectName("lineEdit_t6")
        self.verticalLayout_2.addWidget(self.lineEdit_t6)
        self.lineEdit_t7 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_t7.setObjectName("lineEdit_t7")
        self.verticalLayout_2.addWidget(self.lineEdit_t7)
        self.lineEdit_t8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_t8.setObjectName("lineEdit_t8")
        self.verticalLayout_2.addWidget(self.lineEdit_t8)
        self.lineEdit_t9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_t9.setObjectName("lineEdit_t9")
        self.verticalLayout_2.addWidget(self.lineEdit_t9)
        self.lineEdit_t10 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_t10.setObjectName("lineEdit_t10")
        self.verticalLayout_2.addWidget(self.lineEdit_t10)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(360, 100, 231, 381))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_p1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_p1.setObjectName("lineEdit_p1")
        self.verticalLayout_3.addWidget(self.lineEdit_p1)
        self.lineEdit_p2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_p2.setText("")
        self.lineEdit_p2.setObjectName("lineEdit_p2")
        self.verticalLayout_3.addWidget(self.lineEdit_p2)
        self.lineEdit_p3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_p3.setObjectName("lineEdit_p3")
        self.verticalLayout_3.addWidget(self.lineEdit_p3)
        self.lineEdit_p4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_p4.setObjectName("lineEdit_p4")
        self.verticalLayout_3.addWidget(self.lineEdit_p4)
        self.lineEdit_p5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_p5.setObjectName("lineEdit_p5")
        self.verticalLayout_3.addWidget(self.lineEdit_p5)
        self.lineEdit_p6 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_p6.setObjectName("lineEdit_p6")
        self.verticalLayout_3.addWidget(self.lineEdit_p6)
        self.lineEdit_p7 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_p7.setObjectName("lineEdit_p7")
        self.verticalLayout_3.addWidget(self.lineEdit_p7)
        self.lineEdit_p8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_p8.setObjectName("lineEdit_p8")
        self.verticalLayout_3.addWidget(self.lineEdit_p8)
        self.lineEdit_p9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_p9.setObjectName("lineEdit_p9")
        self.verticalLayout_3.addWidget(self.lineEdit_p9)
        self.lineEdit_p10 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_p10.setObjectName("lineEdit_p10")
        self.verticalLayout_3.addWidget(self.lineEdit_p10)
        self.dateEdit_startDate = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_startDate.setGeometry(QtCore.QRect(180, 510, 110, 22))
        self.dateEdit_startDate.setObjectName("dateEdit_startDate")
        self.dateEdit_endDate = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_endDate.setGeometry(QtCore.QRect(180, 540, 110, 22))
        self.dateEdit_endDate.setObjectName("dateEdit_endDate")
        self.label_startDate = QtWidgets.QLabel(self.centralwidget)
        self.label_startDate.setGeometry(QtCore.QRect(100, 500, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_startDate.setFont(font)
        self.label_startDate.setObjectName("label_startDate")
        self.label_endDate = QtWidgets.QLabel(self.centralwidget)
        self.label_endDate.setGeometry(QtCore.QRect(100, 530, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_endDate.setFont(font)
        self.label_endDate.setObjectName("label_endDate")
        self.label_endDate.raise_()
        self.label_startDate.raise_()
        self.Button1.raise_()
        self.label.raise_()
        self.verticalLayoutWidget.raise_()
        self.label_annualReturn.raise_()
        self.label_standardDeviation.raise_()
        self.textEdit_annualReturn.raise_()
        self.textEdit_standardDeviation.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.dateEdit_startDate.raise_()
        self.dateEdit_endDate.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def pushButton1(self):
        tinkerInputs = [self.lineEdit_t1.text(), self.lineEdit_t2.text(), self.lineEdit_t3.text(),
                        self.lineEdit_t4.text(), self.lineEdit_t5.text(), self.lineEdit_t6.text(),
                        self.lineEdit_t7.text(), self.lineEdit_t8.text(), self.lineEdit_t9.text(),
                        self.lineEdit_t10.text()]

        weightInputs = [self.lineEdit_p1.text(), self.lineEdit_p2.text(), self.lineEdit_p3.text(),
                        self.lineEdit_p4.text(), self.lineEdit_p5.text(), self.lineEdit_p6.text(),
                        self.lineEdit_p7.text(), self.lineEdit_p8.text(), self.lineEdit_p9.text(),
                        self.lineEdit_p10.text()]

        new_tinkerInputs = []
        new_weightInputs = []
        for i in range(10):
            if tinkerInputs[i] != "":
                new_tinkerInputs.append(tinkerInputs[i])
                if weightInputs[i] == "":
                    weight = 0.0
                else:
                    weight = float(weightInputs[i])
                new_weightInputs.append(weight)

        start = str(self.dateEdit_startDate.date().year()) + '-' + str(
            self.dateEdit_startDate.date().month()) + '-' + str(self.dateEdit_startDate.date().day())
        end = str(self.dateEdit_endDate.date().year()) + '-' + str(self.dateEdit_endDate.date().month()) + '-' + str(
            self.dateEdit_endDate.date().day())


        annualReturn, standardDeviation = calculate(new_tinkerInputs, new_weightInputs, start, end)


        self.textEdit_annualReturn.setText(str(round(annualReturn,2) * 100) + "%")
        self.textEdit_standardDeviation.setText(str(round(standardDeviation, 2) * 100) + "%")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Portfolio Analysis Tool"))
        self.Button1.setText(_translate("MainWindow", "Calculate"))
        self.label.setText(_translate("MainWindow", "Portfolio Assets"))
        self.label_1.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "3"))
        self.label_4.setText(_translate("MainWindow", "4"))
        self.label_5.setText(_translate("MainWindow", "5"))
        self.label_6.setText(_translate("MainWindow", "6"))
        self.label_7.setText(_translate("MainWindow", "7"))
        self.label_8.setText(_translate("MainWindow", "8"))
        self.label_9.setText(_translate("MainWindow", "9"))
        self.label_10.setText(_translate("MainWindow", "10"))
        self.label_annualReturn.setText(_translate("MainWindow", "Expected Annual Return: "))
        self.label_standardDeviation.setText(_translate("MainWindow", "Standard Deviation:"))
        self.lineEdit_t1.setPlaceholderText(_translate("MainWindow", "Tinker Symbol"))
        self.lineEdit_t2.setPlaceholderText(_translate("MainWindow", "Tinker Symbol"))
        self.lineEdit_t3.setPlaceholderText(_translate("MainWindow", "Tinker Symbol"))
        self.lineEdit_t4.setPlaceholderText(_translate("MainWindow", "Tinker Symbol"))
        self.lineEdit_t5.setPlaceholderText(_translate("MainWindow", "Tinker Symbol"))
        self.lineEdit_t6.setPlaceholderText(_translate("MainWindow", "Tinker Symbol"))
        self.lineEdit_t7.setPlaceholderText(_translate("MainWindow", "Tinker Symbol"))
        self.lineEdit_t8.setPlaceholderText(_translate("MainWindow", "Tinker Symbol"))
        self.lineEdit_t9.setPlaceholderText(_translate("MainWindow", "Tinker Symbol"))
        self.lineEdit_t10.setPlaceholderText(_translate("MainWindow", "Tinker Symbol"))
        self.lineEdit_p1.setPlaceholderText(_translate("MainWindow", "Percentage"))
        self.lineEdit_p2.setPlaceholderText(_translate("MainWindow", "Percentage"))
        self.lineEdit_p3.setPlaceholderText(_translate("MainWindow", "Percentage"))
        self.lineEdit_p4.setPlaceholderText(_translate("MainWindow", "Percentage"))
        self.lineEdit_p5.setPlaceholderText(_translate("MainWindow", "Percentage"))
        self.lineEdit_p6.setPlaceholderText(_translate("MainWindow", "Percentage"))
        self.lineEdit_p7.setPlaceholderText(_translate("MainWindow", "Percentage"))
        self.lineEdit_p8.setPlaceholderText(_translate("MainWindow", "Percentage"))
        self.lineEdit_p9.setPlaceholderText(_translate("MainWindow", "Percentage"))
        self.lineEdit_p10.setPlaceholderText(_translate("MainWindow", "Percentage"))
        self.dateEdit_startDate.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.dateEdit_endDate.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.label_startDate.setText(_translate("MainWindow", "Start Date"))
        self.label_endDate.setText(_translate("MainWindow", "End Date"))

def calculate(stocks, weight, start, end):
    # Import Pandas web data access library

    import pandas as pd
    import pandas_datareader.data as web
    import numpy as np

    # Set the stock symbols, data source, and time range

    source = 'yahoo'
    # start = '2010-01-01'
    # end = '2016-01-01'

    # Retrieve stock price data and save just the dividend adjusted closing prices

    data = pd.DataFrame()

    for symbol in stocks:
        try:
            data[symbol] = web.DataReader(symbol, data_source=source, start=start, end=end)['Adj Close']
        except:
            error = f"Ticker Symbol {symbol} cannot be found"

    # Calculate simple linear returns

    returns = (data - data.shift(1)) / data.shift(1)

    # Calculate individual mean returns and covariance between the stocks

    meanDailyReturns = returns.mean()
    covMatrix = returns.cov()

    # Calculate expected portfolio performance

    weights = np.array(weight)
    portReturn = np.sum(meanDailyReturns * weights)
    annualReturn = portReturn * 365
    portStdDev = np.sqrt(np.dot(weights.T, np.dot(covMatrix, weights)))


    return annualReturn, portStdDev

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
