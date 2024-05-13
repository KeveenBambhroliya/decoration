from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from adminpanel.models import Gallery,Category,Decoration
from wewindecoration.models import Order,Cart
from account.models import User_Profile,ContactForm 
from django.db import connection
from django.core.management import call_command






def admin_login(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            admin_user = User.objects.filter(username=username)

            #username
            if not admin_user.exists():
                return HttpResponse('not found!!!')
            
            #login for admin
            admin_user = authenticate(username=username, password=password)
            if admin_user is not None and admin_user.is_superuser:  
                
                login(request,admin_user)
                return redirect('admin_home')
            
            else:
                return HttpResponse('thi id is not for admin!!!')

    return render(request,'Backend/accounts/admin_login.html')

def admin_logout(request):
     logout(request)
     return redirect('home')

@staff_member_required(login_url='admin_login')
def admin_home(request):
     return render(request,'Backend/adminpanel/admin_home.html')

@staff_member_required(login_url='admin_login')
def admin_gallery_management(request):
        categories = Category.objects.all()
        selected_category_id = request.GET.get('category')

        if selected_category_id:
            selected_category = Category.objects.get(pk=selected_category_id)
            gallery_list = Gallery.objects.filter(category=selected_category)
        else:
            selected_category = None
            gallery_list = Gallery.objects.all()
        
        context = {
            'categories': categories,
            'selected_category': selected_category,
            'gallery_list': gallery_list,
        }
        
        return render(request,'Backend/adminpanel/Gallery_managment.html',context)

@staff_member_required(login_url='admin_login')
def add_gallery(request):
    
    
    categories = Category.objects.all()

    if request.method == 'POST':
        type = request.POST.get('type')
        date = request.POST.get('date')
        image = request.POST and request.FILES.get('image')
        category_id = request.POST['category']
        
        if category_id :
            category = Category.objects.get(pk=category_id)
        else:
            category = None
       
        form = Gallery(type=type,date=date,image=image,category=category)
        form.save()


        return redirect('admin_gallery_management')
    return render(request,'Backend/adminpanel/Add_gallery.html',{'categories': categories})


@staff_member_required(login_url='admin_login')
def edit_gallery(request, item_id):
     
     
     item = get_object_or_404(Gallery, pk=item_id)

     if request.method == 'POST':
        
        new_type = request.POST.get('type')
        new_date = request.POST.get('date')
        
        if 'image' in request.FILES:
            new_image = request.FILES['image']
            item.image.delete(save=False)

        else:
            
            new_image = item.image

        # Update the item's data
        item.type = new_type
        item.date = new_date
        item.image = new_image
        item.save()


        return redirect('admin_gallery_management')

     return render(request, 'Backend/adminpanel/Edit_gallery.html', {'item': item})

@staff_member_required(login_url='admin_login')
def delete_gallery(request, item_id):
    
     
     item = get_object_or_404(Gallery, id=item_id)

     # for image delete
     item.image.delete(save=False)


     item.delete()
     return redirect('admin_gallery_management')


# -----------------------------------------------Category_Management-------------------------------------------------

@staff_member_required(login_url='admin_login')
def admin_category_management(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if Category.objects.filter(name=name).exists():
            messages.error(request, 'A category with this name already exists.')            
            return redirect('admin_category_management')
        else:
            form = Category(name=name)
            form.save()
        return redirect('admin_category_management')

    categories = Category.objects.all()

    return render(request,'Backend/Category_Management/Category_management.html',{'categories':categories})




@staff_member_required(login_url='admin_login')
def edit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    if request.method == 'POST':
        name = request.POST.get('name')
       
        # Update the category with the new values
        category.name = name
        category.save()

        
        return redirect('admin_category_management')
    return render(request,'Backend/Category_Management/Edit_category.html',{'category': category})





@staff_member_required(login_url='admin_login')
def delete_category(request,category_id):
     category = get_object_or_404(Category, id=category_id)
     category.delete()
     return redirect('admin_category_management')



# -----------------------------------------------Decoration_Management-------------------------------------------------

@staff_member_required(login_url='admin_login')
def admin_decoration_management(request):
        categories = Category.objects.all()
        selected_category_id = request.GET.get('category')

        if selected_category_id:
            selected_category = Category.objects.get(pk=selected_category_id)
            decoration_list = Decoration.objects.filter(category=selected_category)
        else:
            selected_category = None
            decoration_list = Decoration.objects.all()
        
        context = {
            'categories': categories,
            'selected_category': selected_category,
            'decoration_list': decoration_list,
        }
        
        return render(request,'Backend/Decoration_Management/Decoration_management.html',context)

@staff_member_required(login_url='admin_login')
def add_decoration(request):
    
    
    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        details = request.POST.get('details')
        image = request.POST and request.FILES.get('image')
        category_id = request.POST['category']
        
        if category_id :
            category = Category.objects.get(pk=category_id)
        else:
            category = None
       
        form = Decoration(name=name,price=price,details=details,image=image,category=category)
        form.save()


        return redirect('admin_decoration_management')
    return render(request,'Backend/Decoration_Management/Add_decoration.html',{'categories': categories})


@staff_member_required(login_url='admin_login')
def edit_decoration(request, item_id):
     
     
     item = get_object_or_404(Decoration, pk=item_id)

     if request.method == 'POST':
        
        new_name = request.POST.get('name')
        new_price = request.POST.get('price')
        new_details = request.POST.get('details')

        
        
        if 'image' in request.FILES:
            new_image = request.FILES['image']
            item.image.delete(save=False)

        else:
            
            new_image = item.image

        # Update the item's data
        item.name = new_name
        item.price = new_price
        item.details = new_details
        item.image = new_image
        item.save()


        return redirect('admin_decoration_management')

     return render(request, 'Backend/Decoration_Management/Edit_decoration.html', {'item': item})

@staff_member_required(login_url='admin_login')
def delete_decoration(request, item_id):
    
     
     item = get_object_or_404(Decoration, id=item_id)

     # for image delete
     item.image.delete(save=False)


     item.delete()
     return redirect('admin_decoration_management')


@staff_member_required(login_url='admin_login')
def admin_order_management(request):
    orders = Order.objects.all()   
    return render(request,'Backend/Order/order.html',{'orders': orders})

@staff_member_required(login_url='admin_login')
def order_details(request,order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,'Backend/Order/order_details.html',{'order': order})

@staff_member_required(login_url='admin_login')
def order_detail(request, order_id):
    order = Order.objects.prefetch_related('images').get(id=order_id)
    return render(request, 'Backend/Order/order_details.html', {'order': order})


@staff_member_required(login_url='admin_login')
def contactus(request):
    contact = ContactForm.objects.all()
    return render(request, 'Backend/accounts/contactus.html', {'contact': contact})

@staff_member_required(login_url='admin_login')
def contactusdetails(request,contact_id):
    contact = ContactForm.objects.get(id=contact_id)
    return render(request, 'Backend/accounts/contactusdetails.html', {'contact': contact})


# -------------------------------------------------Reset_Database------------------------------------------
@staff_member_required(login_url='admin_login')
def reset_database(request):
    if request.method == 'POST':
        call_command('flush', interactive=False)
        return HttpResponse("Database reset successfully!")
    else:
        return render(request, 'Backend/reset_database/reset_database.html')



@staff_member_required(login_url='admin_login')
def reset_tables(request):
    if request.method == 'POST':
        selected_tables = request.POST.getlist('tables')
        if selected_tables:
            with connection.cursor() as cursor:
                for table_name in selected_tables:
                    cursor.execute(f'TRUNCATE TABLE {table_name};')
            return render(request, 'Backend/reset_database/reset_tables.html', {'success_message': 'Tables reset successfully!'})           
        else:
            return render(request, 'Backend/reset_database/reset_tables.html', {'error_message': 'No tables selected!'})
    else:
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES;")
            table_names = [row[0] for row in cursor.fetchall()]
        return render(request, 'Backend/reset_database/reset_tables.html', {'table_names': table_names})