import time
from selenium import webdriver
from PIL import Image
from pytesseract import image_to_string

class Bot:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.navigate()
        self.url = url

    def take_screenshot(self):
        self.driver.save_screenshot("avito_screen.png")

    def tel_info(self):
        image = Image.open("tel.gif")
        tel = image_to_string(image)

    def crop(self, location, size):
        image = Image.open("avito_screen.png")
        x = location["x"]
        y = location["y"]
        width = size["width"]
        height = size["height"]

        image.crop((x, y, x+width, y+height)).save("tel.gif")
        self.tel_info()


    def navigate(self):
        self.driver.get(url)

        button = self.driver.find_element_by_xpath('//button[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
        button.click()
        time.sleep(3)
        self.take_screenshot()

        image = self.driver.find_element_by_xpath('//div[@class="item-phone-big-number js-item-phone-big-number"]//*')
        location = image.location # dict
        size = image.size
        self.crop(location, size)
