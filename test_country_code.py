import pytest
import allure
from src.load_data import load



class TestCountryCode:

    @allure.feature("Тестирование параметра country_code")
    @allure.story("Позитивные кейсы")
    @pytest.mark.parametrize("data", [x for x in load("test_country_code_positive.json")])
    def test_positive(self, regions_api, data):
        allure.dynamic.title(data["title"])
        response = regions_api.get(params={"country_code":data["value"]})
        response = response.json()
        for regions in response["items"]:
            with allure.step(f'Проверка кода региона: {regions["country"]["code"]}'):
                assert regions["country"]["code"] in data["expected_value"]

    @allure.feature("Тестирование параметра country_code")
    @allure.story("Негативный кейсы")
    @pytest.mark.parametrize("data", [x for x in load("test_country_code_negative.json")])
    def test_negative(self, regions_api, data):
        allure.dynamic.title(data["title"])
        response = regions_api.get(params={"country_code":data["value"]})
        response = response.json()
        with allure.step(f'Проверка возвращаемой ошибки: {response["error"]["message"]}'):
            assert response["error"]["message"] in data["expected_value"]
