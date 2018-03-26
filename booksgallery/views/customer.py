# Created by: bhavana
# Created on: 3/26/2018
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, FormView

from booksgallery.forms.customer import CustomerSignUpForm, SelectSearchForm
from booksgallery.models import User
from booksgallery.decorators import customer, admin


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'researcher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('customer:customer_home')


@method_decorator([login_required, customer.customer_required], name='dispatch')
class CustomerHomePage(FormView):
    form_class = SelectSearchForm
    template_name = 'customer_home.html'
