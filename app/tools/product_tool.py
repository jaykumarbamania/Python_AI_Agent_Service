import requests

from langchain_core.tools import tool

from app.config.app_config import CLIENT_SERVICE_BASE_URL


@tool
def get_product_details(product_id: str):
    """
    Get product information.

    Use productId returned from orders.
    """

    print(f"Calling Product API for {product_id}")

    response = requests.get(
        f"{CLIENT_SERVICE_BASE_URL}/products/{product_id}"
    )

    return response.json()