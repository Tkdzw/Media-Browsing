import sys, os
import platform
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import QDir, Qt, QUrl, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyle, QStackedWidget, QMenu, QShortcut, QFileDialog, QAction 
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtGui import QIcon, QKeySequence, QPixmap
from pathlib import Path

from UI.Ui_cube import Ui_MainWindow


class Cube(QMainWindow):
	"""docstring for Cube"""
	def __init__(self):
		super(Cube, self).__init__()
		icon = QIcon()
		icon.addPixmap(QPixmap("img/cube.svg"), QIcon.Selected,QIcon.On)
		self.setWindowIcon(icon)

		
	def positionChanged(self, position):
		self.ui.positionSlider.setValue(position)
		millis = position
		millis = int(millis)
		seconds=(millis/1000)%60
		seconds = int(seconds)
		minutes=(millis/(1000*60))%60
		minutes = int(minutes)
		hours=(millis/(1000*60*60))%24	
		self.ui.lblelapsed.setText(str(str("%d:%d:%d" % (hours, minutes, seconds))))

	def mediaStateChanged(self, state):
		if self.ui.mediaPlayer.state() == QMediaPlayer.PlayingState:
			self.ui.btnPlay.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
		else:
			self.ui.btnPlay.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

	def durationChanged(self, duration):
		self.ui.positionSlider.setRange(0, duration)
		millis = duration
		millis = int(millis)
		seconds=(millis/1000)%60
		seconds = int(seconds)
		minutes=(millis/(1000*60))%60
		minutes = int(minutes)
		hours=(millis/(1000*60*60))%24

		self.ui.lblduration.setText(str("%d:%d:%d" % (hours, minutes, seconds)))

	def mediaStateChanged(self, state):
		if self.ui.mediaPlayer.state() == QMediaPlayer.PlayingState:
			self.ui.btnPlay.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
		else:
			self.ui.btnPlay.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

	def play(self):
		print("Class Call")
		if self.ui.mediaPlayer.state() == QMediaPlayer.PlayingState:
			self.ui.mediaPlayer.pause()
		else:
			self.ui.mediaPlayer.play()

	def Foward10(self):
		now = self.ui.positionSlider.value()
		seek = now + 10000
		self.ui.mediaPlayer.setPosition(seek)
	

	def Backward10(self):
		now = self.ui.positionSlider.value()
		seek = now - 10000
		self.ui.mediaPlayer.setPosition(seek)


def openFile(self, fileName):

	if fileName != '':
		self.ui.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
		self.ui.btnPlay.setEnabled(True)
		#self.ui.style().standardIcon(QStyle.SP_MediaPlay)
		self.ui.mediaPlayer.play()
		self.setWindowTitle("Millisec : " + Path(fileName).stem)

#Controls Widget timer Start#
		#self.timer = QTimer()
		#self.timer.timeout.connect(self.hideW)



#Keyboard Shortcuts Start#
'''
		self.shortcutFullScreen = QShortcut(QKeySequence("F"),self)
		self.shortcutFullScreen.activated.connect(self.fullscreenAction)

		self.shortcut = QShortcut(QKeySequence("Space"),self)
		self.shortcut.activated.connect(self.play)

		self.shortcut = QShortcut(QKeySequence("Media Play"),self)
		self.shortcut.activated.connect(self.play)

		self.shortcut = QShortcut(QKeySequence("Media Next"),self)
		self.shortcut.activated.connect(self.Foward10)

		self.shortcut = QShortcut(QKeySequence("Media Previous"),self)
		self.shortcut.activated.connect(self.Backward10)

		self.shortcut = QShortcut(QKeySequence("Right"),self)
		self.shortcut.activated.connect(self.Foward10)

		self.shortcut = QShortcut(QKeySequence("Left"),self)
		self.shortcut.activated.connect(self.Backward10)

	def fullscreenAction(self):
		if (self.isMaximized()==True):
			self.showFullScreen()
			self.hideW()
		else:
			self.showMaximized()
			self.showW()	
	
	def eventFilter(self, source, event):
		if event.type() == QtCore.QEvent.MouseMove:
			if event.buttons() == QtCore.Qt.NoButton:
				self.showW()
			else:
				self.timer.stop()
				self.start()
		return QMainWindow.eventFilter(self, source, event)
'''

def start(self):
	self.timer.start(10000)

def hideW(self):
	self.ui.controlWidget.hide()

def showW(self):
	self.ui.controlWidget.show()

def Foward10(self):
	now = self.ui.positionSlider.value()
	seek = now + 10000
	self.ui.mediaPlayer.setPosition(seek)
	

def Backward10(self):
	now = self.ui.positionSlider.value()
	seek = now - 10000
	self.ui.mediaPlayer.setPosition(seek)

def mouseDoubleClickEvent(self, event):
	self.fullscreenAction()

def fullscreenAction(self):
	if (self.isMaximized()==True):
		self.showFullScreen()
		self.hideW()
	else:
		self.showMaximized()
		self.showW()			




def exitCall(self):
	self.ui.hide()

def play(self):
	print("Module Call")
	if self.ui.mediaPlayer.state() == QMediaPlayer.PlayingState:
		self.ui.mediaPlayer.pause()
	else:
		self.ui.mediaPlayer.play()

def mediaStateChanged(self, state):
	if self.ui.mediaPlayer.state() == QMediaPlayer.PlayingState:
		self.ui.btnPlay.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
	else:
		self.ui.btnPlay.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))


def positionChanged(self, position):
	self.ui.positionSlider.setValue(position)
	millis = position
	millis = int(millis)
	seconds=(millis/1000)%60
	seconds = int(seconds)
	minutes=(millis/(1000*60))%60
	minutes = int(minutes)
	hours=(millis/(1000*60*60))%24	
	self.ui.lblelapsed.setText(str(str("%d:%d:%d" % (hours, minutes, seconds))))

def durationChanged(self, duration):
	self.ui.positionSlider.setRange(0, duration)
	millis = duration
	millis = int(millis)
	seconds=(millis/1000)%60
	seconds = int(seconds)
	minutes=(millis/(1000*60))%60
	minutes = int(minutes)
	hours=(millis/(1000*60*60))%24
	
	self.ui.lblduration.setText(str("%d:%d:%d" % (hours, minutes, seconds)))

def setPosition(self, position):
	self.ui.mediaPlayer.setPosition(position)

def handleError(self):
	self.ui.btnPlay.setEnabled(False)


		#self.show()

#Buttons Styles #
		#self.btnPlay.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
		#self.btnf10s.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekForward))
		#self.btnb10s.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekBackward))
		#self.btnOpen.setIcon(self.style().standardIcon(QStyle.SP_ToolBarVerticalExtensionButton))
#
#Button #Function Calls
		#self.btnf10s.clicked.connect(self.Foward10)
		#self.btnb10s.clicked.connect(self.Backward10)
		#self.btnPlay.clicked.connect(self.play)
		#
		#
		#contextMenu = QMenu(self)
#
		##openAct = contextMenu.addAction("Open\t\t", self.openFile)
		##openFolderAct = contextMenu.addAction("Open Folder\t\t")
		#quitAct = contextMenu.addAction("Exit\t\t", self.exitCall)
#
		#self.btnOpen.setMenu(contextMenu)


#Media Player Functions Start#
'''
		self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
		self.mediaPlayer.setVideoOutput(self.videoWidget)
		self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
		self.mediaPlayer.positionChanged.connect(self.positionChanged)
		self.mediaPlayer.durationChanged.connect(self.durationChanged)
		self.mediaPlayer.error.connect(self.handleError)
'''