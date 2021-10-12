from client.user_client import UserClient


class TestUser:

    def test_user_creation(self):
        user_client = UserClient()

        test_data = user_client.get_test_data("Create_User_Details.json")
        config = user_client.get_config()

        test_data = user_client.set_user_details(test_data)
        response = user_client.create_user_record(test_data, config)
        assert response.status_code == 200, "User is not Created Successfully"
        assert response.json()['code'] == 200, "Code is wrong in response"
        assert response.json()['message'] == "ok", "Message is wrong in response"

        response = user_client.delete_user_record(config, test_data[0]['username'])
        assert response.json()['code'] == 200, "Code is wrong in response"
        assert response.json()['type'] == 'unknown', "wrong Type"
        assert response.json()['message'] == test_data[0]['username'], "wrong message"

    def test_get_user_details_for_wrong_user(self):
        user_client = UserClient()
        config = user_client.get_config()

        response = user_client.get_user_details(config, "user1")
        assert response.status_code == 404, "Wrong Status Code"
        assert response.json()['code'] == 1, "Wrong Code in response"
        assert response.json()['type'] == "error", "Wrong Type in Response"
        assert response.json()['message'] == "User not found", "Wrong Message in response"

    def test_get_user_details(self):
        user_client = UserClient()
        config = user_client.get_config()

        response = user_client.get_user_details(config, "TestUser")
        assert response.status_code == 200, "Wrong Status Code"
        assert response.json()['username'] == "TestUser", "Wrong User Name in response"
        assert response.json()['firstName'] == "Test", "Wrong First Name in response"
        assert response.json()['lastName'] == "User", "Wrong Last Name in response"
        assert response.json()['email'] == "test.user@gmail.com", "Wrong email in response"
        assert response.json()['password'] == "test_password", "Wrong Password in response"

    def test_user_login(self):
        user_client = UserClient()
        config = user_client.get_config()

        response = user_client.user_login(config, "TestUser", "test_password")
        assert response.status_code == 200, "Wrong Status Code"
        message = response.json()['message']
        if "logged in user" in message:
            assert True
        else:
            assert False, "Wrong Message in Response"

    def test_user_logout(self):
        user_client = UserClient()
        config = user_client.get_config()

        response = user_client.user_logout(config)
        assert response.status_code == 200, "Wrong Status Code"
        assert response.json()['code'] == 200, "Wrong Code in Response"
        assert response.json()['type'] == "unknown", "Wrong Type in Response"
        assert response.json()['message'] == "ok", "Wrong Message in Response"
