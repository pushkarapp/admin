from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Coin)
admin.site.register(Diamond)
admin.site.register(Gift)
admin.site.register(UserCoinPurchase)
admin.site.register(UserDiamondPurchase)
admin.site.register(UserGiftPurchase)

admin.site.register(UserAssetsReports)