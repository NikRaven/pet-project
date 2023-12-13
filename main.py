# Импортируйте необходимые классы для создания окна и элементов управления:
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QProgressBar
from PyQt5 import QtWidgets
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtGui import QIcon
import category_window
from PyQt5.QtCore import QThread
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import WebBrauser
import tab_result


# Создадим основной класс приложения, который будет содержать главное окно:
class WebParserApp(QWidget):

    def __init__(self, simple, simple2):
        super().__init__()
        self.simple = simple
        self.simple2 = simple2
        self.setWindowTitle('Message box')
        self.init_ui()
        self.informatortuple = dict()
        self.counter_elements_in_dict = 1
        self.itog2 = {}

    def closeEvent(self, event):
        msg = QMessageBox(self)
        msg.setWindowIcon(QIcon("./image_here/free-icon-dragon.png"))
        msg.setWindowTitle("Выход")
        msg.setIcon(QMessageBox.Question)
        msg.setText("Вы действительно хотите выйти ?")

        button_aceptar = msg.addButton("Да хочу", QMessageBox.YesRole)
        button_cancelar = msg.addButton("Отменить", QMessageBox.RejectRole)
        msg.setDefaultButton(button_aceptar)
        msg.exec_()

        if msg.clickedButton() == button_aceptar:
            event.accept()
        elif msg.clickedButton() == button_cancelar:
            event.ignore()

    def init_ui(self):
        self.setWindowIcon(QIcon("./image_here/free-icon-dragon2.png"))

        # Создание элементов управления

        layout = QVBoxLayout()
        self.url_input = QLineEdit()  # QLineEdit()
        self.url_input.setText(self.simple)  # 'https://www.avito.ru/all/avtomobili?cd=1'
        self.key_world = QLineEdit()
        self.key_world.setText(self.simple2)
        self.parse_button = QPushButton('Parse')
        self.parse_button2 = QPushButton('Выбрать Категорию')
        self.parse_button3 = QPushButton('Применить Категорию')
        self.parse_button4 = QPushButton('Открыть Браузер')
        self.parse_button5 = QPushButton('Открыть Таблицу')
        self.result_output = QTextEdit()
        self.pbar = QProgressBar(self)
        # setting its geometry
        # self.pbar.setGeometry(30, 40, 200, 25)
        # Добавление элементов управления на окно
        layout.addWidget(self.url_input)
        layout.addWidget(self.key_world)
        layout.addWidget(self.parse_button)
        layout.addWidget(self.parse_button2)
        layout.addWidget(self.result_output)
        layout.addWidget(self.parse_button4)
        layout.addWidget(self.parse_button3)
        layout.addWidget(self.parse_button5)
        layout.addWidget(self.pbar)

        # Связывание кнопки с функцией парсинга
        self.parse_button.clicked.connect(self.parse_website)
        # Связывание кнопки с функцией выбора категории
        self.parse_button2.clicked.connect(self.open_category)
        # Связывание кнопки с функцией применения категории
        self.parse_button3.clicked.connect(self.use_category)
        # Связывание кнопки с функцией выбора фильтров
        self.parse_button4.clicked.connect(self.use_brauser)
        # Связывание кнопки с функцией выбора фильтров
        self.parse_button5.clicked.connect(self.use_table)

        self.setLayout(layout)
        self.setWindowTitle('Dragon Parser')

        # Message Box
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QIcon("./image_here/free-icon-dragon3.png"))
        msg.setWindowTitle("Dragon Parser")
        msg.setText("Программа предназначена для тестового использования!"
                    "Если Вы согласны с данным условием, нажмите OK")
        msg.setIcon(QtWidgets.QMessageBox.Information)  # QtWidgets.QMessageBox.Critical
        msg.exec_()

    # parse_website будет выполнять парсинг сайта при нажатии кнопки:
    # https://www.avito.ru/all/avtomobili?cd=1
    # код для парсинга сайта avito с использованием BeautifulSoup
    # Результат парсинга можно выводить в QTextEdit с помощью метода self.result_output.setText()
    def parse_website(self):
        itog = set()
        self.itog2.clear()
        url = self.url_input.text()  # ('https://www.avito.ru/all/avtomobili?cd=1')
        n = self.key_world.text()  # вводим модель, которую хотим найти
        self.pbar.setValue(0)
        time_control = datetime.now().strftime("%H_%M_%S")
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!для работы Chrome в headless режиме!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run Chrome in headless mode
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        driver = webdriver.Chrome(chrome_options)
        driver.get(url)  # загружаем страницу с поиском авто по категориям
        # assert "Купить авто" in driver.title  # регистрируем текстовое поле и имитируем ввод строки "Купить авто"
        search = driver.find_element(By.CLASS_NAME, "input-input-Zpzc1")
        search.send_keys(n)

        open_search = driver.find_element(By.CLASS_NAME, "desktop-15w37ob")
        open_search.click()

        time.sleep(1)  # ставим на паузу, чтобы страница прогрузилась
        control_url = driver.current_url
        count_pages = 0
        count_links = 0
        for num in range(1, 101):
            #print(control_url + f'&p={num}')
            driver.get(control_url + f'&p={num}')
            time.sleep(1)

            soup = BeautifulSoup(driver.page_source, 'lxml')
            # загружаем страницу и извлекаем ссылки через атрибут class
            all_publications2 = \
                soup.find_all('a', {'class': 'iva-item-sliderLink-uLz1v'})
            #print(len(all_publications2))
            count_links += len(all_publications2)
            if len(all_publications2) == 0:
                count_pages = num - 1
                break
            # форматируем результат
            for article in all_publications2:
                obj_i = "https://www.avito.ru" + article['href'] + "KISEL" + article['title']
                obj_url = "https://www.avito.ru" + article['href']
                obj_description = article['title']
                itog.add(obj_i)

            # ____________________________________________________________________________
            for element in itog:
                self.itog2[self.counter_elements_in_dict] = element
                self.counter_elements_in_dict += 1
            # for keys, values in self.itog2.items():
            #     print(keys, values)
            # ____________________________________________________________________________

            # Открываем или создаем файл с именем "example.txt" в режиме записи ("w")
            with open(f'./file/{self.key_world.text()}_{time_control}.txt', 'a') as file:
                for index, value in enumerate(itog):
                    # Записываем текст в файл
                    file.write(f'{index}:{value}' + '\n')
            itog.clear()
            self.pbar.setValue(num)
        self.pbar.setValue(100)
        #print(time_control + '_______' + datetime.now().strftime("%H_%M_%S"))
        out_result = self.result_output.setText(
            f'В папке file Вы обнаружите ссылки по ключевому слову "{self.key_world.text()}"!\n'
            f'Обработано страниц сайта: {count_pages}\n'
            f'Найдено упоминаний: {count_links}')

    def use_brauser(self):
        self.showbrauser = WebBrauser.MainWindow()

    def use_table(self):
        self.showbrauser2 = tab_result.MainWindow2()
        self.showbrauser2.get_item(len(self.itog2), self.itog2)
        self.showbrauser2.show()

    def open_category(self):
        self.category_win = category_window.CategoryWindow()
        self.category_win.show()

    def use_category(self):
        self.url_input.setText(self.category_win.category_id)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    prosto = 'выбор категории -> применить категорию'
    prosto2 = 'поле для ключевого слова'
    window = WebParserApp(prosto, prosto2)
    window.show()
    sys.exit(app.exec_())
