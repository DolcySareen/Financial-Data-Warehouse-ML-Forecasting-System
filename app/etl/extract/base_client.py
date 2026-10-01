import requests

class FMPClient:
    BASE_URL = "https://financialmodelingprep.com/api/"

    def __init__(self, api_key):
        self.api_key = api_key

    def _make_request(self, endpoint, params=None):
        url = f"{self.BASE_URL}/{endpoint}"
        params = params or {}
        params['apikey'] = self.api_key
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API request failed: {response.status_code} - {response.text}")
