
class LOCELEMENT :

    MAINPAGE_ACTIONSHEET_BYACCESSORIES = "Action Sheets"
    MAINPAGE_ACTIVITYINDICATORS_BYACCESSORIES="Activity Indicators"
    MAINPAGE_ALERTVIEWS_BYACCESSORIES= "Alert Views"
    MAINPAGE_BUTTONS_BYACCESSORIES="Buttons"
    MAINPAGE_DATEPICKER_BYACCESSORIES="Date Picker"
    MAINPAGE_IMAGEVIEW_BYACCESSORIES="Image View"
    MAINPAGE_PAGECONTROL_BYACCESSORIES = "Page Control";
    MAINPAGE_PICKERVIEW_BYACCESSORIES = "Picker View";
    MAINPAGE_PROGRESSVIEWS_BYACCESSORIES = "Progress Views";
    MAINPAGE_SEGMENTEDCONTROLS_BYACCESSORIES = "Segmented Controls";
    MAINPAGE_SLIDERS_BYACCESSORIES = "Sliders";
    MAINPAGE_STEPPERS_BYACCESSORIES = "Steppers";
    MAINPAGE_SWITCHES_BYACCESSORIES = "Switches";
    MAINPAGE_TEXTFIELDS_BYACCESSORIES = "Text Fields";
    MAINPAGE_TEXTVIEW_BYACCESSORIES = "Text View";
    MAINPAGE_WEBVIEW_BYACCESSORIES = "Web View";
    MAINPAGE_SEARCHBARS_BYACCESSORIES = "Search Bars";
    MAINPAGE_TOOLBARS_BYACCESSORIES = "Toolbars";



    #ActionSheet
    PAGE_ACTIONSHEETS_OKCANCEL_XPATH ="//XCUIElementTypeStaticText[@value='Okay / Cancel']";
    PAGE_ACTIONSHEETS_OTHER_XPATH ="//XCUIElementTypeStaticText[@value='Other']";
    PAGE_ACTIONSHEETS_OKCANCEL_OK_XPATH ="//XCUIElementTypeButton[@name='OK']";
    PAGE_ACTIONSHEETS_OKCANCEL_CANCEL_XPATH ="//XCUIElementTypeButton[@name='Cancel']";
    PAGE_ACTIONSHEETS_DESTRUCTIVECHOICE_XPATH="//XCUIElementTypeButton[@name='Destructive Choice']";
    PAGE_ACTIONSHEETS_SAFECHOICE_XPATH="//XCUIElementTypeButton[@name='Safe Choice']";


    #Alert Views
    PAGE_ALERTVIEWS_SIMPLE_OK_XPATH="//XCUIElementTypeStaticText[@name='OK']";
    PAGE_ALERTVIEWS_OKCANCEL_OK_XPATH="//XCUIElementTypeButton[@name='OK']";
    PAGE_ALERTVIEWS_OKCANCEL_CANCEL_XPATH="//XCUIElementTypeButton[@name='Cancel']";
    PAGE_ALERTVIEWS_OTHER_CHOICEONE_XPATH="//XCUIElementTypeButton[@name='Choice One']";
    PAGE_ALERTVIEWS_OTHER_CHOICTWO_XPATH="//XCUIElementTypeButton[@name='Choice Two']";
    PAGE_ALERTVIEWS_OTHER_CANCEL_XPATH="//XCUIElementTypeButton[@name='Cancel']";
    PAGE_ALERTVIEWS_TEXTENTRY_FIELD_XPATH="//XCUIElementTypeAlert[@name='A Short Title Is Best']/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField";
    PAGE_ALERTVIEWS_TEXTENTRY_OK_XPATH="//XCUIElementTypeButton[@name='OK']";
    PAGE_ALERTVIEWS_TEXTENTRY_CANCEL_XPATH="//XCUIElementTypeButton[@name='Cancel']";
    PAGE_ALERTVIEWS_SECURETEXTENTRY_FIELD_XPATH="//XCUIElementTypeAlert[@name='A Short Title Is Best']/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther";
    PAGE_ALERTVIEWS_SECURETEXTENTRY_OK_XPATH="//XCUIElementTypeButton[@name='OK']";
    PAGE_ALERTVIEWS_SECURETEXTENTRY_CANCEL_XPATH="//XCUIElementTypeButton[@name='Cancel']";
    PAGE_ALERTVIEWS_TEXTENTRY_XPATH="//XCUIElementTypeStaticText[@name='Text Entry']";

    PAGE_SEGMENTEDCONTROLS_TINTED_CHECK_XPATH = "(//XCUIElementTypeButton[@name='Check'])[2]";
    PAGE_SEGMENTEDCONTROLS_TINTED_SEARCH_XPATH = "(//XCUIElementTypeButton[@name='Search'])[2]";
    PAGE_SEGMENTEDCONTROLS_TINTED_TOOLS_XPATH = "(//XCUIElementTypeButton[@name='Tools'])[2]";

    PAGE_SLIDERVIEW_DEFAULT_SLIDER_XPATH = "//XCUIElementTypeSlider"
    PAGE_SLIDERVIEW_TINTED_SLIDER_XPATH = "(//XCUIElementTypeSlider)[2]"
    PAGE_SLIDERVIEW_CUSTOM_SLIDER_XPATH = "(//XCUIElementTypeSlider)[3]"


    PAGE_DATEPICKER_DAY_XPATH = "//XCUIElementTypePickerWheel";
    PAGE_DATEPICKER_HOUR_XPATH = "//XCUIElementTypePickerWheel[2]";
    PAGE_DATEPICKER_MINUTE_XPATH = "//XCUIElementTypePickerWheel[3]";
    PAGE_DATEPICKER_AMPM_XPATH = "//XCUIElementTypePickerWheel[4]";




    OK ="OK";
    CANCEL ="CANCEL";
    PAGE_ALERTVIEWS_OTHER_XPATH="//XCUIElementTypeStaticText[@name='Other']";













    def __init__(self):
        print ("loading LOCELEMENT");


