# Generated by Django 3.1.1 on 2020-09-26 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoice', '0003_delete_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9999)),
                ('invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='invoice.invoice')),
            ],
        ),
    ]
