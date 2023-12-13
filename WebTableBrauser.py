from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys


class MainWindow2(QMainWindow):

    def __init__(self, st_url):
        super(MainWindow2, self).__init__()
        self.st_url = st_url

        self.tabs = QTabWidget()

        self.tabs.setDocumentMode(True)

        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

        self.tabs.currentChanged.connect(self.current_tab_changed)

        self.tabs.setTabsClosable(True)

        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        self.setCentralWidget(self.tabs)

        self.status = QStatusBar()

        self.setStatusBar(self.status)

        navtb = QToolBar("Навигация")

        self.addToolBar(navtb)

        back_btn = QAction("Назад", self)

        back_btn.setStatusTip("На предыдущую страницу")

        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())

        navtb.addAction(back_btn)

        next_btn = QAction("Вперёд", self)
        next_btn.setStatusTip("Вперёд на следующую страницу")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navtb.addAction(next_btn)

        reload_btn = QAction("Обновить", self)
        reload_btn.setStatusTip("Обновить страницу")
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

        home_btn = QAction("Домой", self)
        home_btn.setStatusTip("На главную страницу")

        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        self.urlbar = QLineEdit()

        self.urlbar.returnPressed.connect(self.navigate_to_url)

        navtb.addWidget(self.urlbar)

        stop_btn = QAction("Стоп", self)
        stop_btn.setStatusTip("Остановить загрузку страницы")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

        self.add_new_tab(QUrl(self.st_url), 'страница запроса')

        self.show()

        self.setWindowTitle("Dragon eyes")

    def add_new_tab(self, qurl=None, label="Blank"):

        if qurl is None:
            qurl = QUrl('http://www.yandex.com')

        browser = QWebEngineView()

        browser.setUrl(qurl)

        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))

        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))

    def tab_open_doubleclick(self, i):

        if i == -1:
            self.add_new_tab()

    def current_tab_changed(self, i):

        qurl = self.tabs.currentWidget().url()

        self.update_urlbar(qurl, self.tabs.currentWidget())

        self.update_title(self.tabs.currentWidget())

    def close_current_tab(self, i):

        if self.tabs.count() < 2:
            return

        self.tabs.removeTab(i)

    def update_title(self, browser):

        if browser != self.tabs.currentWidget():
            return

        title = self.tabs.currentWidget().page().title()

        self.setWindowTitle("% s - Dragon eyes" % title)

    def navigate_home(self):

        self.tabs.currentWidget().setUrl(QUrl("http://www.yandex.com"))

    def navigate_to_url(self):

        q = QUrl(self.urlbar.text())

        if q.scheme() == "":
            q.setScheme("http")

        self.tabs.currentWidget().setUrl(q)

    def update_urlbar(self, q, browser=None):

        if browser != self.tabs.currentWidget():
            return

        self.urlbar.setText(q.toString())

        self.urlbar.setCursorPosition(0)
