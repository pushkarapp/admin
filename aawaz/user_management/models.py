from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from admin_panel.drop_down_choices import Choices


# class User(AbstractUser):
#     phone_number = models.CharField(max_length=20)

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class UserLavel(BaseModel):
    name = models.CharField(max_length=20)
    total_spending = models.FloatField(default=0.00)
    def __str__(self):
        return self.name


class UserProfile(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    #nickname = models.CharField(max_length=30, unique=True)
    profile_image = models.ImageField(upload_to ='uploads/profile/')
    mobile_number = models.CharField(max_length=15)
    cover_image = models.ImageField(upload_to='uploads/cover/')
    date_of_birth = models.DateField(default=date.today)
    gender = models.CharField(max_length=20, choices=Choices().gender)
    about = models.TextField(max_length=500)
    location = models.CharField(max_length=100)
    lavel = models.ForeignKey('UserLavel', on_delete=models.PROTECT, default=1)
    last_activity = models.DateTimeField(auto_now=True)
    email_verified = models.BooleanField(default=True)
    signid_in_through = models.CharField(max_length=20)
    inactive_till = models.DateTimeField(default=datetime.now())
    address_line_one = models.TextField(max_length=100)
    address_line_two = models.TextField(max_length=100)
    pincode = models.CharField(max_length=6)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=100)
    pan_number = models.CharField(max_length=10)
    pan_verification_date = models.DateTimeField(default=datetime.now(), null=True, blank=True)

    @property
    def age(self):
        days_in_year = 365.2425   
        age = int((date.today() - self.date_of_birth).days / days_in_year)
        return age
    def __str__(self) :
        return self.user.first_name
 

class MemberBlocked(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logged_in_user')
    bolcked_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocked_by_logged_in_user')

    def __str__(self):
        return self.user