from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from PageObject.driver.AndroidClient import AndroidClient
from appium.webdriver.common.touch_action import TouchAction

class MarketPage(object):

    def click_pop_windows(self):
        self.display_wait(AndroidClient.driver, By.XPATH, "//*[@text='创建您的专属选股策略']", "not find this elements")
        react = AndroidClient.driver.get_window_rect()
        actions = TouchAction(AndroidClient.driver)
        actions.tap(x=react['width'] * 0.8, y=react['height'] * 0.8).perform().release()
        #actions.perform()

    def getStockNumberByName(self, name):
        price = AndroidClient.driver.find_element_by_xpath(
            "//*[@text = '"+name+"']/..//*[contains(@resource-id, 'index_price')]"
        ).text
        print(price)
        return float(price)

    def display_wait(self, drvier, local, value, message, times=10, interval=0.5, exception=None):
        WebDriverWait(drvier, times, interval, exception).until(
            EC.presence_of_element_located((local, value)), message=message)

