from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class BookMark(QWidget):
    # Test
    okta = 'https://tableau.okta.com/app/UserHome?fromLogin=true'
    max_act = 'https://alpo/#/views/FNOLicenseInformation_0/FNOLicenseInfo-DesktopMaxActivation?:iid=1'
    site_pick = 'https://alpo/#/views/SiteLookup/SitePicker'
    tfs = ''
    chameleon = 'https://chameleon.tsi.lan/'
    LOGIN = 'https://tableau.my.salesforce.com/home/home.jsp'
    FNO = 'https://tableau--c.na61.visual.force.com/apex/FNOBrowser'
    SITE_PICKER = 'https://alpo/#/views/SiteLookup/SitePicker'
    AWS = 'https://signin.aws.amazon.com'
    AWS_HOME = 'https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#Home:'
    AWS_EC2 = 'https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2'
    AWS_SSO = 'https://tableau.okta.com/home/amazon_aws/0oa99s5jwv5qu9YUA356/272?fromHome=true'
    # AWS_SSO = 'https://us-west-2.console.aws.amazon.com/ec2/home?region=us-west-2#Instances:sort=tag:Name'
    SALESFORCE = 'https://tableau.lightning.force.com/lightning/o/Case/list?filterName=00B0d00000787zVEAQ'
    DESKTOP_MAXACT = 'https://alpo/#/views/FNOLicenseInformation_0/FNOLicenseInfo-DesktopMaxActivation?:iid=1'
    OKTA = 'https://tableau.okta.com/app/UserHome'
    WEBEX = 'https://tableau.webex.com/webappng/sites/tableau/dashboard?siteurl=tableau'
    SPLUNK = 'https://splunk.tsi.lan/'
    DINGO = 'https://dingo.tsi.lan/'
    CHAMELEON = 'https://chameleon.tsi.lan/'
    OT = 'https://app.smartsheet.com/b/form/c92f94a13dad4b849247e41402093dc1?SFConfirm=DrKDXCwjVKLIUI2T8dHZ3Set9--aN9o2'
    OT2 ='https://app.smartsheet.com/b/form/c92f94a13dad4b849247e41402093dc1'
    crash_shark = 'https://crashshark.tsi.lan/'
    log_shark = 'https://logshark.tsi.lan'
    splunk = 'https://splunk.tsi.lan'
    splunk_search_query = 'https://mytableau.tableaucorp.com/pages/viewpage.action?spaceKey=cesupport&title=Splunk+Search+Queries'
    onlinesupport = 'https://help.tableau.com/current/online/en-us/enable_support_access.htm'
    schedules   = "https://mytableau.tableaucorp.com/display/devprodops/Tableau+Release+Schedules+and+Calendar+Tables"
    mobile_ts = 'https://mytableau.tableaucorp.com/display/cesupport/Tableau+Mobile+Troubleshooting+Guide'
    canned = 'https://mytableau.tableaucorp.com/display/cesupport/Canned+Responses'
    support_role_online = 'https://mytableau.tableaucorp.com/pages/viewpage.action?spaceKey=cesupport&title=Support+User+Role+for+Tableau+Online'
    support_service = 'https://www.tableau.com/resources/teams-organizations/premium-support'

    def __init__(self, parent):
        super(BookMark, self).__init__(parent)
        self.init_Ui()
        self.setup_events()
        self.show()

    def init_Ui(self):
        self.vlay = QGridLayout() # Top Level

        # First Groupbox
        self.gbox_okta = QGroupBox("Main")
        self.glay = QGridLayout()
        # Creating Widgets
        self.btn_okta = QPushButton("Tableau OKTA Home")
        # self.btn_maxact = QPushButton("Max Activation")
        # self.btn_sitepik = QPushButton("Site Picker")
        self.btn_chameleon = QPushButton("Chameleon")
        self.btn_logshark = QPushButton("Logshark")
        self.btn_spk = QPushButton("Splunk")
        self.btn_aws = QPushButton("AWS")
        self.btn_aws.setMinimumSize(QSize(50, 50))
        # self.btn_aws.resize(50, 50)
        self.btn_onlinesupport = QPushButton("Tableau Online Support Access")
        self.btn_picker = QPushButton("Site Picker")

        # Adding Widgets to Layout
        self.glay.addWidget(self.btn_okta, 0,0)
        self.glay.addWidget(self.btn_onlinesupport, 0, 1)
        # self.glay.addWidget(self.btn_maxact,0,1)
        # self.glay.addWidget(self.btn_sitepik, 0,2)
        self.glay.addWidget(self.btn_chameleon, 2, 0)
        self.glay.addWidget(self.btn_aws, 2, 1)
        self.glay.addWidget(self.btn_spk, 3, 1)
        self.glay.addWidget(self.btn_picker, 3, 0)
        self.gbox_okta.setLayout(self.glay)

        # Second GroupBox
        self.gbox_server = QGroupBox("Tableau Test Server Env")
        self.glay_server = QGridLayout()
        self.gbox_server.setLayout(self.glay_server)

        self.cbox_apac = QComboBox()
        self.cbox_apac.addItems(("APAC", "APAC2020-4","APAC2021-1","APAC2021-2","APAC2021-3"))
        self.btn_apac_go = QPushButton("Go")
        self.cbox_syd = QComboBox()
        self.cbox_syd.addItems(("Sydney", "Sydney2020-4","Sydney2021-1","Sydney2021-2","Sydney2021-3"))
        self.btn_syd_go = QPushButton("Go")

        self.glay_server.addWidget(self.cbox_apac, 0,0)
        self.glay_server.addWidget(self.btn_apac_go, 0, 1)
        self.glay_server.addWidget(self.cbox_syd, 1, 0)
        self.glay_server.addWidget(self.btn_syd_go, 1, 1)

        self.gbox_admin = QGroupBox("Admin")
        self.glay_admin = QGridLayout()
        self.gbox_admin.setLayout(self.glay_admin)
        self.btn_ot = QPushButton("OT - Smartsheet")
        self.glay_admin.addWidget(self.btn_ot, 0,0)

        self.gbox_wiki = QGroupBox("Wiki")
        self.glay_wiki = QGridLayout()
        self.gbox_wiki.setLayout(self.glay_wiki)
        self.btn_canned = QPushButton("Canned Responses")
        self.btn_schedules = QPushButton("Tableau Release Schedules and Calendar Tables")
        self.btn_splunk_search_query = QPushButton("Splunk Search Query")
        self.btn_mobile_ts = QPushButton("Tableau Mobile TShoot")
        self.btn_support_role_online = QPushButton("Support User Role for Tableau Online")
        self.btn_support_service = QPushButton("Support Services")
        self.glay_wiki.addWidget(self.btn_canned, 0, 0)
        self.glay_wiki.addWidget(self.btn_schedules, 1, 0)
        self.glay_wiki.addWidget(self.btn_splunk_search_query, 2, 0)
        self.glay_wiki.addWidget(self.btn_mobile_ts, 3, 0)
        self.glay_wiki.addWidget(self.btn_support_role_online, 4, 0)
        self.glay_wiki.addWidget(self.btn_support_service, 5, 0)

        # Set Layout to the main widget
        self.vlay.addWidget(self.gbox_okta, 0,0)
        self.vlay.addWidget(self.gbox_server, 0,1)
        self.vlay.addWidget(self.gbox_admin, 1, 0)
        self.vlay.addWidget(self.gbox_wiki, 1, 1)
        self.setLayout(self.vlay)

    def setup_events(self):
        self.btn_okta.clicked.connect(lambda : self.open_link(self.okta))
        # self.btn_maxact.clicked.connect(lambda: self.open_link(self.max_act))
        self.btn_chameleon.clicked.connect(lambda: self.open_link(self.chameleon))
        self.btn_spk.clicked.connect(lambda: self.open_link(self.SPLUNK))
        self.btn_picker.clicked.connect(lambda: self.open_link(self.site_pick))
        self.btn_aws.clicked.connect(lambda: self.open_link(self.AWS_SSO))
        self.btn_apac_go.clicked.connect(lambda :self.open_server_link(self.cbox_apac.currentText()))
        self.btn_syd_go.clicked.connect(lambda : self.open_server_link(self.cbox_syd.currentText()))
        self.btn_ot.clicked.connect(lambda : self.open_link(self.OT))
        self.btn_onlinesupport.clicked.connect(lambda: self.open_link(self.onlinesupport))
        self.btn_schedules.clicked.connect(lambda: self.open_link(self.schedules))
        self.btn_splunk_search_query.clicked.connect(lambda: self.open_link(self.splunk_search_query))
        self.btn_mobile_ts.clicked.connect(lambda: self.open_link(self.mobile_ts))
        self.btn_canned.clicked.connect(lambda: self.open_link(self.canned))
        self.btn_support_role_online.clicked.connect(lambda: self.open_link(self.support_role_online))
        self.btn_support_service.clicked.connect(lambda: self.open_link(self.support_service))

    def open_link(self, link):
        print(link)
        url = QUrl(link)
        if not QDesktopServices.openUrl(url):
            QMessageBox.warning(self, 'Open Url', 'Could not open url')

    def open_server_link(self, param):
        url = QUrl("http://"+param+".tsi.lan")
        if not QDesktopServices.openUrl(url):
            QMessageBox.warning(self, 'Open Url', 'Could not open url')

