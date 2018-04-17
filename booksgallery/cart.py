# Created by: bhavana
# Created on: 4/7/2018
from decimal import Decimal
# from Scripts._decimal import Decimal

from Txstate_BookFinder import settings
from booksgallery.forms.customer import CartAddBookForm
from booksgallery.models import BookDetails


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, book, title,  price, quantity=1, update_quantity=False):
        book_id = str(book)
        print(book)
        print(title)
        if book_id not in self.cart:
            self.cart[book_id] = {'quantity': 0,
                                  'price': str(price),
                                  'title': title}

        if update_quantity:
            self.cart[book_id]['quantity'] = quantity
        else:
            self.cart[book_id]['quantity'] += quantity

        print(self.cart[book_id])

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, book):
        book_id = str(book)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def __iter__(self):
        book_ids = self.cart.keys()

        books = BookDetails.objects.filter(id__in=book_ids)

        for book in books:
            self.cart[str(book.id)]['book'] = book.title

        for item in self.cart.values():
            item['price'] = str(item['price'])
            item['total_price'] = float(item['price']) * float(item['quantity'])
            yield item

        print(self.cart)

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def total_count(self):
        return len(self.cart)

    def update(self, book, price, quantity, update_quantity):
        book_id = str(book)
        if book_id in self.cart:
            self.cart[book_id]['quantity'] = quantity
            self.save()
