###
#版本号 V1.0.0.0
###

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt, QPoint, QDateTime

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #设置窗口无标题栏
        self.setWindowFlag(Qt.FramelessWindowHint)
        #设置窗口透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        #设置窗口置顶
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.setGeometry(1000, 100, 300, 150)
        self.setWindowTitle('Desktop Clock')

        self.timeLabel = QLabel(self)
        self.timeLabel.setAlignment(Qt.AlignCenter)
        self.timeLabel.setStyleSheet("font-size: 30px; font-weight: bold; color:red;")

        layout = QVBoxLayout()
        layout.addWidget(self.timeLabel)

        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.updateTime)
        timer.start(1000)  # 更新时间间隔为1秒

        self.show()

    def updateTime(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString('hh:mm:ss\n')
        self.timeLabel.setText(displayText)
        currentDate = QDateTime.currentDateTime()
        displayTextdate = currentDate.toString('yyyy-MM-dd')
        self.timeLabel.setText(displayText + displayTextdate)

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if hasattr(self, 'offset'):
            x = event.globalX()
            y = event.globalY()
            x_w = self.offset.x()
            y_w = self.offset.y()
            self.move(x - x_w, y - y_w)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    sys.exit(app.exec_())
