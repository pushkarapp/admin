from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from unicodedata import name
from django.db import models
from admin_panel.drop_down_choices import Choices
from user_management.models import BaseModel
from django.contrib.auth.models import User
# Create your models here.

class Product(BaseModel):
    product_type = models.CharField(max_length=50, choices=Choices.product_type)
    package_type = models.CharField(max_length=50, choices=Choices.product_type)
    product_name = models.CharField(max_length=120)
    product_image = models.ImageField(upload_to = 'upload/products/')
    product_rate = models.FloatField(default=0.00)
    number_in_bundle = models.IntegerField(default=0)
    extra_product = models.IntegerField(default=0)

    @property
    def price(self):
        
        return self.product_rate * self.number_in_bundle
    def __str__(self):
        return self.product_name

class Coin(BaseModel):
    coin_name = models.CharField(max_length=120)
    coin_image = models.ImageField(upload_to = 'upload/products/coin')
    coin_rate = models.FloatField(default=0.00)
    available_stock = models.IntegerField(default=0)
    def __str__(self):
        return self.coin_name

class Diamond(BaseModel):
    diamond_name = models.CharField(max_length=120)
    diamond_image = models.ImageField(upload_to = 'upload/products/diamond')
    diamond_rate = models.FloatField(default=0.00)
    available_stock = models.IntegerField(default=0)
    def __str__(self):
        return self.diamond_name

class Gift(BaseModel):
    gift_name = models.CharField(max_length=120)
    gift_image = models.ImageField(upload_to = 'upload/products/gift')
    #gift_rate_coin = models.FloatField(default=0.00)
    gift_rate_diamond = models.FloatField(default=0.00)
    available_stock = models.IntegerField(default=0)
    def __str__(self):
        return self.gift_name


class UserPurchase(BaseModel):
    user_purchased = models.ForeignKey(User, on_delete=models.CASCADE)
    rate_purchased = models.FloatField(default=0.00)
    total_amount = models.FloatField(default=0.00)
    quantity = models.IntegerField(default=0)
    class Meta:
        abstract = True

class UserGiftPurchase(UserPurchase):
    gift_id = models.ForeignKey(Gift, models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.user_purchased

class UserDiamondPurchase(UserPurchase):
    diamond_id = models.ForeignKey(Diamond, models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.user_purchased.username

class UserCoinPurchase(UserPurchase):
    coin_id = models.ForeignKey(Coin, models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user_purchased.username


class UserAssetsReports(BaseModel):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name='user_assets_report' )
    total_coin_purchased = models.IntegerField(default=0)
    available_coins = models.IntegerField(default=0)
    total_diamonds_purchased = models.IntegerField(default=0)
    available_diamonds = models.IntegerField(default=0)
    total_gifts_purchased = models.IntegerField(default=0)
    available_gift = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username


    



