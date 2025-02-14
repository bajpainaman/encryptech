import requests

class EncryptechClient:
    def __init__(self, api_key, base_url="https://api.encryptech.ai"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def send_update(self, update):
        """
        Sends a model update to the Encryptech API.
        """
        endpoint = f"{self.base_url}/update"
        response = requests.post(endpoint, json=update, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_aggregate(self):
        """
        Retrieves the aggregated model weights from the Encryptech API.
        """
        endpoint = f"{self.base_url}/aggregate"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_compliance_report(self):
        """
        Retrieves a compliance report from the Encryptech API.
        """
        endpoint = f"{self.base_url}/compliance"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()
