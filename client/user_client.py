import random

import names
import requests
from retry import retry

from utilities.Base import Base


class UserClient(Base):
    random_number = random.randint(1, 10)

    def set_id(self, test_data):
        test_data[0]['id'] = self.random_number
        return test_data

    def set_first_name(self, test_data):
        test_data[0]['firstName'] = names.get_first_name()
        return test_data

    def set_last_name(self, test_data):
        test_data[0]['lastName'] = names.get_last_name()
        return test_data

    def set_username(self, test_data):
        test_data[0]['username'] = test_data[0]['firstName'] + "_" + test_data[0]['lastName']
        return test_data

    def set_email(self, test_data):
        test_data[0]['email'] = test_data[0]['username'] + "@test.com"
        return test_data

    def set_password(self, test_data):
        test_data[0]['password'] = test_data[0]['username'] + "_123"
        return test_data

    def set_phone_number(self, test_data):
        test_data[0]['phone'] = "1234567891"
        return test_data

    def set_user_details(self, test_data):
        test_data = self.set_id(test_data)
        test_data = self.set_first_name(test_data)
        test_data = self.set_last_name(test_data)
        test_data = self.set_username(test_data)
        test_data = self.set_email(test_data)
        test_data = self.set_password(test_data)
        test_data = self.set_phone_number(test_data)
        return test_data

    def create_user_record(self, test_data, config):
        response = requests.post(config['API']['BASEURL'] + config['API']['CREATEUSER'], json=test_data)
        response.raise_for_status()
        return response

    @retry(tries=-5, delay=2)
    def delete_user_record(self, config, user):
        response = requests.delete(config['API']['BASEURL'] + config['API']['DELETEUSER'] + user)
        response.raise_for_status()
        return response

    def get_user_details(self, config, user):
        response = requests.get(config['API']['BASEURL'] + config['API']['GETUSER'] + user)
        return response

    def user_login(self, config, username, password):
        response = requests.get(
            config['API']['BASEURL'] + config['API']['USERLOGIN'] + "?username=" + username + "&password=" + password)
        return response

    def user_logout(self, config):
        response = requests.get(config['API']['BASEURL'] + config['API']['USERLOGOUT'])
        return response
