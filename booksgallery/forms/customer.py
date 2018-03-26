# Created by: bhavana
# Created on: 3/26/2018
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from booksgallery.models import User


class CustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_researcher = True
        user.save()
        return user
