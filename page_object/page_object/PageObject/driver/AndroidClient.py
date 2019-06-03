
from appium import webdriver

class AndroidClient(object):

    #driver:webdriver
    @classmethod
    def install_app(cls) -> webdriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["unicodeKeyboard"] = True
        caps["autoGrantPermissions"] = True

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(30)
        return cls.driver