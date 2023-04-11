from PyQt5.QtCore import QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import QStyle, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QPushButton
from PyQt5.QtMultimediaWidgets import QVideoWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMouseTracking(True)
        MainWindow.setTabletTracking(True)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.videoWidget = QVideoWidget(self.centralwidget)
        self.videoWidget.setObjectName(u"videoWidget")
        self.videoWidget.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.videoWidget)

        self.controlWidget = QWidget(self.centralwidget)
        self.controlWidget.setObjectName(u"controlWidget")
        self.controlWidget.setMaximumSize(QSize(16777215, 89))
        self.controlWidget.setStyleSheet(u"*{\n"
"	/*background-color: rgb(0, 0, 0);*/\n"
"}\n"
"QLabel{\n"
"	color: rgb(171, 171, 171);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.controlWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.controlWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.lblelapsed = QLabel(self.widget)
        self.lblelapsed.setObjectName(u"lblelapsed")
        font = QFont()
        font.setFamily(u"Garamond")
        font.setPointSize(9)
        self.lblelapsed.setFont(font)
        self.lblelapsed.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.lblelapsed)

        self.positionSlider = QSlider(self.widget)
        self.positionSlider.setObjectName(u"positionSlider")
        self.positionSlider.setMaximumSize(QSize(16777215, 16777215))
        self.positionSlider.setMouseTracking(True)
        self.positionSlider.setTabletTracking(True)
        self.positionSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 1px;\n"
"    height: 2px;\n"
"    margin: 15px;\n"
"    background-color: rgb(171, 171, 171);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    /*background-color: rgb(55, 62, 76);*/\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background-color:rgb(0, 0, 0);\n"
"    border: 2px solid rgb(171, 171, 171);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: -9px ;\n"
"    border-radius: 9px;\n"
"    padding: 2px ;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"	background-color:rgb(171, 171, 171);\n"
"    border: 2px solid rgb(171, 171, 171) ;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: -9px ;\n"
"    border-radius: 9px;\n"
"    padding: 2px ;\n"
"}")
        self.positionSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.positionSlider)

        self.lblduration = QLabel(self.widget)
        self.lblduration.setObjectName(u"lblduration")
        self.lblduration.setFont(font)

        self.horizontalLayout.addWidget(self.lblduration)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.controlWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 16)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.btnOpen = QPushButton(self.widget_3)
        self.btnOpen.setObjectName(u"btnOpen")
        self.btnOpen.setMinimumSize(QSize(40, 35))
        self.btnOpen.setMaximumSize(QSize(40, 16777215))
        font1 = QFont()
        font1.setFamily(u"Wingdings 3")
        font1.setPointSize(30)
        self.btnOpen.setFont(font1)
        self.btnOpen.setStyleSheet(u"color: rgb(33, 33, 33);")
        self.btnOpen.setFlat(True)

        self.horizontalLayout_4.addWidget(self.btnOpen)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")

        self.horizontalLayout_4.addWidget(self.widget_6)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnb10s = QPushButton(self.widget_4)
        self.btnb10s.setObjectName(u"btnb10s")
        self.btnb10s.setMaximumSize(QSize(40, 35))
        self.btnb10s.setIconSize(QSize(30, 30))
        self.btnb10s.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnb10s)

        self.btnPlay = QPushButton(self.widget_4)
        self.btnPlay.setObjectName(u"btnPlay")
        self.btnPlay.setMaximumSize(QSize(48, 41))
        self.btnPlay.setStyleSheet(u"")
        self.btnPlay.setIconSize(QSize(40, 35))
        self.btnPlay.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnPlay)

        self.btnf10s = QPushButton(self.widget_4)
        self.btnf10s.setObjectName(u"btnf10s")
        self.btnf10s.setMaximumSize(QSize(40, 35))
        self.btnf10s.setIconSize(QSize(30, 30))
        self.btnf10s.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnf10s)


        self.horizontalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")

        self.horizontalLayout_2.addWidget(self.widget_5)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.controlWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblelapsed.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.lblduration.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.btnOpen.setText("")
        self.btnb10s.setText("")
        self.btnPlay.setText("")
        self.btnf10s.setText("")
    # retranslateUi

