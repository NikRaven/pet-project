from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread
from PyQt5.QtGui import *


class Thread(QThread):
    def __init__(self, latency):  # <----
        super().__init__()
        self.latency = latency  # <----

    def run(self):
        print(f'\nself.latency = {self.latency}')  # <----


class CategoryWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Message box')
        self.choose_category()
        self.category_id = ''

    def choose_category(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowIcon(QIcon("./image_here/free-icon-dragon4.png"))

        layout_category = QVBoxLayout()

        self.category_button = QPushButton('Авто')
        self.category_button2 = QPushButton('Недвижимость')
        self.category_button3 = QPushButton('Работа')
        self.category_button4 = QPushButton('Одежда/Обувь/Аксессуары')
        self.category_button5 = QPushButton('Хобби и отдых')
        self.category_button6 = QPushButton('Животные')
        self.category_button7 = QPushButton('Готовый бизнес')
        self.category_button8 = QPushButton('Распродажа')
        self.category_button9 = QPushButton('Услуги')
        self.category_button10 = QPushButton('Электроника')
        self.category_button11 = QPushButton('Для дома и дачи')
        self.category_button12 = QPushButton('Запчасти')
        self.category_button13 = QPushButton('Для детей')
        self.category_button14 = QPushButton('Жильё посуточно')
        self.category_button15 = QPushButton('Красота и здоровье')

        # Добавление элементов управления на окно
        layout_category.addWidget(self.category_button)
        layout_category.addWidget(self.category_button2)
        layout_category.addWidget(self.category_button3)
        layout_category.addWidget(self.category_button4)
        layout_category.addWidget(self.category_button5)
        layout_category.addWidget(self.category_button6)
        layout_category.addWidget(self.category_button7)
        layout_category.addWidget(self.category_button8)
        layout_category.addWidget(self.category_button9)
        layout_category.addWidget(self.category_button10)
        layout_category.addWidget(self.category_button11)
        layout_category.addWidget(self.category_button12)
        layout_category.addWidget(self.category_button13)
        layout_category.addWidget(self.category_button14)
        layout_category.addWidget(self.category_button15)

        # Связывание кнопки с функцией выбора категории
        self.category_button.clicked.connect(self.category_avto)
        self.category_button.setCheckable(True)
        # Связывание кнопки с функцией выбора категории
        self.category_button2.clicked.connect(self.category_building)
        self.category_button2.setCheckable(True)
        # Связывание кнопки с функцией выбора категории
        self.category_button3.clicked.connect(self.category_work)
        self.category_button3.setCheckable(True)
        # Связывание кнопки с функцией выбора категории
        self.category_button4.clicked.connect(self.category_cloth)
        self.category_button4.setCheckable(True)
        # Связывание кнопки с функцией выбора категории
        self.category_button5.clicked.connect(self.category_hobby)
        self.category_button5.setCheckable(True)
        # Связывание кнопки с функцией выбора категории
        self.category_button6.clicked.connect(self.category_animals)
        self.category_button6.setCheckable(True)
        # Связывание кнопки с функцией выбора категории
        self.category_button7.clicked.connect(self.category_bussines)
        self.category_button7.setCheckable(True)
        # Связывание кнопки с функцией выбора категории
        self.category_button8.clicked.connect(self.category_sale)
        self.category_button8.setCheckable(True)
        # Связывание кнопки с функцией выбора категории
        self.category_button9.clicked.connect(self.category_services)
        self.category_button9.setCheckable(True)
        # Связывание кнопки с функцией выбора категории
        self.category_button10.clicked.connect(self.category_electronic)
        self.category_button10.setCheckable(True)
        # Связывание кнопки с функцией выбора категории
        self.category_button11.clicked.connect(self.category_house)
        self.category_button11.setCheckable(True)
        # Связывание кнопки с функцией выбора категории
        self.category_button12.clicked.connect(self.category_avtodetails)
        self.category_button12.setCheckable(True)
        # Связывание кнопки с функцией выбора категории
        self.category_button13.clicked.connect(self.category_child)
        self.category_button13.setCheckable(True)
        # Связывание кнопки с функцией выбора категории
        self.category_button14.clicked.connect(self.category_nothomeless)
        self.category_button14.setCheckable(True)
        # Связывание кнопки с функцией выбора категории
        self.category_button15.clicked.connect(self.category_beauty)
        self.category_button15.setCheckable(True)

        self.setLayout(layout_category)
        self.setWindowTitle('Category')
        self.show()

    def category_avto(self):
        self.category_button.setChecked(True)
        self.category_button2.setChecked(False)
        self.category_button3.setChecked(False)
        self.category_button4.setChecked(False)
        self.category_button5.setChecked(False)
        self.category_button6.setChecked(False)
        self.category_button7.setChecked(False)
        self.category_button8.setChecked(False)
        self.category_button9.setChecked(False)
        self.category_button10.setChecked(False)
        self.category_button11.setChecked(False)
        self.category_button12.setChecked(False)
        self.category_button13.setChecked(False)
        self.category_button14.setChecked(False)
        self.category_button15.setChecked(False)

        self.category_id = 'https://www.avito.ru/all/transport'
        return self.category_id

    def category_building(self):
        self.category_button.setChecked(False)
        self.category_button2.setChecked(True)
        self.category_button3.setChecked(False)
        self.category_button4.setChecked(False)
        self.category_button5.setChecked(False)
        self.category_button6.setChecked(False)
        self.category_button7.setChecked(False)
        self.category_button8.setChecked(False)
        self.category_button9.setChecked(False)
        self.category_button10.setChecked(False)
        self.category_button11.setChecked(False)
        self.category_button12.setChecked(False)
        self.category_button13.setChecked(False)
        self.category_button14.setChecked(False)
        self.category_button15.setChecked(False)
        self.category_id = 'https://www.avito.ru/all/nedvizhimost'
        return self.category_id

    def category_work(self):
        self.category_button.setChecked(False)
        self.category_button2.setChecked(False)
        self.category_button3.setChecked(True)
        self.category_button4.setChecked(False)
        self.category_button5.setChecked(False)
        self.category_button6.setChecked(False)
        self.category_button7.setChecked(False)
        self.category_button8.setChecked(False)
        self.category_button9.setChecked(False)
        self.category_button10.setChecked(False)
        self.category_button11.setChecked(False)
        self.category_button12.setChecked(False)
        self.category_button13.setChecked(False)
        self.category_button14.setChecked(False)
        self.category_button15.setChecked(False)
        self.category_id = 'https://www.avito.ru/all/rabota'
        return self.category_id

    def category_cloth(self):
        self.category_button.setChecked(False)
        self.category_button2.setChecked(False)
        self.category_button3.setChecked(False)
        self.category_button4.setChecked(True)
        self.category_button5.setChecked(False)
        self.category_button6.setChecked(False)
        self.category_button7.setChecked(False)
        self.category_button8.setChecked(False)
        self.category_button9.setChecked(False)
        self.category_button10.setChecked(False)
        self.category_button11.setChecked(False)
        self.category_button12.setChecked(False)
        self.category_button13.setChecked(False)
        self.category_button14.setChecked(False)
        self.category_button15.setChecked(False)
        self.category_id = 'https://www.avito.ru/all/lichnye_veschi'
        return self.category_id

    def category_hobby(self):
        self.category_button.setChecked(False)
        self.category_button2.setChecked(False)
        self.category_button3.setChecked(False)
        self.category_button4.setChecked(False)
        self.category_button5.setChecked(True)
        self.category_button6.setChecked(False)
        self.category_button7.setChecked(False)
        self.category_button8.setChecked(False)
        self.category_button9.setChecked(False)
        self.category_button10.setChecked(False)
        self.category_button11.setChecked(False)
        self.category_button12.setChecked(False)
        self.category_button13.setChecked(False)
        self.category_button14.setChecked(False)
        self.category_button15.setChecked(False)
        self.category_id = 'https://www.avito.ru/all/hobbi_i_otdyh'
        return self.category_id

    def category_animals(self):
        self.category_button.setChecked(False)
        self.category_button2.setChecked(False)
        self.category_button3.setChecked(False)
        self.category_button4.setChecked(False)
        self.category_button5.setChecked(False)
        self.category_button6.setChecked(True)
        self.category_button7.setChecked(False)
        self.category_button8.setChecked(False)
        self.category_button9.setChecked(False)
        self.category_button10.setChecked(False)
        self.category_button11.setChecked(False)
        self.category_button12.setChecked(False)
        self.category_button13.setChecked(False)
        self.category_button14.setChecked(False)
        self.category_button15.setChecked(False)
        self.category_id = 'https://www.avito.ru/all/zhivotnye'
        return self.category_id

    def category_bussines(self):
        self.category_button.setChecked(False)
        self.category_button2.setChecked(False)
        self.category_button3.setChecked(False)
        self.category_button4.setChecked(False)
        self.category_button5.setChecked(False)
        self.category_button6.setChecked(False)
        self.category_button7.setChecked(True)
        self.category_button8.setChecked(False)
        self.category_button9.setChecked(False)
        self.category_button10.setChecked(False)
        self.category_button11.setChecked(False)
        self.category_button12.setChecked(False)
        self.category_button13.setChecked(False)
        self.category_button14.setChecked(False)
        self.category_button15.setChecked(False)
        self.category_id = 'https://www.avito.ru/all/dlya_biznesa'
        return self.category_id

    def category_sale(self):
        self.category_button.setChecked(False)
        self.category_button2.setChecked(False)
        self.category_button3.setChecked(False)
        self.category_button4.setChecked(False)
        self.category_button5.setChecked(False)
        self.category_button6.setChecked(False)
        self.category_button7.setChecked(False)
        self.category_button8.setChecked(True)
        self.category_button9.setChecked(False)
        self.category_button10.setChecked(False)
        self.category_button11.setChecked(False)
        self.category_button12.setChecked(False)
        self.category_button13.setChecked(False)
        self.category_button14.setChecked(False)
        self.category_button15.setChecked(False)
        self.category_id = 'https://www.avito.ru/all/sale'
        return self.category_id

    def category_services(self):
        self.category_button.setChecked(False)
        self.category_button2.setChecked(False)
        self.category_button3.setChecked(False)
        self.category_button4.setChecked(False)
        self.category_button5.setChecked(False)
        self.category_button6.setChecked(False)
        self.category_button7.setChecked(False)
        self.category_button8.setChecked(False)
        self.category_button9.setChecked(True)
        self.category_button10.setChecked(False)
        self.category_button11.setChecked(False)
        self.category_button12.setChecked(False)
        self.category_button13.setChecked(False)
        self.category_button14.setChecked(False)
        self.category_button15.setChecked(False)
        self.category_id = 'https://www.avito.ru/all/predlozheniya_uslug'
        return self.category_id

    def category_electronic(self):
        self.category_button.setChecked(False)
        self.category_button2.setChecked(False)
        self.category_button3.setChecked(False)
        self.category_button4.setChecked(False)
        self.category_button5.setChecked(False)
        self.category_button6.setChecked(False)
        self.category_button7.setChecked(False)
        self.category_button8.setChecked(False)
        self.category_button9.setChecked(False)
        self.category_button10.setChecked(True)
        self.category_button11.setChecked(False)
        self.category_button12.setChecked(False)
        self.category_button13.setChecked(False)
        self.category_button14.setChecked(False)
        self.category_button15.setChecked(False)
        self.category_id = 'https://www.avito.ru/all/bytovaya_elektronika'
        return self.category_id

    def category_house(self):
        self.category_button.setChecked(False)
        self.category_button2.setChecked(False)
        self.category_button3.setChecked(False)
        self.category_button4.setChecked(False)
        self.category_button5.setChecked(False)
        self.category_button6.setChecked(False)
        self.category_button7.setChecked(False)
        self.category_button8.setChecked(False)
        self.category_button9.setChecked(False)
        self.category_button10.setChecked(False)
        self.category_button11.setChecked(True)
        self.category_button12.setChecked(False)
        self.category_button13.setChecked(False)
        self.category_button14.setChecked(False)
        self.category_button15.setChecked(False)
        self.category_id = 'https://www.avito.ru/all/dlya_doma_i_dachi'
        return self.category_id

    def category_avtodetails(self):
        self.category_button.setChecked(False)
        self.category_button2.setChecked(False)
        self.category_button3.setChecked(False)
        self.category_button4.setChecked(False)
        self.category_button5.setChecked(False)
        self.category_button6.setChecked(False)
        self.category_button7.setChecked(False)
        self.category_button8.setChecked(False)
        self.category_button9.setChecked(False)
        self.category_button10.setChecked(False)
        self.category_button11.setChecked(False)
        self.category_button12.setChecked(True)
        self.category_button13.setChecked(False)
        self.category_button14.setChecked(False)
        self.category_button15.setChecked(False)
        self.category_id = 'https://www.avito.ru/all/zapchasti_i_aksessuary'
        return self.category_id

    def category_child(self):
        self.category_button.setChecked(False)
        self.category_button2.setChecked(False)
        self.category_button3.setChecked(False)
        self.category_button4.setChecked(False)
        self.category_button5.setChecked(False)
        self.category_button6.setChecked(False)
        self.category_button7.setChecked(False)
        self.category_button8.setChecked(False)
        self.category_button9.setChecked(False)
        self.category_button10.setChecked(False)
        self.category_button11.setChecked(False)
        self.category_button12.setChecked(False)
        self.category_button13.setChecked(True)
        self.category_button14.setChecked(False)
        self.category_button15.setChecked(False)
        self.category_id = 'https://www.avito.ru/all/tovary_dlya_detey_i_igrushki'
        return self.category_id

    def category_nothomeless(self):
        self.category_button.setChecked(False)
        self.category_button2.setChecked(False)
        self.category_button3.setChecked(False)
        self.category_button4.setChecked(False)
        self.category_button5.setChecked(False)
        self.category_button6.setChecked(False)
        self.category_button7.setChecked(False)
        self.category_button8.setChecked(False)
        self.category_button9.setChecked(False)
        self.category_button10.setChecked(False)
        self.category_button11.setChecked(False)
        self.category_button12.setChecked(False)
        self.category_button13.setChecked(False)
        self.category_button14.setChecked(True)
        self.category_button15.setChecked(False)
        self.category_id = 'https://www.avito.ru/all/kvartiry/sdam/posutochno/' \
                           '-ASgBAgICAkSSA8gQ8AeSUg?context=H4sIAAAAAAAA' \
                           '_0q0MrSqLrYyNLVSyix2yy9KTg1LLSrJTE7MUbJOsjK0rgUEAAD__8Y6r8whAAAA'
        return self.category_id

    def category_beauty(self):
        self.category_button.setChecked(False)
        self.category_button2.setChecked(False)
        self.category_button3.setChecked(False)
        self.category_button4.setChecked(False)
        self.category_button5.setChecked(False)
        self.category_button6.setChecked(False)
        self.category_button7.setChecked(False)
        self.category_button8.setChecked(False)
        self.category_button9.setChecked(False)
        self.category_button10.setChecked(False)
        self.category_button11.setChecked(False)
        self.category_button12.setChecked(False)
        self.category_button13.setChecked(False)
        self.category_button14.setChecked(False)
        self.category_button15.setChecked(True)
        self.category_id = 'https://www.avito.ru/all/krasota_i_zdorove'
        return self.category_id
