# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QMainWindow, QSizePolicy, QWidget)

class Ui_WeatherTracker(object):
    def setupUi(self, WeatherTracker):
        if not WeatherTracker.objectName():
            WeatherTracker.setObjectName(u"WeatherTracker")
        WeatherTracker.setWindowModality(Qt.WindowModality.NonModal)
        WeatherTracker.resize(755, 599)
        WeatherTracker.setStyleSheet(u"QMainWindow {\n"
"    border-radius: 15px;\n"
"    background-color: #ffffff;\n"
"}")
        self.centralwidget = QWidget(WeatherTracker)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    border-radius: 15px;\n"
"    background-color: #737feb;\n"
"}")
        self.gridFrame = QFrame(self.centralwidget)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setGeometry(QRect(10, 50, 341, 551))
        self.Temp = QLabel(self.gridFrame)
        self.Temp.setObjectName(u"Temp")
        self.Temp.setGeometry(QRect(90, 340, 211, 171))
        self.Temp.setStyleSheet(u"QLabel {\n"
"	border-radius: 15px;\n"
"	background-color: #98a1f5;\n"
"	font-size: 140px;\n"
"\n"
"	text-align: left;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"	color: white;\n"
"}")
        self.iconWeather = QLabel(self.gridFrame)
        self.iconWeather.setObjectName(u"iconWeather")
        self.iconWeather.setGeometry(QRect(40, 10, 281, 281))
        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setGeometry(QRect(0, 10, 751, 41))
        self.CityBox = QComboBox(self.verticalFrame)
        self.CityBox.setObjectName(u"CityBox")
        self.CityBox.setGeometry(QRect(300, 0, 154, 41))
        self.CityBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #98a1f5;\n"
"    border: 1px solid #4a5568;\n"
"    border-radius: 6px;\n"
"    padding: 8px 15px;\n"
"    color: #0c0c0d;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 0px solid #0c0c0d;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    border-top: 4px solid #0c0c0d;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #white;\n"
"    border: 1px solid #4a5568;\n"
"	border-radius: 6px;\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    background-color: #3d4163;\n"
"	border: 0px;\n"
"    border-radius: 6px;\n"
"	color: white;\n"
"}")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(380, 60, 361, 541))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.otherStat = QLabel(self.frame)
        self.otherStat.setObjectName(u"otherStat")
        self.otherStat.setGeometry(QRect(20, 0, 331, 461))
        self.otherStat.setStyleSheet(u"QLabel {\n"
"	border-radius: 15px;\n"
"	background-color: #98a1f5;\n"
"	border: 1px solid #020203;\n"
"	font-size: 20px;\n"
"	color: #25252b;\n"
"		\n"
"	font-weight: bold;\n"
"	font-style: italic;\n"
"\n"
"	qproperty-alignment: 'AlignLeft';\n"
"    padding: 5px 10px;                   \n"
"    margin: 2px;\n"
"}")
        WeatherTracker.setCentralWidget(self.centralwidget)

        self.retranslateUi(WeatherTracker)

        QMetaObject.connectSlotsByName(WeatherTracker)
    # setupUi

    def retranslateUi(self, WeatherTracker):
        WeatherTracker.setWindowTitle(QCoreApplication.translate("WeatherTracker", u"MainWindow", None))
        self.Temp.setText("")
        self.iconWeather.setText("")
        self.otherStat.setText(QCoreApplication.translate("WeatherTracker", u"Text", None))
    # retranslateUi

