from appium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from LOCELEMENT import LOCELEMENT;
from appium.webdriver.common.touch_action import TouchAction


def capabilities ():

        PATH = "/Users/ivantay/Automation/Appium/helomaven/Appium_Tools/appium_web/app/UICatalog.app"

        desired_caps = {}
        desired_caps['deviceName'] = 'iPhone 11'
        desired_caps['platformName'] = 'IOS'
        desired_caps['platformVersion'] = '13.3'
        desired_caps['automationName'] = 'XCuiTest'
        desired_caps['noReset'] = 'true'
        desired_caps['forceMjsonwp'] = 'true'
        desired_caps['app'] = PATH
        desired_caps['autoDismissAlerts'] = 'true'

        return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def navigateMainPage():
    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_ACTIONSHEET_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_ACTIVITYINDICATORS_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_ALERTVIEWS_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_BUTTONS_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_DATEPICKER_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_PAGECONTROL_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_IMAGEVIEW_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_PAGECONTROL_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_PICKERVIEW_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_PROGRESSVIEWS_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_SEGMENTEDCONTROLS_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_SLIDERS_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_STEPPERS_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_SWITCHES_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_TEXTFIELDS_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_TEXTVIEW_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_WEBVIEW_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_SEARCHBARS_BYACCESSORIES).click();
    driver.back();

    driver.find_element_by_accessibility_id(LOCELEMENT.MAINPAGE_TOOLBARS_BYACCESSORIES).click();
    driver.back();

driver = capabilities()
navigateMainPage()
