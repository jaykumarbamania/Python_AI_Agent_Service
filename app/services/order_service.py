from app.services.base_service import BaseService


class OrderService:

    @staticmethod
    def get_order(order_id: str):

        return BaseService.get(
            f"/orders/{order_id}"
        )