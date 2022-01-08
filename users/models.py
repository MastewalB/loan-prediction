from django.db import models
from django.core.mail import send_mail
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


def upload_to(instance, filename):
    return '{datetime}{filename}'.format(datetime=datetime.now(), filename=filename)


class User(AbstractUser):
    # username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    # email = models.EmailField(max_length=255, unique=True)
    profile_pic = models.ImageField(
        upload_to=upload_to, default='media\\user-default.jpg')

    def email_user(self, subject, message, from_email=None):

        send_mail(subject, message, from_email, [self.email])
