import pytest
import allure
from src.load_data import load



class TestQuery:

    @allure.feature("Тестирование параметра q")
    @allure.story("Позитивные кейсы")
    @pytest.mark.parametrize("data", [x for x in load("test_query_positive.json")])
    def test_positive(self, regions_api, data):
        allure.dynamic.title(data["title"])
        response = regions_api.get(params={"q":data["q"]})
        response = response.json()
        for regions in response["items"]:
            with allure.step(f'Проверка названия региона: {regions["name"]}'):
                assert regions["name"] in data["expected_value"]

    @allure.feature("Тестирование параметра q")
    @allure.story("Негативные кейсы")
    @pytest.mark.parametrize("data", [x for x in load("test_query_negative.json")])
    def test_negative(self, regions_api, data):
        allure.dynamic.title(data["title"])
        response = regions_api.get(params={"q":data["q"]})
        response = response.json()
        with allure.step(f'Проверка возвращаемой ошибки: {response["error"]["message"]}'):
            assert response["error"]["message"] in data["expected_value"]
