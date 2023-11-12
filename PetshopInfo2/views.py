from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Max
from .models import Pets, CartItem
from .forms import PetsForm, PetUpdateForm
import openpyxl
from openpyxl.styles import PatternFill, Border, Side, Font
from openpyxl.utils import get_column_letter
from unidecode import unidecode
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import Q
from .models import *
import re
import json
from django.http import JsonResponse


# Connexion - login -logout
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass']

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            username = user.username
            prop = Pets.objects.all()
            cart_count = CartItem.objects.count()
            return render(request, 'shops/index2.html', {'username':username, 'prop': prop, 'cart_count':cart_count})
        else:
            messages.error(request,"Bad credentials")
            return render(request, 'general_tabs/registration_error.html')
    return render(request, 'registration/signin.html')

def signup(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            pass1 = request.POST.get('pass1')
            pass2 = request.POST.get('pass2')
            if User.objects.filter(username=username):
                messages.error(request, "Le nom d'utilisateur existe déjà")
                return render(request, 'general_tabs/error_username.html')
            if User.objects.filter(email=email):
                messages.error(request, "Le mail d'utilisateur existe déjà")
                return render(request, 'general_tabs/error_mail.html')

            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Votre compte a été créé avec succès")
            return redirect('signin')
        except Exception:
            return render(request, 'registration/signup.html')
    return render(request, 'registration/signup.html')

def terminer_la_session(request):
    logout(request)
    return render(request, 'registration/logout.html')
    

# Accueil
def accounts(request):
    return render(request, "registration/login.html")
def accueil(request):
    return render(request, "general_tabs/accueil.html")
def inicio(request):
    return render(request, "general_tabs/accueil.html")


@login_required
def shops(request):
    prop = Pets.objects.all()
    return render(request, "shops/statusAnimal.html", {'prop':prop}) 

@login_required
def index2(request):
    prop = Pets.objects.all()
    cart_count = CartItem.objects.count()
    return render(request, "shops/index2.html",{'prop':prop, 'cart_count':cart_count})

# Accès à la vue administrateur
def admin(request):
    return render(request, "admin.py") 

def is_valid_name(name):
    # Utiliza una expresión regular para verificar que solo hay letras y espacios
    return re.match("^[a-zA-Z ]*$", name)

def update_pet(request, pet_name):
    try:
        pet = get_object_or_404(Pets, name=pet_name)

        if request.method == 'POST':
            new_name = request.POST.get('name')

            # Verifica que el nuevo nombre sea válido
            if not is_valid_name(new_name):
                return render(request, 'general_tabs/error_update.html')

            pet.name = new_name
            pet.price = request.POST.get('price')
            pet.sold = request.POST.get('sold')
            pet.hungry = request.POST.get('hungry')
            pet.location = request.POST.get('location')
            print(request.POST.get('location'))
            pet.save()

            return render(request, 'general_tabs/update_pet.html')

    except:
        return render(request, 'general_tabs/error_update.html')

def delete_pet(request, pet_name):
    pet = get_object_or_404(Pets, name=pet_name)
    if request.method == 'POST':
        pet.delete()
        return render(request, 'general_tabs/delete_pet_conf.html', {'pet': pet})
    return render(request, 'general_tabs/delete_pet_conf.html', {'pet': pet})

# def new_pet(request):
#     if request.method == 'POST':
#         form = PetsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index2')  # Cambia 'nombre_de_la_url_donde_quieres_redirigir' a la URL a la que deseas redirigir después de agregar la mascota.
#     else:
#         form = PetsForm()
#     return render(request, 'shops/new_pet.html', {'form': form})

def create_pet(request):
    if request.method == 'POST':
        form = PetsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'shops/successful_creation.html') # Cambia 'nombre_de_la_url_donde_quieres_redirigir' a la URL a la que deseas redirigir después de agregar la mascota.
    else:
        form = PetsForm()
    return render(request, 'shops/new_pet.html', {'form': form})


def cart(request):
    cart_info = CartItem.objects.all()
    total_price = sum(item.price for item in cart_info)
    # for i in cart_info:
    #     print(f" EL NOMBRE ES: {i.name}")
    #     print(F" EL PRECIO ES : {i.price} ")
    #print("SI SE LLAMA LA FUNCION")
    #print(f"LA INFO QUE SE PASA ES : {cart_info}")
    return render(request, 'shops/cart.html', {'cart_info': cart_info, 'total_price': total_price})

def get_cart_count(request):
    cart_count = CartItem.objects.count()
    return JsonResponse({'carritoCount': cart_count})

def product_list(request):
    # Tu lógica actual para obtener los productos
    prop = Pets.objects.all()

    if request.method == 'POST':
        # Manejar la lógica de agregar al carrito aquí
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')

        # Agregar el elemento al carrito (usando sesiones para almacenar temporalmente)
        cart_item = CartItem(name=product_name, price=product_price)
        # print(f" EL NOMBRE ES: {cart_item.name}")
        # print(F" EL PRECIO ES : {cart_item.price} ")
        cart_item.save()
        #print(CartItem.objects.all())

        # Devolver una respuesta JSON indicando el éxito y la nueva cantidad en el carrito
        # return JsonResponse({'success': True, 'carritoCount': CartItem.objects.count()})
    cart_count = CartItem.objects.count()

    return render(request, "shops/index2.html", {'prop': prop, 'cart_count':cart_count})


def buy_items(request):
    # Obtén todos los elementos en el carrito
    cart_items = CartItem.objects.all()

    # Vende cada elemento y actualiza la base de datos
    for item in cart_items:
        pet = Pets.objects.get(name=item.name)
        pet.sell_pet()

    # Vacía el carrito
    CartItem.objects.all().delete()

    # Redirige a la página de confirmación de compra
    return render(request, "shops/confirmation_of_purchase.html")


def delete_item(request, item_name):
    item_to_delete = CartItem.objects.get(name=item_name)
    item_to_delete.delete()
    cart_info = CartItem.objects.all()
    total_price = sum(item.price for item in cart_info)
    return render(request, 'shops/cart.html', {'cart_info': cart_info, 'total_price': total_price})
