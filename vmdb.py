import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QMenu, QDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtCore
import imdb, socket
from imdb import IMDbError
from bs4 import BeautifulSoup
import requests


class webSearch(QDialog):
	"""docstring for IMDb"""
	def __init__(self):
		super(webSearch, self).__init__()
		loadUi("UI/web search.ui", self)
		self.btnSearch.clicked.connect(self.search)
		  	
	def search(self):
		##Request Page source
		url = "https://www.imdb.com/find?s=tt&q=" + self.txtSearch.text()
		try:
			page = requests.get(url)
			soup = BeautifulSoup(page.content, "html.parser")
			scraped_movies = soup.find_all('a', class_= "ipc-metadata-list-summary-item__t")

			movies = []
			for movie in scraped_movies:

				movie = movie.get_text().replace('\n', "")
				movies.append(movie)

			soup = BeautifulSoup(page.content, "html.parser")
			scraped_years = soup.find_all('span', class_= "ipc-metadata-list-summary-item__li")

			years = []
			for year in scraped_years:

				year = year.get_text().replace('\n', "")
				years.append(year)

			i=0
			self.listWidget.clear()
			for movie in scraped_movies:
				#stf = float(ratings[i])
				self.listWidget.addItem(movies[i])

				i+=1

		except Exception as e:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText('Error: "{}"'.format(e))
			retval = msg.exec_()

