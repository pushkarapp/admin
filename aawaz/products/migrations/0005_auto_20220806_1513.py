# Generated by Django 3.2.14 on 2022-08-06 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220806_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdiamondpurchase',
            name='diamond_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.diamond'),
        ),
        migrations.AlterField(
            model_name='usergiftpurchase',
            name='gift_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.gift'),
        ),
    ]
