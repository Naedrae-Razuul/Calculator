# Made by Nathaniel Masson

from PyQt5 import QtCore, QtGui, QtWidgets


class equation:
    first = None
    second =  None
    third = None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 679)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(20, 100, 121, 121))
        self.one.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.one.setIcon(icon)
        self.one.setIconSize(QtCore.QSize(100, 100))
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(170, 100, 121, 121))
        self.two.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.two.setIcon(icon1)
        self.two.setIconSize(QtCore.QSize(100, 100))
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(320, 100, 121, 121))
        self.three.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.three.setIcon(icon2)
        self.three.setIconSize(QtCore.QSize(100, 100))
        self.three.setObjectName("three")
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(20, 240, 121, 121))
        self.four.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./images/4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.four.setIcon(icon3)
        self.four.setIconSize(QtCore.QSize(100, 100))
        self.four.setObjectName("four")
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(170, 240, 121, 121))
        self.five.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./images/5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.five.setIcon(icon4)
        self.five.setIconSize(QtCore.QSize(100, 100))
        self.five.setObjectName("five")
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(320, 240, 121, 121))
        self.six.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./images/6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.six.setIcon(icon5)
        self.six.setIconSize(QtCore.QSize(100, 100))
        self.six.setObjectName("six")
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(20, 380, 121, 121))
        self.seven.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./images/7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.seven.setIcon(icon6)
        self.seven.setIconSize(QtCore.QSize(100, 100))
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(170, 380, 121, 121))
        self.eight.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./images/8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eight.setIcon(icon7)
        self.eight.setIconSize(QtCore.QSize(100, 100))
        self.eight.setObjectName("eight")
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(320, 380, 121, 121))
        self.nine.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./images/9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nine.setIcon(icon8)
        self.nine.setIconSize(QtCore.QSize(100, 100))
        self.nine.setObjectName("nine")
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(140, 520, 121, 61))
        self.zero.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("./images/0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zero.setIcon(icon9)
        self.zero.setIconSize(QtCore.QSize(50, 100))
        self.zero.setObjectName("zero")
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(20, 10, 421, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(65)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.output.setFont(font)
        self.output.setAutoFillBackground(True)
        self.output.setFrameShape(QtWidgets.QFrame.Box)
        self.output.setLineWidth(1)
        self.output.setMidLineWidth(1)
        self.output.setTextFormat(QtCore.Qt.PlainText)
        self.output.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output.setObjectName("output")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(140, 580, 121, 61))
        self.clear.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("./images/CLEAR.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear.setIcon(icon14)
        self.clear.setIconSize(QtCore.QSize(100, 100))
        self.clear.setObjectName("clear")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(260, 520, 121, 61))
        self.add.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("./images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add.setIcon(icon10)
        self.add.setIconSize(QtCore.QSize(50, 100))
        self.add.setObjectName("add")
        self.equal = QtWidgets.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(380, 520, 61, 121))
        self.equal.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("./images/equal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.equal.setIcon(icon15)
        self.equal.setIconSize(QtCore.QSize(50, 100))
        self.equal.setObjectName("add_2")
        self.subtract = QtWidgets.QPushButton(self.centralwidget)
        self.subtract.setGeometry(QtCore.QRect(20, 520, 121, 61))
        self.subtract.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("./images/subtract.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subtract.setIcon(icon11)
        self.subtract.setIconSize(QtCore.QSize(50, 100))
        self.subtract.setObjectName("subtract")
        self.divide = QtWidgets.QPushButton(self.centralwidget)
        self.divide.setGeometry(QtCore.QRect(20, 580, 121, 61))
        self.divide.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("./images/divide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.divide.setIcon(icon12)
        self.divide.setIconSize(QtCore.QSize(50, 100))
        self.divide.setObjectName("divide")
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setGeometry(QtCore.QRect(260, 580, 121, 61))
        self.multiply.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("./images/multiply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.multiply.setIcon(icon13)
        self.multiply.setIconSize(QtCore.QSize(50, 100))
        self.multiply.setObjectName("multiply")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def zero():
            if equation.first == 0:
                return
            if equation.second == None:
                if equation.first != None:
                    equation.first = str(equation.first) + str(0)
                    self.output.setText(str(equation.first))
                    return
                else:
                    equation.first = 0
                    self.output.setText(str(equation.first))
                    return

            if equation.third != None:
                equation.third = str(equation.third) + str(0)
                self.output.setText(str(equation.third))
                return
            else:
                equation.first = 0
                self.output.setText(str(equation.first))



        def one():
            if equation.second == None:
                if equation.first != None:
                    equation.first = str(equation.first) + str(1)
                    self.output.setText(str(equation.first))
                    return
                if equation.first == None:
                    equation.first = 1
                    self.output.setText(str(equation.first))
                    return

            if equation.third != None:
                equation.third = str(equation.third) + str(1)
                self.output.setText(str(equation.third))
                return
            if equation.third == None:
                equation.third = 1
                self.output.setText(str(equation.third))
        def two():
            if equation.second == None:
                if equation.first != None:
                    equation.first = str(equation.first) + str(2)
                    self.output.setText(str(equation.first))
                    return
                if equation.first == None:
                    equation.first = 2
                    self.output.setText(str(equation.first))
                    return

            if equation.third != None:
                equation.third = str(equation.third) + str(2)
                self.output.setText(str(equation.third))
                return
            if equation.third == None:
                equation.third = 2
                self.output.setText(str(equation.third))
        def three():
            if equation.second == None:
                if equation.first != None:
                    equation.first = str(equation.first) + str(3)
                    self.output.setText(str(equation.first))
                    return
                if equation.first == None:
                    equation.first = 3
                    self.output.setText(str(equation.first))
                    return

            if equation.third != None:
                equation.third = str(equation.third) + str(3)
                self.output.setText(str(equation.third))
                return
            if equation.third == None:
                equation.third = 3
                self.output.setText(str(equation.third))
        def four():
            if equation.second == None:
                if equation.first != None:
                    equation.first = str(equation.first) + str(4)
                    self.output.setText(str(equation.first))
                    return
                if equation.first == None:
                    equation.first = 4
                    self.output.setText(str(equation.first))
                    return

            if equation.third != None:
                equation.third = str(equation.third) + str(4)
                self.output.setText(str(equation.third))
                return
            if equation.third == None:
                equation.third = 4
                self.output.setText(str(equation.third))
        def five():
            if equation.second == None:
                if equation.first != None:
                    equation.first = str(equation.first) + str(5)
                    self.output.setText(str(equation.first))
                    return
                if equation.first == None:
                    equation.first = 5
                    self.output.setText(str(equation.first))
                    return

            if equation.third != None:
                equation.third = str(equation.third) + str(5)
                self.output.setText(str(equation.third))
                return
            if equation.third == None:
                equation.third = 5
                self.output.setText(str(equation.third))
        def six():
            if equation.second == None:
                if equation.first != None:
                    equation.first = str(equation.first) + str(6)
                    self.output.setText(str(equation.first))
                    return
                if equation.first == None:
                    equation.first = 6
                    self.output.setText(str(equation.first))
                    return

            if equation.third != None:
                equation.third = str(equation.third) + str(6)
                self.output.setText(str(equation.third))
                return
            if equation.third == None:
                equation.third = 6
                self.output.setText(str(equation.third))
        def seven():
            if equation.second == None:
                if equation.first != None:
                    equation.first = str(equation.first) + str(7)
                    self.output.setText(str(equation.first))
                    return
                if equation.first == None:
                    equation.first = 7
                    self.output.setText(str(equation.first))
                    return

            if equation.third != None:
                equation.third = str(equation.third) + str(7)
                self.output.setText(str(equation.third))
                return
            if equation.third == None:
                equation.third = 7
                self.output.setText(str(equation.third))
        def eight():
            if equation.second == None:
                if equation.first != None:
                    equation.first = str(equation.first) + str(8)
                    self.output.setText(str(equation.first))
                    return
                if equation.first == None:
                    equation.first = 8
                    self.output.setText(str(equation.first))
                    return

            if equation.third != None:
                equation.third = str(equation.third) + str(8)
                self.output.setText(str(equation.third))
                return
            if equation.third == None:
                equation.third = 8
                self.output.setText(str(equation.third))
        def nine():
            if equation.second == None:
                if equation.first != None:
                    equation.first = str(equation.first) + str(9)
                    self.output.setText(str(equation.first))
                    return
                if equation.first == None:
                    equation.first = 9
                    self.output.setText(str(equation.first))
                    return

            if equation.third != None:
                equation.third = str(equation.third) + str(9)
                self.output.setText(str(equation.third))
                return
            if equation.third == None:
                equation.third = 9
                self.output.setText(str(equation.third))
        def add():
            self.output.setText("+")
            global equation
            equation.second = "+"
        def subtract():
            self.output.setText("-")
            equation.second = "-"
        def multiply():
            self.output.setText("x")
            equation.second = "x"
        def divide():
            self.output.setText("/")
            equation.second = "/"
        def equal():
            try:
                if equation.second == "+":
                    eq = int(equation.first) + int(equation.third)
                if equation.second == "-":
                    eq = int(equation.first) - int(equation.third)
                if equation.second == "x":
                    eq = int(equation.first) * int(equation.third)
                if equation.second == "/":
                    eq = int(equation.first) / int(equation.third)
                    print(float(eq))
            except:
                print("none are true")
            self.output.setText("= " + str(eq))
            equation.first = None
            equation.second = None
            equation.third = None
        def clear():
            equation.first = None
            equation.second = None
            equation.third = None
            self.output.setText("")

        self.zero.clicked.connect(zero)
        self.one.clicked.connect(one)
        self.two.clicked.connect(two)
        self.three.clicked.connect(three)
        self.four.clicked.connect(four)
        self.five.clicked.connect(five)
        self.six.clicked.connect(six)
        self.seven.clicked.connect(seven)
        self.eight.clicked.connect(eight)
        self.nine.clicked.connect(nine)
        self.add.clicked.connect(add)
        self.subtract.clicked.connect(subtract)
        self.multiply.clicked.connect(multiply)
        self.divide.clicked.connect(divide)
        self.equal.clicked.connect(equal)
        self.clear.clicked.connect(clear)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
