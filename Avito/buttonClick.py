from selenium import webdriver
import requests
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.avito.ru/moskva/kvartiry/1-k_kvartira_18_m_33_et._575430586')

submit_button = driver.find_element_by_class_name("button item-phone-button")
html = requests.get("https://www.avito.ru/moskva/kvartiry/1-k_kvartira_18_m_33_et._575430586")
print(html)