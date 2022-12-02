from django.shortcuts import render
from rest_framework.decorators import APIView
from django.http import JsonResponse
from rest_framework import authentication, permissions

from django.contrib.auth.models import User
from firebase_auth.authentication import custom_firebase_authentication
from products.models import *
from rest_framework.decorators import api_view
# Create your views here.

class CoinsAPI(APIView):
    def get(request, self):
        try:
            data = Coin.objects.all().order_by('id').values()
            return JsonResponse({"success":True, "data":list(data) })
        except Exception as e:
            return JsonResponse({"success":False, "message":f"{e}"})


class GiftsAPI(APIView):
    #authentication_classes = [authentication.A]
    #permission_classes = ([permissions.AllowAny])
    def get(request, self):
        try:
            data = Gift.objects.all().order_by('id').values()
            return JsonResponse({"success":True, "data":list(data) })
        except Exception as e:
            return JsonResponse({"success":False, "message":f"{e}"})

    

class DiamondsAPI(APIView):
    #authentication_classes = [authentication.A]
    #permission_classes = ([permissions.AllowAny])
    def get(request, self):
        try:
            data = Diamond.objects.all().order_by('id').values()
            return JsonResponse({"success":True, "data":list(data) })
        except Exception as e:
            return JsonResponse({"success":False, "message":f"{e}"})


class CoinPurchasePI(APIView):

    @api_view(['POST'])
    def purchase_coin(request):
        auth_user=custom_firebase_authentication(request)
        if auth_user:
            try:
                quantity = request.data['quantity']
                user = User.objects.get(username=auth_user.username)
                coin_rate = Coin.objects.all()[:1]
                if int(quantity)>0:
                    total_amount = coin_rate[0].coin_rate*float(quantity) ## ## Redirect to get paymnet through paymnet gateway

                    print("remaning amount paid")
                    #on success payment
                    UserCoinPurchase.objects.create(user_purchased=user, rate_purchased = coin_rate[0].coin_rate, total_amount=total_amount, quantity=quantity)
                    
                    try:
                        user_report_obj = UserAssetsReports.objects.get(user=user)
                        user_report_obj.total_coin_purchased += float(quantity)
                        user_report_obj.available_coins += float(quantity)
                        user_report_obj.save()
                    except Exception:
                        user_report_obj = UserAssetsReports.objects.create(user=user, total_coin_purchased=quantity, available_coins=quantity)
                    return JsonResponse({"success":True, "message":"Coins Purchased"})
                else:
                    return JsonResponse({"success":False, "message":"Invalid Input"})
            except Exception as e:
                return JsonResponse({"success":False, "message":f"{e}"})
        else:
            return JsonResponse({"success":False, "message":f"{e}"})


class diamondPurchasePI(APIView):
    @api_view(['POST'])
    def purchase_diamonds(request):
        auth_user=custom_firebase_authentication(request)
        try:
            if auth_user:
                try:
                    quantity = request.data['quantity']
                    #diamond_id = request.data['diamond_id']
                    user = User.objects.get(username=auth_user.username)
                    # diamond_id_obj = Diamond.objects.get(id=diamond_id)
                    diamond_id_obj = Diamond.objects.all()[:1]
                    if int(quantity)>0:
                        dd_object = Diamond.objects.get(id=diamond_id_obj[0].id)
                        diamond_rate = diamond_id_obj[0].diamond_rate
                        required_coin = diamond_rate*float(quantity)
                        # Get Available Coins of this user
                        try:
                            current_user_available_coin = UserAssetsReports.objects.get(user=user).available_coins
                        except:
                            current_user_available_coin = UserAssetsReports.objects.create(user=user)
                        balance_coin = current_user_available_coin-required_coin
                        if balance_coin>=0:
                            UserDiamondPurchase.objects.create(user_purchased=user, rate_purchased = diamond_rate, total_amount=required_coin, quantity=quantity, diamond_id=dd_object)
                            try:
                                user_report_obj = UserAssetsReports.objects.get(user=user)
                                user_report_obj.available_coins -= required_coin
                                user_report_obj.total_diamonds_purchased += float(quantity)
                                user_report_obj.available_diamonds += float(quantity)
                                user_report_obj.save()
                            except Exception:
                                user_report_obj = UserAssetsReports.objects.create(user=user, total_diamonds_purchased=quantity, available_diamonds=quantity)
                        else:
                            remmainng_left_coin = abs(balance_coin)
                            coin_rate = Coin.objects.all()[:1]
                            ## Redirect to get paymnet through paymnet gateway
                            total_amount = coin_rate*remmainng_left_coin
                            print("remaning amount paid")
                            # on sucess payment 
                            UserDiamondPurchase.objects.create(user_purchased=user, rate_purchased = diamond_rate, total_amount=required_coin, quantity=quantity, diamond_id=dd_object)
                            try:
                                user_report_obj = UserAssetsReports.objects.get(user=user)
                                user_report_obj.available_coins = 0
                                user_report_obj.total_diamonds_purchased += float(quantity)
                                user_report_obj.available_diamonds += float(quantity)
                                user_report_obj.save()
                            except Exception:
                                user_report_obj = UserAssetsReports.objects.create(user=user, total_diamonds_purchased=quantity, available_diamonds=quantity)
                        return JsonResponse({"success":True, "message":"Diamonds Purchased"})
                    return JsonResponse({"success":False, "message":"Invalid Input"})
                except Exception as e:
                    return JsonResponse({"success":False, "message":f"{e}"})
            else:
                return JsonResponse({"success":False, "message":f"{e}"})
        except Exception as e:
            return JsonResponse({"success":False, "message":f"{e}"})

class GiftPurchaseAPI(APIView):
    @api_view(['POST'])
    def purchasegifts(request):
        auth_user=custom_firebase_authentication(request)
        try:
            if auth_user:
                try:
                    quantity = float(request.data['quantity'])
                    gift_id = request.data['gift_id']
                    user = User.objects.get(username=auth_user.username)
                    gift_id_obj = Gift.objects.get(id=gift_id)
                    if quantity>0:
                        gift_obj = Gift.objects.get(id=gift_id_obj.id)
                        gift_rate = gift_id_obj.gift_rate_diamond
                        required_diamonds = gift_rate*quantity
                        try:
                            current_available_diamonds = UserAssetsReports.objects.get(user=user).available_diamonds
                        except:
                            current_available_diamonds = UserAssetsReports.objects.create(user=user)
                        
                        balance_diamond = current_available_diamonds-required_diamonds
                        if balance_diamond>=0:
                            UserGiftPurchase.objects.create(user_purchased=user, rate_purchased = gift_rate, total_amount=required_diamonds, quantity=quantity, gift_id=gift_obj)
                            try:
                                user_report_obj = UserAssetsReports.objects.get(user=user)
                                user_report_obj.available_diamonds -= balance_diamond
                                user_report_obj.total_gifts_purchased += quantity
                                user_report_obj.total_gifts_purchased +=quantity
                                user_report_obj.save()
                            except Exception:
                                user_report_obj = UserAssetsReports.objects.create(user=user, total_gifts_purchased=quantity, available_gift=quantity, gift_id=gift_obj)
                        else:
                            remmainng_left_diamonds = abs(balance_diamond)
                            ## get the quantity of coins to purchase these diamond
                            diamond_id_obj = Diamond.objects.all()[:1]
                            diamond_rate = diamond_id_obj[0].diamond_rate
                            required_coin = diamond_rate*remmainng_left_diamonds 
                            current_available_coins = UserAssetsReports.objects.get(user=user).available_coins

                            balance_coin = current_available_coins-required_coin
                            if balance_coin>=0:
                                UserGiftPurchase.objects.create(user_purchased=user, rate_purchased = gift_rate, total_amount=required_diamonds, quantity=quantity, gift_id=gift_obj)
                                try:
                                    user_report_obj = UserAssetsReports.objects.get(user=user)
                                    user_report_obj.available_diamonds = 0
                                    user_report_obj.available_coins = balance_coin
                                    user_report_obj.total_gifts_purchased += quantity
                                    user_report_obj.total_gifts_purchased +=quantity
                                    user_report_obj.save()
                                except Exception:
                                    user_report_obj = UserAssetsReports.objects.create(user=user, total_gifts_purchased=quantity, available_gift=quantity, gift_id=gift_obj)
                            else:
                                remmainng_left_coin = abs(balance_coin)
                                coin_rate = Coin.objects.all()[:1]

                                ## Redirect to get paymnet through paymnet gateway
                                total_amount = coin_rate*remmainng_left_coin
                                print("remaning amount paid")
                                # sucess payment 
                                UserGiftPurchase.objects.create(user_purchased=user, rate_purchased = gift_rate, total_amount=required_diamonds, quantity=quantity, gift_id=gift_obj)
                                try:
                                    user_report_obj = UserAssetsReports.objects.get(user=user)
                                    user_report_obj.available_diamonds = 0
                                    user_report_obj.available_coins = 0
                                    user_report_obj.total_gifts_purchased += quantity
                                    user_report_obj.total_gifts_purchased +=quantity
                                    user_report_obj.save()
                                except Exception:
                                    user_report_obj = UserAssetsReports.objects.create(user=user, total_gifts_purchased=quantity, available_gift=quantity, gift_id=gift_obj)
                        return JsonResponse({"success":True, "message":"Gift Purchased"})
                        
                except Exception as e:
                    return JsonResponse({"success":False, "message":f"{e}"})
            else:
                return JsonResponse({"success":False, "message":f"{e}"})
        except Exception as e:
            return JsonResponse({"success":False, "message":f"{e}"})
    

class AllAssetsAPI(APIView):
    @api_view(['GET'])
    def all_assets_information(request):
        auth_user=custom_firebase_authentication(request)
        try:
            if auth_user:
                data = UserAssetsReports.objects.filter(user__username=auth_user.username).values()
                return JsonResponse({"success":True, "data":list(data) })
            else:
                return JsonResponse({"success":False, "message":f"{e}"})
        except Exception as e:
            return JsonResponse({"success":False, "message":f"{e}"})

    @api_view(['GET'])
    def all_Purchase_report(request):
        auth_user=custom_firebase_authentication(request)
        try:
            if auth_user:
                data = UserCoinPurchase.objects.filter(user_purchased__username=auth_user.username).values()
                return JsonResponse({"success":True, "data":list(data) })
            else:
                return JsonResponse({"success":False, "message":f"{e}"})
        except Exception as e:
            return JsonResponse({"success":False, "message":f"{e}"})

