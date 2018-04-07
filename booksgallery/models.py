from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q


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
    price = models.DecimalField(decimal_places=2, max_digits=5, max_length=10, null=False)
    image = models.ImageField(upload_to='books_images', null=False)
    publish_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title


class ShoppingCart(models.Model):
    id = models.UUIDField(primary_key=True, max_length=10)
    books = models.ForeignKey(BookDetails, on_delete=models.CASCADE, related_name='cart_books')

    def __str__(self):
        return self.id


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='customer')
    shoppingCart = models.OneToOneField(ShoppingCart, on_delete=models.CASCADE)
    cards = models.ForeignKey(CreditCardDetails, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class ProfessorDetail(models.Model):
    name = models.CharField(max_length=100, null=False)
    website = models.URLField()

    def __str__(self):
        return self.name


class Courses(models.Model):
    course_id = models.CharField(max_length=10, null=False)
    course_name = models.CharField(max_length=100, null=False)
    professor = models.ForeignKey(ProfessorDetail, on_delete=models.CASCADE, null=True, related_name='course_professors')
    book = models.ForeignKey(BookDetails, on_delete=models.CASCADE, null=True, related_name='course_books')

    def __str__(self):
        return self.course_id
