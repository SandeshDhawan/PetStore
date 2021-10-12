from client.store_client import StoreClient


class TestStore:

    def test_user_is_able_to_create_pet_record(self):
        store_client = StoreClient()

        test_data = store_client.get_test_data("Create_Store_Details.json")
        config = store_client.get_config()

        test_data = store_client.update_store_id(test_data)
        test_data = store_client.update_pet_id(test_data)

        response = store_client.create_store_entry(test_data, config)

        assert response.json()['id'] == test_data['id'], "Id is wring in response"
        assert response.json()['petId'] == test_data['petId'], "Pet Id is wrong in response"

        response = store_client.delete_store_entry(config, test_data['id'])
        assert response.status_code == 200, "Status Code is Wrong"
        assert response.json()['message'] == str(test_data['id']), "Message is wrong in response"

    def test_user_is_able_to_get_store_detail_by_order_id(self):
        store_client = StoreClient()
        config = store_client.get_config()

        response = store_client.get_store_details_by_order_id(config, 2)
        assert response.status_code == 200, "Status Code is wrong in response"
        assert response.json()['id'] == 2, "ID is wrong in response"

    def test_user_is_able_to_get_pet_inventories(self):
        store_client = StoreClient()
        config = store_client.get_config()

        response = store_client.get_store_inventory(config)
        assert response.status_code == 200, "Status Code is wrong"
