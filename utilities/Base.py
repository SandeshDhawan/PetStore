import json

import configparser
import os


class Base:

    BASEPATH = os.path.dirname(os.path.abspath(__file__))

    def get_test_data(self, file_name):
        test_data_file_path = self.BASEPATH.replace("utilities", "test_data") + "\\" + file_name
        with open(test_data_file_path) as f:
            payload = json.load(f)
        return payload

    def get_config(self):
        config = configparser.ConfigParser()
        config.read(self.BASEPATH + "\\" + "properties.ini")
        return config
