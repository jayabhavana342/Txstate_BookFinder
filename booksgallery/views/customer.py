# Created by: bhavana
# Created on: 3/26/2018
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic.edit import FormMixin

from booksgallery.cart import Cart
from booksgallery.decorators import customer
from booksgallery.forms.customer import CustomerSignUpForm, SelectSearchForm, CartAddBookForm
from booksgallery.models import User, BookDetails


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
    second_form_class = CartAddBookForm
    template_name = 'customer_home.html'
    model = BookDetails

    success_url = reverse_lazy('customer:customer_cart')

    def get_queryset(self):
        object_list = super().get_queryset()

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

        return object_list

    def get_context_data(self, **kwargs):
        context = super(CustomerHomePage, self).get_context_data(**kwargs)

        if 'form' not in context:
            context['form'] = self.form_class
        if 'form2' not in context:
            context['form2'] = self.second_form_class

        # for item in Cart(self.request):
        #     item['update_quantity_form'] = CartAddBookForm(initial={
        #         'quantity': str(item['quantity']),
        #         'update': True,
        #     })

        if 'form2' in self.request.GET:
            cart = Cart(self.request)
            book = get_object_or_404(BookDetails, id=self.request.GET.get('book_id'))

            form = CartAddBookForm(self.request.GET)

            if form.is_valid():
                cd = form.cleaned_data
                cart.add(book=book.id,
                         title=book.title,
                         price=book.price,
                         quantity=cd['quantity'],
                         update_quantity=cd['update'])

        # if 'form3' not in context:
        #     context['form3'] = CartAddBookForm()
        #
        # if 'form3' in self.request.GET:
        #     cart = Cart(self.request)
        #     form = CartAddBookForm(self.request.GET)
        #     book = get_object_or_404(BookDetails, id=self.request.GET.get('book_id'))
        #     print(book)
        #
        #     if form.is_valid():
        #         cd = form.cleaned_data
        #         cart.update(book=book.id,
        #                     price=book.price,
        #                     quantity=cd['quantity'],
        #                     update_quantity=cd['update']
        #                     )

        context['cart'] = Cart(self.request)
        for item in context['cart']:
            print(item)
            print('------')
        context['search'] = self.get_queryset()
        return context


def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(BookDetails, id=book_id)
    cart.remove(book)
    return redirect('cart:cart_details')


class CustomerCartPage(CustomerHomePage):
    template_name = 'customer_cart.html'
