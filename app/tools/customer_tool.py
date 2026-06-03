import requests

from langchain_core.tools import tool

from app.config.app_config import CLIENT_SERVICE_BASE_URL

from app.services.customer_service import CustomerService


@tool
def get_customer_details(customer_id: str):
    """
    Get customer information.

    Use customerId returned from orders.
    """

    return CustomerService.get_customer(customer_id)