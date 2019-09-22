from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
try:
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button1 = browser.find_element_by_id("book").click()
    input1 = browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('input_value').text))
    button2 = browser.find_element_by_id("solve").click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
except Exception as error:
    print(f'Произошла ошибка, вот её описание: {error}')
finally:
    browser.quit()
