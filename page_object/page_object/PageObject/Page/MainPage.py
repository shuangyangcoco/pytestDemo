from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.Page.MarketPage import MarketPage
from PageObject.Page.SelectPage import SelectPage
from PageObject.driver.AndroidClient import AndroidClient

class MainPage(object):

    def __init__(self):
        AndroidClient.install_app()

    def gotoSelectPage(self):
        #click selected:
        AndroidClient.driver.find_element_by_xpath("//*[@text='自选']")
        AndroidClient.driver.find_element_by_xpath("//*[@text='自选']").click()
        return SelectPage()

    def gotoMarketPage(self):
        self.display_wait(AndroidClient.driver, By.XPATH, "//*[@text='行情']", "not find this elements")
        #AndroidClient.driver.find_element_by_xpath("//*[@text='行情']")
        AndroidClient.driver.find_element_by_xpath("//*[@text='行情']").click()
        return MarketPage()

    def display_wait(self, drvier, local, value, message, times=10, interval=0.5, exception=None):
        WebDriverWait(drvier, times, interval, exception).until(
            EC.presence_of_element_located((local, value)), message=message)
