from django.shortcuts import get_object_or_404, render, HttpResponse
from django.contrib.auth.models import User
import  datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from .forms import *
# Create your views here.



class ManageUsers:
    def all_users(request):
        if request.user.is_authenticated:
            users = User.objects.all().order_by('-id')
            context = {
                "users": users,
            }

            return render(request, "user/index.html", context)
        else:
            return redirect("admin-login")

    def create(request):
         if request.user.is_authenticated:
            form = UserForm()
            if request.method == "POST":
                form = UserForm(request.POST)
                detail_form = UserDetailForm(request.POST, request.FILES)
                if form.is_valid():
                    #UserLavel.objects.create(name=1)

                    username = request.POST["username"]
                    password = request.POST["password"]
                    first_name = request.POST["first_name"]
                    last_name = request.POST["last_name"]
                    email = request.POST["email"]
                    status = request.POST["is_active"]
                    mobile_number = request.POST["mobile_number"]
                    profile_image = request.POST.get('profile_image') 
                    cover_image = request.POST.get('cover_image')
                    date_of_birth = request.POST["date_of_birth"]
                    gender = request.POST["gender"]
                    about = request.POST["about"]
                    location = request.POST["location"]
                    lavel = request.POST["lavel"]
                    address_line_one = request.POST["address_line_one"]
                    address_line_two = request.POST["address_line_two"]
                    pincode = request.POST["pincode"]
                    city = request.POST["city"]
                    state = request.POST["state"]
                    pan_number = request.POST["pan_number"]
                    pan_verification_date = request.POST["pan_verification_date"]


                    user_obj = User.objects.create_user(email=email, password=password, username=username)
                
                    user_obj.username = username
                    user_obj.password = password
                    user_obj.first_name = first_name
                    user_obj.last_name = last_name
                    user_obj.email = email
                    user_obj.is_active = status
                    user_obj.save()
                    user_detail_obj = UserProfile()
                    user_detail_obj.mobile_number=mobile_number
                    user_detail_obj.profile_image=profile_image
                    user_detail_obj.cover_image=cover_image
                    user_detail_obj.date_of_birth=date_of_birth
                    user_detail_obj.gender=gender
                    user_detail_obj.about=about
                    user_detail_obj.location=location
                    user_detail_obj.lavel=UserLavel.objects.get(name=lavel)
                    user_detail_obj.user=user_obj
                    user_detail_obj.address_line_one = address_line_one
                    user_detail_obj.address_line_two = address_line_two
                    user_detail_obj.pincode = pincode
                    user_detail_obj.city = city
                    user_detail_obj.state = state
                    user_detail_obj.pan_number = pan_number
                    user_detail_obj.pan_verification_date = pan_verification_date


                    
                    details_= user_detail_obj.save()

                    return redirect(reverse("user_list"))
                else:
                    print("Invalid Form")
            else:
                form = UserForm()
                detail_form = UserDetailForm()

            return render(request, "user/user_form.html", { "form": form, "detail_form":detail_form })


    def user_details(request, username):
        if request.user.is_authenticated:
            user = get_object_or_404(User, username=username)
            user_details = get_object_or_404(UserProfile, user__username=username)
            print(user_details)
            
            return render(request, "user/userdetails.html", { "user": user,"user_details":user_details })
        else:
            return redirect("admin-login")
        

    def user_update(request, username):
        if request.user.is_authenticated:
            user_obj = get_object_or_404(User, username=username)
            user_detail_obj = get_object_or_404(UserProfile, user__username=username)
            print(user_obj)
            if request.method == 'POST':
                form = UserForm(instance=user_obj, data=request.POST)
                if form.is_valid():
                    username = request.POST["username"]
                    password = request.POST["password"]
                    first_name = request.POST["first_name"]
                    last_name = request.POST["last_name"]
                    email = request.POST["email"]
                    status = request.POST["is_active"]
                    mobile_number = request.POST["mobile_number"]
                    profile_image = request.POST.get('profile_image') 
                    cover_image = request.POST.get('cover_image')
                    date_of_birth = request.POST["date_of_birth"]
                    gender = request.POST["gender"]
                    about = request.POST["about"]
                    location = request.POST["location"]
                    lavel = request.POST["lavel"]
                    address_line_one = request.POST["address_line_one"]
                    address_line_two = request.POST["address_line_two"]
                    pincode = request.POST["pincode"]
                    city = request.POST["city"]
                    state = request.POST["state"]
                    pan_number = request.POST["pan_number"]
                    pan_verification_date = request.POST["pan_verification_date"]

                    print(location)
                    user_obj.username = username
                    user_obj.password = password
                    user_obj.first_name = first_name
                    user_obj.last_name = last_name
                    user_obj.email = email
                    user_obj.is_active = status
                    user_obj.save()
                    user_detail_obj.mobile_number=mobile_number
                    user_detail_obj.profile_image=profile_image
                    user_detail_obj.cover_image=cover_image
                    user_detail_obj.date_of_birth=date_of_birth
                    user_detail_obj.gender=gender
                    user_detail_obj.about=about
                    user_detail_obj.location=location
                    user_detail_obj.lavel=UserLavel.objects.get(name=lavel)
                    user_detail_obj.user=user_obj
                    user_detail_obj.address_line_one = address_line_one
                    user_detail_obj.address_line_two = address_line_two
                    user_detail_obj.pincode = pincode
                    user_detail_obj.city = city
                    user_detail_obj.state = state
                    user_detail_obj.pan_number = pan_number
                    user_detail_obj.pan_verification_date = pan_verification_date
                    details_= user_detail_obj.save()
                    #form.save()
                    return redirect(reverse("user_detail", args=[username,]))
            else:
                form = UserForm(instance=user_obj)

            return render(request, "user/user_form.html", { "form": form, "object": user_obj, "object_detail":user_detail_obj})
        else:
            return redirect("admin-login")

    def user_delete(request,username):
        if request.user.is_authenticated:
            user_obj = get_object_or_404(User, username=username)
            user_obj.delete()
            return redirect(reverse("user_list"))
        else:
            return redirect("admin-login")


class ManageCoins:
    def coin_create(request):
        if request.user.is_authenticated:
            if request.method == "POST":
                form = CoinForm(request.POST, request.FILES, )
                if form.is_valid():
                    coin_name = request.POST["coin_name"]
                    coin_image = request.POST.get('coin_image')
                    #coin_image = request.POST["coin_image"]
                    coin_rate = request.POST["coin_rate"]
                    print(coin_name)
                    form.save()
                    return redirect(reverse("coin_list"))
            else:
                form = CoinForm()
            return render(request, "coin/coin_form.html", { "form": form, })
        else:
            return redirect("admin-login")

    
    def coin_list(request):
        if request.user.is_authenticated:
            coins = Coin.objects.all().order_by('-id')
            context = {
                "coins": coins,
            }

            return render(request, "coin/coin_list.html", context)
        else:
            return redirect("admin-login")
    def coin_details(request, id):
        if request.user.is_authenticated:
            coin = get_object_or_404(Coin, pk=id)
            return render(request, "coin/coin_details.html", { "coin": coin, })
        else:
            return redirect("admin-login")

    def coin_update(request, id):
        if request.user.is_authenticated:
            coin_obj = get_object_or_404(Coin, pk=id)
            if request.method == 'POST':
                #form = CoinForm(instance=task_obj, data=request.POST)
                form = CoinForm(request.POST, request.FILES, instance=coin_obj,)
                if form.is_valid():
                    # coin_name = request.POST["coin_name"]
                    # coin_image = request.POST.get('coin_image')
                    # coin_rate = request.POST["coin_rate"]
                    #print(coin_name)
                    form.save()
                    return redirect(reverse("coin_details", args=[id,]))
            else:
                form = CoinForm(instance=coin_obj)

            return render(request, "coin/coin_form.html", { "form": form, "object": coin_obj})
        else:
            return redirect("admin-login")


    def coin_detele(request, id):
        if request.user.is_authenticated:
            coin_obj = get_object_or_404(Coin, username=id)
            coin_obj.delete()
            return redirect(reverse("coin_list"))
        else:
            return redirect("admin-login")


class ManageDiamonds:
    
    def diamond_create(request):
        if request.user.is_authenticated:
            if request.method == "POST":
                form = DiamondForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect(reverse("diamond_list"))
                else:
                    print("Invalid Form")
            else:
                form = DiamondForm()
            return render(request, "diamonds/diamond_form.html", { "form": form, })
        else:
            return redirect("admin-login")

    
    def diamond_list(request):
        if request.user.is_authenticated:
            diamonds = Diamond.objects.all().order_by('-id')
            print(diamonds)
            context = {
                "coins": diamonds,
            }

            return render(request, "diamonds/diamond_list.html", context)
        else:
            return redirect("admin-login")

    def diamond_details(request, id):
        if request.user.is_authenticated:
            diamond = get_object_or_404(Diamond, pk=id)
            return render(request, "diamonds/diamond_details.html", { "coin": diamond, })
        else:
            return redirect("admin-login")


    def diamond_update(request, id):
        if request.user.is_authenticated:
            diamond_obj = get_object_or_404(Diamond, pk=id)
            if request.method == 'POST':
                #form = CoinForm(instance=task_obj, data=request.POST)
                form = DiamondForm(request.POST, request.FILES, instance=diamond_obj,)
                if form.is_valid():
                    form.save()
                    return redirect(reverse("diamond_details", args=[id,]))
            else:
                form = DiamondForm(instance=diamond_obj)
                                
            return render(request, "diamonds/diamond_form.html", { "form": form, "object": diamond_obj})
        else:
            return redirect("admin-login")


    def diamond_detele(request, id):
        if request.user.is_authenticated:
            diamond_obj = get_object_or_404(DiamondForm, username=id)
            diamond_obj.delete()
            return redirect(reverse("diamond_list"))
        else:
            return redirect("admin-login")



class ManageGifts:
    def gift_create(request):
        if request.user.is_authenticated:
            if request.method == "POST":
                form = GiftForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect(reverse("gift_list"))
                else:
                    print("Invalid Form")
            else:
                form = GiftForm()
            return render(request, "gifts/gift_form.html", { "form": form, })
        else:
            return redirect("admin-login")

    
    def gift_list(request):
        if request.user.is_authenticated:
            gifts = Gift.objects.all().order_by('-id')
            context = {
                "coins": gifts,
            }

            return render(request, "gifts/gift_list.html", context)
        else:
            return redirect("admin-login")

    def gift_details(request, id):
        if request.user.is_authenticated:
            gift = get_object_or_404(Gift, pk=id)
            return render(request, "gifts/gift_details.html", { "coin": gift, })
        else:
            return redirect("admin-login")


    def gift_update(request, id):
        if request.user.is_authenticated:
            gift_obj = get_object_or_404(Gift, pk=id)
            if request.method == 'POST':
                #form = CoinForm(instance=task_obj, data=request.POST)
                form = GiftForm(request.POST, request.FILES, instance=gift_obj,)
                if form.is_valid():
                    form.save()
                    return redirect(reverse("gift_details", args=[id,]))
            else:
                form = GiftForm(instance=gift_obj)
                                
            return render(request, "gifts/gift_form.html", { "form": form, "object": gift_obj})
        else:
            return redirect("admin-login")


    def gift_detele(request, id):
        if request.user.is_authenticated:
            gift_obj = get_object_or_404(GiftForm, username=id)
            gift_obj.delete()
            return redirect(reverse("gift_list"))
        else:
            return redirect("admin-login")




class UsersRooms:

    def room_list(request):
        if request.user.is_authenticated:
            return render(request, "rooms/room_list.html")
        else:
            return redirect("admin-login")





class Reports:
    def assets_report(request):
        if request.user.is_authenticated:
            assets = UserAssetsReports.objects.all().order_by('-total_gifts_purchased')
            context = {
                "assets": assets,
            }
            return render(request, "reports/user_available_assets.html", context)
        else:
            return redirect("admin-login")


def products(request):
    context = {'form':ProductForm(),}
    return render(request, "add_product.html", context)

def login_view(request, *args, **kwargs):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("user_list")


    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            if user.is_superuser:   
                return redirect("/_admin")
            # if destination:
            #     return redirect(destination)
            return redirect("user_list")
    else:
        form = AccountAuthenticationForm()

    context["login_form"] = form

    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("/_admin/login")