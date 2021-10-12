import random

import requests

from utilities.Base import Base


class StoreClient(Base):
    random_number = random.randint(1, 10)

    def create_store_entry(sel, test_data, config):
        response = requests.post(config['API']['BASEURL'] + config['API']['STOREPOST'], json=test_data)
        return response

    def delete_store_entry(sel, config, id):
        response = requests.delete(config['API']['BASEURL'] + config['API']['DELETESTORE'] + str(id))
        return response

    def get_store_details_by_order_id(self, config, id):
        response = requests.get(config['API']['BASEURL'] + config['API']['GETSTOREDETAILS'] + str(id))
        return response

    def get_store_inventory(self, config):
        response = requests.get(config['API']['BASEURL'] + config['API']['GETSTOREINVENTORY'])
        return response

    def update_store_id(self, test_data):
        test_data['id'] = self.random_number
        return test_data

    def update_pet_id(self, test_data):
        test_data['petId'] = self.random_number
        return test_data
