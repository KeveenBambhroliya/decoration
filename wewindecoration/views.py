from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail
from django.contrib import messages
from adminpanel.models import Gallery,Decoration
from account.models import User_Profile
from .models import Cart,Order,OrderImage







# Create your views here.



def index(request):
    return render(request,'Frontend/wewindecoration/Home.html')


def gallery(request):
    gallery= Gallery.objects.all()
    return render(request,'Frontend/wewindecoration/gallery.html',{'gallery':gallery})

def decoration(request):
    decoration= Decoration.objects.all()
    return render(request,'Frontend/wewindecoration/decoration.html',{'decoration':decoration})

def decoration_detail(request, decoration_id):
    decoration= get_object_or_404(Decoration, pk=decoration_id)
    return render(request,'Frontend/wewindecoration/decoration_detail.html',{'decoration':decoration})

# ------------------------------------------------------Cart-------------------------------------------------------
@login_required(login_url='login')
def cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_items = cart.items.all()
            total_price = sum(item.price for item in cart_items)
            return render(request, 'Frontend/wewindecoration/cart.html', {'cart_items': cart_items, 'total_price': total_price})
    return render(request, 'Frontend/wewindecoration/cart.html', {'cart_items': [], 'total_price': 0})
    
@login_required(login_url='login')
def add_to_cart(request, decoration_id):
    decoration = get_object_or_404(Decoration, pk=decoration_id)
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.items.add(decoration)
        return redirect('decoration')  
    else:
        return redirect('login') 
    
@login_required(login_url='login') 
def remove_from_cart(request, decoration_id):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            decoration = get_object_or_404(Decoration, pk=decoration_id)
            cart.items.remove(decoration)  
    return redirect('cart')

@login_required(login_url='login')
def checkout(request):
    user_profile, created = User_Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        date = request.POST.get('date')
        time = request.POST.get('time')

        
        # Update user profile
        user_profile.full_name = full_name
        user_profile.mobile = mobile
        user_profile.address = address
        user_profile.save()

        cart = Cart.objects.filter(user=request.user).first()

        if cart:
            cart_items = cart.items.all()
            total_price = sum(item.price for item in cart_items)
            
        
       
        order = Order.objects.create(
            user_profile=user_profile,
            date=date,
            time=time,
            total_price=total_price,
            
            
           
        )

        if cart:
            for item in cart.items.all():
                
                order_image = OrderImage.objects.create(order=order, image=item.image)

            
            cart.items.clear()
        
        return redirect('/')
    
    return render(request, 'Frontend/wewindecoration/checkout.html',{'user_profile': user_profile})

@login_required(login_url='login')
def order_history(request):
    orders = Order.objects.filter(user_profile__user=request.user)
    return render(request, 'Frontend/wewindecoration/order_history.html', {'orders': orders})

@login_required(login_url='login')
def order_history_details(request,order_id):
    orders = Order.objects.get(id=order_id)
    return render(request, 'Frontend/wewindecoration/order_history_details.html',{'orders': orders})