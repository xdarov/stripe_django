# Generated by Django 4.1.3 on 2022-11-20 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_module', '0002_stripeproductapi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stripeproductapi',
            old_name='item_id',
            new_name='item',
        ),
    ]
