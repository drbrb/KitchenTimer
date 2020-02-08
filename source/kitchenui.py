# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
        MainWindow.resize(549, 217)
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
        self.egg_4.setGeometry(QRect(10, 60, 171, 34))
        self.egg_4.setFont(font)
        self.timer_view = QLabel(self.centralwidget)
        self.timer_view.setObjectName(u"timer_view")
        self.timer_view.setGeometry(QRect(60, 140, 121, 31))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75);
        self.timer_view.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 549, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"KitchenTimer v.0.1", None))
        self.tea_12.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0439 12 \u043c\u0438\u043d", None))
        self.tea_15.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0439 15 \u043c\u0438\u043d", None))
        self.makaron_8.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0430\u0440\u043e\u043d\u044b 8 \u043c\u0438\u043d", None))
        self.duh_40.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0443\u0445\u043e\u0432\u043a\u0430 40 \u043c\u0438\u043d", None))
        self.select_key.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043c\u0438\u043d\u0443\u0442:", None))
        self.egg_4.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0439\u0446\u043e \u0432\u0441\u043c\u044f\u0442\u043a\u0443 4 \u043c\u0438\u043d", None))
        self.timer_view.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
    # retranslateUi

