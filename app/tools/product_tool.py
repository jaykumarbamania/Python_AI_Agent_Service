import requests

from langchain_core.tools import tool

from app.config.app_config import CLIENT_SERVICE_BASE_URL

from app.services.product_service import ProductService


@tool
def get_product_details(product_id: str):
    """
    Get product information.

    Use productId returned from orders.
    """

    return ProductService.get_product(product_id)