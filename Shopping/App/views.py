from django.shortcuts import render, redirect
from .models import Cart, Product, OrderPlaced, Customer
from django.views import View
from .forms import CustomerRegistration, CustomerProfileForm
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import choices
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage

class ProductView(View):
    def get(self, request):
        topwear = Product.objects.filter(category='TW')
        bottomwear = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        return render(request, 'App/home.html', {'topwears': topwear, 'bottomwear': bottomwear, 'mobiles': mobiles})


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'App/productdetail.html', {'product': product, 'item_already_in_cart': item_already_in_cart})


@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')


@login_required
def show_cart(request):
    cart = Cart.objects.filter(user=request.user)
    if cart.exists():
        amount = sum((item.quantity * item.product.discounted_price)
                    for item in cart)
        shipping_amount = 70.0 if amount >= 500 else 0.0
        total_amount = amount + shipping_amount
        return render(request, 'App/addtocart.html', {'carts': cart, 'totalamount': total_amount, 'amount': amount, 'shipping_amount': shipping_amount})
    return render(request,'App/emptycart.html')

def update_cart(request, prod_id, quantity_delta):
    if request.method == "GET":
        cart_item = Cart.objects.get(product=prod_id, user=request.user)
        cart_item.quantity += quantity_delta
        cart_item.save()

    cart_product = Cart.objects.filter(user=request.user)
    amount = sum((item.quantity * item.product.discounted_price)
                 for item in cart_product)
    shipping_amount = 70.0 if amount >= 500 else 0.0

    data = {
        'quantity': cart_item.quantity,
        'amount': amount,
        'total_amount': amount + shipping_amount,
        'shipping_amount': shipping_amount,
    }
    return JsonResponse(data)


def plus_cart(request):
    return update_cart(request, request.GET['prod_id'], 1)


def minus_cart(request):
    return update_cart(request, request.GET['prod_id'], -1)


def remove_cart(request):
    prod_id = request.GET['prod_id']
    Cart.objects.filter(product=prod_id, user=request.user).delete()

    cart_product = Cart.objects.filter(user=request.user)
    amount = sum((item.quantity * item.product.discounted_price)
                 for item in cart_product)
    shipping_amount = 70.0 if amount >= 500 else 0.0

    data = {
        'amount': amount,
        'total_amount': amount + shipping_amount,
        'shipping_amount': shipping_amount,
    }
    return JsonResponse(data)


def buy_now(request):
    return render(request, 'App/buynow.html')


def profile(request):
    return render(request, 'App/profile.html')

@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'App/address.html', {'add': add, 'active': 'btn-primary'})

@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'App/orders.html', {'order_placed': op})


def mobile(request, data=None):
    filter_options = choices.filter_options_m
    mobiles_filter = filter_options.get(data, filter_options[None])
    mobiles = Product.objects.filter(**mobiles_filter)
    return render(request, 'App/mobile.html', {'mobiles': mobiles})


def Topwear(request, data=None):
    filter_options = choices.filter_options_tw
    topwear_filter = filter_options.get(data, filter_options[None])
    topwear = Product.objects.filter(**topwear_filter)

    return render(request, 'App/Topwear.html', {'topwear': topwear})


def Bottomwear(request, data=None):
    filter_options = choices.filter_options_bw
    bottom_wear_filter = filter_options.get(data, filter_options[None])
    bottom_wear = Product.objects.filter(**bottom_wear_filter)
    return render(request, 'App/Bottomwear.html', {'bottomwear': bottom_wear})


def laptop(request, data=None):
    filter_option = choices.filter_options_l
    laptop_filter = filter_option.get(data, filter_option[None])
    laptop_device = Product.objects.filter(**laptop_filter)
    return render(request, 'App/Laptop.html', {'laptop': laptop_device})


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistration()
        return render(request, 'App/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulation! Registration Successful')
        return render(request, 'App/customerregistration.html', {'form': form})


@login_required
def checkout(request):
    user = request.user
    print(user)
    add = Customer.objects.filter(user=user)
    print(add)
    cart_item = Cart.objects.filter(user=user)
    print(cart_item)
    amount = 0.0
    shipping_amount = 0.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    
    if cart_product:
        for i in cart_product:
            tempamount = (i.quantity * i.product.discounted_price)
            amount += tempamount
            if amount <= int(500):
                shipping_amount = 0.0
            else:
                shipping_amount = 70.0
        total_amount = amount + shipping_amount
        print(total_amount)
    return render(request, 'App/checkout.html', {'add': add, 'totalamount': total_amount, 'Cart': cart_item})


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'App/profile.html', {'form': form, 'active': 'btn-primary'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality,
                           city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(
                request, 'Congratulations !! Profile Updated Successfully')
        return render(request, 'App/profile.html', {'form': form, 'active': 'btn-primary'})


@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer,
                    product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")

def Search_data(request):
    queryset = Product.objects.all()

    if request.GET.get('search'):
        Search = request.GET.get('search')
        queryset = queryset.filter(
            Q(title__icontains=Search) |
            Q(description__icontains=Search) |
            Q(brand__icontains=Search)
        )
    # Apply ordering by 'id' in ascending order
    queryset = queryset.order_by('id')
    # Boolean Operation
    page_number = request.GET.get("page", 1)
    paginator = Paginator(queryset, 5)  # Pagination
    try:
        page_obj = paginator.page(page_number)
    except EmptyPage:
        page_obj = paginator.page(1)
    return render(request, 'App/Search.html', {'queryset': page_obj})
