# Generated by Django 3.1.1 on 2020-09-26 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_delete_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='reciept_image',
            field=models.ImageField(blank=True, null=True, upload_to='invoice_receipts/%Y/%m/%d'),
        ),
    ]
