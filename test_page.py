import pytest
import allure
from src.load_data import load



class TestPage:

    @allure.feature("Тестирование параметра page")
    @allure.story("Позитивные кейсы")
    @pytest.mark.parametrize("data", [x for x in load("test_page_positive.json")])
    def test_positive(self, regions_api, data):
        allure.dynamic.title(data["title"])
        if data["value"] == "Default":
            response = regions_api.get()
        else:
            response = regions_api.get(params={"page":data["value"]})
        response = response.json()
        for regions in response["items"]:
            with allure.step(f'Проверка названий элементов на странице: {regions["name"]}'):
                assert regions["name"] in data["expected_value"]

    @allure.feature("Тестирование параметра page")
    @allure.story("Негативный кейсы")
    @pytest.mark.parametrize("data", [x for x in load("test_page_negative.json")])
    def test_negative(self, regions_api, data):
        allure.dynamic.title(data["title"])
        response = regions_api.get(params={"page":data["value"]})
        response = response.json()
        with allure.step(f'Проверка возвращаемой ошибки: {response["error"]["message"]}'):
            assert response["error"]["message"] in data["expected_value"]