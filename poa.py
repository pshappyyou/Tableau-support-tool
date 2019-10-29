import sys
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import poa_model

stylesheet = "QLabel{color: green}"

class PlanOfAction(QWidget):
    def __init__(self, parent):
        super(PlanOfAction, self).__init__(parent)
        self.parent = parent
        self.eg = poa_model.dic
        self.init_Ui()
        self.set_events()
        self.show()
    
    def init_Ui(self):
        self.vlay = QVBoxLayout()
        
        ### Top
        self.gbox_top = QGroupBox("Comment")
        self.vlay_top = QVBoxLayout()
        # Top two sub-layout
        self.glay_top = QGridLayout()
        self.hlay_btn = QHBoxLayout()
        # Top Button part Components
        self.btn_clip = QPushButton("Copy to Clipboard")
        self.btn_copy = QPushButton("Copy to POA")
        self.btn_clear = QPushButton("Clear All")
        self.hlay_btn.addWidget(self.btn_clip)
        self.hlay_btn.addWidget(self.btn_copy)
        self.hlay_btn.addWidget(self.btn_clear)
        # Top two layout into one vlay
        self.vlay_top.addLayout(self.glay_top)
        self.vlay_top.addLayout(self.hlay_btn)
        
        ### Bottom
        self.gbox_bottom = QGroupBox("POA")
        self.glay_bottom = QGridLayout()
        
        # Top Contents Part Components
        self.lb_passto = QLabel("PASS TO")
        self.cbox_passto = QComboBox()
        self.cbox_passto.addItems(("APAC", "EMEA", "USCA"))
        self.cbox_passto.setMaximumWidth(100)
        self.lb_reason = QLabel("REASON")
        self.tbox_reason = QPlainTextEdit()
        # self.tbox_reason.setMaximumHeight(50)
        self.lb_reason_ex = QLabel(self.eg['Reason'])
        self.lb_reason_ex.setStyleSheet(stylesheet)
        # self.lb_reason_ex.setMaximumWidth(10)
        self.lb_issue = QLabel("ISSUE")
        self.tbox_issue = QPlainTextEdit()
        # self.tbox_issue.setMaximumHeight(50)
        self.lb_issue_ex = QLabel(self.eg['Issue'])
        self.lb_issue_ex.setStyleSheet(stylesheet)
        self.lb_steps = QLabel("STEPS TRIED")
        self.tbox_steps = QPlainTextEdit()
        # self.tbox_steps.setMaximumHeight(50)
        self.lb_steps_ex = QLabel(self.eg['StepsTried'])
        self.lb_steps_ex.setStyleSheet(stylesheet)
        self.lb_next = QLabel("NEXT STEPS")
        self.tbox_next = QPlainTextEdit()
        # self.tbox_next.setMaximumHeight(50)
        self.lb_next_ex = QLabel(self.eg['NextSteps'])
        self.lb_next_ex.setStyleSheet(stylesheet)
        self.lb_contact = QLabel("NEXT CUSTOMER CONTACT")
        self.tbox_contact = QLineEdit()
        # self.tbox_contact.setMaximumHeight(50)
        self.lb_contact_ex = QLabel(self.eg['NextCustomerContact'])
        self.lb_contact_ex.setStyleSheet(stylesheet)
        # Set Top Gbox
        # self.glay_top.addWidget(self.tbox, 0,0)
        self.glay_top.addWidget(self.lb_passto, 0,0)
        self.glay_top.addWidget(self.cbox_passto, 0,1)
        self.glay_top.addWidget(self.lb_reason, 1,0)
        self.glay_top.addWidget(self.tbox_reason, 1,1)
        self.glay_top.addWidget(self.lb_reason_ex, 2,1)
        self.glay_top.addWidget(self.lb_issue, 3,0)
        self.glay_top.addWidget(self.tbox_issue, 3,1)
        self.glay_top.addWidget(self.lb_issue_ex, 4,1)
        self.glay_top.addWidget(self.lb_steps, 5,0)
        self.glay_top.addWidget(self.tbox_steps, 5,1)
        self.glay_top.addWidget(self.lb_steps_ex, 6,1)
        self.glay_top.addWidget(self.lb_next, 7,0)
        self.glay_top.addWidget(self.tbox_next, 7,1)
        self.glay_top.addWidget(self.lb_next_ex, 8,1)
        self.glay_top.addWidget(self.lb_contact, 9,0)
        self.glay_top.addWidget(self.tbox_contact, 9,1)
        self.glay_top.addWidget(self.lb_contact_ex, 10,1)
        
        ## Bottom Component
        self.lb_poa_status = QLabel('Status')
        self.tbox_poa_status = QPlainTextEdit()
        # self.tbox_poa_status.setMaximumHeight(50)
        self.btn_poa_status = QPushButton("Copy to Clipboard")
        self.lb_poa_next = QLabel('Next Steps')
        self.tbox_poa_next = QPlainTextEdit()
        # self.tbox_poa_next.setMaximumHeight(50)
        self.btn_poa_next = QPushButton("Copy to Clipboard")
        self.lb_poa_contact = QLabel('Next Contact')
        self.tbox_poa_contact = QPlainTextEdit()
        # self.tbox_poa_contact.setMaximumHeight(50)
        self.btn_poa_contact = QPushButton("Copy to Clipboard")
        
        # Set Bottom Gbox
        self.glay_bottom.addWidget(self.lb_poa_status, 0,0)
        self.glay_bottom.addWidget(self.tbox_poa_status, 0,1)
        self.glay_bottom.addWidget(self.btn_poa_status, 0,2)
        self.glay_bottom.addWidget(self.lb_poa_next, 1,0)
        self.glay_bottom.addWidget(self.tbox_poa_next, 1,1)
        self.glay_bottom.addWidget(self.btn_poa_next, 1,2)
        self.glay_bottom.addWidget(self.lb_poa_contact, 2,0)
        self.glay_bottom.addWidget(self.tbox_poa_contact, 2,1)
        self.glay_bottom.addWidget(self.btn_poa_contact, 2,2)
        
        # Set Gbox layout
        self.gbox_top.setLayout(self.vlay_top)
        self.gbox_bottom.setLayout(self.glay_bottom)
        
        # Set Main layout
        self.vlay.addWidget(self.gbox_top)
        self.vlay.addWidget(self.gbox_bottom)
        self.setLayout(self.vlay)
    
    def set_events(self):
        self.btn_clip.clicked.connect(lambda: self.copy_to_clipboard("btn_clip"))
        self.btn_copy.clicked.connect(self.copy_to_poa)
        self.btn_clear.clicked.connect(self.clear_all)
        self.btn_poa_contact.clicked.connect(lambda: self.copy_to_clipboard("btn_poa_contact"))
        self.btn_poa_next.clicked.connect(lambda: self.copy_to_clipboard("btn_poa_next"))
        self.btn_poa_status.clicked.connect(lambda: self.copy_to_clipboard("btn_poa_status"))
        
    def copy_to_poa(self):
        contact = self.tbox_contact.text()
        reason = self.tbox_reason.toPlainText()
        steps = self.tbox_steps.toPlainText()
        issue = self.tbox_issue.toPlainText()
        next = self.tbox_next.toPlainText()
        passto = self.cbox_passto.currentText()
        poa_status = "Hand off to {passto} because {reason}".format(passto=passto, reason=reason)
        poa_next = next
        poa_contact = contact
        self.tbox_poa_status.clear()
        self.tbox_poa_status.insertPlainText(poa_status)
        self.tbox_poa_next.clear()
        self.tbox_poa_next.insertPlainText(poa_next)
        self.tbox_poa_contact.clear()
        self.tbox_poa_contact.insertPlainText(poa_contact)

    def copy_to_clipboard(self, button=None):
        text = ''
        if button == 'btn_clip':
            text = self.get_text()
        elif button == 'btn_poa_status':
            text = self.tbox_poa_status.toPlainText()
        elif button == 'btn_poa_next':
            text = self.tbox_poa_next.toPlainText()
        elif button == 'btn_poa_contact':
            text = self.tbox_poa_contact.toPlainText()
        
        if sys.platform == 'win32' or sys.platform == 'cygwin':
            subprocess.Popen(['clip'], errors="ignore", stdin=subprocess.PIPE).communicate(text)
            self.parent.statusMiddle.setText(button + ": copied to clipboard")
        else:
            raise Exception('Platform not supported')
        
    def get_text(self):
        contact = self.tbox_contact.text()
        reason = self.tbox_reason.toPlainText()
        steps = self.tbox_steps.toPlainText()
        issue = self.tbox_issue.toPlainText()
        next = self.tbox_next.toPlainText()
        passto = self.cbox_passto.currentText()
        text = "PASS TO: {passto}\n\n" \
               "REASON: {reason}\n\n" \
               "ISSUE: {issue}\n\n" \
                "STEPS TRIED: {steps}\n\n" \
                "NEXT STEPS: {next}\n\n" \
                "NEXT CUSTOMER CONTACT: {contact}".format(passto=passto, issue=issue, reason=reason, steps=steps, next=next, contact=contact)
        return text

    def clear_all(self):
        self.tbox_reason.clear()
        self.tbox_issue.clear()
        self.tbox_steps.clear()
        self.tbox_next.clear()
        self.tbox_contact.clear()
        self.tbox_poa_status.clear()
        self.tbox_poa_next.clear()
        self.tbox_poa_contact.clear()
