# Created by: bhavana
# Created on: 3/25/2018
from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        # if request.user.is_uploader and request.user.is_superuser:
        #     return redirect('uploader:uploader_home')
        # else:
        if request.user.is_authenticated:
            return redirect('customer:customer_home')
    return render(request, 'booksgallery/home.html')