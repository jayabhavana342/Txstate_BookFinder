from django.contrib.auth.models import AbstractUser
from django.db import models


class CreditCardDetails(models.Model):
    CHOICES = (
        ("VISA", "VISA"),
        ("DISCOVER", "DISCOVER"),
        ("MASTER CARD", "MASTER CARD"),
        ("AMERICAN EXPRESS", "AMERICAN EXPRESS"),
    )
    card_num = models.CharField(max_length=19)
    card_type = models.CharField(max_length=20, choices=CHOICES)

    def __str__(self):
        return self.card_num + " " + self.card_type


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class BookDetails(models.Model):
    isbn = models.CharField(max_length=100, null=False)
    title = models.CharField(max_length=500, null=False)
    authors = models.CharField(max_length=500, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=3, max_length=10, null=False)
    image = models.ImageField(width_field=30, height_field=40, null=False)
    publish_date = models.DateField()

    def __str__(self):
        return self.title


class ShoppingCart(models.Model):
    id = models.UUIDField(primary_key=True, max_length=10)
    books = models.ForeignKey(BookDetails, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='researchers')
    shoppingCart = models.OneToOneField(ShoppingCart, on_delete=models.CASCADE)
    cards = models.ForeignKey(CreditCardDetails, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Courses(models.Model):
    course_id = models.CharField(max_length=10, null=False)
    course_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.course_id


class ProfessorDetail(models.Model):
    name = models.CharField(max_length=100, null=False)
    website = models.URLField()
    course_thought = models.ForeignKey(Courses, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name
