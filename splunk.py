from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage


class Splunk(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        # QWebEngineProfile.defaultProfile().setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)
        self.init_Ui()
        self.set_events()
        self.show()

    def init_Ui(self):
        self.glay = QGridLayout()

        self.lb_index = QLabel("Index")
        self.cbox_index = QComboBox()
        self.cbox_index.addItems(("prod-public-uw2", "prod-online-10az-linux", "prod-online-10ay-linux",
                                  "prod-online-us-east-1", "prod-online-useast-a", "prod-online-us-west-2a",
                                  "prod-online-us-west-2b", "prod-online-10ax-v1", "prod-online-dub01",
                                  "prod-online-eu-west-1a", "prod-online*", "prod-online-shared-aws",
                                  "sandbox-dev-qa-near"))

        self.lb_proc = QLabel("Process")
        self.cbox_proc = QComboBox()
        self.cbox_proc.addItems(("Access/HTTPD", "Backgrounder", "Remote Agent Server",
                                  "Site SAML", "Tableau Protocol Server", "VizPortal",
                                  "VizQLServer"))

        self.lb_srctype = QLabel("Source Type")
        self.cbox_srctype = QComboBox()
        self.cbox_srctype.addItems(("tas:gateway:apache:access",""))

        self.lb_sitename = QLabel("Site Name or URL")
        self.tbox_sitename = QLineEdit()
        self.btn_submit = QPushButton("Generate")

        self.lb_query = QLabel("Search Query")
        self.tbox_query = QPlainTextEdit()
        self.tbox_query.setMaximumHeight(50)


        self.glay.addWidget(self.lb_index, 0,0)
        self.glay.addWidget(self.cbox_index, 0, 1)
        self.glay.addWidget(self.lb_sitename, 1, 0)
        self.glay.addWidget(self.tbox_sitename, 1, 1)
        self.glay.addWidget(self.lb_proc, 2, 0)
        self.glay.addWidget(self.cbox_proc, 2, 1)
        self.glay.addWidget(self.lb_srctype, 3, 0)
        self.glay.addWidget(self.cbox_srctype, 3, 1)
        self.glay.addWidget(self.btn_submit, 4, 0)
        self.glay.addWidget(self.lb_query, 5, 0)
        self.glay.addWidget(self.cbox_srctype, 6, 0)


        self.setLayout(self.glay)

    def set_events(self):
        self.cbox_proc.currentTextChanged.connect(self.set_src_type)
        # self.btn_copy.clicked.connect(self.copy_to_poa)
        # self.btn_clear.clicked.connect(self.clear_all)
        # self.btn_poa_contact.clicked.connect(lambda: self.copy_to_clipboard("btn_poa_contact"))
        # self.btn_poa_next.clicked.connect(lambda: self.copy_to_clipboard("btn_poa_next"))
        # self.btn_poa_status.clicked.connect(lambda: self.copy_to_clipboard("btn_poa_status"))

    def set_src_type(self):
        proc = self.cbox_proc.currentText()
        print(proc)
        # self.cbox_srctype.addItem(("A","B","C"))
        if proc == "Backgrounder":
            self.cbox_srctype.clear()
            self.cbox_srctype.addItems(("tas:backgrounder:log", "tas:backgrounder:cpp", "tas:backgrounder:protosrv"))
        elif proc == "Access/HTTPD":
            self.cbox_srctype.clear()
            self.cbox_srctype.addItems(("tas:gateway:apache:access", ""))
        elif proc == "Remote Agent Server":
            self.cbox_srctype.clear()
            self.cbox_srctype.addItems(("tas:remoteagentserver:log", "tas:remoteagentserver:access"))
        elif proc == "Site SAML":
            self.cbox_srctype.clear()
            self.cbox_srctype.addItems(("lambda:sso-sitesaml-aws-dev_cloudwatch_to_splunk", ""))
        elif proc == "Access/HTTPD":
            self.cbox_srctype.clear()
            self.cbox_srctype.addItems(("tas:gateway:apache:access", ""))
        elif proc == "Tableau Protocol Server":
            self.cbox_srctype.clear()
            self.cbox_srctype.addItems(("tas:backgrounder:protosrv", "tas:vizqlserver:protosrv","tas:vizportal:protosrv","tas:dataserver:protosrv"))
        elif proc == "Access/HTTPD":
            self.cbox_srctype.clear()
            self.cbox_srctype.addItems(("tas:gateway:apache:access", ""))
        elif proc == "VizPortal":
            self.cbox_srctype.clear()
            self.cbox_srctype.addItems(("tas:vizportal:log", "tas:vizportal:cpp","tas:vizportal:protosrv"))
        elif proc == "VizQLServer":
            self.cbox_srctype.clear()
            self.cbox_srctype.addItems(("tas:vizqlserver:cpp", "tas:vizqlserver:log","tas:vizqlserver:protosrv"))
