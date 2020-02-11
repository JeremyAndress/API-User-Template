# from django.test import TestCase
from unittest import TestCase
from app.user.models import User, UserHash
from datetime import datetime
from random import random

class HashTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            username = f'AlexFlinn-{random()}',
            first_name = 'Alex',
            last_name = 'Flinn',
            email = 'alexflinn@gmail.com',
            age = 25
        )
        user.save()

        data = {
            'user':user,
            'date_end': datetime.now(),
            'hexa': 'fsfasd4sdf5ag2aef54'
        }
        UserHash.objects.create(**data)
    def compare_hash(self):
        userhash = UserHash.objects.get(hexa="fsfasd4sdf5ag2aef54")
        print('User : {}'.format(userhash))
