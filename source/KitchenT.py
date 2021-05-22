from PySide2 import QtWidgets
from PySide2.QtCore import QTime, QTimer
from datetime import datetime, timedelta
import kitchenui2
import winsound
import yaml
import sys


class KitchenTimer(QtWidgets.QMainWindow, kitchenui2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        with open('g:\\project\\exe\\config.yaml', 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        self.dict_cfg = cfg['buttons']
        self.timer = None
        # self.but1_name = 'чай'
        # self.but1_min = '15'
        self.tea_12.clicked.connect(lambda: self.Start_T(self.dict_cfg['but1_m'], self.dict_cfg['but1_n']))
        self.tea_15.clicked.connect(lambda: self.Start_T(self.dict_cfg['but2_m'], self.dict_cfg['but2_n']))
        self.makaron_8.clicked.connect(lambda: self.Start_T(self.dict_cfg['but3_m'], self.dict_cfg['but3_n']))
        self.duh_40.clicked.connect(lambda: self.Start_T(self.dict_cfg['but4_m'], self.dict_cfg['but4_n']))
        self.egg_4.clicked.connect(lambda: self.Start_T(self.dict_cfg['but5_m'], self.dict_cfg['but5_n']))
        # self.tea_12.clicked.connect(lambda: self.Start_T('12', 'чай'))
        # self.tea_15.clicked.connect(lambda: self.Start_T('15', 'чай'))
        # self.makaron_8.clicked.connect(lambda: self.Start_T('8', 'макароны'))
        # self.duh_40.clicked.connect(lambda: self.Start_T('40', 'духовка'))
        # self.egg_4.clicked.connect(lambda: self.Start_T('4', 'яйцо'))
        self.select_key.clicked.connect(lambda: self.Start_T(self.select_text.text(), 'выбор'))
        self.show_timerview = {"tv1": "0", "tv2": "0", "tv3": "0", "tv4": "0"}

    def Start_T(self, time_min, text_view):
        global count
        count = 0
        self.Reset_T()
        ##self.start_timer()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.begin = datetime.strptime('00:%s:00' % time_min, '%H:%M:%S')

    def Stop_T(self):
        count = 1
        self.timer.stop()

    def Reset_T(self):
        self.timer_view_2.setText('00:00:00')
        if self.timer:
            self.timer.stop()

    def start_timer(self):
        self.timer()

    def showTime(self):
        if self.begin == datetime.strptime(str('00:00:00'), '%H:%M:%S'):
            self.timer.stop()
            winsound.PlaySound("g:\project\KitchenTimer\source\siren.wav", winsound.SND_FILENAME)
            return
        self.begin = self.begin - timedelta(seconds=1)
        self.timer_view_2.setText(str(self.begin).split()[1])


app = QtWidgets.QApplication([])
window = KitchenTimer()
window.show()
app.exec_()
