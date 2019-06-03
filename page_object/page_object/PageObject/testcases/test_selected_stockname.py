import pytest
from PageObject.Page.MainPage import MainPage

class Test_Selected_stockname(object):

    def test_price(self):
        main = MainPage()
        assert main.gotoSelectPage().getPriceByName('科大讯飞') == 29.46

    def test_add_stock(self, name):
        pass

    def test_hushenprice(self):
        main = MainPage()
        main.gotoMarketPage().click_pop_windows()
        assert main.gotoMarketPage().getStockNumberByName('深证成指') == 8943.35