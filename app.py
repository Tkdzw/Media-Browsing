import sys, os

from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import QDir, Qt, QUrl, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyle, QStackedWidget, QMenu, QShortcut, QFileDialog, QMessageBox
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtGui import QIcon, QKeySequence, QPixmap
from pathlib import Path

import mimetypes
mimetypes.init()

import vmdb
from UI.uiMainMenu import Ui_MainWindow
import populate
import milisec

class MainMenu(QMainWindow):
	"""docstring for MainMenu"""
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle("VMDB")
		self.ui.stackedWidget.setCurrentIndex(0)
		self.showMaximized()
			

#Library Buttons
		self.ui.btnMovies.clicked.connect(self.PopulateMovies)
		self.ui.btnTv_Shows.clicked.connect(self.PopulateShows)
		self.ui.btnMusic.clicked.connect(self.PopulateMusic)
		self.ui.btnBack.clicked.connect(self.Back)
		self.ui.btnIMDb.clicked.connect(self.openWebSearch)

#Buttons Styles #
		self.ui.btnPlay.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
		self.ui.btnf10s.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekForward))
		self.ui.btnb10s.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekBackward))
		self.ui.btnOpen.setIcon(self.style().standardIcon(QStyle.SP_ToolBarVerticalExtensionButton))

#Button Function Calls
		self.ui.btnf10s.clicked.connect(self.Forward10)
		self.ui.btnb10s.clicked.connect(self.Backward10)
		self.ui.btnPlay.clicked.connect(self.play)
		
		
		contextMenu = QMenu(self)

		#openAct = contextMenu.addAction("Open\t\t", self.openFile)
		#openFolderAct = contextMenu.addAction("Open Folder\t\t")
		quitAct = contextMenu.addAction("Exit\t\t", self.exitCall)

		self.ui.btnOpen.setMenu(contextMenu)

#Media Player Instantiation		
		self.ui.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
		self.ui.mediaPlayer.setVideoOutput(self.ui.videoWidget)
		self.ui.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
		self.ui.mediaPlayer.positionChanged.connect(self.positionChanged)
		self.ui.mediaPlayer.durationChanged.connect(self.durationChanged)
		#self.ui.mediaPlayer.error.connect(self.handleError)

		self.ui.positionSlider.setRange(0,0)
		self.ui.positionSlider.sliderMoved.connect(self.setPosition)

#Populate Functions
	def PopulateMovies(self):
		movies = populate.PopulateMovies(self)
		
	def PopulateShows(self):
		series = populate.PopulateShows(self)

	def PopulateMusic(self):
		music = populate.PopulateMusic(self)

#Web Search API
	def openWebSearch(self):
		search = vmdb.webSearch()
		widget.addWidget(search)
		widget.setCurrentIndex(widget.currentIndex()+1)
		widget.setGeometry(275, 75, 900, 600)
		widget.setFixedHeight(600)
		widget.setFixedWidth(900)
		#widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		widget.show()

#Context Menu For Opening Files
	def contextMenuEvent(self, event):

		contextMenu = QMenu(self)

		index = self.ui.listView.currentIndex()
		self.ui.path = self.ui.model.filePath(index)
		
		if (os.path.isfile(self.ui.path)):
			openAct = contextMenu.addAction("Play with Millisec\t\t")
			currentAct = contextMenu.addAction("Details\t\t")
			quitAct = contextMenu.addAction("Exit\t\t")

		else:
			openAct = contextMenu.addAction("Open\t\t")
			currentAct = contextMenu.addAction("Properties\t\t")
			quitAct = contextMenu.addAction("Exit\t\t")

		action = contextMenu.exec_(self.mapToGlobal(event.pos()))
		

		if action == openAct:
			self.ui.directory = self.ui.path.split("/")
			self.ui.btnBack.show()

			if (os.path.isfile(self.ui.path)):
				mimestart = mimetypes.guess_type(self.ui.path)[0]
				
				if mimestart != None:
					mimestart = mimestart.split('/')[0]

					if mimestart in ['video']:
						self.ui.stackedWidget.setCurrentIndex(1)
						player = self.openFile(self.ui.path)
				
				self.ui.path = ""
				now = len(self.ui.directory)
				for flp in range(now-1):
					if self.ui.path == "":
						self.ui.path = self.ui.directory[flp]
					else:
						self.ui.path = self.ui.path + "/" + self.ui.directory[flp]				
				self.ui.directory = self.ui.path.split("/")

			else:
				self.nav = "forward"
				self.navPath = self.ui.path
				Navigation = populate.Navigate(self, self.nav, self.navPath)

		elif action == currentAct:
			print(self.ui.path)
		elif action == quitAct:
			self.ui.hide()

#Navigation Funtions

	def Back(self):
		self.back = "back"
		self.navPath = self.ui.directory
		Navigation = populate.Navigate(self, self.back, self.navPath)
		self.ui.directory = Navigation

#Media Player Funtions
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
		if self.ui.mediaPlayer.state() == QMediaPlayer.PlayingState:
			self.ui.mediaPlayer.pause()
		else:
			self.ui.mediaPlayer.play()

	def Forward10(self):
		now = self.ui.positionSlider.value()
		seek = now + 10000
		self.ui.mediaPlayer.setPosition(seek)
	

	def Backward10(self):
		now = self.ui.positionSlider.value()
		seek = now - 10000
		self.ui.mediaPlayer.setPosition(seek)

	def setPosition(self, position):
		self.ui.mediaPlayer.setPosition(position)


	def openFile(self, fileName):

		if fileName != '':
			self.ui.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
			self.ui.btnPlay.setEnabled(True)
			self.ui.mediaPlayer.play()
			self.setWindowTitle("Millisec: " + Path(fileName).stem)

#Keyboard Shortcuts Start#

		self.shortcutFullScreen = QShortcut(QKeySequence("F"),self)
		self.shortcutFullScreen.activated.connect(self.fullscreenAction)

		self.shortcut = QShortcut(QKeySequence("Space"),self)
		self.shortcut.activated.connect(self.play)

		self.shortcut = QShortcut(QKeySequence("Media Play"),self)
		self.shortcut.activated.connect(self.play)

		self.shortcut = QShortcut(QKeySequence("Media Next"),self)
		self.shortcut.activated.connect(self.Forward10)

		self.shortcut = QShortcut(QKeySequence("Media Previous"),self)
		self.shortcut.activated.connect(self.Backward10)

		self.shortcut = QShortcut(QKeySequence("Right"),self)
		self.shortcut.activated.connect(self.Forward10)

		self.shortcut = QShortcut(QKeySequence("Left"),self)
		self.shortcut.activated.connect(self.Backward10)


	def fullscreenAction(self):
		if (self.isMaximized()==True):
			self.showFullScreen()
			self.hideW()
		else:
			self.showMaximized()
			self.showW()	
	
	def mouseDoubleClickEvent(self, event):
		self.fullscreenAction()

	def eventFilter(self, source, event):
		if event.type() == QtCore.QEvent.MouseMove:
			if event.buttons() == QtCore.Qt.NoButton:
				self.showW()
			else:
				self.timer.stop()
				self.start()
		return QMainWindow.eventFilter(self, source, event)

	def start(self):
		self.timer.start(10000)

	def hideW(self):
		self.ui.controlWidget.hide()

	def showW(self):
		self.ui.controlWidget.show()

	def exitCall(self):
		fileName = ""
		self.ui.mediaPlayer.stop()
		self.ui.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
		self.ui.stackedWidget.setCurrentIndex(0)
		self.setWindowTitle("VMDB")


#Main Application Execution
app = QApplication(sys.argv)
mainapp = MainMenu()
widget = QStackedWidget()


try:
	sys.exit(app.exec())
except Exception as e:
	raise e

