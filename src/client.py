import allure
import requests



class ApiClient:

    def __init__(self, address):
        self.address = address

    def get(self, params=None):
        url = f"{self.address}"
        with allure.step(f"GET запрос к: {url}"):
            return requests.get(url=url, params=params)