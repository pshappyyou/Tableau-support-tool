# coding=utf8
import os
import sys
import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import timezone as tz
import sf
import cannedcomment as cc
import dashboard as db
import model
import bookmark as bm
import poa


StyleSheet = """
    QTabWidget::pane {
        border-top: 2px solid #C2C7CB;}
    QTabWidget::tab-bar {
        left: 5px;}
    QTabBar::tab {
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E1E1E1, stop: 0.4 #DDDDDD, stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
        border: 2px solid #C4C4C3;
        border-bottom-color: #C2C7CB;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
        min-width: 8ex;
        padding: 2px;}
    QTabBar::tab:selected, QTabBar::tab:hover {
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fafafa, stop: 0.4 #f4f4f4, stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);}
    QTabBar::tab:selected {
        border-color: #9B9B9B;
        border-bottom-color: #C2C7CB;}
    QTabBar::tab:!selected {
        margin-top: 2px;}
    QStatusBar{
        background:lightgrey;
        font-weight:bold;}
    QPlainTextEdit {
        background-color: #333;
        color: #00FF00;
        text-decoration: ;
        font-size: 20px;
        font-family: Courier;}
"""

# Main Windows
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.model = model.MainModel()
        self.model.load_config()
        self.init_Ui()

    def init_Ui(self):
        self.setWindowTitle('Support Support Tool')
        self.setGeometry(0, 0, 1400, 900)
        self.move_to_center()

        # Adding Status Bar
        self.statusLeft = QLabel("Left")
        self.statusLeft.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.statusMiddle = QLabel("Middle")
        self.statusMiddle.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.statusRight = QLabel("Right")
        self.statusRight.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Started')
        self.statusbar.setStyleSheet(StyleSheet)
        self.statusbar.addPermanentWidget(self.statusLeft, 2)
        self.statusbar.addPermanentWidget(self.statusMiddle, 2)
        self.statusbar.addPermanentWidget(self.statusRight, 1)

        # Adding menu
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        # Adding main tab widget
        self.tab_widget = MainTabWidget(self) # important to give self!
        self.setCentralWidget(self.tab_widget)
        self.show()

    def move_to_center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

# Main Tab Widget
class MainTabWidget(QWidget):
    def __init__(self, parent):
        super(MainTabWidget, self).__init__(parent)
        self.parent = parent
        self.init_Ui()

    def init_Ui(self):
        self.layout = QVBoxLayout()
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab_tz = tz.TimeZone(self.parent)
        self.tab_sf = sf.MySalesForce(self.parent)
        self.tab_cc = cc.CannedComment(self.parent)
        self.tab_db = db.Dashboard(self.parent)
        self.tab_bm = bm.BookMark(self.parent)
        self.tab_poa = poa.PlanOfAction(self.parent)

        # Add tabs
        self.tabs.addTab(self.tab_db, "Dashboard")
        self.tabs.addTab(self.tab_cc, "CannedComments")
        self.tabs.addTab(self.tab_bm, "Bookmarks")
        self.tabs.addTab(self.tab_tz, "Timezone")
        self.tabs.addTab(self.tab_poa, "POA")
        self.tabs.addTab(self.tab_sf, "SalesForce")
        
        self.notepad = QPlainTextEdit()
        self.notepad.setStyleSheet(StyleSheet)
        self.tabs.addTab(self.notepad, "Notepad")

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
    def add_tab(self, tabs, tab_title, widget=None):
        new_tab = QWidget()
        tabs.addTab(new_tab, tab_title)
        new_tab.layout = QVBoxLayout()
        if widget != None:
            new_tab.layout.addWidget(widget)
        new_tab.setLayout(new_tab.layout)
    
if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_UseOpenGLES) # very import to close QtWebEngineProcess to terminate properly.
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    myStyle = QProxyStyle("Fusion")
    app.setStyle(myStyle)
    ex = App()
    sys.exit(app.exec_())
