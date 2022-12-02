from django.urls import include, path


from .views import CoinsAPI, DiamondsAPI, GiftsAPI, CoinPurchasePI,diamondPurchasePI,GiftPurchaseAPI, AllAssetsAPI

urlpatterns = [
  path('coins/', CoinsAPI.as_view(), name="all-coins"),
  path('gifts/', GiftsAPI.as_view(), name="all-gifts"),
  path('diamonds/', DiamondsAPI.as_view(), name="all-diamonds"),
  path('coins/purchase/', CoinPurchasePI.purchase_coin, name="coins-purchase"),
  path('gifts/purchase/', GiftPurchaseAPI.purchasegifts, name="gifts-purchase"),
  path('diamonds/purchase/', diamondPurchasePI.purchase_diamonds, name="diamonds-purchase"),
  path('users-assets/purchased/', AllAssetsAPI.all_assets_information, name="all_assets_information"),
  path('users-assets/history/', AllAssetsAPI.all_Purchase_report, name="all_assets_history"),
  #path('users/assets,',)
]