
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from PyQt5.QtMultimediaWidgets import QVideoWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 672)
        MainWindow.setStyleSheet(u"\n"
"QPushButton{\n"
"	qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0))\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1050, 670))
        self.centralwidget.setStyleSheet(u"*{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Menu = QWidget()
        self.Menu.setObjectName(u"Menu")
        self.verticalLayout_3 = QVBoxLayout(self.Menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.Menu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 90))
        self.widget.setStyleSheet(u"background-color:rgb(3, 37, 65);")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnHumburger = QPushButton(self.widget_5)
        self.btnHumburger.setObjectName(u"btnHumburger")
        self.btnHumburger.setMaximumSize(QSize(43, 16777215))
        font = QFont()
        font.setFamily(u"Gill Sans Ultra Bold Condensed")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnHumburger.setFont(font)
        self.btnHumburger.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	border:0px solid ;\n"
"	color :qlineargradient(spread:pad, x1:0.222, y1:0.478045, x2:0.966, y2:0.461, stop:0.119318 rgba(47, 100, 133, 255), stop:1 rgba(78, 136, 243, 234));\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"	color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"img/Hamburger_icon.svg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnHumburger.setIcon(icon)
        self.btnHumburger.setIconSize(QSize(26, 40))

        self.horizontalLayout_3.addWidget(self.btnHumburger)

        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(160, 16777215))
        self.label.setStyleSheet(u"font: 35pt \"Aquire Light\";\n"
"background-color:rgb(3, 37, 65);\n"
"color: qlineargradient(spread:pad, x1:0.222, y1:0.478045, x2:0.966, y2:0.461, stop:0.119318 rgba(47, 100, 133, 255), stop:1 rgba(78, 136, 243, 234));")
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label.setWordWrap(False)

        self.horizontalLayout_3.addWidget(self.label)

        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")

        self.horizontalLayout_3.addWidget(self.widget_6)


        self.horizontalLayout_2.addWidget(self.widget_5)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")

        self.horizontalLayout_2.addWidget(self.widget_4)


        self.verticalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(self.Menu)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slideMenu = QWidget(self.widget_2)
        self.slideMenu.setObjectName(u"slideMenu")
        self.slideMenu.setMinimumSize(QSize(200, 0))
        self.slideMenu.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(3, 37, 65);\n"
"	font: 15pt \"Gill Sans Ultra Bold Condensed\";\n"
"	\n"
"}\n"
"\n"
"QPushButton{\n"
"	border:0px solid ;\n"
"	color :qlineargradient(spread:pad, x1:0.222, y1:0.478045, x2:0.966, y2:0.461, stop:0.119318 rgba(47, 100, 133, 255), stop:1 rgba(78, 136, 243, 234));\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"	border:2px solid rgb(132, 132, 132);\n"
"	border-color:rgb(3, 37, 65) rgb(3, 37, 65) rgb(3, 37, 65) qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"	color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border:2px solid rgb(132, 132, 132);\n"
"	border-color:rgb(3, 37, 65) rgb(3, 37, 65) rgb(3, 37, 65) qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 20"
                        "0));\n"
"	color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border:2px solid rgb(132, 132, 132);\n"
"	border-color:rgb(3, 37, 65) rgb(3, 37, 65) rgb(3, 37, 65) qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"	color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.slideMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 0, 20, 0)
        self.widget_7 = QWidget(self.slideMenu)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 66))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnBack = QPushButton(self.widget_7)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setMaximumSize(QSize(50, 16777215))
        self.btnBack.setFont(font)
        self.btnBack.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	border:0px solid ;\n"
"	color :qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"	color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"img/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnBack.setIcon(icon1)
        self.btnBack.setIconSize(QSize(35, 50))

        self.horizontalLayout_5.addWidget(self.btnBack, 0, Qt.AlignLeft)

        self.btnHumburger_2 = QPushButton(self.widget_7)
        self.btnHumburger_2.setObjectName(u"btnHumburger_2")
        self.btnHumburger_2.setMaximumSize(QSize(50, 16777215))
        self.btnHumburger_2.setFont(font)
        self.btnHumburger_2.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	border:0px solid ;\n"
"	color :qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"	color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"img/Hamburger_icon.svg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnHumburger_2.setIcon(icon2)
        self.btnHumburger_2.setIconSize(QSize(35, 50))

        self.horizontalLayout_5.addWidget(self.btnHumburger_2, 0, Qt.AlignLeft)

        self.btnHome = QPushButton(self.widget_7)
        self.btnHome.setObjectName(u"btnHome")
        self.btnHome.setMaximumSize(QSize(50, 16777215))
        self.btnHome.setFont(font)
        self.btnHome.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	border:0px solid ;\n"
"	color :qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"	color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: qlineargradient(spread:pad, x1:0.904, y1:0.908682, x2:0.466, y2:0.153, stop:0 rgba(0, 104, 255, 255), stop:0.897727 rgba(23, 115, 155, 200));\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"/img/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnHome.setIcon(icon3)
        self.btnHome.setIconSize(QSize(35, 50))

        self.horizontalLayout_5.addWidget(self.btnHome, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.widget_7)

        self.btnMovies = QPushButton(self.slideMenu)
        self.btnMovies.setObjectName(u"btnMovies")
        self.btnMovies.setMinimumSize(QSize(0, 0))
        self.btnMovies.setMaximumSize(QSize(16777215, 50))
        self.btnMovies.setFont(font)

        self.verticalLayout_2.addWidget(self.btnMovies)

        self.btnTv_Shows = QPushButton(self.slideMenu)
        self.btnTv_Shows.setObjectName(u"btnTv_Shows")
        self.btnTv_Shows.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_2.addWidget(self.btnTv_Shows)

        self.btnMusic = QPushButton(self.slideMenu)
        self.btnMusic.setObjectName(u"btnMusic")
        self.btnMusic.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_2.addWidget(self.btnMusic)

        self.widget_8 = QWidget(self.slideMenu)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(16777215, 98))

        self.verticalLayout_2.addWidget(self.widget_8)

        self.btnIMDb = QPushButton(self.slideMenu)
        self.btnIMDb.setObjectName(u"btnIMDb")

        self.verticalLayout_2.addWidget(self.btnIMDb)

        self.btnTMDb = QPushButton(self.slideMenu)
        self.btnTMDb.setObjectName(u"btnTMDb")
        self.btnTMDb.setIconSize(QSize(114, 67))

        self.verticalLayout_2.addWidget(self.btnTMDb)


        self.horizontalLayout.addWidget(self.slideMenu)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"QWidget #widget_3{\n"
"	\n"
"	background-color: rgb(16, 15, 15);\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.listView = QListView(self.widget_3)
        self.listView.setObjectName(u"listView")
        self.listView.setMaximumSize(QSize(16777215, 600))
        self.listView.setStyleSheet(u"QListView{\n"
"	background-color: rgb(16, 16, 16);\n"
"	font: 87 9pt \"Arial Black\";\n"
"	color:rgb(211, 211, 211);\n"
"}\n"
"\n"
"       ")
        self.listView.setFrameShape(QFrame.NoFrame)
        self.listView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.listView.setTabKeyNavigation(True)
        self.listView.setDragEnabled(True)
        self.listView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listView.setIconSize(QSize(200, 380))
        self.listView.setTextElideMode(Qt.ElideMiddle)
        self.listView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listView.setMovement(QListView.Static)
        self.listView.setFlow(QListView.LeftToRight)
        self.listView.setProperty("isWrapping", True)
        self.listView.setResizeMode(QListView.Adjust)
        self.listView.setSpacing(5)
        self.listView.setViewMode(QListView.IconMode)
        self.listView.setModelColumn(0)
        self.listView.setUniformItemSizes(True)
        self.listView.setWordWrap(True)
        self.listView.setItemAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.listView)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.Menu)
        self.Millisec = QWidget()
        self.Millisec.setObjectName(u"Millisec")
        self.verticalLayout_5 = QVBoxLayout(self.Millisec)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.videoWidget = QVideoWidget(self.Millisec)
        self.videoWidget.setObjectName(u"videoWidget")
        self.videoWidget.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.videoWidget)

        self.controlWidget = QWidget(self.Millisec)
        self.controlWidget.setObjectName(u"controlWidget")
        self.controlWidget.setMaximumSize(QSize(16777215, 89))
        self.controlWidget.setStyleSheet(u"\n"
"QLabel{\n"
"	color: rgb(171, 171, 171);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.controlWidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.controlWidget)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.lblelapsed = QLabel(self.widget_9)
        self.lblelapsed.setObjectName(u"lblelapsed")
        font1 = QFont()
        font1.setFamily(u"Garamond")
        font1.setPointSize(9)
        self.lblelapsed.setFont(font1)
        self.lblelapsed.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.lblelapsed)

        self.positionSlider = QSlider(self.widget_9)
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

        self.horizontalLayout_6.addWidget(self.positionSlider)

        self.lblduration = QLabel(self.widget_9)
        self.lblduration.setObjectName(u"lblduration")
        self.lblduration.setFont(font1)

        self.horizontalLayout_6.addWidget(self.lblduration)


        self.verticalLayout_4.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.controlWidget)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 16)
        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, 0, 0)
        self.btnOpen = QPushButton(self.widget_11)
        self.btnOpen.setObjectName(u"btnOpen")
        self.btnOpen.setMinimumSize(QSize(40, 35))
        self.btnOpen.setMaximumSize(QSize(40, 16777215))
        font2 = QFont()
        font2.setFamily(u"Wingdings 3")
        font2.setPointSize(30)
        self.btnOpen.setFont(font2)
        self.btnOpen.setStyleSheet(u"color: rgb(33, 33, 33);")
        self.btnOpen.setFlat(True)

        self.horizontalLayout_8.addWidget(self.btnOpen)

        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")

        self.horizontalLayout_8.addWidget(self.widget_12)


        self.horizontalLayout_7.addWidget(self.widget_11)

        self.widget_13 = QWidget(self.widget_10)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btnb10s = QPushButton(self.widget_13)
        self.btnb10s.setObjectName(u"btnb10s")
        self.btnb10s.setMaximumSize(QSize(40, 35))
        self.btnb10s.setIconSize(QSize(30, 30))
        self.btnb10s.setFlat(True)

        self.horizontalLayout_9.addWidget(self.btnb10s)

        self.btnPlay = QPushButton(self.widget_13)
        self.btnPlay.setObjectName(u"btnPlay")
        self.btnPlay.setMaximumSize(QSize(48, 41))
        self.btnPlay.setStyleSheet(u"")
        self.btnPlay.setIconSize(QSize(40, 35))
        self.btnPlay.setFlat(True)

        self.horizontalLayout_9.addWidget(self.btnPlay)

        self.btnf10s = QPushButton(self.widget_13)
        self.btnf10s.setObjectName(u"btnf10s")
        self.btnf10s.setMaximumSize(QSize(40, 35))
        self.btnf10s.setIconSize(QSize(30, 30))
        self.btnf10s.setFlat(True)

        self.horizontalLayout_9.addWidget(self.btnf10s)


        self.horizontalLayout_7.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.widget_10)
        self.widget_14.setObjectName(u"widget_14")

        self.horizontalLayout_7.addWidget(self.widget_14)


        self.verticalLayout_4.addWidget(self.widget_10)


        self.verticalLayout_5.addWidget(self.controlWidget)

        self.stackedWidget.addWidget(self.Millisec)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnHumburger.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"VMDB", None))
        self.btnBack.setText("")
        self.btnHumburger_2.setText("")
        self.btnHome.setText("")
#if QT_CONFIG(tooltip)
        self.btnMovies.setToolTip(QCoreApplication.translate("MainWindow", u"Movies", None))
#endif // QT_CONFIG(tooltip)
        self.btnMovies.setText(QCoreApplication.translate("MainWindow", u"Movies", None))
#if QT_CONFIG(tooltip)
        self.btnTv_Shows.setToolTip(QCoreApplication.translate("MainWindow", u"Tv Shows", None))
#endif // QT_CONFIG(tooltip)
        self.btnTv_Shows.setText(QCoreApplication.translate("MainWindow", u"TV Shows", None))
#if QT_CONFIG(tooltip)
        self.btnMusic.setToolTip(QCoreApplication.translate("MainWindow", u"Music", None))
#endif // QT_CONFIG(tooltip)
        self.btnMusic.setText(QCoreApplication.translate("MainWindow", u"Music", None))
#if QT_CONFIG(tooltip)
        self.btnIMDb.setToolTip(QCoreApplication.translate("MainWindow", u"IMDb Movie Explorer", None))
#endif // QT_CONFIG(tooltip)
        self.btnIMDb.setText(QCoreApplication.translate("MainWindow", u"IMDb", None))
#if QT_CONFIG(tooltip)
        self.btnTMDb.setToolTip(QCoreApplication.translate("MainWindow", u"TMDb Movie Explorer", None))
#endif // QT_CONFIG(tooltip)
        self.btnTMDb.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.lblelapsed.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.lblduration.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.btnOpen.setText("")
        self.btnb10s.setText("")
        self.btnPlay.setText("")
        self.btnf10s.setText("")
    # retranslateUi

