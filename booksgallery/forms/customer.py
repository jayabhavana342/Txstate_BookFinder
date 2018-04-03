# Created by: bhavana
# Created on: 3/26/2018
from django import forms
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


class SelectSearchForm(forms.Form):
    CHOICES = (
        (1, "Select Search Type"),
        (2, "ISBN"),
        (3, "Title"),
        (4, "Author"),
        (5, "Course"),
        (6, "Professor"),

    )
    select_type_of_search = forms.ChoiceField(choices=CHOICES)
    search = forms.CharField(
        max_length=2000,
        widget=forms.TextInput(),
    )

    class Meta:
        fields = ['select_type_of_search', 'search']
