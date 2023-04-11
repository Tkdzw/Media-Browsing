#import os, sys
from PyQt5 import QtWidgets,QtCore

def PopulateMovies(self):
	movie = "C:/Users/Tkdzw chiwa/Videos/Movies"
	self.ui.model = QtWidgets.QFileSystemModel()
	self.ui.model.setRootPath((QtCore.QDir.rootPath()))
	self.ui.listView.setModel(self.ui.model)
	self.ui.listView.setRootIndex(self.ui.model.index(movie))

def PopulateShows(self):
	shows = "C:/Users/Tkdzw chiwa/Videos/Series"
	self.ui.model = QtWidgets.QFileSystemModel()
	self.ui.model.setRootPath((QtCore.QDir.rootPath()))
	self.ui.listView.setModel(self.ui.model)
	self.ui.listView.setRootIndex(self.ui.model.index(shows))

def PopulateMusic(self):
	music = "C:/Users/Tkdzw chiwa/Music/MusicBee/Music"
	self.ui.model = QtWidgets.QFileSystemModel()
	self.ui.model.setRootPath((QtCore.QDir.rootPath()))
	self.ui.listView.setModel(self.ui.model)
	self.ui.listView.setRootIndex(self.ui.model.index(music))

def Navigate(self, nav, path):
	
	
	if nav == "back":
		self.directory = path
		count = len(self.directory)
		self.cwd = ""
		for flp in range(count-1):
			if self.cwd == "":
				self.cwd = self.directory[flp]
			else:
				self.cwd = self.cwd + "/" + self.directory[flp]

		self.ui.model = QtWidgets.QFileSystemModel()
		self.ui.model.setRootPath((QtCore.QDir.rootPath()))
		self.ui.listView.setModel(self.ui.model)
		self.ui.listView.setRootIndex(self.ui.model.index(self.cwd))
		self.directory.clear()
		self.directory = self.cwd.split("/")
		self.cwd=""
		return self.directory		
	
	elif nav == "forward":
		self.ui.model = QtWidgets.QFileSystemModel()
		self.ui.model.setRootPath((QtCore.QDir.rootPath()))
		self.ui.listView.setModel(self.ui.model)
		self.ui.listView.setRootIndex(self.ui.model.index(path))
		self.ui.path = ""

	else:
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Warning)
		msg.setText('Error: Invalid Selection')
		retval = msg.exec_()
