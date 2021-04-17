import pytest
import allure
from src.load_data import load



class TestPageSize:

    @allure.feature("Тестирование параметра page_size")
    @allure.story("Позитивные кейсы")
    @pytest.mark.parametrize("data", [x for x in load("test_page_size_positive.json")])
    def test_positive(self, regions_api, data):
        allure.dynamic.title(data["title"])
        if data["page_size"] == "Default":
            response = regions_api.get()
        else:
            response = regions_api.get(params={"page_size":data["page_size"]})
        response = response.json()
        with allure.step(f'Проверка количества элементов на странице: {len(response["items"])}'):
            assert len(response["items"]) == data["expected_value"]

    @allure.feature("Тестирование параметра page_size")
    @allure.story("Негативный кейсы")
    @pytest.mark.parametrize("data", [x for x in load("test_page_size_negative.json")])
    def test_negative(self, regions_api, data):
        allure.dynamic.title(data["title"])
        response = regions_api.get(params={"page_size":data["page_size"]})
        response = response.json()
        with allure.step(f'Проверка возвращаемой ошибки: {response["error"]["message"]}'):
            assert response["error"]["message"] in data["expected_value"]
