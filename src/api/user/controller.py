from app.user.models import User
from .values import UserValues

class UserController:
    def __init__(self):
        self.all_user = UserValues.all_user
    def getUsers(self):
        user = User.objects.values(
            *self.all_user
        )
        return user

userController = UserController()