from PageObject.driver.AndroidClient import AndroidClient

class SelectPage(object):

    def addDefault(self):
        pass

    def getPriceByName(self, name):
        price = AndroidClient.driver.find_element_by_xpath("//*[contains(@resource-id, 'stockName') and @text= '"+name+"']\
        /../../..//*[contains(@resource-id, 'currentPrice')]").text
        return price