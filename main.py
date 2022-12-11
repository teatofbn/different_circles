from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from random import randint


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 370, 100)
        self.setWindowTitle('Кружочки')

        self.btn = QPushButton
        self.btn = QPushButton('Создать', self)
        self.btn.setFixedSize(80, 80)
        self.btn.move(200, 10)
        self.btn.clicked.connect(self.circle)

        self.label = QLabel()
        canvas = QPixmap(400, 400)
        self.label.setPixmap(canvas)

        layout = QGridLayout(self)
        layout.addWidget(self.btn, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, 1, 0)

    def circle(self):
        x, y = [randint(10, 350) for i in range(2)]
        h = randint(10, 200)
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(*[randint(0, 255) for _ in range(3)]))
        painter.setPen(pen)
        painter.drawEllipse(x, y, h, h)
        painter.end()
        self.update()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())