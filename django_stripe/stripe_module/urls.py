from django.urls import path
from .views import ProductPage, ProductPayment, SuccessPage, \
    HomePage, OrderPage, OrderPayment

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('item/<int:item_id>', ProductPage.as_view(), name='item'),
    path('buy/<int:item_id>', ProductPayment.as_view(), name='buy'),
    path('success', SuccessPage.as_view(), name='success'),
    path('order', OrderPage.as_view(), name='order'),
    path('orderbuy', OrderPayment.as_view(), name='orderbuy'),
]
