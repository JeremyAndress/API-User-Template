from django.test import TestCase
from app.user.models import User, Hash
from datetime import datetime

class HashTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            username = 'Nani',
            first_name = 'Na',
            last_name = 'ni',
            email = 'das@gmail.com',
            age = 5
        )
        user.save()

        data = {
            'user':user,
            'date_end': datetime.now(),
            'hexa': 'fsfasd4sdf5ag2aef54'
        }
        Hash.objects.create(**data)

    def test_animals_can_speak(self):
        lion = Hash.objects.get(hexa="fsfasd4sdf5ag2aef54")
        print('here {}'.format(lion))
