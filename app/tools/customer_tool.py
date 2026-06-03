import requests

from langchain_core.tools import tool

from app.config.app_config import CLIENT_SERVICE_BASE_URL


@tool
def get_customer_details(customer_id: str):
    """
    Get customer information.

    Use customerId returned from orders.
    """
    
    print(f"Calling Customer API for {customer_id}")

    response = requests.get(
        f"{CLIENT_SERVICE_BASE_URL}/customers/{customer_id}"
    )

    return response.json()