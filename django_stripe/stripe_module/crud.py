from .models import Item, StripeProductApi, Order
from django.db.models import F


class Crud:
    @staticmethod
    def get_all_item():
        items = Item.objects.all().order_by('price').values()
        return items

    @staticmethod
    def get_item_by_id(item_id: int):
        try:
            return Item.objects.filter(id=item_id).annotate(
                count=F('order__count')).values(
                    'id', 'name', 'description', 'price', 'count')[0]
        except IndexError:
            return None

    @staticmethod
    def get_product_key(id: int):
        try:
            return StripeProductApi.objects.get(item=id).api_key
        except StripeProductApi.DoesNotExist:
            return None

    @staticmethod
    def update_order(item_id: int, count: int):
        if count == 0:
            try:
                Order.objects.get(item_id=item_id).delete()
            except Order.DoesNotExist:
                pass
        else:
            Order.objects.update_or_create(
                item_id=item_id,
                defaults={'count': count}
            )

    @staticmethod
    def get_orders():
        return Order.objects.all().order_by(
            'count').values('item__name', "count")

    @staticmethod
    def get_orders_for_session() -> list[dict]:
        items = Order.objects.annotate(
            price=F('item__api__api_key'),
            quantity=F('count')).values('price', 'quantity')
        return list(items)

    @staticmethod
    def clean_order():
        Order.objects.all().delete()

    @staticmethod
    def get_product_count():
        pass
