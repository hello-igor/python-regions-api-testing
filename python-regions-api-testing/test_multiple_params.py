import pytest
import allure
from src.load_data import load



class TestMultipleParams:

    @allure.feature("Тестирование нескольких параметров")
    @allure.story("Позитивные кейсы")
    @pytest.mark.parametrize("data", [x for x in load("test_multiple_params.json")])
    def test_positive(self, regions_api, data):
        allure.dynamic.title(data["title"])
        params = {}
        if data["q"] != "Default":
            params["q"] = data["q"]
        if data["country_code"] != "Default":
            params["country_code"] = data["country_code"]
        if data["page_size"] != "Default":
            params["page_size"] = data["page_size"] 
        if data["page"] != "Default":
            params["page"] = data["page"] 
        response = regions_api.get(params=params)
        response = response.json()
        for regions in response["items"]:
            with allure.step(f'Проверка названия региона: {regions["name"]}'):
                assert regions["name"] in data["expected_value"]