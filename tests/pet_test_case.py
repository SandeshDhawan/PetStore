import os
import random
import string

import pytest

from client.pet_client import PETClient


class TestPet:

    @pytest.mark.regression
    def test_user_is_able_to_create_pet_record(self):
        pet_client = PETClient()

        test_data = pet_client.get_test_data("Create_Pet_Details.json")
        config = pet_client.get_config()
        test_data = pet_client.update_pet_id(test_data)
        test_data = pet_client.update_pet_category_id(test_data)

        response = pet_client.create_pet_entry(test_data, config)
        Paylod = response.json()
        assert response.status_code == 200
        assert Paylod['id'] == test_data['id'], "Pet id is wrong in response"

        response = pet_client.delete_pet_entry(config)
        Paylod = response.json()
        assert Paylod['code'] == 200, "Code is wrong in response"
        assert Paylod['message'] == str(test_data['id']), "Message is Wrong in Response"

    @pytest.mark.regression
    def test_user_is_able_to_create_pet_record_with_pet_id(self):
        pet_client = PETClient()

        config = pet_client.get_config()
        response = pet_client.create_pet_entry_with_petid(config)
        Paylod = response.json()
        assert Paylod['code'] == 200, "Code is wrong in Response"

    @pytest.mark.regression
    def test_get_pet_details_by_status(self):
        pet_client = PETClient()

        config = pet_client.get_config()

        response = pet_client.get_pet_details_by_status(config, "available")
        payload = response.json()
        for res in range(len(payload)):
            assert payload[res]['status'] == 'available', "Status is wrong in response"

        response = pet_client.get_pet_details_by_status(config, "pending")
        payload = response.json()
        for res in range(len(payload)):
            assert payload[res]['status'] == 'pending', "Status is wrong in response"

        response = pet_client.get_pet_details_by_status(config, "sold")
        payload = response.json()
        for res in range(len(payload)):
            assert payload[res]['status'] == 'sold', "Status is wrong in response"

    @pytest.mark.regression
    def test_pet_details_by_petid(self):
        pet_client = PETClient()

        config = pet_client.get_config()
        response = pet_client.get_pet_details_by_id(config, "1234")

        Payload = response.json()
        assert response.status_code == 200, "Status Code is wrong"
        assert Payload['id'] == 1234, "Pet ID is wrong"

    @pytest.mark.regression
    def test_update_pet_details(self):
        pet_client = PETClient()

        config = pet_client.get_config()
        test_data = pet_client.get_test_data("Create_Pet_Details.json")
        test_data = pet_client.update_pet_category_name(test_data, ''.join(
            (random.choice(string.ascii_lowercase) for x in range(4))))
        response = pet_client.update_pet_details(config, test_data)

        Payload = response.json()
        assert Payload['category']['name'] == test_data['category']['name']

        response = pet_client.get_pet_details_by_id(config, str(test_data['id']))
        Payload = response.json()
        assert Payload['category']['name'] == test_data['category']['name']

