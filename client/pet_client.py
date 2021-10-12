import json
import os

import configparser
import random

import requests
from retry import retry

from utilities.Base import Base


class PETClient(Base):
    random_number = random.randint(100, 999)

    def create_pet_entry(self, test_data, config):
        response = requests.post(config['API']['BASEURL'] + config['API']['POSTPET'], json=test_data)
        return response

    @retry(tries=5, delay=2)
    def delete_pet_entry(self, config):
        response = requests.delete(
            config['API']['BASEURL'] + config['API']['DELETEPET'] + str(self.random_number))
        response.raise_for_status()
        return response

    @retry(tries=5, delay=3)
    def create_pet_entry_with_petid(self, config):
        response = requests.post(config['API']['BASEURL'] + config['API']['CREATEPETWITHID'] + str(self.random_number))
        response.raise_for_status()
        return response

    @retry(tries=5, delay=2)
    def get_pet_details_by_status(self, config, status):
        response = requests.get(
            config['API']['BASEURL'] + config['API']['GETPETDETAILS'] + "?status=" + status)
        response.raise_for_status()
        return response

    @retry(tries=5, delay=2)
    def get_pet_details_by_id(self, config, id):
        response = requests.get(
            config['API']['BASEURL'] + config['API']['GETPETDETAILSBYID'] + id)
        response.raise_for_status()
        return response

    def update_pet_details(self, config, test_data):
        response = requests.put(config['API']['BASEURL'] + config['API']['PURPETDETAILS'], json=test_data)
        response.raise_for_status()
        return response

    def update_pet_id(self, test_data):
        test_data['id'] = self.random_number
        return test_data

    def update_pet_category_id(self, test_data):
        test_data['category']['id'] = self.random_number
        return test_data

    def update_pet_category_name(self, test_data, pet_category_name):
        test_data['category']['name'] = pet_category_name
        return test_data

    def update_pet_name(self, test_data, pet_name):
        test_data['name'] = pet_name
        return test_data

    def update_pet_photo_url(self, test_data, photo_url):
        test_data['photoUrls'] = photo_url
        return test_data

    def update_pet_tags_id(self, test_data, pet_tag_id):
        test_data['tags'][0]['id'] = pet_tag_id
        return test_data

    def update_pet_tag_name(self, test_data, pet_tag_name):
        test_data['tags'][0]['name'] = pet_tag_name
        return test_data

    def update_status(self, test_data, status):
        test_data['status'] = status
        return test_data
