from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from .models import Product, CartItem
from django.http import JsonResponse
# Create your views here.
@login_required
def index(request):
    context = {
        'variable1': 'this is sent',
        'variable2': 'great',
    }
    messages.success(request, "Your message has been sent")
    return render(request, 'index.html', context)
    #return HttpResponse("this is homepage")

@login_required
def about(request):
    return render(request, 'cart.html')
    #return HttpResponse("this is my about page")

@login_required
def services(request):
    #return render(request, 'product.html')
    product = Product.objects.all()
    return render(request, "product.html", {"product": product})
    #return HttpResponse("this is my services page")

@login_required
def contact(request):
    if request.method == "POST":
        email= request.POST.get('email')
        desc= request.POST.get('desc')
        contact = Contact(email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent")
    return render(request, 'contact.html')
    #return HttpResponse("this is my contact page")

@login_required
def home(request):
    return render (request, "index.html", {})


def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {'form': form})


def logout(request):
    return render(request, "registration/logout.html")


def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity", 1)

        try:
            product = Product.objects.get(id=product_id)
            cart_item, created = CartItem.objects.get_or_create(product=product)
            cart_item.quantity = int(quantity)
            cart_item.save()
            message = "product added to cart successfully" if created else "product quantity updated in the cart."
            #return JsonResponse({"status": "success", "message": message})
        except Product.DoesNotExist:
            return JsonResponse({"status": "error", "message": "product does not exist."})
    return redirect("/about")

@login_required
def cart(request):
    cart_items = CartItem.objects.all()
    cart_items_count = cart_items.count()  # Get the count of cart items
    return render(request, "cart.html", {"cart_items": cart_items, "cart_items_count": cart_items_count})


def remove_from_cart(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.delete()
        #return JsonResponse({"status": "success", "message": "Product removed from cart successfully."})
    except CartItem.DoesNotExist:
        return JsonResponse({"status": "error", "message": "product does not exist in the cart."})
    return redirect("/about")





