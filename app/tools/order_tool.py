import requests

from langchain_core.tools import tool
from app.config.app_config import CLIENT_SERVICE_BASE_URL



@tool
def get_order_status(order_id: str):
    """
    Fetch order details.

    Args:
        order_id: Unique order identifier

    Returns:
        orderId, customerName, status, amount
    """

    response = requests.get(
        f"{CLIENT_SERVICE_BASE_URL}/orders/{order_id}"
    )

    return response.json()