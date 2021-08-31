from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage


class Dashboard(QWidget):
    perform =       'https://alpo/#/views/APACTechSupportIndividualPerformance/IndividualPerformance?:iid=1'
    # okta =          'https://tableau.okta.com/app/UserHome?fromLogin=true'
    # okta2 =         'https://tableau.okta.com/app/UserHome'
    max_act =       'https://alpo/#/views/FNOLicenseInformation_0/FNOLicenseInfo-DesktopMaxActivation?:iid=1'
    site_pick =     'https://alpo/#/views/SiteLookup/SitePicker'
    site_pick_emb = 'https://alpo/views/SiteLookup/SitePicker?iframeSizedToWindow=true&:embed=y&:showAppBanner=false&:display_count=no&:showVizHome=no&:origin=viz_share_link'
    # matrix =        'https://alpo/#/views/APACWeightedAdjustedMetrics/MetricHeatmap'
    # matrix =        'https://alpo/#/views/TechSupportProductivityDashboardG3/APACKPIG3'
    matrix = 'https://alpo.tsi.lan/#/views/SupportAPJProductivityG4/APJTSProductivity'
    # onlyme_emb =    'https://alpo/views/APACWeightedAdjustedMetrics/OnlyMe?iframeSizedToWindow=true&:embed=y&:showAppBanner=false&:display_count=no&:showVizHome=no&:origin=viz_share_link'
    # case_q =        'https://alpo/#/views/Tier1TechDash/Tier1TechQueue'
    # case_q_emb =    'https://alpo/views/SupportCaseQueue/Tier1TechQueue?iframeSizedToWindow=true&:embed=y&:showAppBanner=false&:display_count=no&:showVizHome=no&:origin=viz_share_link'
    # mytube =        'https://www.youtube.com/'
    # dash =          'https://alpo/#/views/Tier1TechDash/Tier1TechQueue'
    # dash1 =         'https://alpo/#/signin?redirect=%2Fviews%2FTier1TechDash%2FTier1TechQueue&error=43&disableAutoSignin=false'
    # cockpit =       'http://ndc1tsvwsupdb01.tsi.lan:9001/Cockpit'
    # steve =         'https://alpo/#/views/TechSupportIndividualQueueDashboard/TechSupportIndividualQueueDashboard?:iid=1'
    # xen_lab =       'http://10.70.128.10/#/home?s=power_state%3Arunning+'
    # ohelp =         'https://www.tableau.com/support/help'
    db =            "https://alpo/views/DevTestingDatabaseInfoandStatus_0/ConnectionInformation?:embed=y&:jsdebug=y&:display_count=no&:showVizHome=no&:origin=viz_share_link"
    # slack =         "https://tableau.slack.com/messages"
    # aws =           "https://signin.aws.amazon.com/saml"
    # aws =           "https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#Instances:search=jack-test;sort=tag:Name"
    # aws =           "https://tableau.okta.com/app/amazon_aws/exk99s5jvkwcMJttP356/sso/saml"
    # aws =           "https://tableau.okta.com/app/amazon_aws/"
    # coveo =         "https://tableau--c.na61.visual.force.com/apex/SupportFullSearch#t=Core&sort=relevancy"
    FNO =           'https://tableau--c.na61.visual.force.com/apex/FNOBrowser'
    my_survey =     'https://alpo/#/views/MySupportCaseClosedSurveyssatis/MySurveys?:iid=1'
    # test =          '<h1>Hello World</h1>'
    # apac_q =        'https://alpo/#/views/APACQueueStatus/APACQueueStatus'
    # apac_q =        'https://alpo/views/APACQueueStatus/APACQueueStatus?:showAppBanner=false&:display_count=n&:showVizHome=n&:origin=viz_share_link'
    call =          'https://alpo.tsi.lan/#/views/APACTechSupportCallAttainment_15895220624760/TechSupportCallAttainment'
    # sop =           'https://alpo/#/views/SOPUsage/UsagebyTechnician'
    out_of_q =      'https://alpo/#/views/APACTechSupportAvailabilityCalendar/APACTSOutofQueueV2'
    pto_lookup =    'https://alpo/#/views/APACTechSupportAvailabilityCalendar/APACTSPTOCalendarLookUp'
    dingo =         'https://dingo.tsi.lan/'
    case_age =      'https://alpo/#/views/APAC-CaseStatus/CaseAge'
    age_xlsx =      'https://tableau.sharepoint.com/:x:/r/sites/APACTechSupport/_layouts/15/Doc.aspx?sourcedoc=%7BDAAA6273-507E-45D8-883A-2D76CF464C0E%7D&file=Old-Cases-Master.xlsx&action=default&mobileredirect=true'
    logshark =      'https://logshark.tsi.lan/'
    crashshark =    'https://crashshark.tsi.lan/'
    subcat =        'https://alpo/#/views/subcategoryreporting/TechnicianSubcategoryDash'
    ttr =           'https://alpo/#/views/APAC-AgedCases/IndividualsAlerts'
    realtime =      'https://tableau.sharepoint.com/sites/APACTechSupport/Shared%20Documents/APACTechSupRealTimeDashboard.xlsx?web=1'

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        QWebEngineProfile.defaultProfile().setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)
        self.init_Ui()
        self.show()

    def init_Ui(self):
        # Initialize tab screen
        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()
        # self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.remove_web_tab)
        self.tabs.acceptDrops()

        # Create tabs
        # Que Management
        # self.add_web_tab(self.tabs, "Cockpit", self.cockpit)
        self.add_web_tab(self.tabs, "RealTime", self.realtime)
        self.add_web_tab(self.tabs, "Case Age", self.case_age)
        ## Self Queue & KPI Management
        # self.add_web_tab(self.tabs, "Milestone", self.steve)
        # self.add_web_tab(self.tabs, "TTR", self.ttr)
        self.add_web_tab(self.tabs, "KPI", self.matrix)
        self.add_web_tab(self.tabs, "Perform", self.perform)
        self.add_web_tab(self.tabs, "My Survey", self.my_survey)
        self.add_web_tab(self.tabs, "Call Att", self.call)
        self.add_web_tab(self.tabs, "Sub-Category", self.subcat)
        # self.add_web_tab(self.tabs, "SOP", self.sop)
        # Utilities
        self.add_web_tab(self.tabs, "Site Picker", self.site_pick_emb)
        self.add_web_tab(self.tabs, "Database List", self.db)
        self.add_web_tab(self.tabs, "FNO Info", self.max_act)
        self.add_web_tab(self.tabs, "FNO Browser", self.FNO)
        # self.add_web_tab(self.tabs, "Sydney Lab", self.xen_lab)
        self.add_web_tab(self.tabs, "Dingo", self.dingo)
        self.add_web_tab(self.tabs, "Log Shark", self.logshark)
        self.add_web_tab(self.tabs, "Crash Shark", self.crashshark)
        # self.add_web_tab(self.tabs, "Esxi", self.esxi)
        # Admin
        self.add_web_tab(self.tabs, "Out Q", self.out_of_q)
        # self.add_web_tab(self.tabs, "PTO Lookup", self.pto_lookup)
        # ETC
        #self.add_web_tab(self.tabs, "YouTube", self.mytube)
        # self.add_web_tab(self.tabs, "AWS", self.aws)
        # self.add_web_tab(self.tabs, "OKTA", self.okta2)
        # self.add_web_tab(self.tabs, "OnlineHelp", self.ohelp)
        # self.add_web_tab(self.tabs, "Coveo", self.coveo)
        # self.add_web_tab(self.tabs, "Slack", self.slack)

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

        # lb_link = QLabel()
        # lb_link.setText("<a href='"+url+"'>Open in Browser</a>")
        # lb_link.setOpenExternalLinks(True)
        # new_tab.layout.addWidget(lb_link)

        new_tab.setLayout(new_tab.layout)

    def remove_web_tab(self, index):
        self.tabs.removeTab(index)