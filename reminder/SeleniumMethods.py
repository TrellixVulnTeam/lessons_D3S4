"""
#Selenium
# Явное ожидание, когда элемент будет кликабельным
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()

# пока кнопка станет неактивной
until_not

В модуле expected_conditions есть много других правил, которые позволяют реализовать необходимые ожидания:
text_to_be_present_in_element
title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present

from selenium.webdriver.common.by import By
driver.find_element(By.XPATH, '//button[text()="Some text"]')

driver.find_element_by_id('loginForm')
find_element_by_name('username')
find_element_by_xpath("//input[@name='continue'][@type='button']")
find_element_by_link_text('Continue')
find_element_by_partial_link_text('Cont')
find_element_by_tag_name('h1') или ("input")
find_element_by_class_name('content')
find_element_by_class_name("btn.btn-default")
find_element_by_css_selector('p.content')
find_element_by_css_selector("[for='python']")

find_elements_by_name и т.д.

"""