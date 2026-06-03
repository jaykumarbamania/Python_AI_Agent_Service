import requests

from langchain_core.tools import tool
from app.config.app_config import CLIENT_SERVICE_BASE_URL

from app.services.order_service import OrderService



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

    return OrderService.get_order(order_id)