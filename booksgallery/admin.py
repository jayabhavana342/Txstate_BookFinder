from django.contrib import admin
from booksgallery.models import User, BookDetails, ShoppingCart, CreditCardDetails, ProfessorDetail, Customer, Courses

admin.site.register(User)
admin.site.register(BookDetails)
admin.site.register(ShoppingCart)
admin.site.register(Customer)
admin.site.register(CreditCardDetails)
admin.site.register(ProfessorDetail)
admin.site.register(Courses)
