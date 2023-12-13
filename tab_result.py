from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QPushButton, \
    QTableWidgetItem, QProgressBar
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
import WebTableBrauser

class MainWindow2(QMainWindow):
    # конструктор
    def __init__(self):
        # вызываем методы суперкласса
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(500, 100))  # размер
        self.setWindowTitle("Dragon Table")  # заголовок окна
        central_widget = QWidget(self)  # центральный виджет
        self.setCentralWidget(central_widget)  # устанавливаем центральный виджет
        self.setWindowIcon(QIcon("./image_here/free-icon-dragon5.png"))
        grid_layout = QGridLayout(self)  # создаём QGridLayout
        central_widget.setLayout(grid_layout)  # добавляем layout в центральный виджет

        self.table = QTableWidget(self)  # создаём таблицу
        self.table.setColumnCount(3)  # устанавливаем 3 колонки

        # заголовки таблицы(колонок)
        self.table.setHorizontalHeaderLabels(["url", "Описание", "Подробнее"])

        self.table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        self.table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        self.table.horizontalHeaderItem(2).setToolTip("Column 3 ")

        # расположение заголовков
        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)

        grid_layout.addWidget(self.table, 0, 0)  # добавляем таблицу на grid

        # self.show()

    def get_item(self, i, dictionary_itog2):
        self.table.setRowCount(i)  # устанавливаем количество строк равных количеству найденных элементов
        self.dictionary_itog2 = dictionary_itog2
        row = 0
        for keys, values in self.dictionary_itog2.items():
            self.btn = QPushButton(f'{keys}')
            master = dictionary_itog2.get(row + 1).split('KISEL')
            self.table.setItem(row, 0, QTableWidgetItem(master[0]))
            self.table.setItem(row, 1, QTableWidgetItem(master[1]))
            self.table.setCellWidget(row, 2, self.btn)
            self.table.resizeColumnsToContents()
            # Связывание кнопки с функцией подробнее(открываем браузер на странице с конкретным элементом)
            self.btn.clicked.connect(self.buttonClicked)
            row += 1
            master.clear()

        self.table.resizeColumnsToContents()

    def buttonClicked(self):
        sender = self.sender()
        #print(sender.text())
        self.statusBar().showMessage(sender.text() + ' was pressed')
        master = self.dictionary_itog2.get(int(sender.text())).split('KISEL')
        #print(master[0])
        self.openbrauser = WebTableBrauser.MainWindow2(str(master[0]))
        master.clear()
