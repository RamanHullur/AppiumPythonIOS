from appium import webdriver
from LOCELEMENT import LOCELEMENT;
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


def capabilities():

        PATH = "/Users/ivantay/Automation/Appium/helomaven/Appium_Tools/appium_web/app/UICatalog.app"

        desired_caps = {}
        desired_caps['deviceName'] = 'iPhone 11'
        desired_caps['platformName'] = 'IOS'
        desired_caps['platformVersion'] = '13.3'
        desired_caps['automationName'] = 'XCuiTest'
        desired_caps['app'] = PATH

        return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

def page_DatePicker(strHour, strMinute, meridiem):



    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, LOCELEMENT.MAINPAGE_DATEPICKER_BYACCESSORIES)))
    element.click()
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, LOCELEMENT.PAGE_DATEPICKER_HOUR_XPATH)))
    element.send_keys(strHour)
    driver.find_element_by_xpath(LOCELEMENT.PAGE_DATEPICKER_MINUTE_XPATH).send_keys(strMinute)
    driver.find_element_by_xpath(LOCELEMENT.PAGE_DATEPICKER_AMPM_XPATH).send_keys(meridiem)

strMinute = "55"
strHour = "11"
meridiem = "PM"

driver = capabilities()
LOCELEMENT = LOCELEMENT()
page_DatePicker(strHour, strMinute, meridiem)
