import os
import json
import sys
import getpass
import threading
import subprocess
from tkinter import filedialog
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sf_model

class MySalesForce(QWidget):
    sty_qstatusbar = "QStatusBar{padding-left:8px;background:green;color:black;font-weight:bold;}"
    def __init__(self, parent):
        super(MySalesForce, self).__init__(parent)
        self.parent = parent
        self.model = sf_model.SalesForceModel()
        self.api_link = r'<a href="https://tableau.my.salesforce.com/_ui/system/security/ResetApiTokenEdit?retURL=%2Fui%2Fsetup%2FSetup%3Fsetupid%3DPersonalInfo&setupid=ResetApiToken">'
        self.case_count = 0
        self.dont_push = 0
        self.username = getpass.getuser()
        self.download_pathname = os.path.expanduser("~")
        self.init_Ui()
        self.set_events()
        self.load_api_secret()
        self.parent.statusRight.setText("SalesForce module loaded")

    def init_Ui(self):
        # Main Layout
        self.layout = QVBoxLayout()
        # Login GroupBox
        self.gbox_login = QGroupBox("Login")
        self.glay_cred = QGridLayout()
        self.lb_uname = QLabel("User Name*")
        self.le_uname = QLineEdit(self.username)
        self.lb_dname = QLabel("@tableau.com")
        self.lb_api = QLabel("API Key")
        self.le_api = QLineEdit()
        self.btn_save_key = QPushButton("Save API Key")
        self.lb_api_link = QLabel("How to get API Key(Token)")
        self.lb_api_link.setOpenExternalLinks(True)
        self.lb_api_link.setText("<a href='"+self.api_link+"'>How to get API Key</a>")
        
        self.lb_pwd = QLabel("Password*")
        self.le_pwd = QLineEdit()
        self.le_pwd.setEchoMode(QLineEdit.Password)
        self.btn_login = QPushButton("Login")
        self.btn_login.setToolTip("Login to SalesForce")
        self.glay_cred.addWidget(self.lb_uname,0,0)
        self.glay_cred.addWidget(self.le_uname,0,1)
        self.glay_cred.addWidget(self.lb_dname,0,2)
        self.glay_cred.addWidget(self.lb_pwd, 1,0)
        self.glay_cred.addWidget(self.le_pwd,1,1)
        self.glay_cred.addWidget(self.btn_login,1,2)
        self.glay_cred.addWidget(self.lb_api,2,0)
        self.glay_cred.addWidget(self.le_api,2,1)
        self.glay_cred.addWidget(self.btn_save_key,2,2)
        self.glay_cred.addWidget(self.lb_api_link,3,1)
        self.gbox_login.setLayout(self.glay_cred)

        # User Profile GroupBox
        self.gbox_profile = QGroupBox("User Profile")
        self.glay_profile = QGridLayout()
        self.lb_userid = QLabel("User ID: ")
        self.lb_userid_val = QLabel()
        self.lb_fullname = QLabel("Full Name: ")
        self.lb_fullname_val = QLabel()
        self.lb_title = QLabel("Title: ")
        self.lb_title_val = QLabel()
        self.glay_profile.addWidget(self.lb_userid, 0, 0)
        self.glay_profile.addWidget(self.lb_userid_val, 0, 1)
        self.glay_profile.addWidget(self.lb_fullname, 1, 0)
        self.glay_profile.addWidget(self.lb_fullname_val, 1, 1)
        self.glay_profile.addWidget(self.lb_title, 2, 0)
        self.glay_profile.addWidget(self.lb_title_val, 2, 1)
        self.gbox_profile.setLayout(self.glay_profile)

        # Top Container1
        self.hlay_container1 = QHBoxLayout()
        self.hlay_container1.addWidget(self.gbox_login, 50)
        # self.hlay_container1.addStretch()
        self.hlay_container1.addWidget(self.gbox_profile, 50)

        self.vlay_container = QVBoxLayout()
        self.gbox_case = QGroupBox("Case")
        self.layout_case = QVBoxLayout()
        self.glay_casetop = QGridLayout()
        self.lb_count = QLabel("Case in my Q: ")
        self.btn_refresh = QPushButton("Refresh")
        self.glay_casetop.addWidget(self.lb_count, 0, 0)
        self.glay_casetop.addWidget(self.btn_refresh, 0, 1)
        self.btn_refresh.setDisabled(True)
        self.lb_case_list = QLabel("Case List")
        self.cbox_case = QComboBox()
        self.glay_casetop.addWidget(self.lb_case_list, 1, 0)
        self.glay_casetop.addWidget(self.cbox_case, 1, 1)
        

        # Case Table
        self.tb_case = QTableWidget()
        self.tb_case.setColumnCount(5)
        # self.tb_case.resizeRowsToContents()
        # self.tb_case.resizeColumnsToContents()
        # self.tb_case.horizontalHeader().setVisible(False)
        # self.tb_case.verticalHeader().setVisible(False)
        self.tb_case_hheader = self.tb_case.horizontalHeader()
        # self.tb_case_hheader.setStretchLastSection(True)
        # self.tb_case.horizontalHeader().setStretchLastSection(True)
        self.tb_case_hheader.setSectionResizeMode(0, QHeaderView.Stretch)
        self.tb_case_hheader.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        # self.tb_case_hheader.setSectionResizeMode(QHeaderView.Stretch)
        # self.tb_case_hheader.setSectionResizeMode(QHeaderView.Interactive)
        
        
        # self.layout_case.addWidget(self.lb_count)
        # self.layout_case.addWidget(self.btn_refresh)
        # self.layout_case.addWidget(self.cbox_case)
        self.layout_case.addLayout(self.glay_casetop)
        self.layout_case.addWidget(self.tb_case)
        self.gbox_case.setLayout(self.layout_case)

        self.vlay_container.addLayout(self.hlay_container1)
        self.vlay_container.addWidget(self.gbox_case)

        self.layout.addLayout(self.vlay_container)
        self.setLayout(self.layout)

    def set_events(self):
        self.btn_login.clicked.connect(self.log_in)
        self.btn_save_key.clicked.connect(self.save_api)
        self.btn_refresh.clicked.connect(self.sf_refresh_case)
        self.cbox_case.activated[str].connect(self.sf_update_case_tb_by_case)
        # self.lb_api_link.linkActivated.connect(self.open_link)

    def load_api_secret(self):
        api_secret = self.get_api_secret()
        if api_secret is not '':
            self.le_api.setText(api_secret)
            self.le_api.setDisabled(True)
            self.btn_save_key.setText("Renew API Key")

    def log_in(self):
        login_action = str(self.btn_login.text())
        if login_action == "Login":
            username = str(self.le_uname.text()) + str(self.lb_dname.text())
            password = self.le_pwd.text()
            api_key = self.le_api.text()
            self.set_sf_username(username)
            self.set_sf_password(password)
            self.set_sf_api_key(api_key)
            if self.le_uname.text() != "" and password != "" and api_key != "":
                self.sf_login(username, password, api_key)
            else:
                self.pop_credential_warning()
        else:
            print("Logout!")
            self.log_out()

    def sf_login(self, username, password, api_key):
        sender = self.sender()
        try:
            self.sf_log_in(username, password, api_key)
            print("Login Successfull!")
            self.parent.statusMiddle.setText("Login Successfull!")
            self.le_pwd.setDisabled(True)
            self.btn_login.setText("Logout")
            self.le_uname.setDisabled(True)
            self.btn_refresh.setDisabled(False)
            self.parent.statusRight.setText("Login")
            self.parent.statusRight.setStyleSheet("background: green")
            self.sf_update_profile()
            self.sf_update_case_tb()
            self.sf_update_case_combobox()
            
        except Exception as e:
            self.pop_login_error(e)

    def pop_credential_warning(self):
        QMessageBox.warning(self, "Credential", "One of credential information is not given")

    def pop_login_error(self, exception):
        QMessageBox.critical(self, "Login Error", str(exception))
        
    def pop_empty_key_warning(self):
        QMessageBox.critical(self, "Empty value", "API Key is empty")
        
    def log_out(self):
        try:
            self.close_session()
            self.btn_login.setText("Login")
            self.le_uname.setDisabled(False)
            self.le_pwd.setDisabled(False)
            self.le_pwd.setText("")
            self.btn_refresh.setDisabled(True)
            self.lb_count.setText("Case in my Q: 0")
            self.clear_user_profile()
            self.clear_case_combobox()
            self.clear_case_table()
            self.parent.statusRight.setText("Logout")
            self.parent.statusRight.setStyleSheet("background: normal")
        except Exception as e:
            print(e)

    def clear_user_profile(self):
        self.lb_userid_val.setText("")
        self.lb_fullname_val.setText("")
        self.lb_title_val.setText("")

    def clear_case_table(self):
        self.tb_case.clear()
        self.tb_case.setRowCount(0)
        
    def clear_case_combobox(self):
        self.cbox_case.clear()

    def sf_update_profile(self):
        userid =    self.get_user('Id')
        userfname = self.get_user('FirstName') + " " + self.get_user('LastName')
        title =     self.get_user('Title')
        self.lb_userid_val.setText(userid)
        self.lb_fullname_val.setText(userfname)
        self.lb_title_val.setText(title)

    # Combobox Only
    def sf_update_case_combobox(self, sf=None):
        self.clear_case_combobox()
        cases = self.get_current_case_list()
        self.cbox_case.addItem("All")
        for case in cases:
            case_number = case['CaseNumber']
            case_status = case['Status']
            case_subject = case['Subject']
            case_title = case_number + " - " + case_subject
            self.cbox_case.addItem(case_title)
            self.case_count += 1

    # One Case Only
    def sf_update_case_tb_by_case(self, case_title):
        self.clear_case_table()
        if case_title == 'All':
            self.sf_update_case_tb()
        else:
            # take first 8 digits
            case_number = case_title[:8]
            case = self.get_case_by_number(case_number)
            case_id = case['Id']

            currentRowCount = self.tb_case.rowCount()
            self.tb_case.insertRow(currentRowCount)
            self.tb_case.setSpan(currentRowCount, 0, 1, 5)
            self.tb_case.setItem(currentRowCount, 0, QTableWidgetItem(case_title))

            self.display_attachment_on_table(case_id, self.tb_case)
            self.display_sfile_on_table(case_id, self.tb_case)

    # All
    def sf_update_case_tb(self):
        self.case_count = 0
        self.clear_case_table()
        cases = self.get_current_case_list()
        for case in cases:
            case_id     = case['Id']
            case_number = case['CaseNumber']
            case_status = case['Status']
            case_subject = case['Subject']
            case_title = case_number + " : " + case_status + " - " + case_subject
            # Create Table Top Header Title
            currentRowCount = self.tb_case.rowCount()
            self.tb_case.insertRow(currentRowCount)
            self.tb_case.setSpan(currentRowCount, 0, 1, 5)
            self.tb_case.setItem(currentRowCount, 0, QTableWidgetItem(case_title))
            self.tb_case.item(currentRowCount, 0).setBackground(Qt.red)
            self.tb_case.item(currentRowCount, 0).setForeground(Qt.white)
            # self.tb_case.item(currentRowCount, 0).setFont(QFont.bold)
            self.case_count += 1

            self.display_attachment_on_table(case_id, self.tb_case)
            self.display_sfile_on_table(case_id, self.tb_case)

        self.lb_count.setText("Case in my Q: " + str(self.case_count))

    def display_attachment_on_table(self, case_id, table):
        attachments = self.get_attachment_list(case_id)
        
        for attach in attachments:
            attach_id = attach['Id']
            attach_name = attach['Name']
            attach_body = attach['Body']
            attach_len = attach['BodyLength']
            attach_date = attach['CreatedDate']

            currentRowCount = table.rowCount()
            btn_download = QPushButton("Download")
            pbar_download = QProgressBar()
            table.insertRow(currentRowCount)
            table.setItem(currentRowCount, 0, QTableWidgetItem(attach_name))
            table.setItem(currentRowCount, 1, QTableWidgetItem(str(attach_len)))
            table.setItem(currentRowCount, 2, QTableWidgetItem(str(attach_date)))
            table.setCellWidget(currentRowCount, 3, btn_download)
            table.setCellWidget(currentRowCount, 4, pbar_download)
            btn_download.clicked.connect(lambda test="test",
                                                name=attach_name,
                                                id=attach_id,
                                                body=attach_body,
                                                length=attach_len,
                                                row=currentRowCount:
                                         self.download_att(name, id, body, length, row))

    def display_sfile_on_table(self, case_id, table):
        sfiles = self.get_sfile_list(case_id)
            
        for a_file in sfiles:
            file_id = a_file['Id']
            file_name = a_file['cg__File_Name__c']
            file_len = a_file['cg__File_Size_in_Bytes__c']
            file_date = a_file['CreatedDate']
            currentRowCount = table.rowCount()
            table.insertRow(currentRowCount)
            table.setItem(currentRowCount, 0, QTableWidgetItem(file_name))
            table.setItem(currentRowCount, 1, QTableWidgetItem(str(file_len)))
            table.setItem(currentRowCount, 2, QTableWidgetItem(str(file_date)))

    def download_att(self, attach_name, attach_id, attach_body, attach_length, current_row_number):
        try:
            self.check_session()
        except:
            self.re_login()

        path = self.download_pathname.replace("\\", "/")
        file_loc = QFileDialog.getSaveFileName(None, "Save File", path + "/" + attach_name, "All files (*.*)")[0]
        file_w_thread = threading.Thread(target=self.download,
                                         args=(file_loc, attach_name, attach_id, attach_body, attach_length, current_row_number))
        file_w_thread.start()
        self.download_pathname = os.path.dirname(file_loc)

    @pyqtSlot()
    def sf_refresh_case(self, sf=None):
        try:
            self.check_session()
            print("Session still alive!")
        except Exception as e:
            self.parent.statusRight.setText("Session expired!")
            self.parent.statusRight.setStyleSheet("background: orange")
            self.parent.statusMiddle.setText("Re-attempting login. Please wait...")
            username = self.get_sf_username()
            password = self.get_sf_password()
            api_key = self.get_sf_api_key()
            self.sf_login(username, password, api_key)
        else:
            print("Critical Issue!")

        print("Refreshed ", str(self.dont_push), " times!")
        self.dont_push += 1
        self.case_count = 0
        self.sf_update_profile()
        self.sf_update_case_combobox()
        self.sf_update_case_tb()

    @pyqtSlot()
    def save_api(self):
        api_key_action = str(self.btn_save_key.text())

        if api_key_action == "Renew API Key":
            self.le_api.setDisabled(False)
            self.le_api.setText("")
            self.btn_save_key.setText("Save API Key")
        else: # "Save API Key"
            new_api_key = self.le_api.text()
            if new_api_key is "":
                print("Hey bro, its empty! Try Again!")
                self.pop_empty_key_warning()
            else:
                print(new_api_key)
                self.le_api.setText(new_api_key)
                self.le_api.setDisabled(True)
                self.btn_save_key.setText("Renew API Key")                
                self.set_conf_api_secret(new_api_key)

    def open_link(self, link):
        print("open link")
        print(link)
        QDesktopServices.openUrl(QUrl(link))
    
    def get_api_secret(self):
        return self.model.get_api_secret()
    
    def set_sf_username(self, username):
        self.model.set_sf_username(username)
    
    def set_sf_password(self, password):
        self.model.set_sf_password(password)
    
    def set_sf_api_key(self, api_key):
        self.model.set_sf_api_key(api_key)
        
    def get_sf_username(self):
        return self.model.get_sf_username()
    
    def get_sf_password(self):
        return self.model.get_sf_password()
    
    def get_sf_api_key(self):
        return self.model.get_sf_api_key()
    
    def sf_log_in(self, username, password, api_key):
        return self.model.sf_log_in(username, password, api_key)
    
    def close_session(self):
        self.model.logout()
    
    def check_session(self):
        return self.model.check_session()
    
    def get_user(self, key=None):
        return self.model.get_user(key)
    
    def get_current_case_list(self):
        return self.model.get_current_case_list()
    
    def get_case_by_number(self, case_number):
        return self.model.get_case_by_number(case_number)
    
    def get_attachment_list(self, case_id):
        return self.model.get_attachment_list(case_id)
    
    def get_sfile_list(self, case_id):
        return self.model.get_sfile_list(case_id)
    
    def re_login(self):
        self.model.re_login()
    
    def download(self, file_path, attach_name, attach_id, attach_body, attach_length, current_row_number):
        self.model.download_file(file_path, attach_name, attach_id, attach_body, attach_length, current_row_number)
        
    def set_conf_api_secret(self, new_api_key):
        self.model.set_conf_api_secret(new_api_key)