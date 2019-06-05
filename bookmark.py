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

        # Adding Widgets to Layout
        self.glay.addWidget(self.btn_okta, 0, 0)
        self.glay.addWidget(self.btn_maxact,1,1)
        self.glay.addWidget(self.btn_sitepik, 2, 0)
        self.glay.addWidget(self.btn_chameleon, 3, 0)

        
        # Set Layout to the main widget
        self.setLayout(self.glay)

    def setup_events(self):
        self.btn_okta.clicked.connect(lambda : self.open_link(self.okta))
        self.btn_maxact.clicked.connect(lambda: self.open_link(self.max_act))
        self.btn_sitepik.clicked.connect(lambda: self.open_link(self.site_pick))
        self.btn_chameleon.clicked.connect(lambda: self.open_link(self.chameleon))

    def open_link(self, link):
        print(link)
        url = QUrl(link)
        if not QDesktopServices.openUrl(url):
            QMessageBox.warning(self, 'Open Url', 'Could not open url')