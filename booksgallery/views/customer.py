# Created by: bhavana
# Created on: 3/26/2018
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, FormView, ListView
from django.views.generic.edit import FormMixin

from booksgallery.forms.customer import CustomerSignUpForm, SelectSearchForm
from booksgallery.models import User, BookDetails
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
class CustomerHomePage(FormMixin, ListView):
    form_class = SelectSearchForm
    template_name = 'customer_home.html'
    model = BookDetails

    def get_queryset(self):
        object_list = super().get_queryset()

        print("Before:")
        print(object_list)

        query = self.request.GET.get('search')
        choice = self.request.GET.get('select_type_of_search')

        if choice:
            choice = int(choice)
        # choice = SelectSearchForm().fields['select_type_of_search'].choices[int(choice)-1][1]

        if choice == 2:
            object_list = BookDetails.objects.filter(isbn__icontains=query)
        elif choice == 3:
            print("yes")
            object_list = BookDetails.objects.filter(title__icontains=query)
        elif choice == 4:
            object_list = BookDetails.objects.filter(authors__icontains=query)
        elif choice == 5:
            object_list = BookDetails.objects.filter(Q(course_books__course_name__icontains=query) |
                                                     Q(course_books__course_id__icontains=query)).distinct()
        elif choice == 6:
            object_list = BookDetails.objects.filter(course_books__professor__name__icontains=query)
        else:
            object_list = BookDetails.objects.all()

        print("After:")
        print(object_list)

        return object_list
