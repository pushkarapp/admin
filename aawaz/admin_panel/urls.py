"""aawaz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path

#from .views import index,user_details, products, login_view, logout_view
from .views import ManageDiamonds, ManageUsers,ManageGifts,UsersRooms,Reports, products, login_view, logout_view, ManageCoins
urlpatterns = [
  #path('', index, name='all-users'),
  path('login/', login_view, name='admin-login'),
  path('logout/', logout_view, name='logout'),
  #users
  path('user/create', ManageUsers.create, name='user_create' ),
  #users
  path('', ManageUsers.all_users, name='user_list'),
  path('user/<str:username>', ManageUsers.user_details, name='user_detail'),
  path('user/update/<str:username>', ManageUsers.user_update, name='user_update'),
  path('user/delete/<str:username>', ManageUsers.user_delete, name='user_delete'),
  #coin
  path('coin/create', ManageCoins.coin_create, name='add-coins'),
  path('coin/', ManageCoins.coin_list, name='coin_list'),
  path('coin/<int:id>/', ManageCoins.coin_details, name='coin_details'),
  path('coin/update/<int:id>/', ManageCoins.coin_update, name='coin_update'),
  path('coin/delete/<int:id>/', ManageCoins.coin_detele, name='coin_detele'),

  #Diamonds
  path('diamond/create', ManageDiamonds.diamond_create, name='create_diamond'),
  path('diamond/', ManageDiamonds.diamond_list, name='diamond_list'),
  path('diamond/<int:id>/', ManageDiamonds.diamond_details, name='diamond_details'),
  path('diamond/update/<int:id>/', ManageDiamonds.diamond_update, name='diamond_update'),
  path('diamond/delete/<int:id>/', ManageDiamonds.diamond_detele, name='diamond_detele'),

  #Gifts
  path('gift/create', ManageGifts.gift_create, name='create_gift'),
  path('gift/', ManageGifts.gift_list, name='gift_list'),
  path('gift/<int:id>/', ManageGifts.gift_details, name='gift_details'),
  path('gift/update/<int:id>/', ManageGifts.gift_update, name='gift_update'),
  path('gift/delete/<int:id>/', ManageGifts.gift_detele, name='gift_detele'),

  #Rooms
  path('room/', UsersRooms.room_list, name='room_list'),

  #Reports
  path('reports/assets-report', Reports.assets_report, name='user_assets_report'),

  path('add-gift/', products, name='add-gift'),
  path('add-diamond/', products, name='add-diamond'),
]

