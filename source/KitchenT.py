from PySide2 import QtWidgets
from PySide2.QtCore import QTime, QTimer
from datetime import datetime, timedelta
import kitchenui
import winsound

import sys


class KitchenTimer(QtWidgets.QMainWindow, kitchenui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tea_12.clicked.connect(lambda: self.Start_T('12'))
        self.tea_15.clicked.connect(lambda: self.Start_T('15'))
        self.makaron_8.clicked.connect(lambda: self.Start_T('8'))
        self.duh_40.clicked.connect(lambda: self.Start_T('40'))
        self.egg_4.clicked.connect(lambda: self.Start_T('4'))
        self.select_key.clicked.connect(lambda: self.Start_T(self.select_text.text()))

    def Start_T(self, time_min):
        global count
        count = 0
        ##self.start_timer()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.begin = datetime.strptime('00:%s:00' % time_min, '%H:%M:%S')


    def Stop_T(self):
        count = 1
        self.timer.stop()

    def Reset_T(self):
        self.timer_view.setText('00:00:00')
        self.timer.stop()

    def start_timer(self):
        self.timer()

    def showTime(self):
        if self.begin == datetime.strptime(str('00:00:00'), '%H:%M:%S'):
            self.timer.stop()
            winsound.PlaySound("g:\project\KitchenTimer\source\siren.wav", winsound.SND_FILENAME)
            return
        self.begin = self.begin - timedelta(seconds=1)
        self.timer_view.setText(str(self.begin).split()[1])


app = QtWidgets.QApplication([])
window = KitchenTimer()
window.show()
app.exec_()
