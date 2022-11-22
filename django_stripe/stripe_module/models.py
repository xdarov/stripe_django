from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.description} {self.price}'


class StripeProductApi(models.Model):
    item = models.ForeignKey('Item', related_name='api', on_delete=models.CASCADE)
    api_key = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.api_key}'


class Order(models.Model):
    item = models.ForeignKey('Item', related_name='order', on_delete=models.DO_NOTHING)
    count = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.count}'
