# importing required libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys


# main window
class MainWindow(QMainWindow):

    # конструктор
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # создаём tab widget
        self.tabs = QTabWidget()

        # делаем document mode true
        self.tabs.setDocumentMode(True)

        # добавляем действие при двойном нажатии на область
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

        # добавляем действие если tab изменили
        self.tabs.currentChanged.connect(self.current_tab_changed)

        # делаем tabs(вкладки) закрываемыми
        self.tabs.setTabsClosable(True)

        # действие при закрытии вкладки
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        # делаем вкладку центральным виджетом
        self.setCentralWidget(self.tabs)

        # создам статус бар
        self.status = QStatusBar()
        self.setStatusBar(self.status)

        # создаём tool bar для навигации
        navtb = QToolBar("Навигация")

        # добавляем tool bar на main window
        self.addToolBar(navtb)

        # действие назад
        back_btn = QAction("Назад", self)
        back_btn.setStatusTip("На предыдущую страницу")

        # добавляем действие на кнопку назад
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())

        # добавляем на tool bar
        navtb.addAction(back_btn)

        # кнопка вперёд
        next_btn = QAction("Вперёд", self)
        next_btn.setStatusTip("Вперёд на следующую страницу")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navtb.addAction(next_btn)

        # кнопка обновить
        reload_btn = QAction("Обновить", self)
        reload_btn.setStatusTip("Обновить страницу")
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

        # кнопка домой
        home_btn = QAction("Домой", self)
        home_btn.setStatusTip("На главную страницу")

        # действие к кнопке домой
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        # добавляем сепаратор
        navtb.addSeparator()

        # добавляем поле для отображения и ввода URL
        self.urlbar = QLineEdit()

        # действие при нажатии return
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        # добавляем на tool bar
        navtb.addWidget(self.urlbar)

        # кнопка стоп
        stop_btn = QAction("Стоп", self)
        stop_btn.setStatusTip("Остановить загрузку страницы")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

        # создаём первую вкладку
        self.add_new_tab(QUrl('http://www.yandex.com'), 'Домашняя страница')

        # показать всё
        self.show()

        # заголовок окна программы
        self.setWindowTitle("Dragon eyes")

    # метод добавления новой вкладки
    def add_new_tab(self, qurl=None, label="Blank"):

        # if url is blank
        if qurl is None:
            # creating a yandex url
            qurl = QUrl('http://www.yandex.com')

        # creating a QWebEngineView object
        browser = QWebEngineView()

        # setting url to browser
        browser.setUrl(qurl)

        # setting tab index
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        # adding action to the browser when url is changed
        # update the url
        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))

        # adding action to the browser when loading is finished
        # set the tab title
        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))

    # когда двойное нажатие на вкладку
    def tab_open_doubleclick(self, i):

        # checking index i.e
        # No tab under the click
        if i == -1:
            # creating a new tab
            self.add_new_tab()

    # когда вкладка изменена
    def current_tab_changed(self, i):

        # get the curl
        qurl = self.tabs.currentWidget().url()

        # update the url
        self.update_urlbar(qurl, self.tabs.currentWidget())

        # update the title
        self.update_title(self.tabs.currentWidget())

    # когда вкладка закрыта
    def close_current_tab(self, i):

        # if there is only one tab
        if self.tabs.count() < 2:
            # do nothing
            return

        # else remove the tab
        self.tabs.removeTab(i)

    # обновить заголовок
    def update_title(self, browser):

        # if signal is not from the current tab
        if browser != self.tabs.currentWidget():
            # do nothing
            return

        # get the page title
        title = self.tabs.currentWidget().page().title()

        # set the window title
        self.setWindowTitle("% s - Dragon eyes" % title)

    # действие домой
    def navigate_home(self):

        # go to yandex
        self.tabs.currentWidget().setUrl(QUrl("http://www.yandex.com"))

    # навигация по url
    def navigate_to_url(self):

        # get the line edit text
        # convert it to QUrl object
        q = QUrl(self.urlbar.text())

        # if scheme is blank
        if q.scheme() == "":
            # set scheme
            q.setScheme("http")

        # set the url
        self.tabs.currentWidget().setUrl(q)

    # обновление url
    def update_urlbar(self, q, browser=None):

        # If this signal is not from the current tab, ignore
        if browser != self.tabs.currentWidget():
            return

        # set text to the url bar
        self.urlbar.setText(q.toString())

        # set cursor position
        self.urlbar.setCursorPosition(0)
