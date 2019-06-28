import os
import json
import pytz
import time
import subprocess
import threading
from datetime import datetime
from simple_salesforce import Salesforce

class SalesForceModel:
    def __init__(self):
        # print("Instantiated SalesForceModel Object")
        self.config_file = os.path.join(os.path.dirname(__file__), "config.json")
        self.sf : Salesforce()
        self.user_id = ""
        self.username = ""
        self.password = ""
        self.api_key = ""

    def get_sf_username(self):
        return self.username

    def set_sf_username(self, username):
        self.username = username

    def get_sf_password(self):
        return self.password

    def set_sf_password(self, password):
        self.password = password

    def get_sf_api_key(self):
        return self.api_key

    def set_sf_api_key(self, api_key):
        self.api_key = api_key

    def get_api_secret(self):
        api_secret = ''
        config_file = os.path.join(os.path.dirname(__file__), "config.json")
        try:
            with open(config_file, "r") as f:
                data = json.load(f)
                api_secret = data['secret_key']
        except FileNotFoundError:
            print("no config file found! " + str(FileNotFoundError))
            api_secret = ''
        except KeyError:
            print("no such key - secret_key! " + str(KeyError))
            api_secret = ''
        return api_secret
    
    def update_conf(self, key, value):
        config_file = self.config_file
        with open(config_file, "r") as cf:
            config_data = json.load(cf)
        config_data.update({key : value})
        with open(config_file, 'w') as cf:
            json.dump(config_data, cf)
        
    def set_conf_api_secret(self, new_api_key):
        config_file = self.config_file
        with open(config_file, "r") as cf:
            config_data = json.load(cf)
        config_data.update({'secret_key': new_api_key})
        with open(config_file, 'w') as cf:
            json.dump(config_data, cf)

    def sf_log_in(self, username=None, password=None, api_key=None):
        self.username = username
        self.password = password
        self.api_key = api_key
        self.sf = Salesforce(username=username, password=password, security_token=api_key)
        self.user_id = self.get_user_id()
        # return self.sf

    def re_login(self):
        username = self.get_sf_username()
        password = self.get_sf_password()
        api_key = self.get_sf_api_key()
        self.sf = Salesforce(username=username, password=password, security_token=api_key)
        self.user_id = self.get_user_id()

    def logout(self):
        return self.sf.session.close()

    def get_user(self, info=None):
        # return user object
        # the info string can be 'Id', 'FirstName', 'LastName', 'Title'
        identity_url = self.sf.restful('')['identity']
        user = self.sf.User.get(identity_url[-18:])
        if info != None:
            info = user[info]
            return info
        else:
            return user

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        identity_url = self.sf.restful('')['identity']
        user = self.sf.User.get(identity_url[-18:])
        user_id = user['Id']
        return user_id

    def get_user_fname(self):
        identity_url = self.sf.restful('')['identity']
        user = self.sf.User.get(identity_url[-18:])
        user_fname = user['FirstName']
        return user_fname

    def get_user_lname(self):
        identity_url = self.sf.restful('')['identity']
        user = self.sf.User.get(identity_url[-18:])
        user_lname = user['LastName']
        return user_lname

    def get_user_title(self):
        identity_url = self.sf.restful('')['identity']
        user = self.sf.User.get(identity_url[-18:])
        user_title = user['Title']
        return user_title

    def get_current_case_list(self, sf=None):
        userid = self.get_user_id()
        query = "SELECT Id, CaseNumber, OwnerId, Status, Subject FROM Case WHERE OwnerId = '" + \
                userid + "' AND (Status = 'Active' OR Status='New' OR Status='Re-opened')"
        if sf != None:
            list = sf.query(query)
        else:
            list = self.sf.query(query)
        return list['records']

    def get_attachment_list(self, case_id, sf=None):
        query = """SELECT 
                        Id, Name, Body, BodyLength, CreatedDate, 
                        LastModifiedDate, Description 
                    FROM Attachment 
                        WHERE ParentId = '""" + case_id + "'"
        if sf != None:
            list = sf.query(query)
        else:
            list = self.sf.query(query)
        return list['records']

    def get_sfile_list(self, case_id, sf=None):
        query = """SELECT 
                        Id, Name, 
                        cg__Case__c, 
                        cg__File_Name__c, 
                        cg__File_Size_in_Bytes__c, 
                        cg__File_Size__c,
                        CreatedDate,
                        LastModifiedDate,
                        cg__Description__c,
                        cg__Parent_Folder_Id__c,
                        cg__Key__c
                    FROM cg__CaseFile__c 
                        WHERE cg__Case__c = '""" + case_id + "'"
        if sf != None:
            list = sf.query(query)
        else:
            list = self.sf.query(query)
        return list['records']

    def get_case_by_id(self, case_id, sf=None):
        if sf != None:
            case_obj = sf.Case.get(case_id)
        else:
            case_obj = self.sf.Case.get(case_id)
        return case_obj

    def get_case_by_number(self, case_number, sf=None):
        query = "SELECT Id, CaseNumber, OwnerId, Status, Subject FROM Case WHERE OwnerId = '" + \
                self.user_id + "' AND (Status = 'Active' OR Status='New' OR Status='Re-opened') AND (CaseNumber = '" + case_number + "')"
        if sf != None:
            case_dic = sf.query(query)
        else:
            case_dic = self.sf.query(query)
        return case_dic['records'][0]

    def get_case_id(self, case_number, sf=None):
        query = "SELECT Id, CaseNumber, OwnerId, Status, Subject FROM Case WHERE OwnerId = '" + \
                self.user_id + "' AND (Status = 'Active' OR Status='New' OR Status='Re-opened') AND (CaseNumber = '" + case_number + "')"
        if sf != None:
            case_dic = sf.query(query)
        else:
            case_dic = self.sf.query(query)
        return case_dic['records'][0]['Id']

    def check_session(self, sf=None):
        return self.sf.restful('')['identity']

    def download_file(self, file_path, attach_name, attach_id, attach_body, attach_length, current_row_number):
        # requires to be threading
        # attach progress bar
        # progress = QProgressBar()
        completed = 0
        # progress.setMaximum(100)
        total = attach_length

        base = 'https://tableau.my.salesforce.com/'
        url = base + attach_body
        result = self.sf._call_salesforce(method='GET', url=url)
        # print(result)
        # print(result.headers)
        # print(result.headers.get('content-length'))

        try:
            with open(file_path, 'wb+') as file:
                total = int(total)
                # retrieve the bytes from the resources incrementally
                for chunk in result.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                    completed += len(chunk)
                    file.write(chunk)
                    done = int(50*completed/total)
                    print(str(completed))
                    print(str(done))
            print("Download Completed!")
            file_path = file_path.replace("/", "\\")
            # Windows specific function
            open_ex_file = r'explorer /select, "' + file_path + '"'
            subprocess.Popen(open_ex_file)
        except Exception as e:
            print(str(e))

    def create_folder(self, path):
        print(path)
        try:
            os.makedirs(path)
        except OSError as e:
            # print(e)
            # e.errno
            # print(e.errno)
            # print(e.winerror)
            # print(e.strerror)
            if e.winerror == 183:
                return "folder_alreay_exist"
                # messagebox.showwarning("Folder Creation Error", "The folder already exist:  %s" % path)
            else:
                return str(e)
                # messagebox.showerror("Folder Creation Error", "Reason: %s" % e.strerror)
        else:
            return "folder_created"
            # messagebox.showinfo("Folder Creation Info", "Successfully created the directory %s " % path)