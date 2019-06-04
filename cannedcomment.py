# coding=utf8
import sys
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import canned_model2

class CannedComment(QWidget):

    def __init__(self, parent):
        super(CannedComment, self).__init__(parent)
        self.parent = parent
        self.dic = canned_model2.canned_dic
        self.init_Ui()

    def init_Ui(self):
        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()

        for language in self.dic:
            sub_tabs = QTabWidget()
            sub_tabs.setTabBar(MyTabBar(width=100, height=25))
            sub_tabs.setTabPosition(QTabWidget.West)
            # First Level Tabs
            self.add_tab(self.tabs, language, sub_tabs)
            
            for comment in self.dic[language]:
                text = self.dic[language][comment]
                sub_tab_widget = QWidget()
                sub_tab_layout = QVBoxLayout()
                btn_copy = QPushButton('Copy')
                txt_edit = QTextEdit()
                txt_edit.insertPlainText(text)
                # txt_edit.insertHtml(text)
                sub_tab_layout.addWidget(btn_copy)
                sub_tab_layout.addWidget(txt_edit)
                sub_tab_widget.setLayout(sub_tab_layout)
                btn_copy.clicked.connect(lambda test='test', title=comment, text=text: self.copy_to_clipboard(title, text))
                # Second Level (Sub) Tabs
                self.add_tab(sub_tabs, comment, sub_tab_widget)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def add_tab(self, tabs, tab_title, widget=None):
        new_tab = QWidget()
        tabs.addTab(new_tab, tab_title)
        if widget != None:
            tab_widget = widget
        else:
            tab_widget = QWidget()
        new_tab.layout = QVBoxLayout()
        new_tab.layout.addWidget(tab_widget)
        new_tab.setLayout(new_tab.layout)
    
    def copy_to_clipboard(self, title=None, text=None):
        if sys.platform == 'win32' or sys.platform == 'cygwin':
            # subprocess.Popen(['clip'], encoding='utf-8', errors="ignore", stdin=subprocess.PIPE).communicate(text)
            subprocess.Popen(['clip'], errors="ignore", stdin=subprocess.PIPE).communicate(text)
            self.parent.statusMiddle.setText(title + ": copied to clipboard")
        else:
            raise Exception('Platform not supported')

class MyTabBar(QTabBar):
    def __init__(self, *args, **kwargs):
        self.tabSize = QSize(kwargs.pop('width'), kwargs.pop('height'))
        super(MyTabBar, self).__init__(*args, **kwargs)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QStylePainter(self)
        option = QStyleOptionTab()

        for index in range(self.count()):
            self.initStyleOption(option, index)
            tabRect = self.tabRect(index)
            tabRect.moveLeft(10)
            painter.drawControl(QStyle.CE_TabBarTabShape, option)
            painter.drawText(tabRect, Qt.AlignVCenter | Qt.TextDontClip, self.tabText(index))

    def tabSizeHint(self, index: int) -> QSize:
        return self.tabSize
