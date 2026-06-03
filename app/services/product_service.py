from app.services.base_service import BaseService


class ProductService:

    @staticmethod
    def get_product(product_id: str):

        return BaseService.get(
            f"/products/{product_id}"
        )