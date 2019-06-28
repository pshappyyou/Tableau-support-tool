import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# import PyQt5.QtWebEngineWidgets
# from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage


class Dashboard(QWidget):

    okta =          'https://tableau.okta.com/app/UserHome?fromLogin=true'
    okta2 =         'https://tableau.okta.com/app/UserHome'
    max_act =       'https://alpo/#/views/FNOLicenseInformation_0/FNOLicenseInfo-DesktopMaxActivation?:iid=1'
    site_pick =     'https://alpo/#/views/SiteLookup/SitePicker'
    site_pick_emb = 'https://alpo/views/SiteLookup/SitePicker?iframeSizedToWindow=true&:embed=y&:showAppBanner=false&:display_count=no&:showVizHome=no&:origin=viz_share_link'
    onlyme =        'https://alpo/#/views/APACWeightedAdjustedMetrics/OnlyMe?:iid=1'
    onlyme_emb =    'https://alpo/views/APACWeightedAdjustedMetrics/OnlyMe?iframeSizedToWindow=true&:embed=y&:showAppBanner=false&:display_count=no&:showVizHome=no&:origin=viz_share_link'
    case_q_emb =    'https://alpo/views/SupportCaseQueue/Tier1TechQueue?iframeSizedToWindow=true&:embed=y&:showAppBanner=false&:display_count=no&:showVizHome=no&:origin=viz_share_link'
    mytube =        'https://www.youtube.com/'
    dash =          'https://alpo/#/views/Tier1TechDash/Tier1TechQueue'
    dash1 =         'https://alpo/#/signin?redirect=%2Fviews%2FTier1TechDash%2FTier1TechQueue&error=43&disableAutoSignin=false'
    cat =           'http://ndc1tsvwsupdb01.tsi.lan:9001/'
    steve =         'https://alpo/#/views/TechSupportIndividualQueueDashboard/TechSupportIndividualQueueDashboard?:iid=1'
    xen_lab =       'http://10.70.128.10/#/home?s=power_state%3Arunning+'
    ohelp =         'https://www.tableau.com/support/help'
    db =            "https://alpo/views/DevTestingDatabaseInfoandStatus_0/ConnectionInformation?:embed=y&:jsdebug=y&:display_count=no&:showVizHome=no&:origin=viz_share_link"
    slack =         "https://tableau.slack.com/messages"
    aws =           "https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#Instances:search=jack-test;sort=tag:Name"
    aws =           "https://tableau.okta.com/app/amazon_aws/exk99s5jvkwcMJttP356/sso/saml"
    aws =           "https://tableau.okta.com/app/amazon_aws/"
    # aws =           "https://signin.aws.amazon.com/saml"
    coveo =         "https://tableau--c.na61.visual.force.com/apex/SupportFullSearch#t=Core&sort=relevancy"

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        QWebEngineProfile.defaultProfile().setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)
        self.init_Ui()
        self.show()

    def init_Ui(self):
        self.layout = QVBoxLayout()
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.remove_web_tab)
        self.tabs.acceptDrops()

        # Create tabs
        # self.add_web_tab(self.tabs, "OKTA", self.okta2)
        self.add_web_tab(self.tabs, "Case Q", self.case_q_emb)
        self.add_web_tab(self.tabs, "Milestone", self.steve)
        self.add_web_tab(self.tabs, "KPI", self.onlyme_emb)
        # self.add_web_tab(self.tabs, "Cat", self.cat)
        self.add_web_tab(self.tabs, "Site Picker", self.site_pick_emb)
        self.add_web_tab(self.tabs, "Database List", self.db)
        self.add_web_tab(self.tabs, "Sydney Lab", self.xen_lab)
        # self.add_web_tab(self.tabs, "OnlineHelp", self.ohelp)
        self.add_web_tab(self.tabs, "Coveo", self.coveo)
        self.add_web_tab(self.tabs, "Slack", self.slack)
        self.add_web_tab(self.tabs, "YouTube", self.mytube)
        # self.add_web_tab(self.tabs, "AWS", self.aws)


        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def add_web_tab(self, tabs, tab_title, url):
        new_tab = QWidget()
        tabs.addTab(new_tab, tab_title)
        new_tab.layout = QVBoxLayout()
        web_view = QWebEngineView(self)
        web_view.load(QUrl(url))
        # web_view.page().profile().setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)
        new_tab.layout.addWidget(web_view)
        new_tab.setLayout(new_tab.layout)

    def remove_web_tab(self, index):
        print(index)
        self.tabs.removeTab(index)