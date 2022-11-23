from django.conf import settings
from .crud import Crud
from .models import Item
from django.views.generic import TemplateView
from django.shortcuts import redirect
import stripe


stripe.api_key = settings.STRYPE_API_KEY


class HomePage(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = Crud.get_all_item()
        context.update({'data': items})
        return context


class ProductPage(TemplateView):
    template_name = "product_page.html"
    error = ''

    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data(**kwargs)
        if self.product is not None:
            context.update(self.product | {'error': self.error})
        return context

    def get(self, request, item_id, *args, **kwargs):
        self.product: Item = Crud.get_item_by_id(item_id)
        return super().get(request, *args, **kwargs)

    def validation_form(self, value):
        count = int(value)
        if 0 > count or 9 < count:
            raise ValueError
        return count

    def post(self, request, item_id, *args, **kwargs):
        try:
            count = self.validation_form(request.POST['count'])
        except ValueError:
            self.error = 'Error: 0 <= count <= 9'
            return self.get(request, item_id, args, kwargs)
        Crud.update_order(item_id, count)
        return self.get(request, item_id, *args, **kwargs)


class ProductPayment(TemplateView):
    def create_order(self, line_items: list[dict]):
        stripe_session = stripe.checkout.Session.create(
                success_url=f"http://{settings.DOMEN}/success",
                cancel_url=f"http://{settings.DOMEN}/order",
                line_items=line_items,
                mode="payment",
            )
        return redirect(stripe_session['url'])

    def get(self, request, item_id, *args, **kwargs):
        product_key = Crud.get_product_key(item_id)
        if product_key is not None:
            return self.create_order([{'price': product_key, 'quantity': 1}])
        return redirect('home')


class OrderPayment(ProductPayment):
    def get(self, request, *args, **kwargs):
        return self.create_order(Crud.get_orders_for_session())


class OrderPage(TemplateView):
    template_name = "order.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'data': Crud.get_orders()})
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SuccessPage(TemplateView):
    template_name = 'success.html'

    def get(self, request, *args, **kwargs):
        Crud.clean_order()
        return super().get(request, *args, **kwargs)
