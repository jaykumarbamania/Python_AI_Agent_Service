import requests

from langchain_core.tools import tool


@tool
def get_order_status(order_id: str):
    """
    Fetch order information using order id
    """

    response = requests.get(
        f"http://localhost:8080/orders/{order_id}"
    )

    return response.json()