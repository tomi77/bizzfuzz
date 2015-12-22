import random

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import pre_save


class UserProfileManager(BaseUserManager):
    def create_user(self, username, password, birthday, **extra_fields):
        user = self.model(username=username, birthday=birthday, is_superuser=False)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password, birthday, **extra_fields):
        user = self.model(username=username, birthday=birthday, is_superuser=True)
        user.set_password(password)
        user.save()

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=40, unique=True, db_index=True)
    birthday = models.DateField()
    random_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['birthday']

    class Meta:
        swappable = 'AUTH_USER_MODEL'


def generate_random_number(sender, instance, **kwargs):
    if instance.pk is None:
        instance.random_number = random.random() * 100


pre_save.connect(generate_random_number, sender=UserProfile)
