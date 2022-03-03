'''
Here we defining static methods so that we can call these functions directly with the class name only,
No need to create object for accessing class methods.
for each common data we have created separated methods as static so that we will call them directly
using classname in test_login.py file.
'''

import configparser

config = configparser.RawConfigParser()
config.read(".//Configurations//Config.ini")

class ReadConfig:
    @staticmethod
    def getURL():
        url = config.get("common data", "baseURL")
        return url

    @staticmethod
    def getUsername():
        uname = config.get("common data", "username")
        return uname

    @staticmethod
    def getPassword():
        password = config.get("common data", "password")
        return password

