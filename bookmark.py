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
    SALESFORCE = 'https://tableau.lightning.force.com/lightning/o/Case/list?filterName=00B0d00000787zVEAQ'
    DESKTOP_MAXACT = 'https://alpo/#/views/FNOLicenseInformation_0/FNOLicenseInfo-DesktopMaxActivation?:iid=1'
    OKTA = 'https://tableau.okta.com/app/UserHome'
    WEBEX = 'https://tableau.webex.com/webappng/sites/tableau/dashboard?siteurl=tableau'
    SPLUNK = 'https://splunk.tsi.lan/'
    DINGO = 'https://dingo.tsi.lan/'
    CHAMELEON = 'https://chameleon.tsi.lan/'
    OT = 'https://app.smartsheet.com/b/form/c92f94a13dad4b849247e41402093dc1?SFConfirm=DrKDXCwjVKLIUI2T8dHZ3Set9--aN9o2'

    def __init__(self, parent):
        super(BookMark, self).__init__(parent)
        self.init_Ui()
        self.setup_events()
        self.show()

    def init_Ui(self):
        self.glay = QGridLayout()
        # Creating Widgets
        self.btn_okta = QPushButton("OKTA")
        self.btn_maxact = QPushButton("Max Activation")
        self.btn_sitepik = QPushButton("Site Picker")
        self.btn_chameleon = QPushButton("Chameleon")
        self.btn_fno = QPushButton("FNO")
        self.btn_aws = QPushButton("AWS")

        # Adding Widgets to Layout
        self.glay.addWidget(self.btn_okta, 0, 0)
        self.glay.addWidget(self.btn_maxact,1,1)
        self.glay.addWidget(self.btn_sitepik, 2, 0)
        self.glay.addWidget(self.btn_chameleon, 3, 0)
        self.glay.addWidget(self.btn_fno, 3, 1)
        self.glay.addWidget(self.btn_aws, 3, 2)

        # Set Layout to the main widget
        self.setLayout(self.glay)

    def setup_events(self):
        self.btn_okta.clicked.connect(lambda : self.open_link(self.okta))
        self.btn_maxact.clicked.connect(lambda: self.open_link(self.max_act))
        self.btn_sitepik.clicked.connect(lambda: self.open_link(self.site_pick))
        self.btn_chameleon.clicked.connect(lambda: self.open_link(self.chameleon))
        self.btn_fno.clicked.connect(lambda: self.open_link(self.FNO))
        self.btn_aws.clicked.connect(lambda: self.open_link(self.AWS_SSO))

    def open_link(self, link):
        print(link)
        url = QUrl(link)
        if not QDesktopServices.openUrl(url):
            QMessageBox.warning(self, 'Open Url', 'Could not open url')