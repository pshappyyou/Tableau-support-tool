import os
import json

class MainModel:
    def __init__(self):
        print("MainModel Class")

    def nike(self):
        print("Just Do It!")

    def load_config(self):
        try:
            config_file = os.path.join(os.path.dirname(__file__), "config.json")
            with open(config_file, "r") as cf:
                self.config_data = json.load(cf)
        except IOError:
            print("Hey man there is no config file!")
            print(IOError)
            self.create_config_file()
        except OSError:
            print("No Config file!")
            print(OSError)
            self.create_config_file()

    def create_config_file(self):
        print("Creating a new config file")
        new_config_file_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(new_config_file_path, "w") as new_config_file:
            new_config_file.write('{"version": "0.1.1", '
                                  '"autoupdate": "true", '
                                  '"updatealram": "true"}')
        try:
            with open(new_config_file_path, "r") as check_config_file:
                check_file = json.load(check_config_file)
        except:
            print("Config file creating completed!")