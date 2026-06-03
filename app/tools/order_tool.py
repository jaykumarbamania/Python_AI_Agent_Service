import requests

from langchain_core.tools import tool
from app.config.app_config import CLIENT_SERVICE_BASE_URL



@tool
def get_order_status(order_id: str):
    """
    Get order information.

    Returns:
    orderId,
    customerId,
    productId,
    status,
    amount
    """

    print(f"Calling Order API for {order_id}")

    response = requests.get(
        f"{CLIENT_SERVICE_BASE_URL}/orders/{order_id}"
    )

    return response.json()