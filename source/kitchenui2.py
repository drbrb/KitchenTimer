# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui2.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import yaml
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(793, 191)
        with open('g:\\project\\exe\\config.yaml', 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        self.dict_cfg_v = cfg['buttons']
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tea_12 = QPushButton(self.centralwidget)
        self.tea_12.setObjectName(u"tea_12")
        self.tea_12.setGeometry(QRect(10, 20, 112, 34))
        font = QFont()
        font.setFamily(u"Arial")
        font.setBold(True)
        font.setWeight(75);
        self.tea_12.setFont(font)
        self.tea_15 = QPushButton(self.centralwidget)
        self.tea_15.setObjectName(u"tea_15")
        self.tea_15.setGeometry(QRect(130, 20, 112, 34))
        self.tea_15.setFont(font)
        self.makaron_8 = QPushButton(self.centralwidget)
        self.makaron_8.setObjectName(u"makaron_8")
        self.makaron_8.setGeometry(QRect(250, 20, 141, 34))
        self.makaron_8.setFont(font)
        self.duh_40 = QPushButton(self.centralwidget)
        self.duh_40.setObjectName(u"duh_40")
        self.duh_40.setGeometry(QRect(400, 20, 141, 34))
        self.duh_40.setFont(font)
        self.select_key = QPushButton(self.centralwidget)
        self.select_key.setObjectName(u"select_key")
        self.select_key.setGeometry(QRect(320, 100, 112, 34))
        self.select_key.setFont(font)
        self.select_text = QLineEdit(self.centralwidget)
        self.select_text.setObjectName(u"select_text")
        self.select_text.setGeometry(QRect(270, 110, 41, 25))
        self.select_text.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 110, 241, 21))
        self.label.setFont(font)
        self.egg_4 = QPushButton(self.centralwidget)
        self.egg_4.setObjectName(u"egg_4")
        self.egg_4.setGeometry(QRect(10, 60, 112, 34))
        self.egg_4.setFont(font)

        self.egg_3 = QPushButton(self.centralwidget)
        self.egg_3.setObjectName(u"egg_3")
        self.egg_3.setGeometry(QRect(130, 60, 112, 34))
        self.egg_3.setFont(font)

        self.reset_timer_1 = QPushButton(self.centralwidget)
        self.reset_timer_1.setObjectName(u"reset_timer_1")
        self.reset_timer_1.setGeometry(QRect(250, 60, 112, 34))
        self.reset_timer_1.setFont(font)

        self.timer_view_2 = QLabel(self.centralwidget)
        self.timer_view_2.setObjectName(u"timer_view_2")
        self.timer_view_2.setGeometry(QRect(680, 10, 111, 31))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75);
        self.timer_view_2.setFont(font1)
        self.timer_view_4 = QLabel(self.centralwidget)
        self.timer_view_4.setObjectName(u"timer_view_4")
        self.timer_view_4.setGeometry(QRect(680, 40, 111, 31))
        self.timer_view_4.setFont(font1)
        self.timer_view_6 = QLabel(self.centralwidget)
        self.timer_view_6.setObjectName(u"timer_view_6")
        self.timer_view_6.setGeometry(QRect(680, 70, 111, 31))
        self.timer_view_6.setFont(font1)
        self.timer_view_8 = QLabel(self.centralwidget)
        self.timer_view_8.setObjectName(u"timer_view_8")
        self.timer_view_8.setGeometry(QRect(680, 100, 111, 31))
        self.timer_view_8.setFont(font1)
        self.timer_view_5 = QLabel(self.centralwidget)
        self.timer_view_5.setObjectName(u"timer_view_5")
        self.timer_view_5.setGeometry(QRect(590, 70, 81, 31))
        self.timer_view_5.setFont(font1)
        self.timer_view_3 = QLabel(self.centralwidget)
        self.timer_view_3.setObjectName(u"timer_view_3")
        self.timer_view_3.setGeometry(QRect(590, 40, 81, 31))
        self.timer_view_3.setFont(font1)
        self.timer_view_7 = QLabel(self.centralwidget)
        self.timer_view_7.setObjectName(u"timer_view_7")
        self.timer_view_7.setGeometry(QRect(590, 100, 81, 31))
        self.timer_view_7.setFont(font1)
        self.timer_view_1 = QLabel(self.centralwidget)
        self.timer_view_1.setObjectName(u"timer_view_1")
        self.timer_view_1.setGeometry(QRect(590, 10, 81, 31))
        self.timer_view_1.setFont(font1)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(553, 20, 20, 131))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 793, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"KitchenTimer v.0.2", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.tea_12.setText(QCoreApplication.translate("MainWindow", f"{self.dict_cfg_v['but1_n'].encode('cp1251').decode('utf8')} {self.dict_cfg_v['but1_m']} \u043c\u0438\u043d", None))
        self.tea_15.setText(QCoreApplication.translate("MainWindow", f"{self.dict_cfg_v['but2_n'].encode('cp1251').decode('utf8')} {self.dict_cfg_v['but2_m']} \u043c\u0438\u043d", None))
        self.makaron_8.setText(QCoreApplication.translate("MainWindow",
                                                          f"{self.dict_cfg_v['but3_n'].encode('cp1251').decode('utf8')} {self.dict_cfg_v['but3_m']} \u043c\u0438\u043d",
                                                          None))
        self.duh_40.setText(QCoreApplication.translate("MainWindow",
                                                       f"{self.dict_cfg_v['but4_n'].encode('cp1251').decode('utf8')} {self.dict_cfg_v['but4_m']} \u043c\u0438\u043d",
                                                       None))
        self.select_key.setText(QCoreApplication.translate("MainWindow", f"{self.dict_cfg_v['but6_n'].encode('cp1251').decode('utf8')}", None))
        self.egg_4.setText(QCoreApplication.translate("MainWindow",
                                                      f"{self.dict_cfg_v['but5_n'].encode('cp1251').decode('utf8')} {self.dict_cfg_v['but5_m']} \u043c\u0438\u043d",
                                                      None))


        self.egg_3.setText(QCoreApplication.translate("MainWindow", f"{self.dict_cfg_v['but7_n'].encode('cp1251').decode('utf8')} {self.dict_cfg_v['but7_m']} \u043c\u0438\u043d", None))
        self.reset_timer_1.setText(QCoreApplication.translate("MainWindow", f"{self.dict_cfg_v['but8_n'].encode('cp1251').decode('utf8')} {self.dict_cfg_v['but8_m']} \u043c\u0438\u043d", None))

        # self.tea_12.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0439 12 \u043c\u0438\u043d", None))
        # self.tea_15.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0439 15 \u043c\u0438\u043d", None))
        # self.makaron_8.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0430\u0440\u043e\u043d\u044b 8 \u043c\u0438\u043d", None))
        # self.duh_40.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0443\u0445\u043e\u0432\u043a\u0430 40 \u043c\u0438\u043d", None))
        # self.select_key.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043c\u0438\u043d\u0443\u0442:", None))
        # self.egg_4.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0439\u0446\u043e \u0432\u0441\u043c\u044f\u0442\u043a\u0443 4 \u043c\u0438\u043d", None))
        self.timer_view_2.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.timer_view_4.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.timer_view_6.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.timer_view_8.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.timer_view_5.setText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u043a\u043b", None))
        self.timer_view_3.setText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u043a\u043b", None))
        self.timer_view_7.setText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u043a\u043b", None))
        self.timer_view_1.setText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u043a\u043b", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

