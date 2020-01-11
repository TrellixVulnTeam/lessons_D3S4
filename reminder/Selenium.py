"""
# Assert
assert "successful" in element.text

# Выпадающие списки
browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("option:nth-child(2)").click()
browser.find_element_by_css_selector("[value='1']").click()
# В Селениуме есть отдельный метод для списков
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1")
или
select.select_by_visible_text("Текст")
select.select_by_index(1)

# Модальное окно (например, alert)
alert = browser.switch_to.alert
alert_text = alert.text # Получаем текст из алерта
alert.accept()
# Если есть кнопка Отмена
alert.dismiss()
# Если там есть поля ввода
alert.send_keys("My answer")

# Переключение между окнами и фрэймами
#При открытии новой вкладки WebDriver продолжит работать со старой вкладкой. Для переключения на новую вкладку надо явно указать,
#на какую вкладку мы хотим перейти. Это делается с помощью команды switch_to.window:
browser.switch_to.window(window_name)
#Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок.
#Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
new_window = browser.window_handles[1]
#Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
first_window = browser.window_handles[0]

# Scroll
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
#Scroll на 100px
browser.execute_script("window.scrollBy(0, 100);")

# Import файлов
import os
current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
print(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
print(os.path.abspath(os.path.dirname(__file__)))
element = browser.find_element_by_id("file")
element.send_keys(file_path)
Элемент в форме, который выглядит, как кнопка добавления файла, имеет атрибут type="file".
Мы должны сначала найти этот элемент с помощью селектора, а затем применить к нему метод send_keys(file_path).

# Вызов JS
browser.execute_script("alert('Robots at work');")
browser.execute_script("document.title='Script executing';alert('Robots at work');")

Вместо встроенных find_element_by... можно использовать вот такую конструкцию:
element = browser.execute_script('document.getElementsByName("name")')
Так же есть:
getElementById
getElementsByTagName
getElementsByClassName
querySelector - для CSS
querySelectorAll - для CSS (находит все совпадения)
evaluate - для XPATH.

# Перетаскивание
from selenium.webdriver import ActionChains
element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target)
"""