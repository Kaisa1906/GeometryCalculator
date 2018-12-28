import sys
import math
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont


class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle('Вычисление площади')
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 600, 500)

        self.btnhsquare = QPushButton('Высота и сторона', self)
        self.btnhsquare.resize(200, 50)
        self.btnhsquare.move(50, 100)
        self.btnhsquare.clicked.connect(self.hsquare)

        self.btnssquare = QPushButton('По трём сторонам', self)
        self.btnssquare.resize(200, 50)
        self.btnssquare.move(50, 150)
        self.btnssquare.clicked.connect(self.ssquare)

        self.btnasquare = QPushButton('Угол и прилежащие стороны', self)
        self.btnasquare.resize(200, 50)
        self.btnasquare.move(50, 200)
        self.btnasquare.clicked.connect(self.asquare)

        self.btnisquare = QPushButton('Радиус вписанной окружности', self)
        self.btnisquare.resize(200, 50)
        self.btnisquare.move(50, 250)
        self.btnisquare.clicked.connect(self.isquare)

        self.btncsquare = QPushButton('Радиус описанной окружности', self)
        self.btncsquare.resize(200, 50)
        self.btncsquare.move(50, 300)
        self.btncsquare.clicked.connect(self.csquare)

        self.title = QLabel(self)
        self.title.setText('Выберите вариант вычисления площади:')
        self.title.move(50, 50)
        self.title.setFont(QFont('TimesNewRoman', 15))

        self.h = QLabel(self)
        self.h.setFont(QFont('TimesNewRoman', 12))
        self.h.setText('Высотак стороне а:')
        self.h.move(300, 100)

        self.inputh = QLineEdit(self)
        self.inputh.move(450, 100)

        self.a = QLabel(self)
        self.a.setFont(QFont('TimesNewRoman', 12))
        self.a.setText('Сторона а:')
        self.a.move(300, 120)

        self.inputa = QLineEdit(self)
        self.inputa.move(450, 120)

        self.b = QLabel(self)
        self.b.setFont(QFont('TimesNewRoman', 12))
        self.b.setText('Сторона b:')
        self.b.move(300, 140)

        self.inputb = QLineEdit(self)
        self.inputb.move(450, 140)

        self.c = QLabel(self)
        self.c.setFont(QFont('TimesNewRoman', 12))
        self.c.setText('Сторона c:')
        self.c.move(300, 160)

        self.inputc = QLineEdit(self)
        self.inputc.move(450, 160)

        self.A = QLabel(self)
        self.A.setFont(QFont('TimesNewRoman', 12))
        self.A.setText('Угол А:')
        self.A.move(300, 180)

        self.inputA = QLineEdit(self)
        self.inputA.move(450, 180)

        self.B = QLabel(self)
        self.B.setFont(QFont('TimesNewRoman', 12))
        self.B.setText('Угол В:')
        self.B.move(300, 200)

        self.inputB = QLineEdit(self)
        self.inputB.move(450, 200)

        self.C = QLabel(self)
        self.C.setFont(QFont('TimesNewRoman', 12))
        self.C.setText('Угол С:')
        self.C.move(300, 220)

        self.inputC = QLineEdit(self)
        self.inputC.move(450, 220)

        self.r = QLabel(self)
        self.r.setFont(QFont('TimesNewRoman', 12))
        self.r.setText('Радиус вписанной окружности:')
        self.r.move(300, 240)

        self.inputr = QLineEdit(self)
        self.inputr.move(450, 265)

        self.R = QLabel(self)
        self.R.setFont(QFont('TimesNewRoman', 12))
        self.R.setText('Радиус описанной окружности:')
        self.R.move(300, 285)

        self.inputR = QLineEdit(self)
        self.inputR.move(450, 310)

        self.S = QLabel(self)
        self.S.setText('Площадь:')
        self.S.setFont(QFont('TimesNewRoman', 20))
        self.S.move(100, 425)

        self.error = QLabel(self)
        self.error.setFont(QFont('TimesNewRoman', 20))
        self.error.setText('Введены неверные данные')
        self.error.move(3000, 1000)

        self.LCD_count = QLCDNumber(self)
        self.LCD_count.move(300, 435)

    def hsquare(self):
        self.error.move(3000, 1000)
        try:
            h = float(self.inputh.text())
            a = float(self.inputa.text())
            self.LCD_count.display(0.5 * h * a)
        except Exception:
            self.error.move(150, 375)

    def ssquare(self):
        self.error.move(3000, 1000)
        try:
            a = float(self.inputa.text())
            b = float(self.inputb.text())
            c = float(self.inputc.text())
            p = (a + b + c) / 2
            self.LCD_count.display((p * (p - a) * (p - b) * (p - c)) ** 0.5)
        except Exception:
            self.error.move(150, 375)

    def asquare(self):
        self.error.move(3000, 1000)
        try:
            a = float(self.inputa.text())
            b = float(self.inputb.text())
            C = float(self.inputC.text())
            self.LCD_count.display(0.5 * math.sin(math.pi * C / 180) * a * b)
        except Exception:
            self.error.move(150, 375)

    def isquare(self):
        self.error.move(3000, 1000)
        try:
            a = float(self.inputa.text())
            b = float(self.inputb.text())
            c = float(self.inputc.text())
            p = (a + b + c) / 2
            r = float(self.inputr.text())
            self.LCD_count.display(r * p)
        except Exception:
            self.error.move(150, 375)

    def csquare(self):
        self.error.move(3000, 1000)
        try:
            a = float(self.inputa.text())
            b = float(self.inputb.text())
            c = float(self.inputc.text())
            R = float(self.inputR.text())
            self.LCD_count.display(a * b * c / (4 * R))
        except Exception:
            self.error.move(150, 375)


class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Вычисление стороны треугольника')
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 600, 350)

        self.title = QLabel(self)
        self.title.setText('Выберите способ вычисления стороны:')
        self.title.move(50, 50)
        self.title.setFont(QFont('TimesNewRoman', 15))

        self.h = QLabel(self)
        self.h.setFont(QFont('TimesNewRoman', 12))
        self.h.setText('Высота:')
        self.h.move(300, 100)

        self.inputh = QLineEdit(self)
        self.inputh.move(450, 100)

        self.a = QLabel(self)
        self.a.setFont(QFont('TimesNewRoman', 12))
        self.a.setText('Сторона а:')
        self.a.move(300, 120)

        self.inputa = QLineEdit(self)
        self.inputa.move(450, 120)

        self.b = QLabel(self)
        self.b.setFont(QFont('TimesNewRoman', 12))
        self.b.setText('Сторона b:')
        self.b.move(300, 140)

        self.inputb = QLineEdit(self)
        self.inputb.move(450, 140)

        self.A = QLabel(self)
        self.A.setFont(QFont('TimesNewRoman', 12))
        self.A.setText('Угол А:')
        self.A.move(300, 180)

        self.inputA = QLineEdit(self)
        self.inputA.move(450, 180)

        self.B = QLabel(self)
        self.B.setFont(QFont('TimesNewRoman', 12))
        self.B.setText('Угол В:')
        self.B.move(300, 200)

        self.inputB = QLineEdit(self)
        self.inputB.move(450, 200)

        self.C = QLabel(self)
        self.C.setFont(QFont('TimesNewRoman', 12))
        self.C.setText('Угол С')
        self.C.move(300, 220)

        self.inputC = QLineEdit(self)
        self.inputC.move(450, 220)

        self.S = QLabel(self)
        self.S.setFont(QFont('TimesNewRoman', 12))
        self.S.setText('Площадь:')
        self.S.move(300, 240)

        self.inputS = QLineEdit(self)
        self.inputS.move(450, 240)

        self.btnhs = QPushButton('Высота и площадь', self)
        self.btnhs.resize(200, 50)
        self.btnhs.move(50, 100)
        self.btnhs.clicked.connect(self.hs)

        self.btnCBb = QPushButton('Углы С, B  и сторона b', self)
        self.btnCBb.resize(200, 50)
        self.btnCBb.move(50, 150)
        self.btnCBb.clicked.connect(self.CBb)

        self.btnasquare = QPushButton('Угол С и прилежащие стороны', self)
        self.btnasquare.resize(200, 50)
        self.btnasquare.move(50, 200)
        self.btnasquare.clicked.connect(self.Cab)

        self.r = QLabel(self)
        self.r.setText('Сторона с:')
        self.r.setFont(QFont('TimesNewRoman', 15))
        self.r.move(100, 270)

        self.error = QLabel(self)
        self.error.setFont(QFont('TimesNewRoman', 20))
        self.error.setText('Введены неверные данные')
        self.error.move(3000, 1000)

        self.LCD_count = QLCDNumber(self)
        self.LCD_count.move(300, 280)

    def hs(self):
        self.error.move(3000, 1000)
        try:
            S = float(self.inputS.text())
            h = float(self.inputh.text())

            self.LCD_count.display(2 * S / h)
        except Exception:
            self.error.move(150, 300)

    def CBb(self):
        self.error.move(3000, 1000)
        try:
            C = float(self.inputC.text())
            B = float(self.inputB.text())
            b = float(self.inputb.text())

            self.LCD_count.display(b * math.sin(math.pi * C / 180) / math.sin(math.pi * B / 180))
        except Exception:
            self.error.move(150, 300)

    def Cab(self):
        self.error.move(3000, 1000)
        try:
            C = float(self.inputC.text())
            a = float(self.inputa.text())
            b = float(self.inputb.text())

            self.LCD_count.display((a * a + b * b - 2 * a * b * math.cos(math.pi * C / 180)) ** 0.5)
        except Exception:
            self.error.move(150, 300)


class Window3(QWidget):
    def __init__(self):
        super(Window3, self).__init__()
        self.setWindowTitle('Вычисление радиуса вписанной оружности')
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 600, 300)

        self.title = QLabel(self)
        self.title.setText('Вычислите радиус вписанной окружности:')
        self.title.move(50, 50)
        self.title.setFont(QFont('TimesNewRoman', 15))

        self.a = QLabel(self)
        self.a.setFont(QFont('TimesNewRoman', 12))
        self.a.setText('Сторона а:')
        self.a.move(50, 120)

        self.inputa = QLineEdit(self)
        self.inputa.move(200, 120)

        self.b = QLabel(self)
        self.b.setFont(QFont('TimesNewRoman', 12))
        self.b.setText('Сторона b:')
        self.b.move(50, 140)

        self.inputb = QLineEdit(self)
        self.inputb.move(200, 140)

        self.c = QLabel(self)
        self.c.setFont(QFont('TimesNewRoman', 12))
        self.c.setText('Сторона c:')
        self.c.move(50, 160)

        self.inputc = QLineEdit(self)
        self.inputc.move(200, 160)

        self.r = QLabel(self)
        self.r.setText('Радиус вписанной окружности:')
        self.r.setFont(QFont('TimesNewRoman', 15))
        self.r.move(100, 200)

        self.LCD_count = QLCDNumber(self)
        self.LCD_count.move(300, 235)

        self.btn1 = QPushButton('Вычислить', self)
        self.btn1.resize(100, 100)
        self.btn1.move(400, 95)
        self.btn1.clicked.connect(self.run)

        self.error = QLabel(self)
        self.error.setFont(QFont('TimesNewRoman', 20))
        self.error.setText('Введены неверные данные')
        self.error.move(3000, 1000)

    def run(self):
        self.error.move(3000, 1000)
        try:
            a = float(self.inputa.text())
            b = float(self.inputb.text())
            c = float(self.inputc.text())
            p = (a + b + c) / 2
            self.LCD_count.display((p * (p - a) * (p - b) * (p - c)) ** 0.5 / p)

        except Exception:
            self.error.move(120, 260)


class Window4(QWidget):
    def __init__(self):
        super(Window4, self).__init__()
        self.setWindowTitle('Вычисление радиуса описанной оружности')
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 600, 300)

        self.title = QLabel(self)
        self.title.setText('Вычислите радиус описанной окружности:')
        self.title.move(50, 50)
        self.title.setFont(QFont('TimesNewRoman', 15))

        self.a = QLabel(self)
        self.a.setFont(QFont('TimesNewRoman', 12))
        self.a.setText('Сторона а:')
        self.a.move(50, 120)

        self.inputa = QLineEdit(self)
        self.inputa.move(200, 120)

        self.b = QLabel(self)
        self.b.setFont(QFont('TimesNewRoman', 12))
        self.b.setText('Сторона b:')
        self.b.move(50, 140)

        self.inputb = QLineEdit(self)
        self.inputb.move(200, 140)

        self.c = QLabel(self)
        self.c.setFont(QFont('TimesNewRoman', 12))
        self.c.setText('Сторона c:')
        self.c.move(50, 160)

        self.inputc = QLineEdit(self)
        self.inputc.move(200, 160)

        self.R = QLabel(self)
        self.R.setText('Радиус описанной окружности:')
        self.R.setFont(QFont('TimesNewRoman', 15))
        self.R.move(100, 200)

        self.LCD_count = QLCDNumber(self)
        self.LCD_count.move(300, 235)

        self.btn1 = QPushButton('Вычислить', self)
        self.btn1.resize(100, 100)
        self.btn1.move(400, 95)
        self.btn1.clicked.connect(self.run)

        self.error = QLabel(self)
        self.error.setFont(QFont('TimesNewRoman', 20))
        self.error.setText('Введены неверные данные')
        self.error.move(3000, 1000)

    def run(self):
        self.error.move(3000, 1000)
        try:
            a = float(self.inputa.text())
            b = float(self.inputb.text())
            c = float(self.inputc.text())
            p = (a + b + c) / 2

            self.LCD_count.display(a * b * c / (4 * (p * (p - a) * (p - b) * (p - c)) ** 0.5))
        except Exception:
            self.error.move(120, 260)


class Window5(QWidget):
    def __init__(self):
        super(Window5, self).__init__()
        self.setWindowTitle('Вычисление высоты треугольника')
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 600, 300)

        self.title = QLabel(self)
        self.title.setText('Выберите способ вычисления высоты:')
        self.title.move(50, 50)
        self.title.setFont(QFont('TimesNewRoman', 15))

        self.a = QLabel(self)
        self.a.setFont(QFont('TimesNewRoman', 12))
        self.a.setText('Сторона а:')
        self.a.move(50, 100)

        self.inputa = QLineEdit(self)
        self.inputa.move(200, 100)

        self.b = QLabel(self)
        self.b.setFont(QFont('TimesNewRoman', 12))
        self.b.setText('Сторона b:')
        self.b.move(50, 120)

        self.inputb = QLineEdit(self)
        self.inputb.move(200, 120)

        self.c = QLabel(self)
        self.c.setFont(QFont('TimesNewRoman', 12))
        self.c.setText('Сторона c:')
        self.c.move(50, 140)

        self.inputc = QLineEdit(self)
        self.inputc.move(200, 140)

        self.B = QLabel(self)
        self.B.setFont(QFont('TimesNewRoman', 12))
        self.B.setText('Угол В:')
        self.B.move(50, 160)

        self.inputB = QLineEdit(self)
        self.inputB.move(200, 160)

        self.r = QLabel(self)
        self.r.setText('Высота к стороне а:')
        self.r.setFont(QFont('TimesNewRoman', 15))
        self.r.move(100, 200)

        self.LCD_count = QLCDNumber(self)
        self.LCD_count.move(300, 235)

        self.btn1 = QPushButton('По трём сторонам', self)
        self.btn1.resize(200, 40)
        self.btn1.move(350, 100)
        self.btn1.clicked.connect(self.sides)

        self.btn1 = QPushButton('По стороне и углу', self)
        self.btn1.resize(200, 40)
        self.btn1.move(350, 150)
        self.btn1.clicked.connect(self.angleside)

        self.error = QLabel(self)
        self.error.setFont(QFont('TimesNewRoman', 20))
        self.error.setText('Введены неверные данные')
        self.error.move(3000, 1000)

    def sides(self):
        self.error.move(3000, 1000)
        try:
            a = float(self.inputa.text())
            b = float(self.inputb.text())
            c = float(self.inputc.text())
            p = (a + b + c) / 2

            self.LCD_count.display(2 * (p * (p - a) * (p - b) * (p - c)) ** 0.5 / a)
        except Exception:
            self.error.move(120, 260)

    def angleside(self):
        self.error.move(3000, 1000)
        try:
            b = float(self.inputb.text())
            B = float(self.inputB.text())

            self.LCD_count.display(b * math.sin(math.pi * B / 180))
        except Exception:
            self.error.move(120, 260)


class Window6(QWidget):
    def __init__(self):
        super(Window6, self).__init__()
        self.setWindowTitle('Вычисление длины биссектрисы')
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 600, 300)

        self.title = QLabel(self)
        self.title.setText('Выберите способ вычисления биссектрисы:')
        self.title.move(50, 50)
        self.title.setFont(QFont('TimesNewRoman', 15))

        self.a = QLabel(self)
        self.a.setFont(QFont('TimesNewRoman', 12))
        self.a.setText('Сторона а:')
        self.a.move(50, 100)

        self.inputa = QLineEdit(self)
        self.inputa.move(200, 100)

        self.b = QLabel(self)
        self.b.setFont(QFont('TimesNewRoman', 12))
        self.b.setText('Сторона b:')
        self.b.move(50, 120)

        self.inputb = QLineEdit(self)
        self.inputb.move(200, 120)

        self.c = QLabel(self)
        self.c.setFont(QFont('TimesNewRoman', 12))
        self.c.setText('Сторона c:')
        self.c.move(50, 140)

        self.inputc = QLineEdit(self)
        self.inputc.move(200, 140)

        self.C = QLabel(self)
        self.C.setFont(QFont('TimesNewRoman', 12))
        self.C.setText('Угол C:')
        self.C.move(50, 160)

        self.inputC = QLineEdit(self)
        self.inputC.move(200, 160)

        self.r = QLabel(self)
        self.r.setText('Биссекриса к стороне с:')
        self.r.setFont(QFont('TimesNewRoman', 15))
        self.r.move(100, 200)

        self.LCD_count = QLCDNumber(self)
        self.LCD_count.move(300, 235)

        self.btn1 = QPushButton('По трём сторонам', self)
        self.btn1.resize(200, 40)
        self.btn1.move(350, 100)
        self.btn1.clicked.connect(self.sides)

        self.btn1 = QPushButton('По двум сторонам и углу', self)
        self.btn1.resize(200, 40)
        self.btn1.move(350, 150)
        self.btn1.clicked.connect(self.angleside)

        self.error = QLabel(self)
        self.error.setFont(QFont('TimesNewRoman', 20))
        self.error.setText('Введены неверные данные')
        self.error.move(3000, 1000)

    def sides(self):
        self.error.move(3000, 1000)
        try:
            a = float(self.inputa.text())
            b = float(self.inputb.text())
            c = float(self.inputc.text())

            self.LCD_count.display((a * b * (a + b + c) * (a + b - c)) ** 0.5 / (a + b))
        except Exception:
            self.error.move(120, 260)

    def angleside(self):
        self.error.move(3000, 1000)
        try:
            a = float(self.inputa.text())
            b = float(self.inputb.text())
            C = float(self.inputC.text())

            self.LCD_count.display(a * b * math.cos(math.pi * (С / 2) / 180) / (a + b))
        except Exception:
            self.error.move(120, 260)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('project.ui', self)
        self.pushButton_1.clicked.connect(self.square)
        self.pushButton_3.clicked.connect(self.findside)
        self.pushButton_5.clicked.connect(self.inscribedradius)
        self.pushButton_6.clicked.connect(self.circumscribedradius)
        self.pushButton_7.clicked.connect(self.findaltitude)
        self.pushButton_8.clicked.connect(self.findbisector)

    def square(self):
        self.w1 = Window1()
        self.w1.show()

    def findside(self):
        self.w2 = Window2()
        self.w2.show()

    def circumscribedradius(self):
        self.w3 = Window3()
        self.w3.show()

    def inscribedradius(self):
        self.w4 = Window4()
        self.w4.show()

    def findaltitude(self):
        self.w5 = Window5()
        self.w5.show()

    def findbisector(self):
        self.w6 = Window6()
        self.w6.show()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())