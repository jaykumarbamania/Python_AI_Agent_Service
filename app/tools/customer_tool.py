import requests

from langchain_core.tools import tool

from app.config.app_config import CLIENT_SERVICE_BASE_URL


@tool
def get_customer_details(customer_id: str):
    """
    Fetch customer details using customer id.

    Args:
        customer_id: Unique customer identifier

    Returns:
        customerId, name, email, city
    """
    print(f"Calling Customer API for {customer_id}")
    
    response = requests.get(
        f"{CLIENT_SERVICE_BASE_URL}/customers/{customer_id}"
    )

    return response.json()