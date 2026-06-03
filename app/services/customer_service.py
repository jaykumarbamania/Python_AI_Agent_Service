from app.services.base_service import BaseService


class CustomerService:

    @staticmethod
    def get_customer(customer_id: str):

        return BaseService.get(
            f"/customers/{customer_id}"
        )