import requests

from app.config.app_config import CLIENT_SERVICE_BASE_URL


class BaseService:

    @staticmethod
    def get(path: str):

        url = f"{CLIENT_SERVICE_BASE_URL}{path}"

        print(f"Calling API: {url}")

        response = requests.get(url, timeout=5)

        response.raise_for_status()

        return response.json()