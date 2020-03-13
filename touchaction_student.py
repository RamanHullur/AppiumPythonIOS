import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


def capabilities():

        PATH = "/Users/ivantay/Automation/Appium/helomaven/Appium_Tools/appium_web/app/UICatalog.app"

        desired_caps = {}
        desired_caps['deviceName'] = 'iPhone 11'
        desired_caps['platformName'] = 'IOS'
        desired_caps['platformVersion'] = '13.3'
        desired_caps['automationName'] = 'XCuiTest'
        desired_caps['app'] = PATH
        return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


driver = capabilities()

action = TouchAction(driver)
action.press(x=0, y=300).wait(2000).move_to(x=-0, y=-800).release().perform()

#quit
time.sleep(10)
driver.quit()
