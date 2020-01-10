from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.IntegerField(null=True,blank=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return "{}".format(self.username)

'''
AbstractBaseUser:
    -id
    -password
    -last_login

AbstractUser:
    -username
    -first_name
    -last_name
    -email
    -password
    -groups
    -user_permissions
    -is_staff
    -is_active
    -is_superuser
    -last_login
    -date_joined
'''