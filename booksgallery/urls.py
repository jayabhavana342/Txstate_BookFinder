from django.urls import path, include

from .views import booksgallery, customer

# app_name = 'booksgallery'

urlpatterns = [
    path('', booksgallery.home, name='home'),

    path('customer/', include(([
                                   path('', customer.CustomerHomePage.as_view(), name='customer_home'),
                                   path('cart/', customer.CustomerCartPage.as_view(), name='customer_cart'),
                               ], 'booksgallery'), namespace='customer')),
]
